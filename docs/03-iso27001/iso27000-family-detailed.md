---
title: ISO/IEC 27000 Family Detailed Guide
description: Detailed practical overview of major ISO/IEC 27000-family standards and how security teams use them.
---

# ISO/IEC 27000 Family Detailed Guide

The ISO/IEC 27000 family is a set of standards for information security, cybersecurity, privacy, risk management, and related management practices. ISO/IEC 27001 is the certifiable requirements standard, but it is only one part of the family.

## How to think about the family

| Standard | Practical role |
|---|---|
| ISO/IEC 27000 | ISMS overview; confirm terminology against the current applicable sources and edition |
| ISO/IEC 27001 | Certifiable ISMS requirements |
| ISO/IEC 27002 | Guidance for implementing information security controls |
| ISO/IEC 27005 | Guidance for information security risk management |
| ISO/IEC 27017 | Cloud security control guidance |
| ISO/IEC 27018 | Protection of PII in public cloud processor environments |
| ISO/IEC 27701 | Privacy information management extension |
| ISO/IEC 27035 | Incident management guidance |
| ISO/IEC 27031 | information and communication technology (ICT) readiness for business continuity |
| ISO/IEC 27036 | Supplier relationship security guidance |
| ISO/IEC 27037 | Digital evidence handling guidance |

## ISO/IEC 27000

ISO/IEC 27000:2026 is the sixth-edition ISMS overview. It replaces the withdrawn ISO/IEC 27000:2018 fifth edition, which served as an overview and vocabulary reference. Verify the current publication status; use the 2018 edition only for legacy traceability and edition comparison. Validate terminology against the current standard applicable to the subject.

See [Terminology Governance](../15-reference/terminology-governance.md) for the copyright-safe source hierarchy and review process.

## ISO/IEC 27001

ISO/IEC 27001 defines what an ISMS must do. Certification bodies audit against ISO/IEC 27001, not against the entire 27000 family.

It contains:

- Management-system requirements in clauses 4–10
- Annex A control reference set
- Requirements for risk assessment and risk treatment
- Requirements for the Statement of Applicability
- Internal audit, management review, and continual improvement requirements

## ISO/IEC 27002

ISO/IEC 27002 provides guidance for implementing controls. It is especially useful for control owners because it explains intent and implementation considerations.

## ISO/IEC 27005

ISO/IEC 27005 supports risk-management design. Use it when designing methodology, criteria, risk registers, and treatment approaches.

## ISO/IEC 27017 and 27018

These are useful for cloud-heavy organizations:

- ISO/IEC 27017 focuses on cloud security controls and shared responsibilities.
- ISO/IEC 27018 focuses on protecting personally identifiable information in public cloud processor contexts.

## ISO/IEC 27701

ISO/IEC 27701 extends the ISMS toward privacy information management. It is relevant when an organization processes personal data and wants privacy governance integrated with security governance.

## Common mistake

A common mistake is treating ISO/IEC 27001 as a technical checklist. The correct approach is to treat ISO/IEC 27001 as the management-system backbone and use related standards for implementation detail where useful.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** The ISO/IEC 27000 family contains over 40 published standards. Only ISO/IEC 27001 is a certifiable management system standard. The remaining standards provide vocabulary (ISO/IEC 27000), control guidance (ISO/IEC 27002), risk management guidance (ISO/IEC 27005), sector-specific extensions (ISO/IEC 27017, 27018, 27701), and activity-specific guidance (ISO/IEC 27031, 27035, 27036, 27037). None of the supporting standards impose standalone requirements.
- **Implementation guidance:** Identify which family members are relevant to the organisation's scope, risk treatment, and contractual commitments. Map each standard to the ISMS element it supports.
- **Best practice:** Use the family as a reference library — pull what is useful, but do not treat every standard as mandatory. The ISMS backbone is ISO/IEC 27001 clauses 4-10; the rest is implementation detail.

## Practical example

An ISMS manager mapping the organisation's documentation landscape identifies which ISO/IEC 27000-series standards provide normative requirements (27001, 27701), which provide implementation guidance (27002, 27017, 27018), and which provide sector-specific or activity-specific detail (27005, 27031, 27035, 27036). This mapping prevents treating all standards as mandatory and keeps the management system lean.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- clause or control mapping
- approved management-system document
- operating records from the scoped process
- internal-audit or management-review result

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
