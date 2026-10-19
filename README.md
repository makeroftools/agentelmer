# mvp-website

The minimum-viable website for the project — an elegant, single-page scroll
story generated deterministically from markdown. No framework, no dependencies,
stdlib only.

## Build

```sh
python3 build.py
```

Writes `dist/index.html` and copies `site/` assets into `dist/`. Same content in
produces the same bytes out.

## Preview

```sh
python3 -m http.server -d dist 4000
```

Then open <http://localhost:4000>.

## Author

Add or edit beats in `content/`. Each file is markdown with a flat `Key: value`
header, then a blank line, then the body:

```text
id: products
kind: products
label: The two products
title: Build the engine first. Then the world.

Body markdown…
```

Header keys (closed set): `id`, `kind`, `label`, `title`, `subtitle`.
Kinds: `hero`, `prose`, `principle`, `products`, `cta`.
Files render in filename order.

The markdown subset is headings, paragraphs, lists, blockquotes, inline
emphasis / code / links, and fenced blocks. A ```` ```html ```` fence injects raw
markup — the sanctioned escape hatch for hand-drawn SVG diagrams.

## Layout

```
content/   story beats (markdown)          — authored
site/      style.css · app.js              — the design system
build.py   the generator                   — deterministic
dist/      generated output                — do not edit
```

## Design

Elmer is the organic agent; the lattice is the deterministic machine; the clamp
is where they meet. Warm hand-drawn mascot moments, hairline-precise engine
moments, contrast as the idea.

## Next

- Real Elmer mascot art (original — the Terrapin reference is inspiration only).
- More beats: origin timeline, the fractal, the creator economy, the roadmap.
- A present mode for live pitching.
- Deployment target (static host).
