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

This control ensures that the organization responds to security incidents through coordinated assessment, containment, eradication, recovery, communication, and evidence handling as applicable. Response quality can reduce harm and support timely decisions, but legal or contractual notification depends on the applicable facts and requirements, not on response speed alone.

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

## Common mistakes

- Response focuses on technical eradication while ignoring communication — affected parties, regulators, and management are not informed.
- Evidence is destroyed during containment — systems are rebuilt without preserving forensic artifacts.
- The same person leads response for every incident — no succession or escalation path when the primary responder is unavailable.
- Incidents are closed when systems are restored — root cause is not addressed, leaving the same vulnerability exploitable.

## Auditor questions

- How are incidents escalated, and who has authority to make containment decisions?
- How is evidence preserved during response activities?
- How are communication obligations (regulatory, customer, internal) managed during an incident?
- Show evidence of a recent incident response — from detection through containment, eradication, recovery, and closure.

## Checklist

- [ ] incident response procedures documented
- [ ] escalation and authority levels defined
- [ ] evidence preservation procedures in place
- [ ] communication templates and contacts prepared
- [ ] containment and eradication steps documented per scenario
- [ ] post-incident review triggers defined

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
