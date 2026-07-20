---
title: ISO 27001 and SOC 2
description: Relationship between ISO certification and SOC 2 reporting.
category: Mappings
difficulty: Intermediate
reviewed_on: 2026-07-20
applies_to:
  - ISO/IEC 27001:2022
  - AICPA Trust Services Criteria
tags:
  - mapping
---

# ISO 27001 and SOC 2

ISO/IEC 27001 is a certifiable management-system standard. SOC 2 is an attestation report based on Trust Services Criteria.

## Practical differences

| Topic | ISO 27001 | SOC 2 |
|---|---|---|
| Output | Certificate | Attestation report |
| Scope | information security management system (ISMS)-defined scope | System/service description |
| Approach | Risk-based management system | Criteria-based control reporting |
| Audience | Global customers and stakeholders | Often customer assurance, especially in software as a service (SaaS) |

## Evidence reuse

Many controls and evidence types overlap, especially access control, change management, incident response, risk assessment, vendor management, logging, and monitoring.

| Reuse question | Why it matters |
|---|---|
| Are the ISMS and system-description boundaries the same? | Excluded entities, infrastructure, locations, or processes can invalidate reuse. |
| Does the evidence cover the same period and population? | A point-in-time ISO sample may not support a period-of-time attestation test. |
| Are the control objective and Trust Services Criteria point of focus addressed? | Similar control names can conceal a different assertion or test purpose. |
| Are complementary user-entity and subservice-organization controls identified? | These may sit outside the organization's direct ISO control operation. |

Confirm the applicable AICPA Trust Services Criteria and reporting requirements with the responsible CPA firm; a private crosswalk is not an attestation opinion.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).


## Practical example

A quarterly access review covers the same production service, identities, and period used for both programs. The evidence can be reused, but the ISO audit evaluates the ISMS control and risk rationale while the SOC 2 examination tests the control against the scoped system description and applicable criteria.

## Sources

- [AICPA SOC 2 resources](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2)
