---
title: A.5.26 Response to information security incidents
description: Practical implementation, evidence, and audit guidance for A.5.26.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.26 Response to information security incidents

## Overview

Incident response coordinates containment, eradication, recovery, communication, evidence, and decision-making. Actions should limit harm while preserving business priorities and the ability to understand what happened.

## Purpose

The purpose of A.5.26 is to reduce the likelihood or impact of failures related to **response to information security incidents**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.26 when selected or otherwise committed to.
- **Implementation guidance:** Define **response to information security incidents** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- mean time to triage
- mean time to contain
- incidents with lessons learned
- repeat incidents

## Practical example

After a mailbox compromise, the team disables active sessions, resets credentials, checks forwarding rules, searches for related activity, assesses exposed information, communicates decisions, and verifies normal operation before closure.

## Evidence to retain

- incident ticket and timeline
- severity and escalation decision
- preserved logs and artifacts
- communication and notification record
- lessons learned and corrective actions

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
