---
title: A.5.8 Information security in project management
description: Practical implementation, evidence, and audit guidance for A.5.8.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.8 Information security in project management

## Overview

Projects can create security risk long before a system goes live. Security requirements, risk decisions, assurance, and ownership should therefore be built into project gates and deliverables rather than added at the end.

## Purpose

The purpose of A.5.8 is to reduce the likelihood or impact of failures related to **information security in project management**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.8 when selected or otherwise committed to.
- **Implementation guidance:** Define **information security in project management** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

Embed proportionate security gates in the organization's project method:

1. **Authorization:** define the problem, security outcome, sponsor, scope, assumptions, affected information and services, and initial risks before selecting a solution.
2. **Planning and design:** assign security requirements, acceptance criteria, competence, evidence, dependencies, whole-life resources, and risk owners.
3. **Build and verification:** trace requirements through design, implementation, testing, findings, remediation, and controlled changes.
4. **Release and handover:** confirm operational ownership, monitoring, support, recovery, training, procedures, supplier obligations, residual-risk acceptance, and rollback.
5. **Closure and outcome review:** transfer open items, reconcile assets and records, capture lessons, and verify after representative operation that the intended risk reduction was achieved.

Track project-delivery risks separately from the information-security risks the project is intended to treat. A project can meet schedule and budget while failing its security outcome.

## Practical example

A customer-analytics project cannot pass design approval until it has documented data flows, classification, access roles, supplier dependencies, security tests, residual risks, and the owner who will operate each control after launch.

## Evidence to retain

- approved project-security method, tailoring criteria, and gate authority
- problem statement, outcome, scope, requirements, acceptance criteria, and risk records
- design, change, test, remediation, retest, and release decisions
- operational acceptance, training, monitoring, recovery, support, and evidence ownership
- exception, residual-risk, closure, lessons-learned, and post-implementation review records

## Common mistakes

- security is consulted only after design or procurement;
- the proposed product is mistaken for a problem statement;
- project completion is accepted without measurable security criteria;
- scope and design changes bypass security-risk review;
- project and security risks are mixed together; and
- the project closes before controls, evidence, support, and residual risk have operational owners.

## Auditor questions

- Which projects require security involvement, and how is depth tailored?
- How do security requirements trace to acceptance and retained evidence?
- Who can approve a gate, change, exception, release, and residual risk?
- How is operational ownership demonstrated before project closure?
- Which post-implementation evidence shows that recent projects achieved their security outcomes?

## Checklist

- [ ] Control owner assigned
- [ ] Applicability decision recorded in the SoA
- [ ] Security-project applicability and tailoring rules defined
- [ ] Problem, outcome, scope, risks, sponsor, and authority recorded
- [ ] Requirements have owners, acceptance criteria, and evidence sources
- [ ] Security-impacting changes and exceptions follow authorized decisions
- [ ] Testing, remediation, retesting, and release evidence traceable
- [ ] Operational handover and residual-risk acceptance completed
- [ ] Outcome review and lessons learned retained

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
- [Security Project Delivery Guide](../../16-implementation-guides/security-project-delivery-guide.md)
