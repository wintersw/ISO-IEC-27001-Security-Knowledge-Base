---
title: A.8.33 Test information
description: Practical implementation, evidence, and audit guidance for A.8.33.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.33 Test information

## Overview

Test information can be sensitive, misleading, or harmful if copied without control. Selection, generation, masking, access, transfer, retention, refresh, and deletion should protect both test validity and the source information.

## Purpose

The purpose of A.8.33 is to reduce the likelihood or impact of failures related to **test information**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.33 when selected or otherwise committed to.
- **Implementation guidance:** Define **test information** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

This control protects information selected, generated, copied, or used for testing. Prefer representative synthetic data; where production information is necessary, minimize and authorize its use, preserve required integrity, restrict access, separate environments, monitor handling, and remove it when the approved need ends.

### Measures that support decisions

- test data sets with recorded owner, source, classification, and purpose
- approved production-data exceptions and exceptions past expiry
- sensitive fields masked or replaced before test use
- test data retained beyond the approved period or found in unauthorized environments

## Practical example

A test team uses synthetic customer records for routine work. A rare production-data exception is minimized, masked where possible, approved by the data owner, restricted to a temporary environment, logged, and deleted after testing.

## Evidence to retain

- test-information inventory and classification
- synthetic-data design or approved production-data exception
- masking, extraction, transfer, and access records
- test-environment protection and monitoring evidence
- refresh, retention, deletion, and exception-review records

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
