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
