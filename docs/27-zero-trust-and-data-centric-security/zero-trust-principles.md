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

- approved policy, standard, procedure, or architecture record
- risk assessment or design review
- owner and role assignment
- implementation plan
- operating records
- monitoring records
- exception or waiver decisions
- test results
- audit records
- management review decisions

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **Zero Trust Principles** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Practical example

A service owner replaces a broad network-trust assumption with a policy based on verified identity, device condition, resource sensitivity, and monitored sessions, then tests both permitted and denied access paths.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
