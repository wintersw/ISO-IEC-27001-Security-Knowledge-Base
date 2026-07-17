---
title: A.6.7 Remote working
description: Practical implementation, evidence, and audit guidance for A.6.7.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.6.7 Remote working

## Overview

Remote work moves information and access beyond normal premises, networks, and supervision. Rules should cover approved locations, devices, connectivity, privacy, physical protection, support, incident reporting, and return of assets.

## Purpose

Remote working controls protect information accessed, processed, or stored outside the organization's premises by defining approved locations, devices, connectivity, physical security measures, and incident reporting requirements tailored to off-site risks.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.6.7 when selected or otherwise committed to.
- **Implementation guidance:** Define **remote working** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A worker may access confidential records remotely only from a managed device using multifactor authentication and an approved connection. Screen privacy, local storage, household access, travel, loss reporting, and support are covered in guidance.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Allowing remote work without defining which information classifications may be accessed remotely and which must remain on-premises
- Assuming the home network and physical environment meet the same security standard as the office without verification
- Not addressing screen privacy, shoulder-surfing, or household access to devices in shared living spaces
- Failing to define what must happen when a remote worker's device is lost, stolen, or compromised

## Auditor questions

- How do you determine which roles, devices, and information types are approved for remote access?
- What minimum security controls must be in place on a remote worker's device and connection before access is allowed?
- How do you handle incident reporting when a remote worker's device is lost or stolen?
- What training or guidance do remote workers receive about physical security and privacy in their working environment?

## Checklist

- [ ] Remote working policy defines approved locations, devices, and connectivity requirements
- [ ] Information classification restrictions for remote access documented and enforced
- [ ] Minimum device controls defined (encryption, screen lock, MFA, patching, endpoint protection)
- [ ] Physical security and privacy guidance provided to all remote workers
- [ ] Incident reporting procedure for remote-specific scenarios tested and communicated

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
