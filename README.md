# Personal site

Static site. No framework, no build pipeline, no CI. You write Markdown in
`content/`, run one Python script, and commit the HTML it produces.

## Setup (once)

```bash
pip install markdown pillow
```

## Edit → build → publish

```bash
# 1. edit files under content/
# 2. regenerate the HTML
python3 build.py
# 3. preview locally
python3 -m http.server 8000     # then open http://localhost:8000
# 4. publish
git add -A && git commit -m "update" && git push
```

## Deploying to GitHub Pages

1. Create a repo named **`YOURUSERNAME.github.io`** (the exact name matters —
   that's what makes it a user site served at the root domain).
2. Push this directory to it:

   ```bash
   git remote add origin git@github.com:YOURUSERNAME/YOURUSERNAME.github.io.git
   git branch -M main
   git push -u origin main
   ```

3. In the repo: **Settings → Pages → Source: Deploy from a branch → `main` / `/ (root)`**.
4. Wait ~60 seconds. Live at `https://YOURUSERNAME.github.io`.

No Actions workflow is needed because the HTML is committed. The `.nojekyll`
file (written automatically by `build.py`) tells Pages to serve the files as-is
instead of running them through Jekyll.

### Custom domain

Put your domain in a file named `CNAME` at the repo root (one line, no
protocol, e.g. `jessicachen.com`), point a CNAME DNS record at
`YOURUSERNAME.github.io`, then set the domain under Settings → Pages.

## Layout

```
content/
  pages/            one Markdown file per top-level page
  projects/         one Markdown file per project → projects/<slug>.html
  static/           images, PDFs, posters → copied to files/
assets/style.css    all styling; edit the CSS variables at the top to restyle
build.py            the whole build system, ~200 lines
```

Generated files (`index.html`, `research.html`, `projects.html`, `cv.html`,
`projects/*.html`, `files/`) are committed on purpose — that's what GitHub Pages
serves. Don't hand-edit them; they get overwritten on the next build.

See `content/README.md` for the front-matter reference.
