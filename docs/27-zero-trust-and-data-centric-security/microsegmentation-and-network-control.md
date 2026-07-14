---
title: Microsegmentation and Network Control
description: Segmentation patterns to limit lateral movement and protect sensitive resources.
category: Zero Trust and Data-Centric Security
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - microsegmentation
  - network-security
---

# Microsegmentation and Network Control

Microsegmentation limits which workloads, users, and services can communicate.

## Use cases

- isolate critical databases
- protect administration interfaces
- separate development/test/production
- contain ransomware
- control east-west traffic
- limit supplier or remote access

## Design steps

1. identify protect surface
2. map normal flows
3. define allowed flows
4. block everything else
5. monitor denied flows
6. tune policy
7. test incident containment


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
