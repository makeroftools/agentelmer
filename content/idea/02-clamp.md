id: clamp
kind: prose
label: The move
title: Clamp the nondeterminism.

Nondeterminism is not forbidden — it is *bounded*. The model may propose; a strict schema, canonical bytes, and a content address decide whether the proposal becomes real. Everything downstream is reproducible: same inputs, same outcome, every time.

```html
<figure class="diagram">
<svg viewBox="0 0 1000 380" role="img" aria-label="Nondeterminism is admitted only at the boundary">
  <defs>
    <linearGradient id="seam" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#e6a15a"/>
      <stop offset="1" stop-color="#5ad1c8"/>
    </linearGradient>
    <radialGradient id="warmglow" cx="30%" cy="50%" r="65%">
      <stop offset="0" stop-color="#e6a15a" stop-opacity="0.20"/>
      <stop offset="1" stop-color="#e6a15a" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="0" y="0" width="500" height="380" fill="url(#warmglow)"/>
  <path d="M60,250 C120,140 210,120 300,180 C380,232 430,210 470,160"
        fill="none" stroke="#e6a15a" stroke-width="1.5" stroke-opacity="0.7"/>
  <path d="M40,300 C160,240 260,260 340,300 C400,330 450,320 480,300"
        fill="none" stroke="#e6a15a" stroke-width="1.2" stroke-opacity="0.4"/>
  <g fill="#e6a15a">
    <circle cx="120" cy="180" r="3"/><circle cx="180" cy="120" r="2.4"/>
    <circle cx="250" cy="200" r="3.2"/><circle cx="330" cy="150" r="2.2"/>
    <circle cx="90" cy="260" r="2.6"/><circle cx="400" cy="120" r="2.8"/>
    <circle cx="300" cy="90" r="2.0"/><circle cx="440" cy="220" r="2.4"/>
  </g>
  <line x1="500" y1="22" x2="500" y2="360" stroke="url(#seam)" stroke-width="2"/>
  <text x="500" y="14" text-anchor="middle" fill="#f4f2ec"
        font-family="ui-monospace, monospace" font-size="12" letter-spacing="4">CLAMP</text>
  <g stroke="#5ad1c8" stroke-opacity="0.34" stroke-width="1">
    <line x1="560" y1="60" x2="560" y2="320"/><line x1="620" y1="60" x2="620" y2="320"/>
    <line x1="680" y1="60" x2="680" y2="320"/><line x1="740" y1="60" x2="740" y2="320"/>
    <line x1="800" y1="60" x2="800" y2="320"/><line x1="860" y1="60" x2="860" y2="320"/>
    <line x1="920" y1="60" x2="920" y2="320"/><line x1="960" y1="60" x2="960" y2="320"/>
    <line x1="540" y1="60" x2="980" y2="60"/><line x1="540" y1="120" x2="980" y2="120"/>
    <line x1="540" y1="180" x2="980" y2="180"/><line x1="540" y1="240" x2="980" y2="240"/>
    <line x1="540" y1="300" x2="980" y2="300"/>
  </g>
  <g fill="#5ad1c8" fill-opacity="0.85">
    <rect x="612" y="112" width="16" height="16" rx="3"/>
    <rect x="738" y="172" width="16" height="16" rx="3"/>
    <rect x="858" y="112" width="16" height="16" rx="3"/>
    <rect x="678" y="232" width="16" height="16" rx="3"/>
    <rect x="918" y="232" width="16" height="16" rx="3"/>
  </g>
</svg>
<figcaption class="muted">Nondeterminism on the left; the deterministic lattice on the right; the boundary is the only door.</figcaption>
</figure>
```
