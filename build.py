#!/usr/bin/env python3
"""
Static site builder — no framework, no CI required.

You write Markdown in content/. You run `python3 build.py`. It writes plain
HTML next to itself, which GitHub Pages serves directly. That's the whole
system. If you ever get sick of it, the generated HTML still works on its own.

    pip install markdown
    python3 build.py

Front matter is a `---` fenced block of `key: value` lines at the top of each
Markdown file. Supported keys are documented in content/README.md.
"""

import os
import re
import shutil
import html
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
SITE_TITLE = "Jessica Chen"
SITE_TAGLINE = "AI x biosecurity: misuse monitoring, agent evaluation, and the wet-lab context behind them"
BASE_URL = ""  # e.g. "" for user.github.io, or "/repo-name" for a project page

# Each nav item is a dict: {href, label, external?}.
# `href` is written relative to the site root; it's re-based per page depth.
# `external: True` opens in a new tab and never gets the current-page marker
# (use it for links to files like the CV PDF rather than generated pages).
NAV = [
    {"href": "index.html", "label": "About"},
    {"href": "projects.html", "label": "Research"},
    {"href": "writing.html", "label": "Writing"},
    {"href": "cv.html", "label": "CV"},
]

FOOTER_LINKS = [
    ("mailto:jessica@agihouse.org", "Email"),
    ("https://github.com/JessSanChen", "GitHub"),
    # ("https://arxiv.org/a/chen_j_1", "arXiv"),
    ("https://blog.agihouse.org/team-members/jessica-chen", "AGI House"),
]

# Projects are grouped on the index page by `section` (falling back to `kind`),
# in this order. `kind` is shown as the small tag on each entry.
SECTION_ORDER = ["AI x biosecurity", "AI agents and evaluation", "Mechanism design", "Lab research"]
KIND_ORDER = ["Publication", "Under review", "In progress", "Preprint", "Project", "Program", "Course paper", "Hackathon", "Lab"]
# Your name as it appears in `authors:`; it's bolded in author lists.
SELF_NAME = "J. Chen"


# --------------------------------------------------------------------------
# Front matter
# --------------------------------------------------------------------------

def parse_front_matter(text):
    meta, body = {}, text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            block = text[3:end]
            body = text[end + 4:].lstrip("\n")
            for line in block.strip().splitlines():
                if not line.strip() or line.strip().startswith("#"):
                    continue
                if ":" not in line:
                    continue
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    return meta, body


def parse_links(raw):
    """`links: Paper|https://... ; Code|https://...` -> [(label, url), ...]"""
    out = []
    for part in (raw or "").split(";"):
        part = part.strip()
        if not part:
            continue
        if "|" in part:
            label, url = part.split("|", 1)
            out.append((label.strip(), url.strip()))
        else:
            out.append((part, part))
    return out


MD = markdown.Markdown(extensions=["extra", "sane_lists", "smarty", "toc"])


def render_md(body):
    MD.reset()
    return MD.convert(body)


# --------------------------------------------------------------------------
# Layout
# --------------------------------------------------------------------------

# The page is assembled from small component builders. Each returns a chunk of
# HTML; `layout()` composes them. `up` is the relative prefix ("../" per level of
# nesting) that re-bases root-relative links for pages served from a subdirectory.

def render_head(page_title, desc, up):
    return f"""<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(page_title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(page_title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="{up}assets/style.css">
</head>"""


def render_nav(current, up):
    items = []
    for item in NAV:
        attrs = ""
        if not item.get("external") and item["href"] == current:
            attrs += ' aria-current="page"'
        if item.get("external"):
            attrs += ' target="_blank" rel="noopener"'
        items.append(
            '        <a href="{u}{href}"{attrs}>{label}</a>'.format(
                u=up, href=item["href"], attrs=attrs, label=html.escape(item["label"]))
        )
    return "\n".join(items)


def render_header(current, up):
    return f"""<header class="site">
  <p class="name"><a href="{up}index.html">{html.escape(SITE_TITLE)}</a></p>
  <nav class="site">
{render_nav(current, up)}
  </nav>
</header>"""


def render_footer():
    links = "\n".join(
        '      <a href="{href}">{label}</a>'.format(href=html.escape(url), label=html.escape(label))
        for url, label in FOOTER_LINKS
    )
    return f"""<footer class="site">
{links}
</footer>"""


def layout(title, body_html, current, depth=0, description=""):
    up = "../" * depth
    page_title = SITE_TITLE if title == SITE_TITLE else "{} — {}".format(title, SITE_TITLE)
    desc = description or "{} — {}".format(SITE_TITLE, SITE_TAGLINE)
    return f"""<!DOCTYPE html>
<html lang="en">
{render_head(page_title, desc, up)}
<body>

{render_header(current, up)}

<main>
{body_html}
</main>

{render_footer()}

</body>
</html>
"""


# --------------------------------------------------------------------------
# Projects
# --------------------------------------------------------------------------

def load_projects():
    items = []
    pdir = CONTENT / "projects"
    if not pdir.exists():
        return items
    for path in sorted(pdir.glob("*.md")):
        meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
        if meta.get("draft", "").lower() in ("true", "yes", "1"):
            continue
        meta["slug"] = meta.get("slug") or path.stem
        meta["body"] = body
        meta["links"] = parse_links(meta.get("links"))
        items.append(meta)
    # newest first, then by explicit `order`
    items.sort(key=lambda m: (m.get("order", "500"), m.get("date", "")), reverse=False)
    items.sort(key=lambda m: m.get("date", ""), reverse=True)
    return items


