---
title: A.8.34 Protection of information systems during audit testing
description: Practical implementation, evidence, and audit guidance for A.8.34.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.34 Protection of information systems during audit testing

## Overview

Audit tests can disrupt services, expose information, or weaken controls if performed without coordination. Scope, methods, access, timing, safeguards, evidence, restoration, and responsibility should be agreed before testing operational systems.

## Purpose

This control ensures that audit and assurance tests on operational systems are planned, coordinated, and controlled to prevent disruption, data exposure, or control weakening. Audit testing should not itself become the cause of the incident the organization is trying to prevent.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.34 when selected or otherwise committed to.
- **Implementation guidance:** Define **protection of information systems during audit testing** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

This control prevents assurance work from creating unacceptable operational or information-security risk. The system owner and auditor should agree scope, methods, timing, access, data handling, monitoring, stop conditions, restoration, communications, and responsibility before testing begins.

### Measures that support decisions

- audit tests with approved scope and system-owner authorization
- tests using privileged or write access
- unplanned service impact, stop-condition activation, or scope deviation
- temporary access and test changes removed within target

## Practical example

A production security review has an approved window, named contacts, read-only access by default, prohibited tests, rate limits, monitoring, stop conditions, evidence handling, and verification that temporary access and changes were removed.

## Evidence to retain

- approved audit test plan, risk assessment, and rules of engagement
- system-owner authorization and scheduled window
- temporary access, monitoring, backup, and change records
- test activity log, protected evidence, and incident record where applicable
- restoration check and confirmation that temporary access or changes were removed

## Common mistakes

- Audit testing is scheduled and executed without system-owner awareness or approval.
- No stop conditions are defined — testing continues even when systems show signs of degradation.
- Temporary access and test accounts created for audit are not removed after testing concludes.
- Test scope creeps beyond what was agreed — auditors test systems or methods not included in the approved plan.

## Auditor questions

- How are audit tests on operational systems authorized, and who must approve the scope and timing?
- What stop conditions are defined, and how are they communicated to the testing team?
- How is it verified that temporary access, accounts, and changes are removed after testing?
- Show evidence from the most recent audit test that scope was adhered to and systems were restored.

## Checklist

- [ ] audit test plan approved by system owner before execution
- [ ] scope, methods, timing, and access limits defined
- [ ] stop conditions and escalation contacts documented
- [ ] monitoring in place during test execution
- [ ] temporary access and changes removed after testing
- [ ] post-test restoration verified and documented

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
