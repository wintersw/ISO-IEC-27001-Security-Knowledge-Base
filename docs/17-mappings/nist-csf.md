---
title: ISO 27001 and NIST Cybersecurity Framework
description: High-level relationship between ISO 27001 and NIST CSF.
category: Mappings
difficulty: Intermediate
reviewed_on: 2026-07-20
applies_to:
  - ISO/IEC 27001:2022
  - NIST CSF 2.0
tags:
  - mapping
---

# ISO 27001 and NIST Cybersecurity Framework

NIST CSF organizes cybersecurity outcomes into functions such as Govern, Identify, Protect, Detect, Respond, and Recover. ISO/IEC 27001 provides a certifiable information security management system (ISMS) structure.

## Practical relationship

| NIST CSF 2.0 Function | ISO/IEC 27001 relationship | Example evidence |
|---|---|---|
| Govern | Clauses 4–7, 9–10 and organizational controls | scope, policies, roles, risk criteria, supplier governance, management decisions |
| Identify | Clauses 4 and 6; A.5.9 and related risk inputs | asset and dependency inventories, risk assessments, impact rationale |
| Protect | selected people, physical, organizational, and technological controls | access reviews, training, configurations, secure-development and data-protection records |
| Detect | A.5.7, A.8.15, A.8.16 and related detection controls | threat-intelligence decisions, log coverage, alert tests and investigations |
| Respond | A.5.24–A.5.28 | plans, cases, communications, evidence handling and lessons learned |
| Recover | A.5.29, A.5.30, A.8.13, A.8.14 and clause 10 | recovery tests, continuity decisions, corrective actions and improvements |

## Best practice

Use ISO 27001 as the management-system backbone and NIST CSF as an outcome-oriented communication framework. A CSF Function is much broader than an Annex A control, and a Function-level match is not a conformity claim. Use the [official NIST CSF 2.0 publication](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) and map Categories/Subcategories for an operational crosswalk.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).


## Practical example

A CSF Current Profile identifies incomplete log coverage under Detect. The organization traces the gap to a risk, evaluates A.8.15 and A.8.16 plus its own monitoring control, updates the treatment plan and SoA, and uses the resulting coverage report in both CSF progress reporting and ISO control assurance.

## Sources

- [NIST Cybersecurity Framework 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final)
