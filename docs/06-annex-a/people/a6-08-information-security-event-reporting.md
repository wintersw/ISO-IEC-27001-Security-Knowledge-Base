---
title: A.6.8 Information security event reporting
description: Practical implementation, evidence, and audit guidance for A.6.8.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.6.8 Information security event reporting

## Overview

People need a simple, trusted way to report suspected security events quickly without first proving that an incident occurred. Reporting guidance should explain examples, channels, urgency, information to provide, and protection from inappropriate retaliation.

## Purpose

The purpose of A.6.8 is to reduce the likelihood or impact of failures related to **information security event reporting**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.6.8 when selected or otherwise committed to.
- **Implementation guidance:** Define **information security event reporting** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

Publish clear, accessible guidance on reportable security events, available channels, useful information to provide, urgent alternatives, and protection for good-faith reporting. Offer channels appropriate to the workforce and risk, including an option usable when normal credentials or systems are unavailable; protect public channels against abuse. Provide training at suitable lifecycle points and test reporting periodically to verify that reports reach the responsible team and are acknowledged within the defined target. Review report trends carefully: low volume can indicate either low exposure or reporting friction, so counts alone are not an effectiveness measure.

### Measures that support decisions

- reports received by channel
- reports acknowledged within target
- awareness training completion rate
- simulated reports reaching correct team

## Practical example

An employee reports an accidentally shared customer link through the published channel. The service records time, recipient, data, actions already taken, and contact details, then routes the event for triage and feedback.

## Evidence to retain

- incident ticket and timeline
- severity and escalation decision
- preserved logs and artifacts
- communication and notification record
- lessons learned and corrective actions

## Common mistakes

- Requiring personnel to determine conclusively that an incident occurred before they may report an event.
- Publishing one channel that becomes unavailable during an outage, account compromise, or loss of normal access.
- Collecting reports without acknowledgement, feedback, triage ownership, or defined urgent escalation.
- Measuring awareness only through training completion or raw report counts without testing the reporting path.

## Auditor questions

- What examples and urgency guidance help personnel recognize and report suspected events?
- Which reporting options remain available when normal systems or credentials cannot be used?
- How are reports acknowledged, protected, triaged, and routed to the responsible process?
- Show the result of a recent reporting-path test and how identified failures were corrected.

## Checklist

- [ ] reportable-event guidance and examples published
- [ ] channels accessible to the intended population and resilient to relevant failure scenarios
- [ ] urgent escalation and acknowledgement targets defined
- [ ] good-faith reports protected and handled confidentially where appropriate
- [ ] awareness and reporting paths tested periodically
- [ ] trends, failures, and corrective actions reviewed

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
