id: trust
kind: prose
label: Trust and security
title: Secure by construction.

Agent Elmer assumes nothing about its environment and grants nothing by default. Every capability is explicit, scoped, and recorded — and the parts that touch your work cannot be bypassed.

- **Default-deny capabilities.** No ambient access to the network, filesystem, secrets, or clock. Each access is a declared, recorded grant.
- **The runtime is not an authority.** A running component cannot make the decisions that belong to the controller, gateway, applier, or verifier. An attempted effect is refused and logged.
- **Secrets stay out.** They never enter arguments, environments, logs, or evidence — only capability references travel.
- **Provenance is recomputable.** Identity is a content address, so what ran, what it produced, and who made it are facts you can re-check.
- **Sovereignty.** Your data is yours. The components you create carry your rights.
