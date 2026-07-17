---
title: A.5.36 Compliance with policies, rules and standards
description: Practical implementation, evidence, and audit guidance for A.5.36.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.36 Compliance with policies, rules and standards

## Overview

Organizations need to check whether people and systems actually follow approved security policies, rules, and standards. Compliance review should use evidence and address causes and consequences of deviations.

## Purpose

This control ensures that compliance with the organization's own security policies, rules, and standards is regularly reviewed — and that deviations are identified, explained, and remediated. A policy that is never checked for compliance is not a policy; it is a suggestion.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.36 when selected or otherwise committed to.
- **Implementation guidance:** Define **compliance with policies, rules and standards** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A monthly configuration review compares internet-facing servers with the approved hardening standard, records authorized exceptions, creates remediation for unexplained drift, and reports recurring failures to the control owner.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Compliance is checked only before certification audits — the rest of the year, drift goes undetected.
- Review scope is limited to a sample of controls — systemic noncompliance in un-sampled areas is invisible.
- Deviations are identified but not investigated for root cause — the same noncompliance recurs in every review.
- Compliance review is treated as a tick-box exercise — reviewers confirm existence of documentation without testing effectiveness.

## Auditor questions

- How is compliance with security policies, rules, and standards reviewed?
- What is the frequency and scope of compliance reviews?
- How are deviations from policies handled — are they corrected, accepted with compensating controls, or ignored?
- Show evidence from a recent compliance review, including identified deviations and corrective actions.

## Checklist

- [ ] compliance review programme defined with scope and frequency
- [ ] review methodology covers documentation and effectiveness
- [ ] deviation handling process defined
- [ ] root cause analysis performed for systemic noncompliance
- [ ] compliance metrics reported to management
- [ ] review findings tracked to corrective actions

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
