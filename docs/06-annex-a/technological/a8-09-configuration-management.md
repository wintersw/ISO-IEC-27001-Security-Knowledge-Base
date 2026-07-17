---
title: A.8.9 Configuration management
description: Practical implementation, evidence, and audit guidance for A.8.9.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.9 Configuration management

## Overview

Configuration management defines, approves, records, monitors, and changes secure settings for systems and services. Baselines should be appropriate to asset purpose and make unauthorized or accidental drift visible.

## Purpose

This control ensures that systems, applications, and network devices are configured to approved security baselines, and that configuration changes are authorized, recorded, and monitored for drift. Uncontrolled configuration changes are a leading cause of security incidents, outages, and audit findings.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.9 when selected or otherwise committed to.
- **Implementation guidance:** Define **configuration management** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A cloud service baseline requires approved identity, logging, encryption, and network settings. Automated checks identify a disabled log source, create a ticket, and verify restoration while an authorized temporary deviation follows the exception process.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Security baselines are documented but not enforced — manual configuration without automated drift detection.
- Default vendor credentials, ports, and services are left enabled after deployment.
- Configuration changes are made directly in production without approval, peer review, or audit trail.
- Configuration baselines are not reviewed after vulnerabilities are disclosed or threat landscape changes.

## Auditor questions

- Where are configuration baselines documented, and how are they enforced across the estate?
- How are configuration changes authorized, tested, and recorded?
- How is configuration drift detected and remediated?
- Show evidence that default credentials and unnecessary services are disabled on deployed systems.

## Checklist

- [ ] security baselines documented for all system types
- [ ] automated configuration enforcement or drift detection in place
- [ ] default credentials and unnecessary services disabled
- [ ] configuration changes follow approved change process
- [ ] baselines reviewed after vulnerability disclosures
- [ ] configuration audit evidence retained

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
