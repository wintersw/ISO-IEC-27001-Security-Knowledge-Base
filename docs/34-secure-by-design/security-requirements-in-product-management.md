---
title: Security Requirements in Product Management
description: How product requirements should include customer security, misuse cases, and lifecycle obligations.
category: Secure by Design
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - secure-by-design
  - product-security
  - devsecops
---

# Security Requirements in Product Management

Security requirements should be part of product discovery and planning, not added during final testing.

## Requirement examples

- administrators must use multifactor authentication (MFA)
- all security-relevant actions must be logged
- tenants must be isolated
- sensitive exports must be auditable
- supported cryptography must be documented
- the product must support secure deletion
- risky defaults must require explicit confirmation
- security updates must not require disruptive manual work

## Misuse cases

A misuse case describes how a product could be abused.

Example:

> An attacker with a stolen support account searches all tenants and exports customer records.

Controls may include tenant-scoped authorization, just-in-time support access, approval, session recording, and anomaly detection.

## Best practices

- write security acceptance criteria
- include abuse cases and recovery cases
- involve security architects early
- prioritize security debt with product debt
- include retirement and support-period requirements


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
