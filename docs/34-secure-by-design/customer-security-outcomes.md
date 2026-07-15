---
title: Customer Security Outcomes
description: How product teams translate security features into measurable customer outcomes.
category: Secure by Design
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - secure-by-design
  - product-security
  - devsecops
---

# Customer Security Outcomes

A feature is not the same as an outcome. A product may support multifactor authentication (MFA), but customers remain exposed if MFA is difficult to configure, unavailable for administrators, or disabled by default.

## Outcome-oriented questions

- Can customers prevent common account takeover?
- Can customers detect suspicious access?
- Can customers recover safely?
- Can customers export evidence for investigation?
- Can customers control privileged access?
- Can customers delete data when required?
- Can customers understand supplier dependencies?
- Can customers maintain security during migration?

## Example

Instead of measuring “MFA feature released,” measure:

- percentage of active tenants with MFA
- percentage of privileged users protected by MFA
- number of high-risk accounts without MFA
- time required to enable MFA
- support cases caused by insecure recovery design

## Best practices

- Measure adoption and effectiveness.
- Design security for small customers as well as large enterprises.
- Include customer-facing evidence and audit capabilities.
- Test usability of security controls.
- Treat customer workarounds as design feedback.


## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- security requirements and architecture decision
- threat or abuse-case analysis
- test and release evidence
- accepted exceptions and vulnerability follow-up

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
