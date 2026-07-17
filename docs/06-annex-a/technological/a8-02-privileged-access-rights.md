---
title: A.8.2 Privileged access rights
description: Practical implementation, evidence, and audit guidance for A.8.2.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.2 Privileged access rights

## Overview

Privileged access permits high-impact changes or access beyond ordinary user rights. It should be limited, separately approved, strongly authenticated, attributable, time-bound where practical, monitored, and regularly reviewed.

## Purpose

This control ensures that privileged access rights are limited, authorized, attributable, appropriately authenticated, and regularly reviewed, with time-bound access and separation from ordinary activity where practical and justified. Privileged access can bypass or alter important safeguards, so its lifecycle and use require stronger assurance than ordinary access.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.2 when selected or otherwise committed to.
- **Implementation guidance:** Define **privileged access rights** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- access reviews completed on time
- orphaned accounts
- privileged accounts without strong authentication
- time to remove leaver access

## Practical example

An engineer requests two hours of production administrator access for an approved change. A separate approver confirms need, the privileged session is logged, access expires automatically, and exceptions receive follow-up review.

## Evidence to retain

- identity inventory or authoritative export
- access request and approval
- access review record
- removal or modification ticket
- authentication and privileged-session logs

## Common mistakes

- Privileged access is granted by default to broad groups ("Domain Admins") rather than assigned to named individuals for specific purposes.
- Shared privileged accounts are used with no individual attribution — everyone logs in as "administrator".
- No just-in-time (JIT) or temporary elevation — privileged rights persist permanently even when not needed.
- Privileged session activity is not logged, monitored, or reviewed, leaving no audit trail for high-impact actions.

## Auditor questions

- Who holds privileged access, and how is the list of privileged accounts reviewed and recertified?
- How are privileged accounts authenticated — is multi-factor authentication enforced differently than for standard users?
- How is emergency or break-glass access granted, logged, and reviewed after the fact?
- Show evidence that privileged sessions are logged and that activity is reviewed for anomalies.

## Checklist

- [ ] privileged account inventory maintained and reviewed regularly
- [ ] approval process required for privileged access grants
- [ ] just-in-time or time-bound elevation configured
- [ ] multi-factor authentication enforced for all privileged access
- [ ] privileged session logging and monitoring enabled
- [ ] emergency access procedure documented and tested

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
