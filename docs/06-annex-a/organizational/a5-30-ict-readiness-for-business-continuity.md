---
title: A.5.30 ICT readiness for business continuity
description: Practical implementation, evidence, and audit guidance for A.5.30.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.30 ICT readiness for business continuity

## Overview

Information and communication technology readiness connects technology recovery capabilities to business continuity needs. Recovery priorities, dependencies, objectives, procedures, and tests should agree with the business impact analysis.

## Purpose

This control ensures that ICT services can be recovered within agreed timeframes and performance levels to support business continuity objectives. ICT readiness is not a paper plan — it is the demonstrated ability to restore services when everything has gone wrong.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.30 when selected or otherwise committed to.
- **Implementation guidance:** Define **ict readiness for business continuity** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- restore tests successful
- recovery time objective (RTO)/recovery point objective (RPO) achieved
- critical services tested
- recovery actions overdue

## Practical example

A payment service requires a four-hour recovery time. A failover exercise tests identity, database, network, supplier, and monitoring dependencies, measures actual recovery, and creates actions where capability misses the approved objective.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- ICT recovery plans exist but have never been tested — the first real invocation will be during an actual disaster.
- Recovery testing is performed in ideal conditions — the real scenario involves degraded infrastructure, unavailable staff, and missing documentation.
- ICT recovery priorities are not aligned with business impact analysis — critical business processes depend on systems deemed "low priority."
- Supplier dependencies are not accounted for — the organization can restore its systems but the supplier's services remain unavailable.

## Auditor questions

- How are ICT recovery objectives (RTO, RPO) defined and aligned with business continuity requirements?
- When were ICT recovery plans last tested, and what were the results?
- How are supplier dependencies addressed in ICT recovery planning?
- Show evidence that test findings resulted in plan improvements.

## Checklist

- [ ] ICT recovery objectives (RTO/RPO) defined per service
- [ ] recovery plans documented and maintained
- [ ] recovery tests performed and results documented
- [ ] supplier dependencies identified and addressed
- [ ] recovery plans aligned with business impact analysis
- [ ] test findings tracked to corrective actions

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
