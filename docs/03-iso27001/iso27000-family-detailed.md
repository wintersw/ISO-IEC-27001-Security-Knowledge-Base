---
title: ISO/IEC 27000 Family Detailed Guide
description: Detailed practical overview of major ISO/IEC 27000-family standards and how security teams use them.
category: ISO/IEC 27001
difficulty: Intermediate
reviewed_on: 2026-07-20
applies_to:
  - ISO/IEC 27001:2022
tags:
  - iso27001
---

# ISO/IEC 27000 Family Detailed Guide

The ISO/IEC 27000 family is a set of standards for information security, cybersecurity, privacy, risk management, and related management practices. ISO/IEC 27001 is the certifiable requirements standard, but it is only one part of the family.

## How to think about the family

| Standard | Practical role |
|---|---|
| ISO/IEC 27000 | ISMS overview; confirm terminology against the current applicable sources and edition |
| ISO/IEC 27001 | Certifiable ISMS requirements |
| ISO/IEC 27002 | Guidance for implementing information security controls |
| ISO/IEC 27004 | Monitoring, measurement, analysis, and evaluation (security metrics) |
| ISO/IEC 27005 | Guidance for information security risk management |
| ISO/IEC 27007 | Guidelines for auditing an ISMS |
| ISO/IEC TS 27008 | Guidelines for the assessment of information security controls |
| ISO/IEC 27014 | Governance of information security |
| ISO/IEC 27017 | Cloud security control guidance; 2015 edition remains current while the second edition is under publication as of 20 July 2026 |
| ISO/IEC 27018:2025 | Protection of PII in public cloud processor environments |
| ISO/IEC 27701:2025 | Standalone privacy information management system requirements and guidance |
| ISO/IEC 27035 | Incident management guidance |
| ISO/IEC 27031:2025 | information and communication technology (ICT) readiness for business continuity |
| ISO/IEC 27033 | Network security (multi-part) |
| ISO/IEC 27034 | Application security (multi-part) |
| ISO/IEC 27036 | Supplier relationship security guidance |
| ISO/IEC 27037 | Digital evidence handling guidance |
| ISO/IEC 27040 | Storage security |
| ISO/IEC 29100 | Privacy framework and terminology |
| ISO 31000 | General risk management guidelines (not part of the 27000 family) |
| ISO/IEC 42001 | Artificial intelligence management system (AIMS) requirements |

## ISO/IEC 27000

ISO/IEC 27000:2026 is the published sixth-edition ISMS overview. It replaces the withdrawn ISO/IEC 27000:2018 fifth edition, which should be used only for legacy traceability and edition comparison. Validate terminology against the current standard applicable to the subject.

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

ISO/IEC 27701:2025 specifies a standalone PIMS. It can be used independently or integrated with ISO/IEC 27001 when an organization wants shared governance for privacy and information security.

## Measurement, audit, and governance standards

Four family members support the “check” and “direct” parts of the management system and are often overlooked by newcomers:

- **ISO/IEC 27004** helps design the metrics programme required by ISO/IEC 27001 Clause 9.1. It explains base measures, derived measures, and indicators, and how to link them to information needs. See [KPIs and KRIs](../04-isms/kpis-and-kris.md) and [Metrics and Management Review](../04-isms/metrics-and-management-review.md).
- **ISO/IEC 27007** guides the audit of an ISMS: programme management, competence of auditors, and conduct of the audit. It complements the generic auditing guidance of ISO 19011. See [Internal Audit](../08-auditing/internal-audit.md).
- **ISO/IEC TS 27008** guides the technical assessment of individual controls (how well a control is implemented), which is narrower than an ISMS audit.
- **ISO/IEC 27014** addresses the governance of information security: how a governing body sets direction and holds management accountable, distinct from day-to-day operation. See [Governance Model](../02-grc/governance-model.md).

## Domain-specific control standards

When scope includes networks, applications, storage, or wider cybersecurity concerns, these guidance standards add depth:

- **ISO/IEC 27033** (network security) supports [Network Security](../07-security-domains/network-security.md).
- **ISO/IEC 27034** (application security) supports [Application Security](../07-security-domains/application-security.md).
- **ISO/IEC 27040** (storage security) supports decisions on encryption at rest, secure deletion, and storage resilience.
- **ISO/IEC 27032** provides guidance on internet and cyber security concepts that cross organizational boundaries.

## Risk and privacy vocabulary standards

- **ISO 31000** provides general risk-management principles and guidance. ISO/IEC 27005 aligns its information-security risk guidance with that broader approach, so the two are commonly read together. See [Risk Methodology](../05-risk-management/risk-methodology.md).
- **ISO/IEC 29100** defines a privacy framework and terminology (including the concept of PII) that underpins ISO/IEC 27701 and 27018.
- **ISO/IEC 42001** specifies a certifiable AI management system. Organizations combining information security and AI governance often integrate it with ISO/IEC 27001. See [AI Governance and Security](../38-ai-governance-and-security/index.md).

## Common mistake

A common mistake is treating ISO/IEC 27001 as a technical checklist. The correct approach is to treat ISO/IEC 27001 as the management-system backbone and use related standards for implementation detail where useful.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** ISO/IEC 27001 specifies certifiable ISMS requirements, while ISO/IEC 27701:2025 specifies certifiable standalone PIMS requirements. Other family members listed here provide overview, control, risk, cloud, incident, continuity, supplier, and evidence guidance. A guidance standard does not become mandatory merely because it belongs to the family, although law, regulation, contract, policy, or risk treatment can make particular commitments binding.
- **Implementation guidance:** Identify which family members are relevant to the organisation's scope, risk treatment, and contractual commitments. Map each standard to the ISMS element it supports.
- **Best practice:** Use the family as a reference library — pull what is useful, but do not treat every standard as mandatory. The ISMS backbone is ISO/IEC 27001 clauses 4-10; the rest is implementation detail.

## Practical example

An ISMS manager mapping the organization's documentation landscape identifies which standards provide management-system requirements (ISO/IEC 27001 and ISO/IEC 27701:2025), which provide implementation guidance, and which provide activity-specific detail. The manager records exact editions and whether each source is required, contractually adopted, or used only as guidance.

## Edition watch

- [ISO/IEC 27018:2025](https://www.iso.org/standard/27018) replaced ISO/IEC 27018:2019.
- [ISO/IEC 27031:2025](https://www.iso.org/standard/27031?browse=ics) replaced ISO/IEC 27031:2011.
- The second edition of [ISO/IEC 27017](https://www.iso.org/standard/82878.html) remained under publication at stage 60.00 on 20 July 2026; ISO/IEC 27017:2015 remains current until the replacement is published.
- [ISO/IEC 27037:2012](https://www.iso.org/standard/44381.html) remained published but under revision review on 16 July 2026.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- clause or control mapping
- approved management-system document
- operating records from the scoped process
- internal-audit or management-review result

## Sources

- [ISO/IEC JTC 1/SC 27 catalogue](https://www.iso.org/committee/45306/x/catalogue/)
- [ISO/IEC 27000:2026](https://www.iso.org/standard/27000)
- [ISO/IEC TS 27008:2019](https://www.iso.org/standard/67397.html)
- [ISO/IEC 27014:2020](https://www.iso.org/standard/74046.html)


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
