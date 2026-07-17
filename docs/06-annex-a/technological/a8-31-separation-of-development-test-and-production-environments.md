---
title: A.8.31 Separation of development, test and production environments
description: Practical implementation, evidence, and audit guidance for A.8.31.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.31 Separation of development, test and production environments

## Overview

Separating development, test, and production reduces accidental or unauthorized impact and prevents untested work from bypassing release controls. Separation should cover access, credentials, data, networks, tools, pipelines, and approvals.

## Purpose

This control ensures that development, test, and production environments are separated to prevent unauthorized access, unintended changes, and the exposure of production data in lower environments. A developer accidentally running a test script against production can cause an outage as severe as any external attack.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.31 when selected or otherwise committed to.
- **Implementation guidance:** Define **separation of development, test and production environments** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- high-risk changes with security review
- security defects escaped to production
- critical findings fixed before release
- emergency changes reviewed

## Practical example

Developers cannot directly change production. A controlled pipeline promotes approved artifacts through test to production using separate credentials, while sanitized test data and restricted emergency access prevent environment shortcuts.

## Evidence to retain

- security requirements
- architecture or threat-model review
- test results
- release/change approval
- defect and remediation records

## Common mistakes

- Developers have direct access to production systems and data for debugging purposes.
- Production credentials are reused in development or test environments, creating a path for accidental or malicious misuse.
- The separation relies on naming conventions ("prod-db" vs "dev-db") rather than network, access, and credential isolation.
- Deployment pipelines share credentials across all environments, so a compromise in development grants access to production.

## Auditor questions

- How are development, test, and production environments separated — at the network, access, and credential levels?
- Who has access to production systems, and how is developer access controlled?
- How are deployment pipelines secured to prevent environment crossover?
- Show evidence that production data is not present in development or test environments without approval and masking.

## Checklist

- [ ] environments separated at network, access, and credential levels
- [ ] developer production access restricted and logged
- [ ] separate credentials per environment
- [ ] deployment pipeline segregation enforced
- [ ] production data excluded from non-production environments
- [ ] environment separation tested and verified

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
