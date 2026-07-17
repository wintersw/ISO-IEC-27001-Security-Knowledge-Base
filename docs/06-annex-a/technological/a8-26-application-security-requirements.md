---
title: A.8.26 Application security requirements
description: Practical implementation, evidence, and audit guidance for A.8.26.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.26 Application security requirements

## Overview

Application security requirements state the security outcomes an application must achieve and the conditions used to accept them. They should derive from risks, data, users, transactions, obligations, architecture, and likely misuse.

## Purpose

This control ensures that application security requirements are identified, specified, approved, and tracked for acquisition, development, use, and significant change. Requirements should be defined early enough to shape design and acceptance, then maintained as risk, architecture, and operating context change.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.26 when selected or otherwise committed to.
- **Implementation guidance:** Define **application security requirements** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

Requirements for a payment feature cover authorization, transaction integrity, auditability, input handling, session security, recovery, privacy, availability, and abuse cases, each with a testable acceptance criterion and owner.

## Evidence to retain

- security requirements
- architecture or threat-model review
- test results
- release/change approval
- defect and remediation records

## Common mistakes

- Security requirements are copied from a generic checklist without tailoring to the specific application, data, and threat model.
- Requirements focus only on confidentiality — integrity, availability, auditability, and privacy are overlooked.
- Requirements are stated as aspirations ("the application must be secure") rather than testable, measurable criteria.
- Requirements are defined after procurement or build has already started, making them de facto optional.

## Auditor questions

- How are security requirements derived — from policy, risk assessment, threat modeling, or regulatory obligations?
- Who must approve security requirements before development or procurement proceeds?
- How are security requirements traced through design, build, test, and acceptance?
- Show a recent example of security requirements that were defined, tested, and verified for a new application.

## Checklist

- [ ] security requirements defined before development or procurement
- [ ] requirements derived from risk, data classification, and threat analysis
- [ ] requirements are specific, measurable, and testable
- [ ] requirements cover confidentiality, integrity, availability, and privacy
- [ ] requirements approved by security and business owners
- [ ] traceability from requirement to test evidence maintained

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
