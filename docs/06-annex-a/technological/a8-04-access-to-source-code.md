---
title: A.8.4 Access to source code
description: Practical implementation, evidence, and audit guidance for A.8.4.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.4 Access to source code

## Overview

Source code and related development assets can reveal design, vulnerabilities, credentials, and intellectual property. Access and changes should be limited, attributable, reviewed, backed up, and separated from unauthorized production influence.

## Purpose

This control ensures that read and write access to source code, build scripts, configuration, and related development artifacts is restricted to authorized personnel, reviewed, and attributable. Uncontrolled source code access exposes intellectual property, hardcoded secrets, and the attack surface of applications.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.4 when selected or otherwise committed to.
- **Implementation guidance:** Define **access to source code** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- access reviews completed on time
- orphaned accounts
- privileged accounts without strong authentication
- time to remove leaver access

## Practical example

Repository membership follows team ownership, multifactor authentication, and quarterly review. Protected branches require peer approval and passing tests, sensitive repositories block public forks, and all changes retain author and review history.

## Evidence to retain

- identity inventory or authoritative export
- access request and approval
- access review record
- removal or modification ticket
- authentication and privileged-session logs

## Common mistakes

- All developers have write access to all repositories — no separation by team, component, or risk level.
- Branch protection rules are absent — code can be pushed directly to production branches without review.
- Hardcoded secrets (API keys, passwords, tokens) exist in source code history and are not scanned for.
- Public repositories or forks are not monitored, and internal code leaks to external platforms go undetected.

## Auditor questions

- Who has access to which repositories, and how is access granted and revoked?
- What branch protection rules exist, and are they enforced on all production branches?
- How are secrets prevented from being committed to source code, and are repositories regularly scanned?
- Show evidence of the most recent access review for source code repositories.

## Checklist

- [ ] repository access permissions defined per team and risk level
- [ ] branch protection rules enforced on production branches
- [ ] multi-factor authentication required for repository access
- [ ] automated secret scanning configured on all repositories
- [ ] public repository/visibility settings reviewed and monitored
- [ ] access reviews conducted at defined intervals

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
