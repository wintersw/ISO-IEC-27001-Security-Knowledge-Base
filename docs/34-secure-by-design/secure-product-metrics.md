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
| privileged users without MFA | account takeover exposure |
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
