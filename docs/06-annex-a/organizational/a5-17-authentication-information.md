---
title: A.5.17 Authentication information
description: Practical implementation, evidence, and audit guidance for A.5.17.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.17 Authentication information

## Overview

Authentication information includes passwords, tokens, keys, recovery codes, and other secrets used to prove identity. It must be issued, stored, transmitted, reset, recovered, and retired without exposing it to unauthorized people or systems.

## Purpose

The purpose of A.5.17 is to reduce the likelihood or impact of failures related to **authentication information**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.17 when selected or otherwise committed to.
- **Implementation guidance:** Define **authentication information** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

Authentication information includes passwords, tokens, keys, recovery codes, and other secrets used to prove identity. It must be issued, stored, transmitted, reset, recovered, and retired without exposing it to unauthorized people or systems.

### Measures that support decisions

- accounts enrolled in multi-factor authentication
- password policy compliance rate
- secrets stored in approved vault or manager
- recovery and reset requests verified through approved process

## Practical example

A help-desk agent verifies a caller through an approved recovery process before resetting access. The temporary credential is delivered through a separate channel, expires quickly, and the event is logged for review.

## Evidence to retain

- identity inventory or authoritative export
- access request and approval
- access review record
- removal or modification ticket
- authentication and privileged-session logs

## Common mistakes

- Sending passwords, tokens, recovery codes, or keys through unprotected or shared channels.
- Using weak identity verification for reset and recovery, allowing an attacker to bypass stronger authentication.
- Sharing authentication information between people or embedding long-lived secrets in code and configuration files.
- Retaining unused secrets or failing to rotate them after exposure, ownership change, or compromise.

## Auditor questions

- How is authentication information generated, issued, stored, transmitted, recovered, rotated, and retired?
- How does reset or recovery verify identity without relying on the compromised factor alone?
- Where are application and service secrets stored, and how are access and use monitored?
- Show evidence from a recent secret rotation or recovery event, including approval and verification.

## Checklist

- [ ] authentication-information lifecycle and owners defined
- [ ] approved protected storage and delivery methods used
- [ ] reset and recovery identity checks risk appropriate
- [ ] shared and embedded secrets prohibited or controlled by exception
- [ ] exposure and lifecycle events trigger rotation or revocation
- [ ] handling and recovery processes tested and reviewed

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
