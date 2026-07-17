---
title: A.8.16 Monitoring activities
description: Practical implementation, evidence, and audit guidance for A.8.16.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.16 Monitoring activities

## Overview

Monitoring activities observe systems, networks, applications, users, and control states so abnormal behavior and failures can be detected and investigated. Useful monitoring has defined coverage, ownership, thresholds, response, retention, and review.

## Purpose

A.8.16 ensures that relevant networks, systems, applications, and user activity are monitored for anomalous behavior, security events, and control failures so suspected incidents can be detected, investigated, and handled within risk-based targets.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.16 when selected or otherwise committed to.
- **Implementation guidance:** Define **monitoring activities** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

Monitoring activities observe the behavior of systems, networks, applications, and users to detect anomalies, policy violations, and security events. Define the scope of monitoring coverage: which systems, what behavior, at what frequency. Establish alerting thresholds that balance detection sensitivity with operational noise, and tune them regularly. Assign clear ownership for each monitoring use case, including who receives alerts, who investigates, and escalation paths. Document detection use cases with expected inputs, logic, and outputs so they can be tested and reviewed. Separate monitoring that detects security events from monitoring that confirms control operation — both are needed but serve different purposes. Schedule periodic reviews of detection coverage against updated threat models and risk assessments.

### Measures that support decisions

- monitored systems with defined coverage
- detection use cases documented and tested
- alerts triaged within target
- false-positive rate and tuning cadence

## Common mistakes

- Deploying monitoring tools without defining what behavior is abnormal or which events are security-relevant.
- Tuning alerts so loosely that analysts ignore them or so tightly that real incidents are missed.
- Failing to document detection use cases with expected inputs, logic, and outputs.
- Treating tool alerts as the only monitoring source — user reports, control failures, and operational anomalies are equally important.

## Auditor questions

- What systems, networks, and applications are within monitoring scope, and what behavior is observed?
- Are detection use cases documented, tested, and reviewed for coverage?
- What is the mean time to triage security alerts, and what is the false-positive rate?
- How are monitoring gaps identified and remediated?

## Checklist

- [ ] Monitoring scope defined with coverage, thresholds, and ownership
- [ ] Detection use cases documented with expected inputs, logic, and outputs
- [ ] Alerts tuned regularly with false-positive rate tracked
- [ ] Alert triage and escalation paths defined and tested
- [ ] Coverage reviewed against updated threat models and risk assessments

## Practical example

A monitoring use case alerts on impossible travel followed by privileged access. The analyst checks identity, device, and application context, records disposition, and the owner reviews detection coverage and false results each month.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
