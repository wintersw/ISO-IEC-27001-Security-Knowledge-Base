---
title: Device Trust and Endpoint Posture
description: Using endpoint state in access decisions.
category: Zero Trust and Data-Centric Security
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - endpoint
  - device-trust
---

# Device Trust and Endpoint Posture

Device trust evaluates whether a device should be allowed to access a resource.

## Posture signals

- managed or unmanaged
- encryption enabled
- EDR active
- patch level
- jailbreak/root status
- certificate presence
- location and network
- recent suspicious activity
- configuration compliance

## Control pattern

High-risk data access should require a stronger device posture than low-risk access.

## Evidence

- device compliance report
- EDR coverage report
- exception list
- conditional access policy
- endpoint incident trends


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
