---
title: ISMS RACI and Responsibility Model
description: Defines accountability and responsibility patterns for an ISMS.
category: ISMS
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - isms
  - best-practice
---

# ISMS RACI and Responsibility Model

A RACI model clarifies who is Responsible, Accountable, Consulted, and Informed.

## Why this matters

Ambiguous ownership is one of the most common causes of ISMS weakness. Policies, controls, risks, and corrective actions fail when everyone assumes someone else owns them.

## Example RACI

| Activity | Security | Risk owner | Asset owner | IT operations | Internal audit |
|---|---|---|---|---|---|
| Risk assessment facilitation | R | A | C | C | I |
| Residual risk acceptance | C | A | C | I | I |
| Access review operation | C | A | R | R | I |
| Internal audit | I | C | C | C | A/R |
| Corrective action | C | A | R | R | I |

## Best practices

- One accountable owner per risk.
- Control owners must know their evidence obligations.
- Internal audit should remain independent from operating controls.
- Security may facilitate risk decisions but should not accept business risk silently.

## Evidence

- role descriptions
- RACI matrix
- governance terms of reference
- risk owner approvals
- action trackers


## Practical example

Two department heads each believe they are accountable for access reviews. The ISMS manager facilitates a RACI workshop where each lists their responsibilities. It emerges that one owns the application and the other owns the identity infrastructure. They agree the application owner is Accountable for the access review, the identity team is Responsible for executing it, and both are Consulted on exceptions. The resulting RACI entry is documented in the governance terms of reference and reviewed after the next access-review cycle.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
