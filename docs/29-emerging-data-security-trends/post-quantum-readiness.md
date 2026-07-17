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

- cryptographic inventory covering protocols, libraries, PKI, and signing
- register of long-lived sensitive data exposed to harvest-now-decrypt-later risk
- migration priority classification and hybrid-approach plans
- procurement requirements and vendor readiness tracking records
- non-production test results for post-quantum algorithms

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

A financial services firm starts its readiness program with inventory, not migration: it catalogs every TLS endpoint, PKI dependency, and code-signing use, then flags archived contracts with 30-year retention as harvest-now-decrypt-later candidates. Vendor readiness for FIPS 203/204/205 goes into procurement questionnaires, and a hybrid key-exchange pilot runs in a test environment — giving management a costed migration roadmap years before it becomes an emergency.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
