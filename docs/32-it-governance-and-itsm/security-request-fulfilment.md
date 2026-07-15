---
title: Security Request Fulfilment
description: Designing repeatable ITSM request workflows for common security needs.
category: IT Governance and ITSM
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - it-governance
  - itsm
  - cobit
  - itil
---

# Security Request Fulfilment

Security requests are predictable, user-initiated needs that should be fulfilled through controlled workflows rather than informal messages.

## Common security request types

- user access
- privileged access
- firewall rule
- certificate
- data export
- encryption key
- supplier account
- security exception
- vulnerability scan
- security architecture review

## Example: privileged-access request

A good workflow captures:

- requester and target system
- business justification
- requested privilege
- duration
- owner approval
- security approval where required
- strong authentication requirement
- session logging
- expiry and removal
- post-use review for emergency access

## Best practices

- Use pre-defined request models.
- Separate request, approval, fulfillment, and verification.
- Link requests to assets and services.
- Require expiry for temporary access.
- Automatically retain evidence.
- Measure fulfillment time and exception rate without sacrificing control quality.


## Practical example

A service owner applies this guidance to a production change, connects the service-management decision to security risk, records approval and testing, and verifies the outcome after implementation.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- service or configuration record
- risk, approval, and segregation-of-duties evidence
- test and implementation logs
- post-implementation review and follow-up actions

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
