# Authoring reference

## Project pages — `content/projects/*.md`

The filename becomes the URL slug: `spike-sorting.md` → `/projects/spike-sorting.html`.

```markdown
---
title: Latent structure in motor cortex during reaching
kind: Publication
venue: NeurIPS 2025 Workshop on NeuroAI
date: 2025-12
blurb: One sentence stating what you found.
links: Paper|https://arxiv.org/abs/2512.00001 ; Code|https://github.com/you/repo ; Poster|../files/poster.pdf
order: 10
draft: false
---

Markdown body goes here.
```

| Key | Required | Notes |
|---|---|---|
| `title` | yes | Page heading and index entry. |
| `kind` | no | Groups the project on the index page. Use one of: `Publication`, `Preprint`, `Research`, `Course research`, `Open source`, `Hackathon`, `Writing`. A new value just creates a new group at the bottom. |
| `venue` | no | Conference, course, or event. Shown in the index meta line. |
| `date` | no | `YYYY-MM`. Sorts the index, newest first. |
| `blurb` | no | One sentence shown on the index. Write it as a finding, not a topic. |
| `links` | no | `Label\|URL` pairs separated by `;`. Relative paths work: `../files/report.pdf`. |
| `order` | no | Tiebreaker within a date. Lower sorts first. |
| `draft` | no | `true` hides it from the build entirely. |
| `slug` | no | Override the URL slug if you don't want the filename. |

## Top-level pages — `content/pages/*.md`

Same front matter, plus `output:` to set the filename (`output: index.html`).

Two template tokens are expanded at build time:

- `{{projects}}` — the full project index, grouped by `kind`.
- `{{selected}}` — the three most recent projects, ungrouped.

## Images and PDFs

Drop them in `content/static/`. They're copied to `files/` on build, so
reference them as `../files/thing.png` from a project page or `files/thing.pdf`
from a top-level page.

```markdown
<figure class="figure">
  <img src="../files/decoding-accuracy.png" alt="Decoding accuracy by area">
  <figcaption>The caption should state the takeaway, not label the axes.</figcaption>
</figure>
```

## Useful CSS classes

| Class | Use |
|---|---|
| `.lede` | Larger opening paragraph. |
| `.muted`, `.small` | Softer / smaller text. |
| `.callout` | Boxed aside. |
| `.row` + `.when` / `.what` | Two-column CV rows. |
| `.tag` | Small uppercase label. |

## Math

If you want LaTeX, add KaTeX to the `<head>` in `build.py`'s `layout()`:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body)"></script>
```

Then `$...$` and `$$...$$` render in any page.

## Featured on the home page

Add `featured: true` to any project's front matter and it appears under
"Selected work" on the home page, ordered by `kind` (publications first) then
date. With none marked, the three most recent are shown.
