---
title: Application Access and SASE
description: Modern application access patterns including ZTNA and SASE.
category: Zero Trust and Data-Centric Security
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - SASE
  - ZTNA
  - zero-trust
---

# Application Access and SASE
SASE combines networking and cloud-delivered security capabilities. zero trust network access (ZTNA) applies Zero Trust principles to application access.

## Capability areas

- ZTNA
- secure web gateway
- cloud access security broker
- firewall as a service
- software-defined wide area network (SD-WAN)
- data loss prevention (DLP)
- device posture integration
- identity integration
- centralized policy

## virtual private network (VPN) migration considerations

Traditional VPN can create broad network access. A Zero Trust approach should prefer access to specific applications and resources rather than implicit access to large network segments.

## Evidence

- application access policy
- SASE/ZTNA architecture
- migration plan
- access logs
- exception register

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

An organization retires a legacy VPN that granted contractors access to entire network segments. Each contractor application is published through ZTNA instead: access requires verified identity, a compliant device, and is limited to the single application. The team tests that a contractor can reach the approved app but can no longer scan or reach neighboring servers, and logs both outcomes as migration evidence.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
