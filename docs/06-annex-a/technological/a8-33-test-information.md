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

This control ensures that test information is appropriately selected, generated, protected, retained, and deleted while preserving test validity. Production information should be avoided where suitable alternatives exist; when its use is justified, authorization and protections should reflect its sensitivity and the test environment's risk.

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

## Common mistakes

- Production data is copied verbatim to test environments without masking, anonymization, or access controls.
- Test data is never cleaned up — sensitive copies accumulate in unmanaged environments indefinitely.
- Synthetic test data is not validated for realism — tests pass but miss real-world edge cases.
- Test environments have weaker access controls than production, yet contain equally sensitive data.

## Auditor questions

- How is test data sourced — synthetic generation, masked production data, or direct copies?
- When production data is used for testing, how is it protected, masked, and authorized?
- How is test data deleted when no longer needed, and how is deletion verified?
- Show evidence that test environments containing sensitive data have access controls comparable to production.

## Checklist

- [ ] test data sourcing policy defined (synthetic preferred)
- [ ] production data use in testing approved and masked
- [ ] test data inventory maintained with classification
- [ ] test environment access controls defined and enforced
- [ ] test data retention and deletion schedules defined
- [ ] test data handling reviewed periodically

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
