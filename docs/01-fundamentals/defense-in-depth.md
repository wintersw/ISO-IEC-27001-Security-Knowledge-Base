---
title: Defense in Depth
description: Explains layered security and how controls support one another.
category: Fundamentals
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - fundamentals
---

# Defense in Depth

Defense in depth means using multiple layers of controls so that failure of one control does not automatically result in compromise.

## Example layers

- governance and policy
- awareness and training
- identity and access control
- endpoint protection
- network segmentation
- secure configuration
- vulnerability management
- logging and monitoring
- incident response
- backup and recovery

## Why this matters

No single control is perfect. multifactor authentication (MFA) can be bypassed, users can make mistakes, patches can fail, and alerts can be missed. Layered controls reduce reliance on any single safeguard.

## ISO perspective

Annex A controls are designed to work together. Access control, logging, monitoring, incident response, backup, supplier management, and secure development all reinforce each other.

## Evidence

- architecture diagrams
- control mappings
- risk treatment plans
- monitoring dashboards
- incident lessons learned

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **Defense in Depth** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Practical example

A team designing a customer-facing service uses this concept to compare design options. It records the chosen safeguard, the risk it addresses, and how the team will verify the intended security outcome.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
