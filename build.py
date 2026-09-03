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
SITE_TAGLINE = "Multi-agent AI systems: mechanism design, real implementations, red-teaming"  # confirm before publishing
BASE_URL = ""  # e.g. "" for user.github.io, or "/repo-name" for a project page

NAV = [
    ("index.html", "About"),
    ("research.html", "Research"),
    ("projects.html", "Projects"),
    ("writing.html", "Writing"),
    ("cv.html", "CV"),
]

FOOTER_LINKS = [
    ("mailto:jessica@agihouse.org", "Email"),
    ("https://github.com/JessSanChen", "GitHub"),
    ("https://arxiv.org/a/chen_j_1", "arXiv"),
    ("https://blog.agihouse.org/team-members/jessica-chen", "AGI House"),
]

# Order in which project kinds are grouped on the index page.
KIND_ORDER = ["Publication", "Preprint", "Research", "Build", "Political economy", "Open source", "Hackathon", "Writing", "Earlier work"]


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

def layout(title, body_html, current, depth=0, description=""):
    up = "../" * depth
    nav = "\n".join(
        '        <a href="{u}{href}"{cur}>{label}</a>'.format(
            u=up, href=href, label=html.escape(label),
            cur=' aria-current="page"' if href == current else "")
        for href, label in NAV
    )
    foot = "\n".join(
        '      <a href="{href}">{label}</a>'.format(href=html.escape(url), label=html.escape(label))
        for url, label in FOOTER_LINKS
    )
    page_title = SITE_TITLE if title == SITE_TITLE else "{} — {}".format(title, SITE_TITLE)
    desc = description or "{} — {}".format(SITE_TITLE, SITE_TAGLINE)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(page_title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(page_title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>

<header class="site">
  <p class="name"><a href="{up}index.html">{html.escape(SITE_TITLE)}</a></p>
  <nav class="site">
{nav}
  </nav>
</header>

<main>
{body_html}
</main>

<footer class="site">
{foot}
</footer>

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


def project_entry_html(p, depth=0):
    up = "../" * depth
    links = "".join(
        '<a href="{}">{}</a>'.format(html.escape(rebase(u, depth)), html.escape(l))
        for l, u in p["links"]
    )
    kind = p.get("kind", "")
    tag = f'<span class="tag">{html.escape(kind)}</span>' if kind else ""
    meta_bits = [b for b in [p.get("venue", ""), p.get("date", "")] if b]
    meta_line = f'<p class="meta">{html.escape(" · ".join(meta_bits))}</p>' if meta_bits else ""
    blurb = f'<p class="blurb">{html.escape(p.get("blurb", ""))}</p>' if p.get("blurb") else ""
    return f"""  <article class="entry">
    <h3><a href="{up}projects/{p['slug']}.html">{html.escape(p.get('title', p['slug']))}</a>{tag}</h3>
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
    for p in projects:
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
            for kind in KIND_ORDER + sorted({p.get("kind", "") for p in projects}):
                if kind in seen:
                    continue
                seen.add(kind)
                bucket = [p for p in projects if p.get("kind", "") == kind]
                if not bucket:
                    continue
                entries = "\n".join(project_entry_html(p) for p in bucket)
                label = kind or "Other"
                groups.append(f'<h2>{html.escape(label)}</h2>\n<div class="entries">\n{entries}\n</div>')
            rendered = rendered.replace("<p>{{projects}}</p>", "\n".join(groups))
            rendered = rendered.replace("{{projects}}", "\n".join(groups))

        # {{selected}} expands to whatever you've marked `featured: true`,
        # in KIND_ORDER then date order. Falls back to the 3 most recent.
        if "{{selected}}" in rendered:
            feat = [p for p in projects if p.get("featured", "").lower() in ("true", "yes", "1")]
            if feat:
                rank = {k: i for i, k in enumerate(KIND_ORDER)}
                feat.sort(key=lambda p: (rank.get(p.get("kind", ""), 99), p.get("date", "")),
                          reverse=False)
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
