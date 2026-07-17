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

- current data flow maps for in-scope systems and processes
- flow records with source, destination, classification, transfer mechanism, and protection
- register of third-party and cross-border transfers
- review records showing maps are updated after system or integration changes
- examples of flow maps used in risk assessments or breach triage

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

During a suspected CRM breach, the response team pulls the data flow map and sees that customer profiles flow nightly via API to the data warehouse and weekly as a CSV export to a marketing SaaS. Within an hour they know which copies exist, which third party must be contacted, and which API gateway logs to preserve — instead of discovering the export weeks later.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
