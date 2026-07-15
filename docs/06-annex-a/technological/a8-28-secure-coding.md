---
title: A.8.28 Secure coding
description: Practical implementation, evidence, and audit guidance for A.8.28.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.28 Secure coding

## Overview

Secure coding turns security requirements and known failure patterns into everyday implementation practices. Standards, training, review, automated checks, dependency controls, secrets handling, testing, and remediation should fit the technologies used.

## Purpose

The purpose of A.8.28 is to reduce the likelihood or impact of failures related to **secure coding**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.28 when selected or otherwise committed to.
- **Implementation guidance:** Define **secure coding** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- high-risk changes with security review
- security defects escaped to production
- critical findings fixed before release
- emergency changes reviewed

## Practical example

A pull request handling file uploads is checked against language guidance, peer-reviewed for authorization and validation, scanned for secrets and vulnerable components, tested with malicious files, and blocked until findings are resolved.

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
