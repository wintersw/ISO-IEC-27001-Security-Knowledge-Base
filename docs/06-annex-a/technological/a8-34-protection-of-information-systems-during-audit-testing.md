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

The purpose of A.8.34 is to reduce the likelihood or impact of failures related to **protection of information systems during audit testing**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

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

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
