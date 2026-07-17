---
title: Incident vs Data Breach
description: Distinguish events, incidents, and data breaches.
category: Incident and Data Breach Management
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - incident
  - breach
---

# Incident vs Data Breach

## Definitions for operating use

| Term | Practical meaning |
|---|---|
| event | observable occurrence that may be benign or suspicious |
| security incident | event or set of events that compromises or threatens security |
| data breach | incident involving unauthorized access, disclosure, loss, alteration, or destruction of protected data |
| personal data breach | breach affecting personal data and potentially individuals' rights or interests |

## Why distinction matters

- escalation differs
- legal notification may differ
- evidence needs differ
- privacy involvement may differ
- management reporting differs
- communication and customer impact differ

## Typical evidence

- documented definitions distinguishing events, incidents, and breaches
- incident classification records showing breach determination decisions
- escalation records where privacy or legal teams were engaged for breaches
- separate handling paths evidenced in incident tickets
- training materials covering the distinction for responders

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

A firewall drops thousands of scan attempts (events, no action needed). One scan finds an unpatched server and deploys a web shell (security incident — escalated, contained, no data accessed). Weeks later, the review of a similar incident on another server shows customer records were exfiltrated — now it is a data breach: privacy and legal join, notification analysis starts, and evidence preservation becomes mandatory. Classifying each level correctly drove three different responses.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
