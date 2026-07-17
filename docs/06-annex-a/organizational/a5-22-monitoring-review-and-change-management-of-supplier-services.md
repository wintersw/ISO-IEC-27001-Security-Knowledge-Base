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

This control ensures that supplier services are monitored and reviewed on a risk-based schedule and that material changes, such as new subcontractors, architecture changes, or service updates, are assessed and managed. Monitoring methods and timing should reflect service criticality, available assurance, contractual rights, and relevant change triggers.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.22 when selected or otherwise committed to.
- **Implementation guidance:** Define **monitoring, review and change management of supplier services** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- high-risk suppliers reviewed on time
- supplier findings overdue
- critical suppliers without exit plan
- supplier incidents

## Practical example

A critical cloud provider announces a new subprocessor and service architecture. The owner assesses location and dependency changes, updates the risk record, obtains required approvals, and tracks contract or control actions.

## Evidence to retain

- supplier tiering decision
- due-diligence assessment
- contract security clauses
- service review record
- incident/change notification and exit evidence

## Common mistakes

- Supplier reviews are scheduled but skipped — no one tracks whether reviews actually occurred.
- Monitoring focuses on uptime and SLAs but ignores security metrics — patching status, incident trends, audit findings.
- Supplier-initiated changes (new subcontractors, data center moves, platform migrations) are implemented without customer review.
- Review findings are recorded but not tracked to resolution — the same gaps appear in every review cycle.

## Auditor questions

- How often are supplier services reviewed, and who performs the review?
- What metrics or indicators are monitored between formal reviews?
- How are supplier-initiated changes assessed for security impact before they affect the organization?
- Show evidence that review findings are tracked to resolution and that overdue items are escalated.

## Checklist

- [ ] supplier review schedule defined per risk tier
- [ ] review scope includes security metrics and incidents
- [ ] supplier change notification and assessment process defined
- [ ] findings tracked to resolution with escalation path
- [ ] service performance monitored between reviews
- [ ] review records retained and accessible

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
