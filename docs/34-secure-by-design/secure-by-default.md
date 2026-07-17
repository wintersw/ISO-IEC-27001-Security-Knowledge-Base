---
title: Secure by Default
description: How to design default configurations that reduce customer risk.
category: Secure by Design
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - secure-by-design
  - product-security
  - devsecops
---

# Secure by Default

Secure by default means that a product starts in a reasonably protected state without requiring extensive customer configuration.

## Example: cloud storage

An insecure product may create storage that is publicly accessible unless the customer changes permissions. A secure-by-default product blocks public access, warns clearly before exposure, logs changes, and allows policy-level prevention.

## Example: administrative access

A secure product should not ship with shared administrator credentials. It should require unique identity, strong authentication, controlled recovery, and audit logging.

## Design checklist

- strong authentication
- least privilege
- secure network exposure
- logging enabled
- encryption enabled
- safe session settings
- secure application programming interface (API) configuration
- automatic updates
- recovery controls
- visible warnings for risky changes

## Common mistakes

- marketing “secure by default” while leaving key controls optional
- providing logs only in expensive tiers
- relying on customers to disable legacy protocols
- shipping broad roles for convenience
- making secure configuration operationally difficult


## Practical example

A product team designing a new file-sharing feature must choose the default permission model. The secure-by-default approach sets newly shared files to "specific people only" with viewer permission, requires explicit confirmation to broaden access, logs all permission changes, and allows administrators to prevent public sharing through organizational policy. The team documents the decision and tests that ordinary use follows the restricted path while broader sharing requires a visible, deliberate action.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- security requirements and architecture decision
- threat or abuse-case analysis
- test and release evidence
- accepted exceptions and vulnerability follow-up


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
