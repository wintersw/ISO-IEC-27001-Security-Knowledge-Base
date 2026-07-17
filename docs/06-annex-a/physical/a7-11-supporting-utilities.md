---
title: A.7.11 Supporting utilities
description: Practical implementation, evidence, and audit guidance for A.7.11.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.7.11 Supporting utilities

## Overview

Power, cooling, communications, water, and other utilities can become single points of failure. Capacity, redundancy, monitoring, maintenance, emergency shutdown, and recovery should reflect the supported service's needs.

## Purpose

This control ensures that power, cooling, water, telecommunications, and other utilities supporting information processing facilities are reliable, monitored, and have adequate capacity and redundancy to prevent service disruption or equipment damage.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.7.11 when selected or otherwise committed to.
- **Implementation guidance:** Define **supporting utilities** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A server room uses monitored uninterruptible power and generator support sized for critical loads. Tests confirm runtime and transfer, fuel and maintenance are tracked, and alerts reach an on-call role.

## Evidence to retain

- site risk assessment
- access records
- visitor records
- inspection or maintenance records
- incident and corrective-action records

## Common mistakes

- Assuming building power is sufficient without calculating actual load, redundancy, and runtime requirements
- Installing a UPS and generator but never testing failover under real load conditions
- Not monitoring utility health proactively — discovering cooling failure only when equipment overheats
- Overlooking single points of failure in utility distribution paths (one circuit feeding both primary and redundant equipment)

## Auditor questions

- How did you determine the capacity and redundancy needed for each supporting utility?
- When were UPS and generator failover tests last conducted, and what were the results?
- How are utility failures or degradation detected and alerted to responsible personnel?
- What is the maximum supported runtime on backup power, and what happens when it is exhausted?

## Checklist

- [ ] Utility requirements assessed for each critical facility and documented
- [ ] Redundancy and capacity margins defined and periodically reviewed
- [ ] UPS and backup power tested under load at defined intervals
- [ ] Utility monitoring with alerts configured for power, cooling, and communications
- [ ] Single points of failure in utility distribution identified and mitigated

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
