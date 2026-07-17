---
title: A.8.10 Information deletion
description: Practical implementation, evidence, and audit guidance for A.8.10.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.10 Information deletion

## Overview

Information deletion ensures data is removed when no longer required and when an authorized request or lifecycle event demands it. Deletion must consider copies, backups, caches, replicas, suppliers, legal holds, and verification limits.

## Purpose

This control ensures that information no longer required is deleted in accordance with policy, retention schedules, and applicable legal or regulatory requirements. Improper or incomplete deletion leaves residual data exposed and can violate data-protection obligations.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.10 when selected or otherwise committed to.
- **Implementation guidance:** Define **information deletion** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

When a customer contract ends, the service deletes active records and exports, triggers provider deletion, records backup expiry, preserves data under a documented legal hold, and retains confirmation of the completed process.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Deletion is assumed to be complete after a single action — backups, replicas, logs, and caches are overlooked.
- No process exists to handle deletion requests from data subjects or to reconcile deletion with legal hold requirements.
- Deletion is not verified — there is no evidence that data was actually removed.
- Retention schedules are missing or inconsistent, so data is either deleted prematurely or kept indefinitely.

## Auditor questions

- How are information deletion requirements identified, and where are retention schedules documented?
- How is deletion verified, and what evidence is retained to demonstrate completion?
- How are competing requirements (e.g., deletion request vs. legal hold) resolved?
- Show how the deletion process addresses active copies, replicas, logs, supplier-held data, and backup copies that may expire through an approved retention cycle.

## Checklist

- [ ] retention and deletion schedules documented
- [ ] deletion process defined and authorized
- [ ] deletion coverage or approved expiry handling addresses backups, replicas, logs, and supplier data
- [ ] deletion verification evidence retained
- [ ] legal hold process defined and enforced
- [ ] deletion request handling procedure documented

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
