---
title: A.8.18 Use of privileged utility programs
description: Practical implementation, evidence, and audit guidance for A.8.18.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.18 Use of privileged utility programs

## Overview

Privileged utility programs can bypass ordinary application and operating-system controls. Their availability and use should be restricted, approved, logged, reviewed, and removed where no legitimate need exists.

## Purpose

A.8.18 ensures that programs capable of bypassing application or operating-system controls are identified and their availability and use are restricted, authorized, and monitored according to risk. Separation from ordinary activity and stronger session controls provide additional assurance where justified.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.18 when selected or otherwise committed to.
- **Implementation guidance:** Define **use of privileged utility programs** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

Identify privileged utility programs across the applicable estate, including administrative tools, system utilities, debuggers, protocol analyzers, and software capable of bypassing application or operating-system controls. Restrict installation and execution through application-control policies or endpoint management. Require approval, justification, and time-bound access where appropriate. Log the user, utility, target, time, and outcome; record parameters only where useful and safe, with secrets and sensitive values redacted or protected. Segregate privileged utility use from normal activity using controls proportionate to risk, such as dedicated privileged workstations or monitored jump hosts. Review execution logs for unauthorized or anomalous use, and remove utilities where no legitimate need exists.

### Measures that support decisions

- privileged utilities inventoried and approved
- executions logged and reviewed
- just-in-time access grants
- utilities removed where no need exists

## Common mistakes

- Failing to inventory privileged utilities, resulting in unknown bypass-capable tools on production systems.
- Granting permanent access to privileged utilities instead of requiring just-in-time, time-bound approval.
- Omitting useful execution context, or logging parameters without redacting secrets and sensitive values.
- Allowing privileged utility use from the same session or device as normal user activity.

## Auditor questions

- Is there an inventory of all privileged utility programs across the estate?
- Are privileged-utility executions logged with sufficient protected context to support review and investigation?
- Is privileged utility use segregated from normal user sessions?
- How are unauthorized or unnecessary utilities identified and removed?

## Checklist

- [ ] Privileged utilities inventoried with business justification
- [ ] Execution restricted through application control or endpoint management
- [ ] Access requires approval with time-bound, just-in-time grants
- [ ] Executions logged with user, utility, target, outcome, and safely captured context
- [ ] Privileged sessions run on dedicated workstations or jump hosts
- [ ] Execution logs reviewed regularly for unauthorized or anomalous use

## Practical example

A database repair utility is absent from standard administrator roles. Emergency use requires an incident ticket and temporary approval, runs through a monitored privileged session, and is reviewed after access expires.

## Evidence to retain

- identity inventory or authoritative export
- access request and approval
- access review record
- removal or modification ticket
- authentication and privileged-session logs

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
