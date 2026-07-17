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

This control ensures that security testing — automated and manual — is planned, executed, and used to verify that systems meet security requirements and resist relevant threats before acceptance and after significant change. Testing that finds nothing is often testing that was not designed to find anything.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.29 when selected or otherwise committed to.
- **Implementation guidance:** Define **security testing in development and acceptance** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

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

## Practical example

Before a new application release, automated and manual tests cover authentication, authorization, input handling, dependencies, configuration, and abuse cases. High-risk findings block release, and fixes require recorded retesting.

## Evidence to retain

- security requirements
- architecture or threat-model review
- test results
- release/change approval
- defect and remediation records

## Common mistakes

- Testing is limited to automated scanning — manual testing for business logic flaws, authorization bypass, and abuse cases is omitted.
- Test environments differ from production, so issues that would manifest in production go undetected.
- Findings are documented but not assigned owners or tracked to closure — the same vulnerabilities appear in every test cycle.
- Testing scope is not risk-based — low-risk components are tested exhaustively while high-risk interfaces get superficial coverage.

## Auditor questions

- How is the scope and depth of security testing determined for each release?
- What combination of automated and manual testing is used, and who performs the manual testing?
- How are security test findings tracked, prioritized, and verified as remediated?
- Show evidence that critical and high-risk findings are resolved before release acceptance.

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
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
