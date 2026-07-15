---
title: Data Security Control Catalog
description: Control catalog for protecting sensitive data across the lifecycle.
category: Data Security Governance
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - control-catalog
  - data-security
---

# Data Security Control Catalog

This catalog supplements Annex A with data-specific implementation patterns.

## Control catalog

| Control area | Example controls |
|---|---|
| discovery | sensitive data scanning, data cataloging |
| classification | classification policy, labeling, handling rules |
| access | least privilege, access reviews, attribute-based access control (ABAC) |
| encryption | encryption at rest, in transit, key rotation |
| masking | dynamic masking, static masking, tokenization |
| data loss prevention (DLP) | egress rules, upload restrictions, alerting |
| deletion | deletion workflows, retention rules, deletion logs |
| monitoring | data access logs, anomalous download detection |
| sharing | sharing approvals, contractual controls |
| analytics | minimization, aggregation, privacy review |
| backups | backup encryption, restore testing |
| incident response | breach triage and evidence preservation |

## Control selection logic

Select controls based on:

- classification
- business impact
- legal obligation
- data subject impact
- threat model
- processing location
- supplier involvement
- retention period

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
