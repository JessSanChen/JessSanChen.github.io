#!/bin/bash
# Rebuilds the git repo cleanly and pushes to GitHub.
# Run from this directory:   bash push.sh
set -e

REPO="https://github.com/JessSanChen/JessSanChen.github.io.git"

echo "==> Removing the damaged .git directory (your files are untouched)"
rm -rf .git

echo "==> Re-initialising on branch 'main'"
git init -b main -q
git add -A
git commit -qm "Personal site"
git remote add origin "$REPO"

echo "==> Archiving the existing al-folio site as branch 'al-folio-archive'"
git fetch -q origin || true
if git rev-parse --verify -q refs/remotes/origin/main >/dev/null; then
  git push -q origin refs/remotes/origin/main:refs/heads/al-folio-archive || \
    echo "    (archive branch already exists or was refused - continuing)"
else
  echo "    (no existing main on the remote - nothing to archive)"
fi

echo "==> Force-pushing the new site to main"
git push -u --force origin main

echo
echo "Done. Now set GitHub Pages:"
echo "  Settings -> Pages -> Source: Deploy from a branch -> main -> / (root)"
