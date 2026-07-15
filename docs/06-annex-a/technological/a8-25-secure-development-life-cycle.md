---
title: A.8.25 Secure development life cycle
description: Practical implementation, evidence, and audit guidance for A.8.25.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.25 Secure development life cycle

## Overview

A secure development lifecycle integrates security decisions and checks from product idea through requirements, design, construction, testing, release, operation, change, and retirement. Responsibilities and evidence should exist at each relevant stage.

## Purpose

The purpose of A.8.25 is to reduce the likelihood or impact of failures related to **secure development life cycle**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.25 when selected or otherwise committed to.
- **Implementation guidance:** Define **secure development life cycle** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- high-risk changes with security review
- security defects escaped to production
- critical findings fixed before release
- emergency changes reviewed

## Practical example

A product release cannot proceed until security requirements, threat review, code and dependency checks, test results, unresolved-risk approval, deployment safeguards, and vulnerability-response ownership meet defined exit criteria.

## Evidence to retain

- security requirements
- architecture or threat-model review
- test results
- release/change approval
- defect and remediation records

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
