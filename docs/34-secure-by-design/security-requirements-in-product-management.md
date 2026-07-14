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

- administrators must use MFA
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
