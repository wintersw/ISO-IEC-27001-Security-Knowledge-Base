---
title: Microsegmentation and Network Control
description: Segmentation patterns to limit lateral movement and protect sensitive resources.
category: Zero Trust and Data-Centric Security
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - microsegmentation
  - network-security
---

# Microsegmentation and Network Control

Microsegmentation limits which workloads, users, and services can communicate.

## Use cases

- isolate critical databases
- protect administration interfaces
- separate development/test/production
- contain ransomware
- control east-west traffic
- limit supplier or remote access

## Design steps

1. identify protect surface
2. map normal flows
3. define allowed flows
4. block everything else
5. monitor denied flows
6. tune policy
7. test incident containment

## Typical evidence

- documented protect surfaces and mapped normal traffic flows
- approved allow-list segmentation policy per zone or workload
- denied-flow monitoring reports and tuning records
- segmentation test results, including incident containment exercises
- change records for firewall or policy modifications

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

After mapping flows to its payment database, a team finds 200+ servers can reach it although only three application servers need to. Microsegmentation policy allows just those three flows and blocks the rest. A later ransomware tabletop confirms the containment value: an infected workstation in the office VLAN has no route to the payment zone, and the denied-flow logs provide test evidence.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
