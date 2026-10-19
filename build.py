#!/usr/bin/env python3
"""build.py — deterministic static-site generator for the MVP website.

Content is authored as markdown in `content/*.md`, each with a tiny flat
`Key: value` header (JSON-free, line-oriented). This generator renders those
beats into one static `dist/index.html`, copying the `site/` assets alongside.
Same content in => same bytes out. Stdlib only.

Header keys (closed set): id, kind, label, title, subtitle.
Kinds: hero | prose | principle | products | cta.

Usage:  python3 build.py        (builds dist/)
        python3 -m http.server -d dist 4000   (preview)
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

HEADER_KEYS = ("id", "kind", "label", "title", "subtitle")


def parse_front(text: str) -> tuple:
    """Flat `Key: value` header, then a blank line, then the body."""
    lines = text.splitlines()
    meta: dict = {}
    i = 0
    while i < len(lines) and lines[i].strip():
        if ":" in lines[i]:
            key, value = lines[i].split(":", 1)
            key = key.strip().lower()
            if key in HEADER_KEYS:
                meta[key] = value.strip()
        i += 1
    body = "\n".join(lines[i:]).strip("\n")
    return meta, body


def inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def render_md(text: str) -> str:
    """A small, fixed markdown subset: headings, paragraphs, lists, quotes,
    inline emphasis/code/links, and fenced blocks (```html injects raw markup —
    the sanctioned escape hatch for hand-drawn SVG diagrams)."""
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
            if info in ("html", "svg"):
                out.append(code)
            else:
                out.append(f"<pre><code>{html.escape(code)}</code></pre>")
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
    parts = [f'<section class="beat beat--{kind}" id="{html.escape(beat_id)}" '
             f'data-beat="{index}">']
    parts.append('<div class="beat__inner">')
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


def build() -> int:
    if not os.path.isdir(CONTENT):
        print("build: no content/ directory", file=sys.stderr)
        return 2
    names = sorted(f for f in os.listdir(CONTENT) if f.endswith(".md"))
    beats = []
    metas = []
    for name in names:
        with open(os.path.join(CONTENT, name), encoding="utf-8") as fh:
            meta, body = parse_front(fh.read())
        metas.append(meta)
        beats.append(render_beat(meta, body, len(beats) + 1))

    def beat_id(i: int, meta: dict) -> str:
        return meta.get("id", f"beat-{i:02d}")

    rail = "\n".join(
        f'<a href="#{html.escape(beat_id(i, m))}" '
        f'data-target="{html.escape(beat_id(i, m))}">{html.escape(m.get("label", ""))}</a>'
        for i, m in enumerate(metas, 1)
    )

    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    if os.path.isdir(SITE):
        for entry in os.listdir(SITE):
            shutil.copy2(os.path.join(SITE, entry), os.path.join(DIST, entry))

    page = PAGE.replace("{body}", "\n".join(beats)).replace("{rail}", rail)
    with open(os.path.join(DIST, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(page)
    print(f"build: wrote {len(beats)} beat(s) -> {os.path.join(DIST, 'index.html')}")
    return 0


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AgentElmer — the agent is you</title>
<meta name="description" content="A deterministic, provable software factory. The agent is you; the AI is the instrument.">
<meta name="theme-color" content="#0b0c0e">
<meta property="og:type" content="website">
<meta property="og:title" content="AgentElmer — the agent is you">
<meta property="og:description" content="A deterministic, provable software factory. The agent is you; the AI is the instrument.">
<meta property="og:image" content="og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@makeroftools">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="style.css">
<noscript><style>.beat__inner{opacity:1;transform:none}</style></noscript>
</head>
<body>
<a class="skip" href="#top">Skip to content</a>
<div class="spine" aria-hidden="true"><span class="spine__fill"></span></div>
<nav class="rail" aria-label="Sections">
{rail}
</nav>
<header class="topbar">
  <span class="mark"><img src="elmer.svg" alt="" class="mark__elmer">AgentElmer</span>
  <nav class="topnav">
    <a href="#capabilities">Capabilities</a>
    <a href="#architecture">How it works</a>
    <a href="#products">Products</a>
    <a href="#pricing">Pricing</a>
    <a href="#faq">FAQ</a>
    <a href="#cta" class="cta">Get started</a>
  </nav>
</header>
<main>
{body}
</main>
<footer class="footer">
  <span>Creative Development Systems · <a href="https://x.com/makeroftools">@makeroftools</a></span>
  <span class="muted">The agent is you. The AI is the instrument.</span>
</footer>
<script src="app.js"></script>
</body>
</html>
"""


if __name__ == "__main__":
    sys.exit(build())
