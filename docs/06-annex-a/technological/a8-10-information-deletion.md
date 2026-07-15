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

The purpose of A.8.10 is to reduce the likelihood or impact of failures related to **information deletion**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

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

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
