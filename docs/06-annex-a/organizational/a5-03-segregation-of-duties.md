---
title: A.5.3 Segregation of duties
description: Practical implementation, evidence, and audit guidance for A.5.3.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.3 Segregation of duties

## Overview

Segregation of duties prevents one person from completing incompatible steps without oversight. Where staffing makes full separation impractical, the organization should add approval, logging, or retrospective review that can detect misuse or error.

## Purpose

This control ensures that conflicting duties are identified and separated so that no single individual can complete a high-risk transaction or process without independent oversight. Where full separation is impractical, compensating controls such as monitoring, audit logging, or retrospective review are essential.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.3 when selected or otherwise committed to.
- **Implementation guidance:** Define **segregation of duties** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A developer may prepare a production change but cannot approve and deploy it alone. An operations engineer deploys the approved release, and emergency self-approval is logged, time-limited, and reviewed the next business day.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Conflicting duties are not formally identified — the organization assumes separation exists where it does not.
- In small teams, one person holds all keys — development, approval, deployment, and audit — with no compensating controls.
- Segregation is enforced in production but bypassed in development or cloud administration consoles.
- Emergency access procedures allow one person to bypass all segregation without post-event review.

## Auditor questions

- Which conflicting duties have been identified, and where are they documented?
- How is segregation enforced technically and procedurally for high-risk transactions?
- Where full segregation is not possible, what compensating controls are in place?
- Show evidence that emergency bypasses of segregation are logged and retrospectively reviewed.

## Checklist

- [ ] conflicting duties identified and documented
- [ ] segregation enforced for high-risk transactions
- [ ] compensating controls defined where full segregation is impractical
- [ ] emergency bypass logged and retrospectively reviewed
- [ ] segregation reviewed when roles or systems change
- [ ] access rights tested against segregation rules

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
