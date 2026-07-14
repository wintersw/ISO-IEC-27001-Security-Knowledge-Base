---
title: A.7.4 Physical security monitoring
description: Practical implementation, evidence, and audit guidance for A.7.4.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.7.4 Physical security monitoring

## Overview

Physical monitoring detects and supports investigation of unauthorized entry or suspicious activity. Cameras, alarms, guards, and access records require defined coverage, response, retention, privacy controls, maintenance, and time synchronization.

## Purpose

The purpose of A.7.4 is to reduce the likelihood or impact of failures related to **physical security monitoring**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.7.4 when selected or otherwise committed to.
- **Implementation guidance:** Define **physical security monitoring** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Key concepts

- **Applicability:** why the control is or is not needed in context.
- **Control owner:** the role accountable for design, operation, evidence, and improvement.
- **Operating evidence:** scoped, dated records showing what occurred and who approved it.
- **Effectiveness:** achievement of the intended outcome, not activity completion alone.

## Practical implementation

This control creates visibility into security-relevant activity. Logs and alerts should be designed around investigation and risk scenarios, protected from tampering, retained appropriately, and reviewed through defined workflows.

For A.7.4, begin by identifying the specific risk, legal requirement, contractual commitment, or operational need that makes the control necessary. The control owner should then define what is in scope, which roles perform the activity, which systems or data sources are authoritative, how exceptions are handled, and what evidence proves that the control operated.

### Measures that support decisions

- critical systems with required logging
- alerts triaged within target
- log-source failures
- use cases tested

Metrics should support decisions. A high completion rate can still be misleading if the population is incomplete, exceptions are hidden, or remediation is not verified.

## Practical example

A forced server-room door generates an alert to the facilities responder. Badge and camera records are correlated, access to footage is restricted, the event is investigated, and failed alarm tests create maintenance actions.

## Evidence to retain

- site risk assessment
- access records
- visitor records
- inspection or maintenance records
- incident and corrective-action records

Retain both design and operating evidence; policy alone does not prove operation. Prefer authoritative, scoped records with approvals, exceptions, and remediation.

## Common mistakes

- policy exists without reliable operation;
- ownership or scope is unclear;
- exceptions lack approval or expiry; and
- evidence or corrective action does not demonstrate effectiveness.

## Auditor questions

- Which risk or requirement does the control address?
- Who owns and operates it, and how is scope determined?
- Which evidence shows recent operation and exception handling?
- How is effectiveness tested and failure remediated?
- What changed after the latest significant review or event?

## Checklist

- [ ] Control owner assigned
- [ ] Applicability decision recorded in the SoA
- [ ] Related risks identified
- [ ] Implementation approach documented
- [ ] Evidence sources identified
- [ ] Review frequency defined

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Abbreviations](../../15-reference/abbreviations.md)
