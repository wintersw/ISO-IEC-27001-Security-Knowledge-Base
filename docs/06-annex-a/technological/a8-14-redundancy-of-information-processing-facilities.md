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

The purpose of A.8.14 is to reduce the likelihood or impact of failures related to **redundancy of information processing facilities**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

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

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
