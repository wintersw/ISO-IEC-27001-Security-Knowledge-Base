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

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **Secure by Default** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
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
