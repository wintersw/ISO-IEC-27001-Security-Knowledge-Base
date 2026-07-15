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

## Key concepts

- **Applicability:** why the control is or is not needed in context.
- **Control owner:** the role accountable for design, operation, evidence, and improvement.
- **Operating evidence:** scoped, dated records showing what occurred and who approved it.
- **Effectiveness:** achievement of the intended outcome, not activity completion alone.

## Practical implementation

This control establishes accountability and prevents security work from becoming an informal activity with no decision owner. Implementation should distinguish who is accountable, who performs the work, who provides assurance, and who must be consulted.

For A.8.8, begin by identifying the specific risk, legal requirement, contractual commitment, or operational need that makes the control necessary. The control owner should then define what is in scope, which roles perform the activity, which systems or data sources are authoritative, how exceptions are handled, and what evidence proves that the control operated.

1. Define the control objective.
2. Assign a control owner and operator.
3. Document the minimum process needed for repeatability.
4. Integrate the control into normal workflows.
5. Define evidence before the control goes live.
6. Monitor operation and exceptions.
7. Review effectiveness and improve.

### Measures that support decisions

- critical vulnerabilities overdue
- scanner asset coverage
- verified remediation rate
- exceptions past expiry

Metrics should support decisions. A high completion rate can still be misleading if the population is incomplete, exceptions are hidden, or remediation is not verified.

- completion rate
- overdue action count
- exception count and age
- control coverage
- remediation time
- review timeliness

## Practical example

A critical vulnerability affects an internet-facing application. The team validates exposure, prioritizes using exploitability and criticality, patches through change management, rescans, and tracks any temporary exception.

The example should be tailored to the organization's scope, size, technology, risk appetite, and regulatory context. A small organization may operate the control manually with clear ownership and evidence. A larger organization may use automated workflows, policy enforcement, continuous monitoring, and independent control testing. The underlying objective remains the same.

## Evidence to retain

- scanner coverage report
- validated finding
- remediation ticket
- change record
- rescan or verification evidence
- exception record

Retain both design and operating evidence; policy alone does not prove operation. Prefer authoritative, scoped records with approvals, exceptions, and remediation.

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
- [Abbreviations](../../15-reference/abbreviations.md)
