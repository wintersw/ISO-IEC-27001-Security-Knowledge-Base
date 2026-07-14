---
title: ITIL 4 Practices and Security
description: How ITIL-style service management practices provide evidence and operation for the ISMS.
category: IT Governance and ITSM
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - it-governance
  - itsm
  - isms
---

# ITIL 4 Practices and Security

ITIL 4 service management practices can support security objectives. The information security management system (ISMS) should reuse these workflows instead of creating duplicate security-only processes.

## information technology service management (ITSM) practices that support the ISMS

| ITSM practice | ISMS contribution |
|---|---|
| incident management | security event handling, escalation, evidence |
| change enablement | secure change, approval, rollback, audit trail |
| service configuration management | asset and dependency visibility |
| problem management | root cause analysis and recurring incident reduction |
| service continuity management | resilience, recovery, availability |
| supplier management | third-party risk and service obligations |
| service desk | user reporting channel and request evidence |
| monitoring and event management | detection and operational visibility |
| release management | secure deployment evidence |
| knowledge management | procedures, known errors, user guidance |
| continual improvement | improvement backlog and lessons learned |

## Example: change enablement

A change ticket can provide evidence of business request, security impact assessment, test results, approval, implementation date, rollback plan, and post-implementation review.

## Best practices

- Add security fields to existing ITSM tickets.
- Use change records as ISMS evidence.
- Link incidents to risks and problems.
- Use problem management for recurring security weaknesses.
- Use configuration management to improve asset and dependency visibility.
- Train service desk staff to recognize security events.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **ITIL 4 Practices and Security** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
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
