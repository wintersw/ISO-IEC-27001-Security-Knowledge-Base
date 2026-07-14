---
title: Security Project Delivery Guide
description: Risk-based planning, delivery, acceptance, and operational handover for security projects.
category: Implementation
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - implementation
  - project-management
  - security-lifecycle
---

# Security Project Delivery Guide

## Overview

A security project should deliver an operating security outcome, not merely install a product or publish a document. The work begins by defining the problem and intended result, then connects requirements, risk, design, acceptance, evidence, and operational ownership through explicit decision gates.

## Purpose

This guide helps project sponsors, managers, security specialists, and operational owners prevent common delivery failures: selecting a solution before understanding the problem, treating activity completion as acceptance, losing security requirements during change, and closing the project before the control can be operated and evidenced.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** ISO/IEC 27001 requires the organization to plan and control relevant information security management system (ISMS) processes, address risks, provide resources and competence, retain necessary documented information, and evaluate results. Annex A.5.8 is considered through risk treatment and the Statement of Applicability; ISO does not prescribe the project method in this guide.
- **Implementation guidance:** Apply proportional gates and records to projects that create or materially change information, technology, facilities, suppliers, business processes, or ISMS arrangements.
- **Best practice:** Separate project-delivery risk from the information-security risk being treated, define acceptance before build, and make operational handover a condition of closure.

## Key concepts

- **Problem statement:** the harmful condition, exposure, obligation, or capability gap to be addressed, without prematurely naming a solution.
- **Outcome:** the observable security and business result expected after delivery.
- **Acceptance criterion:** a measurable condition that must be satisfied for an output or outcome to be accepted.
- **Project risk:** uncertainty that can affect cost, schedule, scope, quality, or delivery.
- **Security risk:** uncertainty about harm to information, services, people, or the organization. A project may finish on time while leaving the security risk untreated.
- **Operational handover:** the transfer of ownership, procedures, competence, monitoring, support, evidence, and unresolved risk into normal operation.

## Practical implementation

### Gate 1 — Frame and authorize

Record the problem, affected services and information, business impact, obligations, sponsor, outcome, scope, exclusions, assumptions, constraints, initial security risk, and authority to proceed. Compare plausible treatment options before committing to a technology or supplier.

### Gate 2 — Plan and design

Translate the outcome into business, security, privacy, operational, legal, contractual, and technical requirements. Assign owners and acceptance criteria. Map dependencies, skills, resources, schedule, whole-life cost, project risks, communications, evidence sources, and change control. Confirm how the design will fail safely, recover, and be retired.

### Gate 3 — Build and verify

Maintain traceability from requirement to design decision, implementation, test, finding, remediation, and acceptance. Control scope changes and record their effect on risk, cost, schedule, evidence, and intended outcomes. Use independent or specialist review where risk warrants it.

### Gate 4 — Release and hand over

Before go-live, confirm security testing, data migration, configuration baselines, monitoring, incident response, backup and recovery, support contacts, supplier obligations, training, procedures, rollback, residual-risk decisions, and evidence ownership. The operational owner should accept the service or control explicitly.

### Gate 5 — Close and realize benefits

Close or transfer open issues, changes, defects, exceptions, and actions. Reconcile assets, documents, risks, controls, contracts, and evidence repositories. Record lessons learned and schedule a post-implementation review that evaluates the intended security outcome after representative operation.

## Practical example

A company starts a project described as “buy a privileged access tool.” The sponsor reframes the problem: administrator accounts are shared, persistent, weakly reviewed, and poorly logged. Options include process changes, identity-platform configuration, and a specialist service. The selected design has acceptance criteria for named accounts, approval, time-limited access, session evidence, emergency access, removal of legacy paths, and operational alert handling. The project closes only after the service owner accepts procedures and support, administrators are trained, residual exceptions have owners and expiry dates, and a 60-day review confirms that unmanaged privileged access has actually fallen.

## Evidence to retain

- approved charter, problem statement, outcome, scope, assumptions, constraints, sponsor, and decision authority;
- stakeholder, role, competence, communication, dependency, schedule, resource, and whole-life-cost records;
- requirements and acceptance-criteria traceability;
- architecture, supplier, risk, privacy, and change decisions;
- build, configuration, test, defect, remediation, retest, and release records;
- operational acceptance, training, procedures, monitoring, recovery, rollback, and support evidence;
- residual-risk and exception approvals; and
- closure, lessons learned, post-implementation review, and benefit-realization evidence.

## Common mistakes

- naming a product as the problem statement;
- measuring installation rather than risk reduction or service outcome;
- omitting users, operations, suppliers, legal, privacy, or assurance stakeholders;
- allowing scope changes to bypass risk and acceptance review;
- confusing project risk with the security risk being treated;
- accepting unresolved findings without an authorized owner and expiry;
- treating documentation and training as end-of-project cleanup; and
- closing before monitoring, support, evidence, and control ownership work in practice.

## Auditor questions

- Which risk, obligation, or objective authorized the project, and who sponsored it?
- How were alternatives, scope, assumptions, dependencies, and whole-life costs evaluated?
- Can requirements be traced to design, testing, acceptance, and retained evidence?
- Who accepted residual risk, operational ownership, and unresolved items?
- What post-implementation evidence shows that the intended security outcome was achieved?

## Checklist

- [ ] Problem, outcome, sponsor, scope, exclusions, assumptions, and authority approved
- [ ] Security risk and project-delivery risk recorded separately
- [ ] Requirements have owners, acceptance criteria, and evidence sources
- [ ] Dependencies, competence, resources, whole-life cost, and communications planned
- [ ] Changes assessed for outcome, risk, schedule, cost, and evidence impact
- [ ] Security tests, findings, fixes, exceptions, and retests traceable
- [ ] Operational owner accepts monitoring, support, recovery, procedures, and training
- [ ] Residual risk and open items have authorized owners and review dates
- [ ] Assets, risks, controls, documents, suppliers, and evidence reconciled at closure
- [ ] Post-implementation outcome and lessons-learned review scheduled

## Related controls, clauses, templates, and checklists

- [A.5.8 Information security in project management](../06-annex-a/organizational/a5-08-information-security-in-project-management.md)
- [Clause 6 — Planning](../03-iso27001/clause-6-planning.md)
- [Change and Release Security Lifecycle](../31-security-lifecycle-management/change-release-lifecycle.md)
- [Certification Project Plan](certification-project-plan.md)
- [ISMS Implementation Workstream Plan Template](../10-templates/implementation-workstream-plan-template.md)
- [Change Security Impact Checklist](../11-checklists/change-security-impact-checklist.md)
- [Abbreviations](../15-reference/abbreviations.md)
