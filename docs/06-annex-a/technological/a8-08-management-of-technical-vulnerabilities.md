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

This control reduces information security risk by establishing clear expectations, repeatable operation, accountability, and evidence for the relevant security activity.

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

- Control exists only on paper.
- Ownership is unclear.
- Evidence is not retained.
- Exceptions are not reviewed.
- Implementation status in the SoA does not match reality.

- policy exists without reliable operation;
- ownership or scope is unclear;
- exceptions lack approval or expiry; and
- evidence or corrective action does not demonstrate effectiveness.

## Auditor questions

- Who owns this control?
- How is it implemented?
- How do you know it operates?
- Show recent evidence.
- How are exceptions handled?
- How is effectiveness reviewed?

- Which risk or requirement does the control address?
- Who owns and operates it, and how is scope determined?
- Which evidence shows recent operation and exception handling?
- How is effectiveness tested and failure remediated?
- What changed after the latest significant review or event?

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
