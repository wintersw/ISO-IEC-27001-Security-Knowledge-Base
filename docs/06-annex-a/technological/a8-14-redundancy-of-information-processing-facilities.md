---
title: A.8.14 Redundancy of information processing facilities
description: Practical implementation, evidence, and audit guidance for A.8.14.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.14 Redundancy of information processing facilities

## Overview

Redundancy uses independent components, paths, or facilities so a single failure does not remove a required service. It should be designed against realistic failure modes and tested rather than assumed from duplicate components.

## Purpose

This control ensures that information processing facilities have sufficient redundancy to meet availability requirements, so that a single component, path, or facility failure does not cause unacceptable service disruption. Redundancy must be designed against realistic failure modes and regularly tested — not assumed from architecture diagrams.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.14 when selected or otherwise committed to.
- **Implementation guidance:** Define **redundancy of information processing facilities** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- restore tests successful
- recovery time objective (RTO)/recovery point objective (RPO) achieved
- critical services tested
- recovery actions overdue

## Practical example

A service runs in separate failure zones with independent network and database capacity. A controlled failover test confirms routing, data consistency, monitoring, staffing, and supplier behavior and measures whether recovery objectives are met.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Redundancy exists on paper (dual power supplies, clustered nodes) but shared failure domains — like a single network switch or power bus — are overlooked.
- Failover is configured but never tested, and the first real failover reveals configuration gaps or data inconsistency.
- Redundancy is designed for component failure but not for facility-level events (fire, flood, cooling loss).
- Redundant components share the same management plane — a misconfiguration propagates to both sides simultaneously.

## Auditor questions

- What failure scenarios were considered in the redundancy design, and how were they validated?
- When was the last failover test, and were recovery time objectives met?
- How are redundant components kept synchronized, and how is split-brain prevented?
- Show evidence that critical services can survive a single component, path, or facility failure.

## Checklist

- [ ] redundancy requirements defined per service criticality
- [ ] failure mode analysis performed and documented
- [ ] failover tested and recovery objectives validated
- [ ] shared failure domains identified and mitigated
- [ ] redundant component synchronization monitored
- [ ] facility-level redundancy considered for critical services

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
