---
title: A.5.15 Access Control
description: Practical implementation, evidence, and audit guidance for A.5.15.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
  - control
status: expanded
---
# A.5.15 Access Control

## Overview

Access control defines how the organization grants, restricts, reviews, and removes access to information and systems.

## Purpose

This control ensures that access to information and associated assets is managed through defined rules that cover both logical and physical access, aligned with business and security requirements. Without a structured access control policy, access decisions are ad-hoc, privileges accumulate unchecked, and the organization cannot demonstrate who should have access to what.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.15 when selected or otherwise committed to.
- **Implementation guidance:** Define **access control** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- access reviews completed on time
- orphaned accounts
- privileged accounts without strong authentication
- time to remove leaver access

Metrics should support decisions. A high completion rate can still be misleading if the population is incomplete, exceptions are hidden, or remediation is not verified.

## Practical example

An employee moves from finance to operations. The mover workflow grants new role access, removes obsolete finance permissions, reassigns owned service accounts, and retains completed tickets as evidence.

## Evidence to retain

- identity inventory or authoritative export
- access request and approval
- access review record
- removal or modification ticket
- authentication and privileged-session logs

## Common mistakes

- Access control rules exist in policy but are not enforced technically — policy says "least privilege" but broad groups and default permissions are used in practice.
- Ownership of access decisions is unclear — IT grants access without data owner approval.
- Access control rules are not reviewed when systems, roles, or business processes change.
- Exceptions to access control rules are granted informally without approval, compensating controls, or expiry.
- Evidence and corrective action do not demonstrate that access control rules produce the intended security outcome.

## Auditor questions

- Where are access control rules documented, and how are they linked to information classification and business requirements?
- How are access rights granted, reviewed, and revoked — and who has authority at each step?
- Show how the principle of least privilege and need-to-know is implemented and enforced.
- How are exceptions to access control rules managed and periodically reviewed?
- What evidence shows that access rights match the documented rules?

## Checklist

- [ ] policy approved
- [ ] request workflow defined
- [ ] approvers identified
- [ ] privileged access controlled
- [ ] multifactor authentication (MFA) applied where required
- [ ] reviews scheduled
- [ ] offboarding integrated

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
