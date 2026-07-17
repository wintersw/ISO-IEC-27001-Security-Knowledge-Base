---
title: A.5.18 Access rights
description: Practical implementation, evidence, and audit guidance for A.5.18.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.18 Access rights

## Overview

Access rights should be requested, approved, provisioned, reviewed, changed, and removed through a controlled lifecycle. Decisions need a legitimate business purpose, an appropriate owner, least privilege, and timely remediation.

## Purpose

The purpose of A.5.18 is to reduce the likelihood or impact of failures related to **access rights**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.18 when selected or otherwise committed to.
- **Implementation guidance:** Define **access rights** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

Access rights should be requested, approved, provisioned, reviewed, changed, and removed through a controlled lifecycle. Decisions need a legitimate business purpose, an appropriate owner, least privilege, and timely remediation.

### Measures that support decisions

- access reviews completed on time
- orphaned accounts
- privileged accounts without strong authentication
- time to remove leaver access

## Practical example

A quarterly review starts from the complete application account export. The data owner removes two leavers, reduces an engineer's obsolete privilege, confirms a service-account owner, and verifies the completed changes before sign-off.

## Evidence to retain

- identity inventory or authoritative export
- access request and approval
- access review record
- removal or modification ticket
- authentication and privileged-session logs

## Common mistakes

- Reviewing an incomplete or manually curated account list rather than the authoritative system population.
- Treating manager approval as sufficient when the approver cannot assess the data, role, or privilege involved.
- Recording removal decisions without verifying that access was actually revoked across dependent systems.
- Running periodic reviews while failing to react promptly to joiner, mover, leaver, contract, and incident events.

## Auditor questions

- How are access requests authorized against business need, least privilege, and segregation requirements?
- How is the completeness of each access-review population established?
- Which events trigger access modification or removal outside the periodic review cycle?
- Show a sample from request through provisioning and later change or removal, including verification.

## Checklist

- [ ] authoritative access populations and owners defined
- [ ] requests include business purpose and appropriate approval
- [ ] least privilege and segregation conflicts assessed
- [ ] event-driven changes and removals meet defined targets
- [ ] periodic reviews use complete populations and record decisions
- [ ] remediation is verified before review closure

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
