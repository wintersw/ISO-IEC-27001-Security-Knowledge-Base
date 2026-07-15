---
title: ITSM Evidence for ISO 27001
description: How to reuse ITSM records as ISO 27001 evidence.
category: IT Governance and ITSM
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - it-governance
  - itsm
  - isms
---

# information technology service management (ITSM) Evidence for ISO 27001

ITSM tools can be excellent information security management system (ISMS) evidence sources when workflows are designed well.

## Evidence examples

| ITSM record | ISO 27001 evidence use |
|---|---|
| incident ticket | incident handling, response, lessons learned |
| change ticket | operational control, approval, rollback, testing |
| problem record | root cause and corrective action |
| service request | access request and approval |
| configuration item | asset inventory and dependency mapping |
| knowledge article | documented procedure or work instruction |
| release record | secure deployment evidence |
| service-level agreement (SLA) report | service performance and availability |
| supplier ticket | third-party operational evidence |

## Evidence quality rules

- records must be complete
- approvals must be visible
- timestamps must be preserved
- owners must be identifiable
- scope and affected assets must be clear
- closure must include outcome
- attachments and linked records must be retained

## Best practices

- Add security-specific fields to ITSM workflows.
- Link tickets to assets and services.
- Use automated reports for recurring evidence.
- Preserve historical workflow records for audit periods.
- Train control owners on how to retrieve evidence.


## Practical example

A service owner applies this guidance to a production change, connects the service-management decision to security risk, records approval and testing, and verifies the outcome after implementation.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
