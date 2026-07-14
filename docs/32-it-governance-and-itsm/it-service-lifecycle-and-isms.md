---
title: IT Service Lifecycle and ISMS
description: How IT service strategy, design, transition, operation, and improvement connect to security.
category: IT Governance and ITSM
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - it-governance
  - itsm
  - isms
---

# IT Service Lifecycle and information security management system (ISMS)

Every IT service has a lifecycle, and the ISMS should influence each stage.

```mermaid
flowchart LR
    A[Strategy / Need] --> B[Service Design]
    B --> C[Build / Transition]
    C --> D[Operate]
    D --> E[Monitor and Review]
    E --> F[Improve or Retire]
    F --> A
```

## Security by lifecycle stage

### Strategy / need

Identify business objective, expected data, interested-party requirements, and risk appetite.

### Design

Review architecture, privacy, suppliers, recovery objectives, logging, monitoring, and access model.

### Build / transition

Implement secure configuration, security testing, change approval, user training, and evidence setup.

### Operate

Operate incident management, access management, vulnerability management, monitoring, backup, and supplier review.

### Improve or retire

Perform lessons learned, risk reassessment, decommissioning, data deletion, and evidence retention.

## Best practices

- Make security requirements part of service design packages.
- Define logging and access controls before production.
- Include security acceptance criteria in release readiness.
- Review services after incidents or significant changes.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **IT Service Lifecycle and ISMS** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
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
