---
title: Data-Centric Security Architecture
description: Architecture model that protects data independent of location, device, application, and network.
category: Data Security Governance
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - architecture
  - data-centric
---

# Data-Centric Security Architecture

Data-centric security protects the data itself instead of relying only on network or application boundaries.

## Architecture principles

- classify before protecting
- attach ownership to data
- protect data wherever it moves
- enforce access near the data
- monitor actual data access
- minimize copies and exports
- protect derived and aggregated data
- keep deletion and retention enforceable
- design for breach investigation

## Control layers

| Layer | Control examples |
|---|---|
| identity | multifactor authentication (MFA), conditional access, service identity |
| authorization | role-based access control (RBAC), attribute-based access control (ABAC), policy decision points |
| data protection | encryption, tokenization, masking |
| data movement | application programming interface (API) gateways, data loss prevention (DLP), secure transfer |
| monitoring | data access logging, anomaly detection |
| governance | ownership, classification, retention |
| assurance | control testing, evidence register |

## Design questions

- Where is the authoritative data source?
- Where are copies created?
- Which users and services can read or modify data?
- How is access logged?
- Can data be masked for non-production use?
- Are keys and secrets managed separately?
- Is deletion enforceable across backups and replicas?

## Typical evidence

- approved data-centric architecture design and review records
- documentation of policy decision and enforcement points for data access
- encryption, tokenization, and masking design records with key-management separation
- data access logging configuration and sample monitoring output
- register of authoritative data sources and approved copies

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

An architecture review of a reporting platform finds that anyone on the internal network can query the data warehouse. The team moves enforcement to the data layer: attribute-based access policies at the warehouse, dynamic masking for analysts, static masking for non-production copies, and centralized data access logging — so the data stays protected even when network boundaries change.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
