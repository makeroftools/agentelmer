#!/usr/bin/env python3
"""build.py — deterministic multi-page static-site generator.

Content is authored as markdown under `content/<page>/`, one directory per page:

    content/
      index/          ->  dist/index.html            (URL "/")
        _page.md      page meta: title, description, nav, order
        01-hero.md    a "beat" (section): id, kind, label, title, subtitle + md
      technology/     ->  dist/technology/index.html (URL "/technology/")

Links and assets in content are written **root-relative** (`/idea/`,
`/elmer-hero.svg`); the generator prefixes them per page depth, so the same
output works at a domain root or under a project subpath. Standard library only.
Same content in => same bytes out.

Usage:  python3 build.py
        python3 -m http.server 4000 --directory dist
"""
from __future__ import annotations

import html
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(ROOT, "content")
SITE = os.path.join(ROOT, "site")
DIST = os.path.join(ROOT, "dist")

SITE_URL = "https://agent-elmer.prodatalab.com"
SITE_NAME = "AgentElmer"
TAGLINE = "The agent is you. The AI is the instrument."
BEAT_KEYS = ("id", "kind", "label", "title", "subtitle")
PAGE_KEYS = ("title", "description", "nav", "order")


def parse_front(text: str, keys: tuple) -> tuple:
    lines = text.splitlines()
    meta: dict = {}
    i = 0
    while i < len(lines) and lines[i].strip():
        if ":" in lines[i]:
            key, value = lines[i].split(":", 1)
            key = key.strip().lower()
            if key in keys:
                meta[key] = value.strip()
        i += 1
    return meta, "\n".join(lines[i:]).strip("\n")


def inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def render_md(text: str) -> str:
    out: list = []
    lines = text.split("\n")
    para: list = []

    def flush() -> None:
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("```"):
            flush()
            info = line.strip()[3:].strip()
            i += 1
            buf = []
            while i < len(lines) and not lines[i].lstrip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            code = "\n".join(buf)
            out.append(code if info in ("html", "svg")
                       else f"<pre><code>{html.escape(code)}</code></pre>")
            continue
        if re.match(r"^#{1,6}\s", line):
            flush()
            m = re.match(r"^(#{1,6})\s+(.*)$", line)
            out.append(f"<h{len(m.group(1))}>{inline(m.group(2))}</h{len(m.group(1))}>")
            i += 1
            continue
        if line.strip().startswith(("- ", "* ")):
            flush()
            items = []
            while i < len(lines) and lines[i].strip().startswith(("- ", "* ")):
                items.append(f"<li>{inline(lines[i].strip()[2:])}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        if line.strip().startswith(">"):
            flush()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            out.append("<blockquote>" + inline(" ".join(quote)) + "</blockquote>")
            continue
        if not line.strip():
            flush()
            i += 1
            continue
        para.append(line.strip())
        i += 1
    flush()
    return "\n".join(out)


def render_beat(meta: dict, body: str, index: int) -> str:
    kind = meta.get("kind", "prose")
    beat_id = meta.get("id", f"beat-{index:02d}")
    parts = [f'<section class="beat beat--{kind}" id="{html.escape(beat_id)}" data-beat="{index}">',
             '<div class="beat__inner">']
    if meta.get("label"):
        parts.append(f'<p class="eyebrow">{inline(meta["label"])}</p>')
    tag = "h1" if kind == "hero" else "h2"
    if meta.get("title"):
        parts.append(f'<{tag} class="beat__title">{inline(meta["title"])}</{tag}>')
    if meta.get("subtitle"):
        parts.append(f'<p class="beat__sub">{inline(meta["subtitle"])}</p>')
    if body:
        parts.append(f'<div class="beat__body">{render_md(body)}</div>')
    parts.append("</div></section>")
    return "\n".join(parts)


def load_pages() -> list:
    pages = []
    for name in sorted(os.listdir(CONTENT)):
        d = os.path.join(CONTENT, name)
        if not os.path.isdir(d):
            continue
        meta_path = os.path.join(d, "_page.md")
        pmeta = {}
        if os.path.isfile(meta_path):
            with open(meta_path, encoding="utf-8") as fh:
                pmeta, _ = parse_front(fh.read(), PAGE_KEYS)
        slug = "" if name == "index" else name
        beats = []
        metas = []
        for f in sorted(x for x in os.listdir(d) if x.endswith(".md") and x != "_page.md"):
            with open(os.path.join(d, f), encoding="utf-8") as fh:
                bmeta, body = parse_front(fh.read(), BEAT_KEYS)
            metas.append(bmeta)
            beats.append(render_beat(bmeta, body, len(beats) + 1))
        pages.append({"name": name, "slug": slug, "meta": pmeta,
                      "order": int(pmeta.get("order", 50)), "beats": beats, "metas": metas})
    pages.sort(key=lambda p: (p["order"], p["name"]))
    return pages


def build() -> int:
    pages = load_pages()
    if not pages:
        print("build: no pages under content/", file=sys.stderr)
        return 2
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    if os.path.isdir(SITE):
        for entry in os.listdir(SITE):
            s = os.path.join(SITE, entry)
            if os.path.isfile(s):
                shutil.copy2(s, os.path.join(DIST, entry))

    # site-wide nav (all pages, in order)
    def url(page) -> str:
        return f"/{page['slug']}/" if page["slug"] else "/"

    for page in pages:
        prefix = "./" if page["slug"] == "" else "../"
        if page["slug"]:
            os.makedirs(os.path.join(DIST, page["slug"]))
        nav = "".join(
            '<a href="%s"%s>%s</a>' % (
                url(p), ' class="active"' if p is page else "",
                html.escape(p["meta"].get("nav", p["name"].title())))
            for p in pages if p["meta"].get("nav")  # only show labelled pages
        )
        rail = "\n".join(
            f'<a href="#{html.escape(m.get("id", f"beat-{i:02d}"))}" '
            f'data-target="{html.escape(m.get("id", f"beat-{i:02d}"))}">{html.escape(m.get("label", ""))}</a>'
            for i, m in enumerate(page["metas"], 1) if m.get("label"))
        title = page["meta"].get("title", SITE_NAME)
        desc = page["meta"].get("description", TAGLINE)
        doc = PAGE.replace("{prefix}", prefix)
        doc = doc.replace("{title}", html.escape(title))
        doc = doc.replace("{description}", html.escape(desc))
        doc = doc.replace("{canonical}", SITE_URL + url(page))
        doc = doc.replace("{og_image}", SITE_URL + "/og.png")
        doc = doc.replace("{brand}", SITE_NAME)
        doc = doc.replace("{nav}", nav)
        doc = doc.replace("{rail}", rail)
        doc = doc.replace("{body}", "\n".join(page["beats"]))
        doc = doc.replace("{tagline}", TAGLINE)
        # prefix root-relative links/assets authored in content
        doc = doc.replace('href="/', f'href="{prefix}')
        doc = doc.replace('src="/', f'src="{prefix}')
        out_dir = DIST if not page["slug"] else os.path.join(DIST, page["slug"])
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(doc)
    print(f"build: wrote {len(pages)} page(s) -> dist/")
    return 0


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0b0c0e">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{og_image}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@makeroftools">
<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{prefix}style.css">
<noscript><style>.beat__inner{opacity:1;transform:none}</style></noscript>
</head>
<body>
<a class="skip" href="#top">Skip to content</a>
<div class="spine" aria-hidden="true"><span class="spine__fill"></span></div>
<nav class="rail" aria-label="Sections">
{rail}
</nav>
<header class="topbar">
  <a class="mark" href="{prefix}"><img src="{prefix}elmer.svg" alt="" class="mark__elmer">{brand}</a>
  <nav class="topnav">
{nav}
    <a href="{prefix}pricing/" class="cta">Get started</a>
  </nav>
</header>
<main>
{body}
</main>
<footer class="footer">
  <span>Creative Development Systems · <a href="https://x.com/makeroftools">@makeroftools</a></span>
  <span class="muted">{tagline}</span>
</footer>
<script src="{prefix}app.js"></script>
</body>
</html>
"""


if __name__ == "__main__":
    sys.exit(build())
