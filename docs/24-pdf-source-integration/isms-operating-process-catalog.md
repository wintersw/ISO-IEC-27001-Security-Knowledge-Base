---
title: ISMS Operating Process Catalog
description: Catalog of recurring ISMS operating processes with roles, inputs, outputs, and interfaces.
category: PDF Source Integration
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - source-integration
  - isms
  - iso27001
---

# information security management system (ISMS) Operating Process Catalog

This catalog converts common ISO/IEC 27001 and ISO/IEC 27002 themes into recurring operational processes.

## Core process catalog

| Process | Typical owner | Key inputs | Key outputs | Key interfaces |
|---|---|---|---|---|
| Personnel security | HR / Security | hiring, role change, termination | screening, onboarding/offboarding records | identity and access management (IAM), legal, managers |
| User registration and deregistration | IAM owner | joiner/mover/leaver events | account creation/removal evidence | HR, service owners |
| Access rights allocation and removal | IAM owner | access request, approval | access changes | asset owners, managers |
| Privileged access management | Security / IAM | administrator access request | privileged account approval, review | IT operations, audit |
| Authentication information management | IAM / IT | credential lifecycle | secrets/password/multifactor authentication (MFA) records | users, service owners |
| Backup and restore management | IT operations | backup policy, systems | backup reports, restore tests | business continuity management system (BCMS), incident management |
| Change security review | Change manager | change request | security approval/conditions | risk, operations, development |
| Malware protection management | Security operations | alerts, endpoint status | detection and remediation records | incident management |
| Vulnerability management | Vulnerability owner | scan results, advisories | remediation tickets, risk acceptance | change, risk, asset owners |
| Incident management | Incident manager | event, alert, report | incident record, lessons learned | legal, privacy, communications |
| Risk management | Risk owner / ISMS | changes, incidents, assets | risk register, treatment plan | SoA, management review |
| Supplier security management | Procurement / Security | supplier onboarding/change | assessment and contract evidence | legal, privacy, risk |
| Awareness and training | ISMS / HR | training need | training records, survey results | managers, HR |
| Internal audit | Audit owner | audit program | audit report, findings | control owners, management |
| Management review | Top management / ISMS | dashboard, risks, audits, incidents | decisions, action plan | all ISMS processes |

## Process maturity scale

| Level | Description |
|---|---|
| 1 Ad hoc | Work occurs but is undocumented |
| 2 Defined | Process exists but evidence is inconsistent |
| 3 Operating | Process is routinely performed |
| 4 Measured | KPIs/KRIs/KCIs exist and are reviewed |
| 5 Improving | Process results drive continual improvement |

## Related documents

- [Control Assurance Methodology](../19-isms-professional-toolkit/control-assurance-methodology.md)
- [Evidence Management Model](../19-isms-professional-toolkit/evidence-management-model.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

A program team uses this synthesis to compare external source ideas with the current ISMS, adopts only practices that address a documented need, and records the local decision rather than treating source material as a requirement.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- source and applicability record
- gap or comparison analysis
- approved adoption decision
- implementation and review evidence

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
