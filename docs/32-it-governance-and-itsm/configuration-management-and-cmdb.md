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

# Configuration Management and CMDB for information security management system (ISMS)

A configuration management database or equivalent asset repository helps the ISMS understand what exists, who owns it, and how it supports business services.

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

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **Configuration Management and CMDB for ISMS** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Practical example

A service owner applies this guidance to a production change, connects the service-management decision to security risk, records approval and testing, and verifies the outcome after implementation.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- service or configuration record
- risk, approval, and segregation-of-duties evidence
- test and implementation logs
- post-implementation review and follow-up actions

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
