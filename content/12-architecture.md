id: architecture
kind: prose
label: How it works
title: A network of components, not a monolith.

Nothing here is bespoke. A **component** is a typed value producer — config → input → output — and a network of components is itself a component. The pipeline, the runtime, and the transport are all components; the topology is defined separately from any of them.

A run moves through a closed, ordered set of stages. The controller runs them in order and refuses a missing stage or a skipped gate.

```html
<div class="flow">
  <span class="flow__node">intake</span><span class="flow__arrow">→</span>
  <span class="flow__node">context</span><span class="flow__arrow">→</span>
  <span class="flow__node">plan</span><span class="flow__arrow">→</span>
  <span class="flow__node">tool-contract</span><span class="flow__arrow">→</span>
  <span class="flow__node">patch</span><span class="flow__arrow">→</span>
  <span class="flow__node">verification</span><span class="flow__arrow">→</span>
  <span class="flow__node">acceptance</span>
</div>
```

- The **model** appears only at the front, to turn natural language into a formal proposal.
- **Transformers** formalize that proposal into strict-schema artifacts.
- The **gateway** admits tools; the **applier** is the only writer; the **verifier** runs a closed catalog.
- **Acceptance** joins the evidence and decides.

Everything the model touches is clamped. Everything past it is reproducible.
