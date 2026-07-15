---
title: A.8.15 Logging
description: Practical implementation, evidence, and audit guidance for A.8.15.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
  - control
status: expanded
---
# A.8.15 Logging

## Overview

Logging records relevant events in systems, applications, networks, identities, and security tools. Logs support detection, investigation, accountability, forensic analysis, compliance, and operational troubleshooting.

## Purpose

This control ensures that events relevant to information security are recorded, protected from tampering, retained for an appropriate period, and available for detection, investigation, and accountability. Without adequate logging, the organization cannot detect attacks, investigate incidents, or demonstrate control operation to auditors.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.15 when selected or otherwise committed to.
- **Implementation guidance:** Define **logging** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

This control creates visibility into security-relevant activity. Logs and alerts should be designed around investigation and risk scenarios, protected from tampering, retained appropriately, and reviewed through defined workflows.

### Measures that support decisions

- critical systems with required logging
- alerts triaged within target
- log-source failures
- use cases tested

Metrics should support decisions. A high completion rate can still be misleading if the population is incomplete, exceptions are hidden, or remediation is not verified.

## Practical example

The data warehouse logs authentication but not queries or exports. The organization enables data-access audit logging, creates alerts for unusual export volume, protects logs, and tests triage procedures.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Logging is enabled but log sources are incomplete — critical systems, databases, or cloud services are not sending logs.
- Logs are collected but never reviewed outside of incident response — proactive monitoring and alerting are absent.
- Log integrity is not protected — logs can be modified or deleted by the same administrators being monitored.
- Retention periods are either undefined (logs deleted too early) or unlimited (storage and privacy risks).
- Clock synchronization is not enforced across log sources, making event correlation unreliable or impossible.

## Auditor questions

- What events are logged, and how were the logging requirements determined (risk, legal, operational)?
- How are logs collected, centralized, and protected from unauthorized access or tampering?
- What is the log retention policy, and how is it enforced across different log types?
- How are logs reviewed — automated alerting, regular manual review, or both? Show evidence of recent review activity.
- How is clock synchronization maintained across log sources (see A.8.17)?

## Checklist

- [ ] logging requirements defined
- [ ] critical sources identified
- [ ] central collection implemented
- [ ] retention defined
- [ ] log access restricted
- [ ] log-source health monitored

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
