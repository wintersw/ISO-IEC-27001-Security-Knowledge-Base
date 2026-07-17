---
title: A.8.5 Secure authentication
description: Practical implementation, evidence, and audit guidance for A.8.5.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.5 Secure authentication

## Overview

Secure authentication verifies identity with strength appropriate to the risk while resisting theft, replay, guessing, and bypass. Design should cover enrollment, factors, sessions, recovery, failure handling, logging, and service identities.

## Purpose

This control ensures that authentication mechanisms are designed, implemented, and operated to resist theft, replay, guessing, bypass, and credential-based attacks. Authentication is the gatekeeper for all digital access — weak or misconfigured authentication undermines every downstream control.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.5 when selected or otherwise committed to.
- **Implementation guidance:** Define **secure authentication** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- access reviews completed on time
- orphaned accounts
- privileged accounts without strong authentication
- time to remove leaver access

## Practical example

Administrators use phishing-resistant multifactor authentication, short privileged sessions, and a controlled recovery process. Tests cover factor loss, repeated failure, session expiry, and prevention of weaker fallback for privileged accounts.

## Evidence to retain

- identity inventory or authoritative export
- access request and approval
- access review record
- removal or modification ticket
- authentication and privileged-session logs

## Common mistakes

- Single-factor password authentication is used for remote or high-risk access without additional factors.
- Password policies are either too weak or so complex that users work around them (e.g., password reuse, sticky notes).
- Account recovery processes are weaker than primary authentication, allowing attackers to bypass MFA through help-desk social engineering.
- Authentication logs are not monitored for brute-force attempts, credential stuffing, or impossible travel patterns.

## Auditor questions

- What authentication factors are required for different access levels, and how is the strength decision documented?
- How are authentication secrets (passwords, tokens, certificates) stored, transmitted, and rotated?
- How is account recovery handled, and what prevents the recovery path from being weaker than primary authentication?
- Show evidence that failed authentication attempts are logged and that brute-force protections are in place.

## Checklist

- [ ] authentication strength tiered by risk level
- [ ] multi-factor authentication enforced for remote and privileged access
- [ ] password policy defined and aligned with current guidance
- [ ] account recovery procedure secured against social engineering
- [ ] authentication logs monitored for attack patterns
- [ ] authentication mechanism tested against common bypass techniques

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
