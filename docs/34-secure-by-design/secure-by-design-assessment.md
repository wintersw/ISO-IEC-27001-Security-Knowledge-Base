---
title: Secure by Design Assessment
description: Assessment model for product and service security maturity.
category: Secure by Design
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - secure-by-design
  - product-security
  - devsecops
---

# Secure by Design Assessment

## Assessment domains

- ownership of customer outcomes
- secure defaults
- identity and access
- logging and transparency
- vulnerability response
- update mechanism
- architecture assurance
- customer evidence
- support and end-of-life
- security metrics

## Sample assessment question

> Can a small customer achieve a reasonably secure baseline without purchasing additional security features or hiring specialist administrators?

A weak answer reveals transferred security burden.

## Maturity interpretation

- **Reactive:** security depends on customer configuration and incident response.
- **Defined:** secure development and review processes exist.
- **Operating:** secure defaults and customer evidence are standard.
- **Measured:** customer exposure and security adoption are tracked.
- **Adaptive:** product design removes recurring vulnerability classes and customer burden.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **Secure by Design Assessment** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Practical example

A product team applies this guidance before approving an architecture. It records customer security outcomes, evaluates abuse cases, selects safe defaults, and verifies the controls before release.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- security requirements and architecture decision
- threat or abuse-case analysis
- test and release evidence
- accepted exceptions and vulnerability follow-up

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
