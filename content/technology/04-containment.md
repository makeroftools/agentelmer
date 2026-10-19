id: containment
kind: prose
label: Containment
title: Every component is bubble-wrapped.

Safety here is not a policy bolted on top. It is the shape of the system.

```html
<figure class="diagram">
<img src="/containment.svg" alt="Nested governance and security boundaries around every component">
<figcaption class="muted">Governance and security at every scale.</figcaption>
</figure>
```

- **Rogue agents are structurally impossible.** Each AI is a small, bounded **domain expert** with no ambient authority. It cannot act outside the capability it was granted, so it has no reach for mischief — and small, fine-grained agents are easy to watch, regulate, and reason about.
- **Every parent governs its children.** A composite component holds immediate, recorded authority over the components it contains. Governance is recursive, so control scales with the topology.
- **Bubble-wrapped, at every scale.** Each fractal structure carries its own security and governance boundary. A fault is contained exactly where it happens.
- **Mission-critical, live.** A component can be repaired or replaced **without downtime** — not a second, not a millisecond, not a microsecond. Identity stays stable; the running instance is swapped underneath it.
