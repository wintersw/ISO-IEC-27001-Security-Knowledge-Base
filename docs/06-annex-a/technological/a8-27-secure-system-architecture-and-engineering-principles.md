---
title: A.8.27 Secure system architecture and engineering principles
description: Practical implementation, evidence, and audit guidance for A.8.27.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.27 Secure system architecture and engineering principles

## Overview

Secure architecture and engineering principles guide consistent decisions about trust, boundaries, failure, privilege, data, interfaces, resilience, and maintainability. Principles become useful when reviews apply them to real designs and exceptions.

## Purpose

This control ensures that systems are designed, built, and operated using consistent security engineering principles — such as defense in depth, least privilege, secure defaults, and fail-safe design. Without principles, every design decision is ad-hoc, and security gaps are introduced through inconsistent choices.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.27 when selected or otherwise committed to.
- **Implementation guidance:** Define **secure system architecture and engineering principles** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

An architecture review challenges a design that trusts internal network location. The team adds service identity, explicit authorization, protected secrets, restricted flows, failure handling, and monitoring, then records one accepted exception.

## Evidence to retain

- security requirements
- architecture or threat-model review
- test results
- release/change approval
- defect and remediation records

## Common mistakes

- Principles are listed in a policy document but never referenced during architecture reviews or design decisions.
- Principles are too abstract ("be secure") to guide real engineering trade-offs.
- Implicit trust in network location, internal users, or third-party APIs replaces explicit authentication and authorization.
- Fail-open designs are used where fail-closed would be appropriate — a failure disables security controls rather than blocking access.

## Auditor questions

- What security engineering principles have been adopted, and where are they documented?
- How are principles applied during architecture and design reviews?
- Who can approve a deviation from a principle, and how are deviations tracked?
- Show evidence from a recent architecture review where principles influenced a design decision.

## Checklist

- [ ] security engineering principles documented and communicated
- [ ] principles applied during architecture and design reviews
- [ ] deviation process defined with approval and tracking
- [ ] principles reviewed and updated periodically
- [ ] engineers trained on applying principles in practice
- [ ] architecture review records demonstrate principle application

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
