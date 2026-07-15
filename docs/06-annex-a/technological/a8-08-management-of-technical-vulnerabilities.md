---
title: A.8.8 Management of Technical Vulnerabilities
description: Practical implementation, evidence, and audit guidance for A.8.8.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
  - control
status: expanded
---
# A.8.8 Management of Technical Vulnerabilities

## Overview

Vulnerability management identifies, evaluates, prioritizes, remediates, and verifies weaknesses in technology. It is not just scanning; it connects asset inventory, threat intelligence, patching, exceptions, and risk acceptance.

## Purpose

This control ensures that technical vulnerabilities in information systems are identified, evaluated, prioritized, and remediated before they can be exploited. Without a structured vulnerability management process, organizations operate blind to exploitable weaknesses, and remediation is driven by ad-hoc scanning rather than risk-based prioritization.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.8 when selected or otherwise committed to.
- **Implementation guidance:** Define **management of technical vulnerabilities** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- critical vulnerabilities overdue
- scanner asset coverage
- verified remediation rate
- exceptions past expiry

Metrics should support decisions. A high completion rate can still be misleading if the population is incomplete, exceptions are hidden, or remediation is not verified.

## Practical example

A critical vulnerability affects an internet-facing application. The team validates exposure, prioritizes using exploitability and criticality, patches through change management, rescans, and tracks any temporary exception.

## Evidence to retain

- scanner coverage report
- validated finding
- remediation ticket
- change record
- rescan or verification evidence
- exception record

## Common mistakes

- Scanning is performed but results are not validated — false positives waste effort; false negatives leave exposure undetected.
- Ownership of findings is unclear — vulnerabilities are assigned to "IT" rather than named asset or application owners.
- Exceptions for unpatched vulnerabilities lack approval, compensating controls, and expiry dates.
- Remediation is reported as complete without verification — the ticket is closed but the vulnerability persists.
- Asset coverage is incomplete — unmanaged devices, cloud resources, or container images are not scanned.
- Evidence or corrective action does not demonstrate that the vulnerability management process is effective at reducing exposure over time.

## Auditor questions

- How is the asset scope for vulnerability scanning determined, and how is coverage verified?
- What is the prioritization methodology, and how are remediation SLAs defined and measured?
- Who owns vulnerability findings, and how are overdue remediations escalated?
- Show evidence of recent scanning, prioritization, remediation, and verification.
- How are exceptions to remediation SLAs approved, tracked, and periodically reviewed?
- How is the effectiveness of the vulnerability management process measured and improved?

## Checklist

- [ ] asset scope defined
- [ ] scan coverage reconciled
- [ ] prioritization method approved
- [ ] owners assigned
- [ ] exceptions controlled
- [ ] remediation verified

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
