---
title: A.8.29 Security testing in development and acceptance
description: Practical implementation, evidence, and audit guidance for A.8.29.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.29 Security testing in development and acceptance

## Overview

Security testing provides evidence that systems meet defined requirements and resist relevant misuse before acceptance and after significant change. Test depth, independence, environments, data, defects, retesting, and release decisions should be planned.

## Purpose

The purpose of A.8.29 is to reduce the likelihood or impact of failures related to **security testing in development and acceptance**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.29 when selected or otherwise committed to.
- **Implementation guidance:** Define **security testing in development and acceptance** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Key concepts

- **Applicability:** why the control is or is not needed in context.
- **Control owner:** the role accountable for design, operation, evidence, and improvement.
- **Operating evidence:** scoped, dated records showing what occurred and who approved it.
- **Effectiveness:** achievement of the intended outcome, not activity completion alone.

## Practical implementation

This control embeds security into system and software lifecycle decisions. Security requirements should be defined early, tested before release, recorded in change evidence, and reviewed when architecture or risk changes.

For A.8.29, begin by identifying the specific risk, legal requirement, contractual commitment, or operational need that makes the control necessary. The control owner should then define what is in scope, which roles perform the activity, which systems or data sources are authoritative, how exceptions are handled, and what evidence proves that the control operated.

Use a risk-based test plan that states:

- the system, version, environment, interfaces, identities, data, suppliers, and excluded components;
- the security requirements and abuse cases being verified;
- permitted techniques, test accounts, data-handling rules, stop conditions, and escalation contacts;
- required independence and competence for the risk level;
- finding severity, release thresholds, exception authority, and remediation deadlines; and
- who confirms fixes, preserves results, and accepts residual risk.

Combine automated testing with targeted manual verification. At minimum, consider external exposure, authentication and recovery, session handling, authorization and business rules, input and output handling, file processing, configuration, dependencies, logging, and failure behavior when relevant to the system. Retest material findings against the released build or configuration.

### Measures that support decisions

- high-risk changes with security review
- security defects escaped to production
- critical findings fixed before release
- emergency changes reviewed

Metrics should support decisions. A high completion rate can still be misleading if the population is incomplete, exceptions are hidden, or remediation is not verified.

## Practical example

Before a new application release, automated and manual tests cover authentication, authorization, input handling, dependencies, configuration, and abuse cases. High-risk findings block release, and fixes require recorded retesting.

## Evidence to retain

- security requirements
- architecture or threat-model review
- test results
- release/change approval
- defect and remediation records

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
- [ ] Test scope, authority, environment, and stop conditions approved
- [ ] Requirements and abuse cases trace to related risks
- [ ] Automated and manual coverage selected for the risk level
- [ ] Release thresholds and exception authority defined
- [ ] Findings assigned, fixed or formally accepted, and retested
- [ ] Results linked to the tested version and retained securely

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Abbreviations](../../15-reference/abbreviations.md)
