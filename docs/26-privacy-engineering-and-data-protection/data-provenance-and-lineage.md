---
title: Data Provenance and Lineage
description: Tracking origin, transformation, movement, and derivation of data.
category: Privacy Engineering and Data Protection
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - lineage
  - provenance
---

# Data Provenance and Lineage

Data provenance records where data came from. Data lineage records how it moved and changed.

## Why it matters

- breach impact analysis
- artificial intelligence (AI) training governance
- data quality
- auditability
- privacy rights handling
- deletion propagation
- model explainability
- supplier assurance

## Lineage fields

- source
- timestamp
- transformation
- destination
- owner
- purpose
- classification
- retention
- access rules
- derived outputs
- deletion dependency

## Typical evidence

- lineage records for key datasets showing source, transformations, and destinations
- provenance documentation for AI training datasets
- deletion-dependency mapping between source data and derived outputs
- lineage traces used in breach impact or rights-request handling
- review records keeping lineage current after pipeline changes

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

A customer submits a deletion request, but their data has already flowed into a data warehouse, two dashboards, and a churn-prediction training set. Because the team maintains lineage records with deletion dependencies, it can locate every derived copy, propagate the deletion, and evidence completion — instead of deleting only the CRM record and leaving untracked copies behind.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
