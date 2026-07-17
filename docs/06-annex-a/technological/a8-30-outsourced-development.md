---
title: A.8.30 Outsourced development
description: Practical implementation, evidence, and audit guidance for A.8.30.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.30 Outsourced development

## Overview

Outsourcing development transfers work but not accountability for product risk. Agreements and oversight should address requirements, competence, methods, access, code ownership, dependencies, testing, defects, evidence, and transition.

## Purpose

This control ensures that when software development is outsourced to external parties, security requirements, development practices, testing, evidence, and acceptance criteria are contractually defined, monitored, and enforced. The organization remains accountable for the security of the delivered product regardless of who wrote the code.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.30 when selected or otherwise committed to.
- **Implementation guidance:** Define **outsourced development** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- high-risk changes with security review
- security defects escaped to production
- critical findings fixed before release
- emergency changes reviewed

## Practical example

An external team develops a mobile component under agreed secure-coding and review rules. The customer controls repository access, reviews dependency and test evidence, accepts releases, and retains rights and transition material.

## Evidence to retain

- security requirements
- architecture or threat-model review
- test results
- release/change approval
- defect and remediation records

## Common mistakes

- The contract covers functionality and deadlines but omits security requirements, testing standards, and evidence obligations.
- The supplier is trusted to "handle security" without verification — no review of their SDL, testing, or code quality.
- Source code ownership and transition rights are not addressed — the organization cannot access or maintain its own code.
- Security acceptance testing is performed by the same supplier that built the software, with no independent verification.

## Auditor questions

- How are security requirements communicated to and enforced with outsourced development suppliers?
- What evidence does the organization review to verify the supplier's security practices?
- Who owns the source code and intellectual property, and what transition provisions exist?
- Show evidence of independent security review or testing of supplier-delivered software before acceptance.

## Checklist

- [ ] security requirements included in development contracts
- [ ] supplier security practices assessed before engagement
- [ ] code ownership and transition rights defined in contract
- [ ] supplier security evidence reviewed regularly
- [ ] independent security testing performed before acceptance
- [ ] defect remediation verified before final acceptance

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
