---
title: Data Flow Mapping
description: How to map data movement for risk, privacy, breach readiness, and control design.
category: Data Security Governance
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - data-flow
  - privacy
  - breach
---

# Data Flow Mapping

Data flow mapping makes invisible data movement visible. It supports risk assessment, privacy engineering, DLP, Zero Trust, breach response, and supplier assurance.

## What to map

- source systems
- data stores
- APIs
- file transfers
- SaaS platforms
- analytics platforms
- backups
- logs
- reports
- exports
- third-party processors
- cross-border transfers
- AI/ML pipelines

## Minimum flow attributes

| Attribute | Example |
|---|---|
| source | CRM |
| destination | data warehouse |
| data type | customer profile, transaction |
| classification | confidential |
| purpose | reporting |
| transfer mechanism | API |
| protection | TLS, token auth, service account |
| owner | data platform owner |
| logging | API gateway logs |
| retention | seven years |
| third party | yes/no |

## Use in breach response

A good data flow map helps determine:

- what data was exposed
- where copies exist
- which systems were affected
- which parties must be contacted
- what logs to preserve
- what downstream datasets may be impacted


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
