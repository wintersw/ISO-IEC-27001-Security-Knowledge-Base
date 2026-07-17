---
title: A.7.13 Equipment maintenance
description: Practical implementation, evidence, and audit guidance for A.7.13.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.7.13 Equipment maintenance

## Overview

Maintenance keeps equipment reliable without exposing information or introducing unauthorized changes. Approved personnel, scheduling, supervision, data protection, configuration checks, and service records should cover on-site and off-site work.

## Purpose

Equipment maintenance ensures that servicing, repair, and upkeep activities do not compromise the confidentiality, integrity, or availability of information — whether performed on-site by internal staff or off-site by external providers.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.7.13 when selected or otherwise committed to.
- **Implementation guidance:** Define **equipment maintenance** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

Before a storage device is sent for repair, the owner confirms backup, removes or sanitizes data where feasible, approves the provider, records custody, and checks configuration and function when it returns.

## Evidence to retain

- site risk assessment
- access records
- visitor records
- inspection or maintenance records
- incident and corrective-action records

## Common mistakes

- Allowing third-party maintenance personnel unsupervised access to equipment containing sensitive data
- Sending equipment for off-site repair without verifying that data has been backed up and sanitized
- Not verifying that the equipment's configuration and security controls are intact after maintenance work
- Failing to log maintenance activities, making it impossible to correlate service events with security incidents

## Auditor questions

- How are maintenance personnel vetted, supervised, and restricted while working on sensitive equipment?
- What happens to data on equipment before it is sent off-site for repair?
- How do you verify that equipment is returned in its expected configuration after maintenance?
- Can you show maintenance logs for critical systems covering the last review period?

## Checklist

- [ ] Maintenance personnel authorized, identified, and supervised based on equipment sensitivity
- [ ] Data backed up and sanitized before equipment leaves the site for repair
- [ ] Post-maintenance checks verify configuration, security controls, and proper function
- [ ] Maintenance activities logged with date, personnel, scope, and outcome
- [ ] Maintenance schedule defined and tracked for all critical equipment

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
