---
title: Secure Product Metrics
description: Metrics that measure security outcomes rather than feature counts.
category: Secure by Design
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - secure-by-design
  - product-security
  - devsecops
---

# Secure Product Metrics

## Useful metrics

| Metric | What it reveals |
|---|---|
| privileged users without multifactor authentication (MFA) | account takeover exposure |
| security logs available to customers | investigative capability |
| known critical vulnerabilities past target | product risk |
| insecure defaults remaining | design debt |
| security-related support cases | usability and configuration problems |
| mean time to deliver security fix | response capability |
| tenants using recommended configuration | adoption |
| repeated vulnerability class | engineering weakness |

## Interpretation example

A falling vulnerability count may be positive, but it may also reflect reduced testing. Pair the metric with test coverage, asset scope, and recurrence analysis.

## Best practices

- measure customer exposure
- include severity and affected population
- report trends
- link metrics to release decisions
- avoid vanity metrics


## Practical example

A product team notices that "privileged users without MFA" has been stuck at 12% for two quarters despite MFA being available. Deeper analysis reveals that legacy administrator accounts created before MFA enforcement are exempt. The team adds a forced MFA enrollment workflow for legacy accounts, sets a 90-day grace period, and tracks the metric weekly. Within one quarter, unprotected privileged users drop below 2%.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- security requirements and architecture decision
- threat or abuse-case analysis
- test and release evidence
- accepted exceptions and vulnerability follow-up


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
