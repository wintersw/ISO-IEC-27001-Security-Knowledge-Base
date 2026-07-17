---
title: A.8.19 Installation of software on operational systems
description: Practical implementation, evidence, and audit guidance for A.8.19.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.19 Installation of software on operational systems

## Overview

Installing software on operational systems can introduce vulnerabilities, instability, license issues, or unauthorized functions. Installation rights, approved sources, testing, change control, inventory, rollback, and verification should be controlled.

## Purpose

This control ensures that software installation on operational systems is controlled through approved sources, change management, testing, and authorization, preventing unauthorized or malicious software from compromising production stability and security. Uncontrolled installation is a primary vector for malware, backdoors, and configuration drift.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.19 when selected or otherwise committed to.
- **Implementation guidance:** Define **installation of software on operational systems** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A production agent update is obtained from a verified source, tested, approved through change management, deployed by an authorized service account, checked for expected version and health, and rolled back if acceptance criteria fail.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Users have local administrator rights and can install any software without approval.
- Software is sourced from unverified locations (personal websites, direct downloads) instead of an approved repository or vendor.
- Installation is not tested in a staging environment before production deployment.
- No inventory of installed software is maintained, making it impossible to identify unauthorized or vulnerable applications.

## Auditor questions

- Who is authorized to install software on operational systems, and how is this enforced?
- What is the process for approving, testing, and recording software installations?
- How is the software inventory maintained, and how are unauthorized installations detected?
- Show evidence that software sources are verified and that installations follow change management.

## Checklist

- [ ] software installation policy defined and communicated
- [ ] installation rights restricted to authorized personnel
- [ ] approved software sources defined and enforced
- [ ] installation testing in non-production environment required
- [ ] software inventory maintained and reconciled
- [ ] unauthorized installation detection and response procedure in place

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
