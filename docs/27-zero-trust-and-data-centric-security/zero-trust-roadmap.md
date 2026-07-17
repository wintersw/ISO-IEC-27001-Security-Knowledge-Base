---
title: Zero Trust Roadmap
description: Step-by-step roadmap for implementing Zero Trust without overengineering.
category: Zero Trust and Data-Centric Security
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - zero-trust
  - roadmap
---

# Zero Trust Roadmap

## Phase 1 — Define protect surfaces

Identify the most important data, applications, assets, and services.

## Phase 2 — Map flows

Map who and what accesses the protect surfaces.

## Phase 3 — Assess current controls

Review identity, device, network, application, and data controls.

## Phase 4 — Define policy

Create access policies based on identity, device, sensitivity, and context.

## Phase 5 — Implement enforcement

Deploy controls incrementally: multifactor authentication (MFA), conditional access, segmentation, zero trust network access (ZTNA), data controls.

## Phase 6 — Monitor and improve

Measure access denials, anomalous activity, policy exceptions, and control effectiveness.

## Start small

Begin with high-risk applications, privileged access, remote access, and sensitive data stores.

## Typical evidence

- documented protect surfaces and prioritization rationale
- flow maps for the first-wave applications and data stores
- gap assessment of current identity, device, network, and data controls
- phased implementation plan with completed milestones
- post-implementation metrics showing enforcement and improvement

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

Instead of a big-bang program, a mid-size company starts Phase 1 with three protect surfaces: the HR system, the payment database, and admin interfaces. Over two quarters it maps their flows, enforces MFA and conditional access, and segments the payment zone. Only after metrics show stable enforcement does the roadmap extend to the next wave of applications — keeping the program small, measurable, and reversible.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
