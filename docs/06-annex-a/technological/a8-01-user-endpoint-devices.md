---
title: A.8.1 User endpoint devices
description: Practical implementation, evidence, and audit guidance for A.8.1.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.1 User endpoint devices

## Overview

User endpoint devices include laptops, phones, tablets, workstations, and similar devices through which people reach information and services. Secure configuration, management, updates, protection, monitoring, loss response, and disposal should follow the device lifecycle.

## Purpose

This control ensures that user endpoint devices — laptops, phones, tablets, and workstations — are securely configured, protected, monitored, and disposed of throughout their lifecycle. Without consistent endpoint management, unpatched devices, weak configurations, and lost or stolen hardware become unmanaged entry points into organizational systems.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.1 when selected or otherwise committed to.
- **Implementation guidance:** Define **user endpoint devices** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A company laptop is enrolled before use, receives an approved configuration, encryption, endpoint protection, patching, screen lock, and remote-loss actions. Compliance status controls access, and retirement includes verified data sanitization.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- BYOD devices are permitted without a formal policy, security baseline, or enrollment requirement.
- Device inventory is incomplete — retired, lost, or personally-owned devices accessing corporate data are unaccounted for.
- Encryption and screen-lock policies are not enforced or verified across all device types.
- Lost or stolen devices lack a documented response procedure with remote wipe capability and notification timelines.

## Auditor questions

- How are endpoint devices hardened before deployment, and how is the configuration baseline enforced and verified?
- What device types are in scope, and how is the inventory kept current?
- How are lost or stolen devices reported, investigated, and remotely wiped?
- Show evidence that endpoint protection (anti-malware, encryption, patching) is deployed and compliant across the fleet.

## Checklist

- [ ] device inventory maintained and reconciled
- [ ] security baseline defined and enforced
- [ ] encryption enabled on all portable devices
- [ ] screen lock configured with appropriate timeout
- [ ] lost/stolen device procedure documented and tested
- [ ] disposal and sanitization process verified

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