def rebase(url, depth):
    """Project front matter is written relative to /projects/ (e.g. `../files/x.pdf`).
    Re-point those when the same link is rendered from a page at a different depth."""
    if url.startswith("../") and depth == 0:
        return url[3:]
    return url


def has_page(p):
    """A project gets its own detail page unless it sets `page: false` in front
    matter — those are link-only entries whose title points straight at the paper."""
    return p.get("page", "").lower() not in ("false", "no", "0")


def project_entry_html(p, depth=0):
    up = "../" * depth
    links = "".join(
        '<a href="{}">{}</a>'.format(html.escape(rebase(u, depth)), html.escape(l))
        for l, u in p["links"]
    )
    kind = p.get("kind", "")
    tag = f'<span class="tag">{html.escape(kind)}</span>' if kind else ""
    meta_bits = [html.escape(b) for b in [p.get("venue", ""), p.get("date", "")] if b]
    if p.get("authors"):
        meta_bits.insert(0, html.escape(p["authors"]).replace(
            SELF_NAME, f"<strong>{SELF_NAME}</strong>"))
    meta_line = f'<p class="meta">{" · ".join(meta_bits)}</p>' if meta_bits else ""
    blurb = f'<p class="blurb">{html.escape(p.get("blurb", ""))}</p>' if p.get("blurb") else ""
    title = html.escape(p.get("title", p["slug"]))
    if has_page(p):
        title_html = f'<a href="{up}projects/{p["slug"]}.html">{title}</a>'
    elif p["links"]:
        title_html = f'<a href="{html.escape(rebase(p["links"][0][1], depth))}">{title}</a>'
    else:
        title_html = title
    return f"""  <article class="entry">
    <h3>{title_html}{tag}</h3>
{meta_line}
{blurb}
    <div class="links">{links}</div>
  </article>"""


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------

def build():
    projects = load_projects()

    # --- individual project pages ---
    outdir = ROOT / "projects"
    outdir.mkdir(exist_ok=True)
    # Drop pages left over from projects that are now drafts or link-only.
    wanted = {f"{p['slug']}.html" for p in projects if has_page(p)}
    for old in outdir.glob("*.html"):
        if old.name not in wanted:
            old.unlink()
    for p in projects:
        if not has_page(p):
            continue
        links = "".join(
            '<a href="{}">{}</a>'.format(html.escape(u), html.escape(l)) for l, u in p["links"]
        )
        meta_bits = [b for b in [p.get("kind", ""), p.get("venue", ""), p.get("date", "")] if b]
        header = f"""<h1>{html.escape(p.get('title', p['slug']))}</h1>
<p class="meta muted small">{html.escape(" · ".join(meta_bits))}</p>
<div class="links" style="margin-bottom:1.5rem">{links}</div>"""
        body = header + render_md(p["body"])
        body += '\n<p class="backlink"><a href="../projects.html">← All projects</a></p>'
        (outdir / f"{p['slug']}.html").write_text(
            layout(p.get("title", p["slug"]), body, "projects.html", depth=1,
                   description=p.get("blurb", "")),
            encoding="utf-8")

    # --- top-level pages ---
    for path in sorted((CONTENT / "pages").glob("*.md")):
        meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
        out_name = meta.get("output") or (path.stem + ".html")
        rendered = render_md(body)

        # {{projects}} expands to the grouped project index
        if "{{projects}}" in rendered:
            groups = []
            seen = set()
            group_of = lambda p: p.get("section") or p.get("kind", "")
            for sec in SECTION_ORDER + sorted({group_of(p) for p in projects}):
                if sec in seen:
                    continue
                seen.add(sec)
                bucket = [p for p in projects if group_of(p) == sec]
                if not bucket:
                    continue
                bucket.sort(key=lambda p: int(p.get("order", "500")))
                entries = "\n".join(project_entry_html(p) for p in bucket)
                label = sec or "Other"
                anchor = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")
                groups.append(f'<h2 id="{anchor}">{html.escape(label)}</h2>\n<div class="entries">\n{entries}\n</div>')
            rendered = rendered.replace("<p>{{projects}}</p>", "\n".join(groups))
            rendered = rendered.replace("{{projects}}", "\n".join(groups))

        # {{selected}} expands to whatever you've marked `featured: true`,
        # in KIND_ORDER then date order. Falls back to the 3 most recent.
        if "{{selected}}" in rendered:
            feat = [p for p in projects if p.get("featured", "").lower() in ("true", "yes", "1")]
            if feat:
                rank = {k: i for i, k in enumerate(SECTION_ORDER)}
                feat.sort(key=lambda p: (rank.get(p.get("section", ""), 99),
                                         int(p.get("order", "500"))))
            else:
                feat = projects[:3]
            entries = "\n".join(project_entry_html(p) for p in feat)
            block = f'<div class="entries">\n{entries}\n</div>'
            rendered = rendered.replace("<p>{{selected}}</p>", block).replace("{{selected}}", block)

        (ROOT / out_name).write_text(
            layout(meta.get("title", SITE_TITLE), rendered, out_name,
                   description=meta.get("description", "")),
            encoding="utf-8")

    # --- static passthrough ---
    src_static = CONTENT / "static"
    if src_static.exists():
        for f in src_static.rglob("*"):
            if f.is_file():
                dest = ROOT / "files" / f.relative_to(src_static)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, dest)

    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Built {len(projects)} project pages + "
          f"{len(list((CONTENT / 'pages').glob('*.md')))} top-level pages.")


if __name__ == "__main__":
    build()
