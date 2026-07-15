---
title: Secure Architecture Review
description: Architecture review process for trust boundaries, data flows, identity, failure modes, and evidence.
category: Secure by Design
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - secure-by-design
  - product-security
  - devsecops
---

# Secure Architecture Review

Architecture review should evaluate how the product behaves under attack, failure, misuse, and operational change.

## Review areas

- trust boundaries
- identity and authorization
- data flows
- tenant isolation
- secrets and key management
- logging and monitoring
- availability and recovery
- dependency risk
- update mechanism
- administrative interfaces
- privacy and data retention

## Example

A multi-tenant software as a service (SaaS) analytics service uses shared infrastructure. Review should confirm tenant identifiers are enforced in every data query, background job, cache, export, and support workflow. Testing should include attempts to cross tenant boundaries.

## Best practices

- use diagrams to make trust boundaries visible
- record assumptions
- include operational teams
- review failure and recovery behavior
- link findings to the risk register
- verify high-risk decisions after implementation


## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- security requirements and architecture decision
- threat or abuse-case analysis
- test and release evidence
- accepted exceptions and vulnerability follow-up

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
