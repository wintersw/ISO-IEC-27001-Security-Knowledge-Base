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

ITIL 4 service management practices can support security objectives. The ISMS should reuse these workflows instead of creating duplicate security-only processes.

## ITSM practices that support the ISMS

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
