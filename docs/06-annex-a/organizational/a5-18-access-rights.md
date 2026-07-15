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

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
