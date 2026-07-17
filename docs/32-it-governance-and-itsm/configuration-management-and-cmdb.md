---
title: Configuration Management and CMDB for ISMS
description: How configuration management supports asset inventory, risk, incident response, and audit evidence.
category: IT Governance and ITSM
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - it-governance
  - itsm
  - isms
---

# Configuration Management and CMDB for ISMS
A configuration management database (CMDB) or equivalent asset repository helps the information security management system (ISMS) understand what exists, who owns it, and how it supports business services.

## Why configuration management matters

Security processes depend on accurate asset and dependency information. Vulnerability management needs asset ownership. Incident response needs dependency maps. Risk assessment needs criticality. Business continuity needs recovery priorities. Audit needs scope evidence.

## Minimum useful fields

| Field | Why it matters |
|---|---|
| asset/service name | identification |
| owner | accountability |
| business service | impact analysis |
| environment | production/test/development |
| data classification | protection requirements |
| criticality | prioritization |
| supplier dependency | third-party risk |
| recovery objective | continuity |
| logging status | incident readiness |
| patch group | vulnerability management |

## Common mistakes

- CMDB exists but is not trusted.
- Security asset inventory and CMDB disagree.
- Cloud assets are missing.
- software as a service (SaaS) services are managed outside IT.
- Ownership is outdated.
- Dependencies are not mapped.

## Best practices

- Reconcile automated discovery with owner validation.
- Include SaaS, cloud, APIs, data stores, and identity platforms.
- Use configuration data in risk and incident workflows.
- Treat missing ownership as a security finding.


## Practical example

During a ransomware incident, the incident-response team uses the CMDB to identify configuration items supporting the affected service, their owners, data classifications, dependencies, and recovery objectives. Trusted configuration data accelerates containment decisions, owner notification, and recovery prioritization; the team verifies critical relationships against current technical evidence rather than assuming the CMDB is complete.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- service or configuration record
- risk, approval, and segregation-of-duties evidence
- test and implementation logs
- post-implementation review and follow-up actions


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
