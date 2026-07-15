---
title: A.5.16 Identity management
description: Practical implementation, evidence, and audit guidance for A.5.16.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.16 Identity management

## Overview

Identity management controls the full lifecycle of human, service, device, and other identities. Each identity should be uniquely attributable where required, sponsored by an owner, changed when its purpose changes, and removed when no longer needed.

## Purpose

The purpose of A.5.16 is to reduce the likelihood or impact of failures related to **identity management**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.16 when selected or otherwise committed to.
- **Implementation guidance:** Define **identity management** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- access reviews completed on time
- orphaned accounts
- privileged accounts without strong authentication
- time to remove leaver access

## Practical example

A team creates a service identity through a workflow that records its owner, purpose, allowed systems, credential location, review date, and expiry. Ownership must be reassigned before the sponsoring engineer leaves.

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
