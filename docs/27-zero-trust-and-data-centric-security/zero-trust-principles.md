---
title: Zero Trust Principles
description: Principles and operating assumptions for Zero Trust implementation.
category: Zero Trust and Data-Centric Security
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - zero-trust
---

# Zero Trust Principles

## Principle 1 — Verify explicitly

Access should be evaluated using identity, device posture, location, behavior, resource sensitivity, and risk signals.

## Principle 2 — Use least privilege

Access should be limited to what is needed, when it is needed, and for as long as it is needed.

## Principle 3 — Assume breach

Design as though attackers may already be inside the environment. Limit lateral movement, monitor behavior, and protect critical data.

## Principle 4 — Protect resources, not only networks

Resources include applications, APIs, databases, files, cloud services, models, data pipelines, and management interfaces.

## Principle 5 — Continuously evaluate

Access decisions should adapt as context changes.

## Typical evidence

- access policy documents showing explicit verification signals (identity, device, context)
- least-privilege and just-in-time access configuration or review records
- assume-breach design artifacts such as segmentation and lateral-movement analysis
- inventory of protected resources beyond network boundaries (APIs, data stores, pipelines)
- records showing access decisions adapt to changed risk context

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

A file-sharing service historically trusted any request from the office network. Applying the principles, the team re-verifies every request (identity plus device posture), scopes access to specific folders instead of the whole share, and treats the office LAN as untrusted. A red-team exercise then shows that a compromised office workstation can no longer enumerate the full file server — evidence that "assume breach" changed real behavior.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
