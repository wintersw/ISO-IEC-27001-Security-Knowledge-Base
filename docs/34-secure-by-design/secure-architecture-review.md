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

A multi-tenant SaaS analytics service uses shared infrastructure. Review should confirm tenant identifiers are enforced in every data query, background job, cache, export, and support workflow. Testing should include attempts to cross tenant boundaries.

## Best practices

- use diagrams to make trust boundaries visible
- record assumptions
- include operational teams
- review failure and recovery behavior
- link findings to the risk register
- verify high-risk decisions after implementation
