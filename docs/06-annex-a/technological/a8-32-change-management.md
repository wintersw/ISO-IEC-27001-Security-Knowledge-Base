---
title: A.8.32 Change management
description: Practical implementation, evidence, and audit guidance for A.8.32.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.32 Change management

## Overview

Change management evaluates, authorizes, tests, implements, verifies, and records changes that can affect information security. The process should be proportionate, include emergency paths, and preserve accountability from request through review.

## Purpose

This control ensures that changes to information processing facilities, systems, and services are planned, assessed for security impact, authorized, tested, implemented, and verified. Poorly controlled change is consistently among the top causes of security incidents and unplanned downtime.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.32 when selected or otherwise committed to.
- **Implementation guidance:** Define **change management** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- high-risk changes with security review
- security defects escaped to production
- critical findings fixed before release
- emergency changes reviewed

## Practical example

A firewall change records purpose, affected services, security impact, test and rollback steps, approvals, implementation logs, and validation. An emergency change is permitted during an incident but receives retrospective review.

## Evidence to retain

- security requirements
- architecture or threat-model review
- test results
- release/change approval
- defect and remediation records

## Common mistakes

- Emergency changes bypass all controls with no retrospective review — "emergency" becomes the normal path.
- Security impact assessment is a checkbox rather than a meaningful review by someone qualified to assess risk.
- Changes are tested only for functionality — security regression testing is not part of the test plan.
- Rollback plans are incomplete or untested — when a change fails, the team cannot restore the previous state.

## Auditor questions

- How are changes classified by risk, and what approval levels correspond to each classification?
- Who performs the security impact assessment, and what criteria do they use?
- How are emergency changes controlled, and how are they reviewed after the fact?
- Show evidence that recent changes included security impact assessment and successful testing.

## Checklist

- [ ] change classification and approval levels defined
- [ ] security impact assessment required for all changes
- [ ] testing includes security regression verification
- [ ] rollback plan documented and tested
- [ ] emergency change procedure with retrospective review defined
- [ ] change records retained with approval and test evidence

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
