#!/usr/bin/env sh
# deploy.sh — build the site and publish dist/ to the gh-pages branch.
# One command: ./deploy.sh
set -eu
here=$(cd "$(dirname "$0")" && pwd)
cd "$here"
python3 build.py
remote=$(git remote get-url origin 2>/dev/null || echo "https://github.com/makeroftools/agentelmer.git")
name=$(git config user.name 2>/dev/null || echo makeroftools)
mail=$(git config user.email 2>/dev/null || echo makeroftools@users.noreply.github.com)
stage=$(mktemp -d)
trap 'rm -rf "$stage"' EXIT
cp -r dist/* "$stage"/
cd "$stage"
git init -q
git branch -M gh-pages
git add -A
git -c user.name="$name" -c user.email="$mail" commit -q -m "publish site"
git remote add origin "$remote"
git push -f origin gh-pages
echo "deployed -> ${remote%.git} (gh-pages)"
