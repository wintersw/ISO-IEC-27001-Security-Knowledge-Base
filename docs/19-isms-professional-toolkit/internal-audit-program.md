---
title: Internal Audit Program
description: Advanced guidance for building and operating an ISO 27001 internal audit program.
category: ISMS Professional Toolkit
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - isms
  - professional-toolkit
---

# Internal Audit Program

An audit program defines how internal audits are planned, prioritized, performed, reported, and followed up.

## Audit universe

The audit universe is the set of auditable areas in the information security management system (ISMS).

Examples:

- clauses 4–10
- risk management
- SoA and control selection
- identity and access management (IAM)
- vulnerability management
- incident response
- supplier management
- backup and recovery
- secure development
- cloud security
- physical security
- awareness and training

## Risk-based scheduling

Audit higher-risk or weaker areas more frequently.

Factors:

- criticality
- previous findings
- control maturity
- incident history
- supplier dependency
- major changes
- legal or contractual obligations

## Audit evidence strategy

Auditors should test:

- design effectiveness
- operating effectiveness
- evidence quality
- consistency across teams
- corrective-action closure
- management awareness

## Audit outputs

- audit plan
- sample list
- interview notes
- evidence record
- findings
- observations
- opportunities for improvement
- report
- corrective-action tracker

## Common mistakes

- Auditing every area equally.
- Auditing documents but not operation.
- Using auditors who lack independence.
- Not following up corrective actions.
- Treating observations as optional forever.

## Related continual improvement lifecycle guidance

Audit findings should feed the improvement backlog. See:

- [Improvement Sources](../23-continual-improvement/improvement-sources.md)
- [Improvement Backlog](../23-continual-improvement/improvement-backlog.md)
- [Continual Improvement Audit Evidence Checklist](../11-checklists/continual-improvement-audit-evidence-checklist.md)


## Practical example

When building the annual audit plan, the audit owner scores each area of the audit universe against risk factors: incident history pushes vulnerability management to twice-yearly audits, while mature and finding-free physical security drops to a lighter review. During the IAM audit, testing goes beyond the access policy document — the auditor samples joiner-mover-leaver cases and finds two leavers with active accounts, raising a finding that is tracked to verified closure before the certification audit.

## Evidence to retain

Retain records showing both program design and audit execution, such as:

- risk-based audit plan with scheduling rationale
- audit working papers (sample lists, interview notes, evidence records)
- audit reports with findings, observations, and improvement opportunities
- corrective-action tracking through to verified closure


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
