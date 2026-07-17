---
title: Problem Management for Security
description: Using problem management to remove recurring security causes.
category: IT Governance and ITSM
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - it-governance
  - itsm
  - cobit
  - itil
---

# Problem Management for Security

Incident management restores normal service or contains damage. Problem management investigates why incidents or control failures recur.

## Example

Several phishing incidents lead to account compromise. The immediate response resets passwords and blocks sessions. Problem analysis finds that a legacy application does not support modern multifactor authentication (MFA) and that users reuse credentials.

The problem record coordinates:

- legacy authentication replacement
- conditional-access improvement
- awareness changes
- monitoring updates
- risk acceptance during transition
- effectiveness review

## Known errors

A known error is a documented problem with an understood cause or workaround.

Example:

> Legacy system cannot support MFA. Temporary control requires restricted network access, monitored privileged use, and monthly risk review until replacement.

## Best practices

- Open problems for recurring incidents, repeat findings, and systemic control failures.
- Link problems to risk and corrective action.
- Track workarounds and expiry.
- Include business and technical owners.
- Verify that the fix reduces recurrence.


## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- service or configuration record
- risk, approval, and segregation-of-duties evidence
- test and implementation logs
- post-implementation review and follow-up actions


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
