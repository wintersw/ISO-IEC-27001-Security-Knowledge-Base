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

This control ensures that security is integrated into every stage of software and system development — from requirements and design through coding, testing, release, and maintenance. Retrofitting security after development is far more expensive and less effective than building it in from the start.

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

## Common mistakes

- Security is treated as a final gate before release — findings at that stage cause delays, shortcuts, or deferred fixes.
- The SDL is defined on paper but not enforced — teams skip security steps under schedule pressure.
- Third-party and open-source components are excluded from the SDL process.
- Security criteria for release are vague ("no critical issues") without measurable thresholds and approval authority.

## Auditor questions

- What security activities are required at each phase of the development lifecycle?
- How is compliance with the SDL verified — are there gates that cannot be bypassed?
- How are open-source and third-party components managed within the SDL?
- Show evidence that security defects found during development are tracked and remediated before release.

## Checklist

- [ ] SDL phases and security activities defined
- [ ] security gates defined with measurable exit criteria
- [ ] SDL applied to in-house, outsourced, and open-source components
- [ ] security training provided to development teams
- [ ] security defect tracking and remediation process in place
- [ ] SDL effectiveness reviewed and improved periodically

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
