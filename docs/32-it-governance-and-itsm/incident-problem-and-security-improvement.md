---
title: Incident, Problem, and Security Improvement
description: How ITSM incident and problem management connect to security improvement.
category: IT Governance and ITSM
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - it-governance
  - itsm
  - isms
---

# Incident, Problem, and Security Improvement

IT Service Management (ITSM) distinguishes between restoring service and removing root cause. Security needs both.

## Incident management

Incident management restores service or contains impact.

Example: disable a compromised account and block malicious IPs.

## Problem management

Problem management investigates root cause and prevents recurrence.

Example: identify that multifactor authentication (MFA) was missing for a legacy application and add it to the improvement backlog.

## information security management system (ISMS) improvement

The ISMS ensures lessons learned update risks, controls, training, evidence, and management decisions.

Example: the risk register is updated, access-control policy is revised, and management approves funding for legacy single sign-on (SSO) integration.

## Best practices

- Link security incidents to problems where recurrence is likely.
- Use problem records as inputs to corrective action.
- Track known errors and compensating controls.
- Include incident trends in management review.
- Do not close lessons learned without effectiveness review.


## Practical example

A series of phishing incidents leads to several account compromises. Incident management contains each event by resetting credentials and blocking sessions. Problem management investigates and finds that a legacy application does not support MFA and that users reuse credentials across services. The ISMS improvement loop updates the risk register, adds MFA enforcement to the access-control policy, funds legacy-application modernization, and measures recurrence at the next management review.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- service or configuration record
- risk, approval, and segregation-of-duties evidence
- test and implementation logs
- post-implementation review and follow-up actions


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
