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

No single control is perfect. Multifactor authentication (MFA) can be bypassed, users can make mistakes, patches can fail, and alerts can be missed. Layered controls reduce reliance on any single safeguard. This principle complements [least privilege](least-privilege.md) and [Zero Trust](zero-trust.md).

## ISO perspective

Annex A controls are designed to work together. Access control, logging, monitoring, incident response, backup, supplier management, and secure development all reinforce each other.

## Evidence

- architecture diagrams
- control mappings
- risk treatment plans
- monitoring dashboards
- incident lessons learned


## Practical example

A targeted spear-phishing campaign illustrates layered defense: the email bypasses the spam filter (layer 1 fails). The recipient clicks the link, but the browser's safe-browsing check blocks the credential-harvesting page (layer 2 succeeds). Even if credentials were stolen, MFA would likely block reuse of the password alone (layer 3). Endpoint detection identifies a staged payload on another machine (layer 4), and the SOC receives an alert within minutes (layer 5). The post-incident review maps each layer that contributed to containment and identifies the email-filter tuning gap.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
