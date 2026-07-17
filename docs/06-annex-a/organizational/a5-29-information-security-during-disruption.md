---
title: A.5.29 Information security during disruption
description: Practical implementation, evidence, and audit guidance for A.5.29.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.29 Information security during disruption

## Overview

Security safeguards must remain appropriate when normal operations are disrupted. Continuity arrangements should identify which controls must continue, which may change temporarily, and how elevated risk is authorized and monitored.

## Purpose

This control ensures that information security is maintained at an appropriate level during disruption — that continuity arrangements do not abandon security in the rush to restore operations. An attacker's ideal time to strike is during a disaster, when normal controls are weakened and attention is elsewhere.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.29 when selected or otherwise committed to.
- **Implementation guidance:** Define **information security during disruption** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

During loss of the primary identity service, emergency accounts provide limited access to recovery staff. Use requires incident-lead approval, is logged, expires after recovery, and receives independent review.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Continuity plans assume full security controls are available — recovery procedures fail when authentication, logging, or encryption services are down.
- Emergency access accounts are permanently active rather than time-limited and scoped to recovery activities.
- Security monitoring is suspended during disruption — no one watches for attacks while the organization is most vulnerable.
- Elevated risks accepted during disruption are never reviewed or rolled back after normal operations resume.

## Auditor questions

- How are security controls maintained or compensated for during disruption?
- What emergency access procedures exist, and how are they controlled and reviewed?
- How is security monitoring maintained during continuity operations?
- Show evidence that temporary risk acceptances during disruption are time-bound and reviewed after recovery.

## Checklist

- [ ] security requirements included in continuity plans
- [ ] emergency access procedures defined and tested
- [ ] security monitoring maintained during disruption
- [ ] temporary risk acceptances time-bound and reviewed
- [ ] continuity plans tested with security controls active
- [ ] post-disruption review includes security control assessment

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
