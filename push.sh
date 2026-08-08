#!/bin/bash
# Commit the compressed PDFs and push. Run from this directory:  bash push.sh
set -e

# Raise git's HTTP buffer - the default 1MB is what caused the earlier HTTP 400
git config http.postBuffer 524288000
git config http.version HTTP/1.1

echo "==> Committing"
git add -A
git commit -qm "Compress PDFs" || echo "    (nothing new to commit)"

echo "==> Pushing to main"
git push -u --force origin main

echo
echo "Done. Now set GitHub Pages:"
echo "  Settings -> Pages -> Source: Deploy from a branch -> main -> / (root)"
