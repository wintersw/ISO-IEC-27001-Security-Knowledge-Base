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

Data flow mapping makes invisible data movement visible. It supports risk assessment, privacy engineering, data loss prevention (DLP), Zero Trust, breach response, and supplier assurance.

## What to map

- source systems
- data stores
- APIs
- file transfers
- software as a service (SaaS) platforms
- analytics platforms
- backups
- logs
- reports
- exports
- third-party processors
- cross-border transfers
- artificial intelligence (AI)/machine learning (ML) pipelines

## Minimum flow attributes

| Attribute | Example |
|---|---|
| source | customer relationship management (CRM) |
| destination | data warehouse |
| data type | customer profile, transaction |
| classification | confidential |
| purpose | reporting |
| transfer mechanism | application programming interface (API) |
| protection | Transport Layer Security (TLS), token auth, service account |
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


## Practical example

A data owner applies this guidance to a customer-data set, records its purpose and sensitivity, approves access and handling rules, and reviews evidence when the data or its processing changes.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
