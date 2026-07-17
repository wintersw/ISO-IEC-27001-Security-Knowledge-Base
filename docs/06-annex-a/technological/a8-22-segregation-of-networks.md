---
title: A.8.22 Segregation of networks
description: Practical implementation, evidence, and audit guidance for A.8.22.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.22 Segregation of networks

## Overview

Network segregation limits unnecessary communication and reduces the spread and impact of compromise. Zones and flows should follow business purpose, sensitivity, identity, device trust, and administration needs, with controlled exceptions.

## Purpose

This control ensures that groups of information services, users, and systems are segregated according to trust, sensitivity, business purpose, and risk, with communication between them controlled and monitored as appropriate. Effective segregation can limit attack paths and the impact of a compromise; zone boundaries alone do not provide that assurance without tested enforcement.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.22 when selected or otherwise committed to.
- **Implementation guidance:** Define **segregation of networks** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

Development, production, user, guest, and management networks use separate policies. Only documented service flows are permitted, administrative access uses a controlled path, and rule reviews remove obsolete connections.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Flat network architecture — all systems, users, and services share the same broadcast domain with no internal segmentation.
- Segregation is implemented but bypassed — management interfaces, backup networks, or IoT devices connect across zones.
- Firewall rules accumulate over time with no periodic review — "temporary" openings become permanent.
- Guest and BYOD networks have the same access level as internal corporate networks.

## Auditor questions

- How are network zones defined, and what criteria determine zone membership?
- What controls govern traffic between zones, and how are exceptions approved and reviewed?
- How often are firewall rules and zone policies reviewed, and who performs the review?
- Show evidence that zone separation is tested and that lateral movement between zones is restricted.

## Checklist

- [ ] network zones defined based on trust and sensitivity levels
- [ ] inter-zone traffic restricted to documented and approved flows
- [ ] guest and BYOD networks isolated from corporate resources
- [ ] firewall rules reviewed on a defined schedule
- [ ] zone separation tested (penetration test or configuration audit)
- [ ] bypass paths identified and documented with compensating controls

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
