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

The purpose of A.8.19 is to reduce the likelihood or impact of failures related to **installation of software on operational systems**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

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

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
