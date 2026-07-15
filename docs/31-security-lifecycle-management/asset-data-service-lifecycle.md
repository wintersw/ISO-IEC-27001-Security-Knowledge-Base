---
title: Asset, Data, and Service Lifecycle
description: How assets, data, and services should be governed from creation to retirement.
category: Security Lifecycle Management
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-lifecycle
  - isms
---

# Asset, Data, and Service Lifecycle

Security teams often maintain inventories, but lifecycle management goes further. It asks what happens before an item appears in the inventory and what happens after it is no longer used.

```mermaid
flowchart LR
    A[Request / Need] --> B[Classify and Assign Owner]
    B --> C[Risk and Security Review]
    C --> D[Approve and Implement]
    D --> E[Operate and Monitor]
    E --> F[Review and Re-certify]
    F --> G[Retire, Delete, or Archive]
```

## Example: customer dataset

A customer dataset is created for analytics. The data owner classifies it as confidential. The information security management system (ISMS) team identifies risks such as unauthorized export, secondary use, re-identification, and over-retention. Controls include restricted access, approved purpose, data minimization, export logging, retention rules, and deletion evidence.

## Best practices

- Do not separate data ownership from system ownership without defining how the roles cooperate.
- Classify data before selecting storage and access controls.
- Link critical services to recovery objectives and supplier dependencies.
- Require retirement records for systems, datasets, accounts, certificates, keys, and suppliers.
- Include shadow data, exports, logs, caches, and backups in lifecycle thinking.

## Lifecycle decision prompts

| Stage | Security decisions | Evidence examples |
|---|---|---|
| Need and initiation | What business outcome is needed, what information is involved, who owns it, and which obligations or risks apply? | approved request, owner, initial classification and risk screen |
| Acquisition or design | Which requirements, architecture constraints, supplier duties, recovery needs, and acceptance criteria apply? | requirements traceability, design and supplier reviews |
| Build, migration, or onboarding | Were configurations, identities, keys, data transfers, dependencies, and rollback arrangements implemented securely? | build records, migration reconciliation, onboarding approval |
| Verification and acceptance | Were requirements tested against representative normal, misuse, failure, and recovery cases, and who accepted residual risk? | test results, exceptions, risk acceptance, release decision |
| Operation and monitoring | Are access, changes, vulnerabilities, backups, logging, incidents, capacity, suppliers, and control evidence managed against defined criteria? | operating records, measures, reviews, exception logs |
| Change or transfer | Does the change affect classification, ownership, data location, interfaces, obligations, recovery, evidence, or downstream consumers? | impact assessment, updated requirements and risk records |
| Retention, archive, and retirement | What must be retained, transferred, revoked, returned, deleted, destroyed, or independently verified? | retention decision, access and key revocation, deletion or destruction evidence |

Use the [Security Requirements Traceability Template](../10-templates/security-requirements-traceability-template.md) to keep the driver-to-evidence chain current across these stages.

## Related chapters

- [Data Security Lifecycle](../25-data-security-governance/data-security-lifecycle.md)
- [Data Flow Mapping](../25-data-security-governance/data-flow-mapping.md)
- [Asset Inventory Template](../10-templates/asset-inventory-template.md)
- [Data Asset Register Template](../10-templates/data-asset-register-template.md)


## Practical example

A process owner applies this lifecycle to a scoped service from initiation through change and retirement, defines decision gates and evidence at each stage, and reviews exceptions before closure.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- lifecycle record with owner and scope
- stage approvals and operating records
- exceptions and remediation actions
- closure and retained-evidence record

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
