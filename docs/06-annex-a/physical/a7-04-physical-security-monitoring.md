---
title: A.7.4 Physical security monitoring
description: Practical implementation, evidence, and audit guidance for A.7.4.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.7.4 Physical security monitoring

## Overview

Physical monitoring detects and supports investigation of unauthorized entry or suspicious activity. Cameras, alarms, guards, and access records require defined coverage, response, retention, privacy controls, maintenance, and time synchronization.

## Purpose

Physical security monitoring provides continuous or periodic surveillance of secure areas to detect, record, and enable response to unauthorized access attempts, suspicious behavior, or environmental anomalies before they escalate into incidents.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.7.4 when selected or otherwise committed to.
- **Implementation guidance:** Define **physical security monitoring** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

This control provides timely visibility of unauthorized physical access and suspicious activity. Monitoring coverage should follow site risk, respect privacy and employment requirements, generate actionable alerts, support investigation, and remain reliable through maintenance, retention, access protection, and time synchronization.

### Measures that support decisions

- monitored high-risk areas covered by functioning sensors or cameras
- physical-security alerts acknowledged within target
- monitoring devices, recording gaps, or alarm paths that failed testing
- unauthorized-entry scenarios tested and corrective actions overdue

## Practical example

A forced server-room door generates an alert to the facilities responder. Badge and camera records are correlated, access to footage is restricted, the event is investigated, and failed alarm tests create maintenance actions.

## Evidence to retain

- monitoring coverage and privacy assessment
- camera, alarm, sensor, or guard configuration records
- alert, access, and investigation records
- inspection, test, maintenance, and recording-availability records
- access-to-footage logs, retention settings, and corrective actions

## Common mistakes

- Installing cameras but never reviewing footage unless an incident has already been reported
- Not defining retention periods for monitoring records, leading to premature deletion or excessive storage costs
- Failing to inform people that monitoring is in place, creating legal and privacy compliance risks
- Placing monitors or camera positions where they can be seen — allowing intruders to identify blind spots

## Auditor questions

- What areas are under surveillance, and what is the rationale for coverage and any gaps?
- How long is monitoring footage retained, and who has access to it?
- When was the last time monitoring led to the detection of an unauthorized access attempt?
- How do you ensure monitoring does not violate privacy laws or employee expectations?

## Checklist

- [ ] Surveillance coverage documented with rationale for covered and uncovered areas
- [ ] Monitoring system tested for functionality and recording quality periodically
- [ ] Retention periods defined and enforced for all monitoring records
- [ ] Access to monitoring records restricted to authorized personnel
- [ ] Privacy notice or signage informing people of monitoring in place

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
