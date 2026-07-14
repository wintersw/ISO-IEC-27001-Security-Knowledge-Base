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
| identity | MFA, conditional access, service identity |
| authorization | RBAC, ABAC, policy decision points |
| data protection | encryption, tokenization, masking |
| data movement | API gateways, DLP, secure transfer |
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
