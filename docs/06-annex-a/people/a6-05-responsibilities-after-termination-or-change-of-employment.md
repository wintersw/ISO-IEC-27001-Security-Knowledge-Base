---
title: A.6.5 Responsibilities after termination or change of employment
description: Practical implementation, evidence, and audit guidance for A.6.5.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.6.5 Responsibilities after termination or change of employment

## Overview

Security duties can continue or change when a person changes role or leaves. Ownership, access, information, equipment, confidentiality, and pending work should be reviewed so obligations and risks do not fall through lifecycle gaps.

## Purpose

This control ensures that security duties, access rights, assets, and confidentiality obligations are properly transferred or revoked when personnel change roles or leave, preventing orphaned access, unaccounted information, and gaps in accountability.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.6.5 when selected or otherwise committed to.
- **Implementation guidance:** Define **responsibilities after termination or change of employment** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

This control keeps security responsibilities, access, assets, confidentiality duties, and ownership aligned when employment or duties change. Human resources, the line manager, identity administration, asset management, and information owners need coordinated triggers and accountable hand-offs.

### Measures that support decisions

- role changes and terminations processed within target
- continuing obligations communicated and acknowledged where required
- responsibilities, assets, and privileged duties transferred before departure
- overdue or failed hand-off, access-removal, or asset-return actions

## Practical example

An employee moving to sales loses development access, acknowledges new data-handling duties, transfers code-signing responsibilities, and completes handover. At later termination, remaining access and equipment are reconciled and removed.

## Evidence to retain

- role-change or termination notification
- responsibility and access review record
- handover and ownership-transfer record
- continuing-obligation communication or acknowledgement
- asset return and unresolved-action record

## Common mistakes

- Disabling the network account but forgetting physical access cards, remote access tokens, or application-specific accounts
- Having no automated trigger from HR to IT when someone resigns, resulting in days or weeks of lingering access
- Assuming all confidentiality obligations end on the last day, without documenting continuing duties
- Failing to transfer ownership of documents, code repositories, or encryption keys before the person departs

## Auditor questions

- What is the maximum time between HR notification and access revocation, and how do you measure and report it?
- How do you identify all access rights, assets, and responsibilities that need to be transferred or revoked?
- Can you show a termination checklist and evidence that it was completed for a recent departure?
- How are continuing confidentiality or non-disclosure obligations communicated and acknowledged?

## Checklist

- [ ] Termination and role-change notification triggers defined between HR, IT, and physical security
- [ ] All access rights revoked or transferred within defined SLA
- [ ] Physical assets returned, accounted for, and reconciled
- [ ] Ownership of documents, code, keys, and responsibilities transferred before departure
- [ ] Continuing confidentiality obligations acknowledged in writing where required

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
