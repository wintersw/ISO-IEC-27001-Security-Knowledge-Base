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
# A.5.30 information and communication technology (ICT) readiness for business continuity

## Overview

Information and communication technology readiness connects technology recovery capabilities to business continuity needs. Recovery priorities, dependencies, objectives, procedures, and tests should agree with the business impact analysis.

## Purpose

The purpose of A.5.30 is to reduce the likelihood or impact of failures related to **ict readiness for business continuity**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.30 when selected or otherwise committed to.
- **Implementation guidance:** Define **ict readiness for business continuity** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Key concepts

- **Applicability:** why the control is or is not needed in context.
- **Control owner:** the role accountable for design, operation, evidence, and improvement.
- **Operating evidence:** scoped, dated records showing what occurred and who approved it.
- **Effectiveness:** achievement of the intended outcome, not activity completion alone.

## Practical implementation

This control supports resilience and recovery. The organization should connect technical recovery capability to business-service requirements, test restoration, document dependencies, and learn from exercises.

For A.5.30, begin by identifying the specific risk, legal requirement, contractual commitment, or operational need that makes the control necessary. The control owner should then define what is in scope, which roles perform the activity, which systems or data sources are authoritative, how exceptions are handled, and what evidence proves that the control operated.

### Measures that support decisions

- restore tests successful
- recovery time objective (RTO)/recovery point objective (RPO) achieved
- critical services tested
- recovery actions overdue

Metrics should support decisions. A high completion rate can still be misleading if the population is incomplete, exceptions are hidden, or remediation is not verified.

## Practical example

A payment service requires a four-hour recovery time. A failover exercise tests identity, database, network, supplier, and monitoring dependencies, measures actual recovery, and creates actions where capability misses the approved objective.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

Retain both design and operating evidence; policy alone does not prove operation. Prefer authoritative, scoped records with approvals, exceptions, and remediation.

## Common mistakes

- policy exists without reliable operation;
- ownership or scope is unclear;
- exceptions lack approval or expiry; and
- evidence or corrective action does not demonstrate effectiveness.

## Auditor questions

- Which risk or requirement does the control address?
- Who owns and operates it, and how is scope determined?
- Which evidence shows recent operation and exception handling?
- How is effectiveness tested and failure remediated?
- What changed after the latest significant review or event?

## Checklist

- [ ] Control owner assigned
- [ ] Applicability decision recorded in the SoA
- [ ] Related risks identified
- [ ] Implementation approach documented
- [ ] Evidence sources identified
- [ ] Review frequency defined

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Abbreviations](../../15-reference/abbreviations.md)
