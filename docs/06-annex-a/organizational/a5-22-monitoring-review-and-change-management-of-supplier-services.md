---
title: A.5.22 Monitoring, review and change management of supplier services
description: Practical implementation, evidence, and audit guidance for A.5.22.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.22 Monitoring, review and change management of supplier services

## Overview

Supplier security does not end at contract signature. Performance, assurance, incidents, changes, subcontractors, and unresolved findings need ongoing review, with escalation when service or risk moves outside agreed limits.

## Purpose

The purpose of A.5.22 is to reduce the likelihood or impact of failures related to **monitoring, review and change management of supplier services**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.22 when selected or otherwise committed to.
- **Implementation guidance:** Define **monitoring, review and change management of supplier services** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Key concepts

- **Applicability:** why the control is or is not needed in context.
- **Control owner:** the role accountable for design, operation, evidence, and improvement.
- **Operating evidence:** scoped, dated records showing what occurred and who approved it.
- **Effectiveness:** achievement of the intended outcome, not activity completion alone.

## Practical implementation

This control establishes accountability and prevents security work from becoming an informal activity with no decision owner. Implementation should distinguish who is accountable, who performs the work, who provides assurance, and who must be consulted.

For A.5.22, begin by identifying the specific risk, legal requirement, contractual commitment, or operational need that makes the control necessary. The control owner should then define what is in scope, which roles perform the activity, which systems or data sources are authoritative, how exceptions are handled, and what evidence proves that the control operated.

### Measures that support decisions

- high-risk suppliers reviewed on time
- supplier findings overdue
- critical suppliers without exit plan
- supplier incidents

Metrics should support decisions. A high completion rate can still be misleading if the population is incomplete, exceptions are hidden, or remediation is not verified.

## Practical example

A critical cloud provider announces a new subprocessor and service architecture. The owner assesses location and dependency changes, updates the risk record, obtains required approvals, and tracks contract or control actions.

## Evidence to retain

- supplier tiering decision
- due-diligence assessment
- contract security clauses
- service review record
- incident/change notification and exit evidence

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
