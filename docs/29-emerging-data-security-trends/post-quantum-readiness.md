---
title: Post-Quantum Readiness
description: Cryptography inventory and migration planning for post-quantum cryptography.
category: Emerging Data Security Trends
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - post-quantum
  - cryptography
---

# Post-Quantum Readiness

Post-quantum readiness prepares the organization for cryptographic migration before quantum-capable attacks become practical.

## Why now

NIST approved the first three post-quantum cryptography FIPS standards in 2024: FIPS 203, FIPS 204, and FIPS 205. Organizations should begin with inventory, dependency analysis, risk prioritization, and migration planning rather than waiting for emergency replacement.

## Readiness steps

1. inventory cryptographic use
2. identify long-lived sensitive data
3. identify external dependencies
4. classify systems by migration priority
5. review protocols and libraries
6. plan hybrid or migration approaches
7. update procurement requirements
8. track vendor readiness
9. test in non-production
10. report progress to management

## High-priority areas

- Transport Layer Security (TLS) and virtual private network (VPN)
- public key infrastructure (PKI)
- code signing
- firmware signing
- backups and archives
- regulated long-lived data
- customer-facing APIs
- identity federation

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


## Practical example

A technology-risk forum evaluates this topic before adoption, separates demonstrated risk from speculation, runs a limited assessment, and records monitoring triggers for revisiting the decision.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
