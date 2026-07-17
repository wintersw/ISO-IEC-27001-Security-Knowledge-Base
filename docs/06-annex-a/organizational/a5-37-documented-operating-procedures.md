---
title: A.5.37 Documented operating procedures
description: Practical implementation, evidence, and audit guidance for A.5.37.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.37 Documented operating procedures

## Overview

Documented operating procedures make important or error-prone work repeatable and transferable. A useful procedure states prerequisites, responsibilities, ordered actions, decisions, expected results, evidence, escalation, and maintenance triggers.

## Purpose

This control ensures that operating procedures for information processing and security operations are documented, maintained, and available to those who need them. When critical procedures exist only in someone's head, a single absence can paralyze operations.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.37 when selected or otherwise committed to.
- **Implementation guidance:** Define **documented operating procedures** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A backup restoration runbook identifies required access, restore order, validation queries, decision points, communications, rollback, evidence capture, and escalation. A technician unfamiliar with the service validates it during an exercise.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Procedures are documented once and never updated — they describe systems and workflows that no longer exist.
- Critical procedures are undocumented — the only person who knows how to restore backups or rotate certificates is on leave.
- Procedures are too verbose or too vague — staff cannot follow them under pressure.
- Procedures exist but are not tested — the first time someone follows the disaster recovery procedure is during a disaster.

## Auditor questions

- What security-relevant operating procedures are documented, and where are they stored?
- How are procedures kept current when systems, roles, or processes change?
- How are staff trained on procedures, and how is competence verified?
- Show evidence that critical procedures have been tested or exercised.

## Checklist

- [ ] security-relevant operating procedures documented
- [ ] procedure ownership and review schedule defined
- [ ] procedures accessible to authorized personnel
- [ ] staff trained on relevant procedures
- [ ] critical procedures tested periodically
- [ ] procedure updates triggered by system or process changes

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
