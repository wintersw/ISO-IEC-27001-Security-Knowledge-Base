---
title: Control Assurance Review Checklist
description: "Professional ISMS checklist: Control Assurance Review Checklist."
category: Checklists
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - checklist
  - isms-professional-toolkit
---

# Control Assurance Review Checklist

Use this shared checklist with any Annex A control or organization-specific control. Individual control pages provide control-specific implementation and evidence guidance; this checklist supplies the common assurance questions that should not be repeated on every page.

## Applicability and design

- [ ] The risk, obligation, or business requirement addressed by the control is identified.
- [ ] The applicability decision and implementation status agree with the Statement of Applicability.
- [ ] The expected security outcome and control objective are testable.
- [ ] Scope, population, frequency, trigger, dependencies, and authoritative data sources are defined.
- [ ] An accountable control owner and the roles that operate, approve, and independently review the control are confirmed.
- [ ] Exception, escalation, and risk-acceptance paths have appropriate authority and expiry criteria.

## Operating effectiveness

- [ ] The control operated at the required frequency and covered the complete in-scope population.
- [ ] A risk-based sample covers different dates, systems, locations, operators, and relevant exceptions.
- [ ] Evidence is dated, attributable, protected, and traceable to the activity performed.
- [ ] Policy or design documents are supported by recent operating records.
- [ ] Failures and exceptions were detected, approved where appropriate, remediated, and followed through to closure.
- [ ] Reperformance, configuration review, observation, data analysis, or another suitable method tests effectiveness rather than activity alone.
- [ ] Incidents, complaints, audit findings, changes, and repeated exceptions were considered when evaluating effectiveness.

## Results and follow-up

- [ ] Design gaps and operating failures are distinguished in the test result.
- [ ] Findings state the criterion, condition, evidence, scope, and risk clearly.
- [ ] Corrective or improvement actions have owners, deadlines, and effectiveness-verification methods.
- [ ] Related risks, treatment plans, control descriptions, and SoA status are updated when necessary.
- [ ] Material or recurring failures are escalated to the appropriate risk owner or governance forum.

## Questions for the control owner

- Which risk or requirement does this control address, and has that basis changed?
- Who owns and operates it, and how is its scope and population established?
- Which evidence demonstrates recent operation, approvals, and exception handling?
- How is effectiveness tested, and what would constitute failure?
- What changed after the latest incident, finding, exception trend, or material review?

## Interpreting measures

A completion percentage is not automatically an effectiveness measure. A control may report 100% completion while omitting part of the population, approving weak exceptions, operating too late, or failing to achieve its security outcome. Pair activity measures with coverage, timeliness, failure, exception, recurrence, and outcome indicators suited to the control.

Example: report not only the percentage of access reviews completed, but also applications omitted, accounts reviewed late, inappropriate access found, remediation time, overdue removals, and repeat findings.

## Common assurance mistakes

- treating the existence of a policy or screenshot as proof of reliable operation;
- accepting an owner assertion without testing the underlying population or records;
- selecting a convenient sample that excludes failures, changes, or exceptions;
- recording an exception without approval, compensating safeguards, owner, or expiry;
- measuring completion without testing whether the intended outcome was achieved; and
- closing a finding when an action is completed without verifying that it worked.

## Evidence to retain

Retain the completed checklist, test plan, population and sample rationale, source records, results, reviewer identity, findings, decisions, assigned actions, and effectiveness verification.

## How to use this checklist

Assign a competent reviewer, scope, period, method, and deadline. Independence should be proportionate to risk; a control owner can perform routine self-checks, but higher-risk controls and disputed results benefit from independent testing. A failed item requires an owned corrective action, justified exception, or authorized risk decision. A checked box alone is not evidence.

## Practical example

An assurance reviewer tests quarterly privileged-access reviews. The reviewer reconciles the application inventory to the review population, samples approvals and removals across the quarter, checks overdue actions and exceptions, and compares results with identity incidents. Although the dashboard reports 100% completion, one acquired application was omitted. The result is therefore partially effective, and the inventory-to-review reconciliation becomes a corrective action subject to later effectiveness verification.

## ISO requirement, implementation guidance, and best practice

This checklist is project guidance, not prescribed ISO wording and not a claim that every test method is mandatory. ISO/IEC 27001 requires the organization to evaluate performance and effectiveness, conduct internal audits, address nonconformities, and retain specified evidence. The organization determines proportionate assurance methods from risk, obligations, its control design, and its audit programme.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](index.md) · [abbreviations](../15-reference/abbreviations.md).

Related guidance: [Control Assurance Methodology](../19-isms-professional-toolkit/control-assurance-methodology.md) · [Control Owner Self-Assessment](../19-isms-professional-toolkit/control-owner-self-assessment.md) · [Evidence and Assurance Lifecycle](../31-security-lifecycle-management/evidence-assurance-lifecycle.md).
