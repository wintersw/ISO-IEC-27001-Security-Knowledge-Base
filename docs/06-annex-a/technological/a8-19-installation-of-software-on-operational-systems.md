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

## Key concepts

- **Applicability:** why the control is or is not needed in context.
- **Control owner:** the role accountable for design, operation, evidence, and improvement.
- **Operating evidence:** scoped, dated records showing what occurred and who approved it.
- **Effectiveness:** achievement of the intended outcome, not activity completion alone.

## Practical implementation

This control supports a defined information security outcome. Implementation should be risk-based, assigned to an owner, integrated into normal work, evidenced, monitored, and improved when conditions change.

For A.8.19, begin by identifying the specific risk, legal requirement, contractual commitment, or operational need that makes the control necessary. The control owner should then define what is in scope, which roles perform the activity, which systems or data sources are authoritative, how exceptions are handled, and what evidence proves that the control operated.

## Practical example

A production agent update is obtained from a verified source, tested, approved through change management, deployed by an authorized service account, checked for expected version and health, and rolled back if acceptance criteria fail.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

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
- [ ] Related risks identified
- [ ] Implementation approach documented
- [ ] Evidence sources identified
- [ ] Review frequency defined

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Abbreviations](../../15-reference/abbreviations.md)
