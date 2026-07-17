---
title: A.8.13 Information backup
description: Practical implementation, evidence, and audit guidance for A.8.13.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.13 Information backup

## Overview

Backups provide recoverable copies of information, software, and configurations when originals are lost, damaged, altered, or unavailable. Scope, frequency, isolation, retention, protection, restoration, and testing should follow business recovery needs.

## Purpose

This control ensures that recoverable copies of necessary information, software, and system configurations are created, protected, retained, and tested according to recovery requirements. Successful job status alone does not demonstrate recoverability; representative restoration and integrity checks provide stronger evidence.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.13 when selected or otherwise committed to.
- **Implementation guidance:** Define **information backup** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- restore tests successful
- recovery time objective (RTO)/recovery point objective (RPO) achieved
- critical services tested
- recovery actions overdue

## Practical example

A critical database has encrypted, isolated backups with monitored completion and defined retention. A quarterly restore test uses a clean environment, validates data and application function, measures recovery, and tracks gaps to closure.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Backups are taken but never tested — the first restore attempt happens during an actual incident and fails.
- Backup scope is incomplete — critical configuration files, encryption keys, or cloud resource definitions are excluded.
- Backups are stored on the same system or network as production — ransomware encrypts both simultaneously.
- Retention periods are undefined or not enforced — backups are either deleted too early or accumulate indefinitely.

## Auditor questions

- What is the backup scope, and how was it determined from business recovery requirements?
- How are backups protected from unauthorized access, modification, and deletion?
- When was the last restore test, and what were the results?
- Show evidence that backup completion is monitored and that failures are remediated.

## Checklist

- [ ] backup scope defined based on recovery requirements
- [ ] backup schedule documented and completion monitored
- [ ] backups isolated from production (offline, immutable, or off-site)
- [ ] restore tests performed and documented regularly
- [ ] backup retention aligned with business and legal requirements
- [ ] backup encryption and access controls in place

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
