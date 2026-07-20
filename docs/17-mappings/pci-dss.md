---
title: ISO 27001 and PCI DSS
description: How ISO/IEC 27001 relates to the Payment Card Industry Data Security Standard.
category: Mappings
difficulty: Intermediate
reviewed_on: 2026-07-20
applies_to:
  - ISO/IEC 27001:2022
  - PCI DSS 4.0.1
tags:
  - mapping
---

# ISO 27001 and PCI DSS

PCI DSS 4.0.1 is the current Payment Card Industry Data Security Standard for entities that store, process, or transmit account data, or can affect the security of the cardholder data environment. ISO/IEC 27001 is a risk-based management-system standard. PCI obligations arise through payment-program and contractual arrangements; an ISMS can govern them but does not replace PCI validation.

## Practical relationship

| PCI DSS requirement area | ISO/IEC 27001 relationship | Example evidence |
|---|---|---|
| 1 — Install and maintain network security controls | A.8.20–A.8.22 | network rules, segmentation design and tests |
| 2 — Apply secure configurations | A.8.9 | approved baselines, configuration monitoring |
| 3–4 — Protect stored account data and transmission with strong cryptography | A.8.24, A.5.14 | data flows, key management, protocol configuration |
| 5–6 — Protect systems from malicious software; develop and maintain secure systems | A.8.7, A.8.8, A.8.25–A.8.29 | anti-malware, patching, software lifecycle and tests |
| 7–9 — Restrict logical and physical access | A.5.15–A.5.18, A.7.1–A.7.4, A.8.2–A.8.5 | access reviews, authentication, physical access records |
| 10–11 — Log, monitor, and regularly test security | A.8.15, A.8.16, A.8.8, A.8.29 | log coverage, alert tests, scans and penetration tests |
| 12 — Support security with organizational policies and programs | Clauses 4–10 and organizational controls | governance, risk, awareness, incident and supplier records |

## Key differences

- **Scope:** PCI DSS scope is defined by the cardholder data environment (CDE); ISMS scope is defined by the organization. The CDE is usually a subset of the ISMS.
- **Prescription:** PCI DSS specifies parameter values (for example, password and log-retention rules); ISO/IEC 27001 requires risk-based decisions and evidence.
- **Assurance:** PCI validation may use a Report on Compliance or an applicable Self-Assessment Questionnaire under payment-program rules; ISO/IEC 27001 uses management-system certification audit. The applicable validation method must be confirmed with the acquiring bank or payment brand.

## Best practice

Run PCI DSS as a scoped, prescriptive obligation inside the ISMS: record it in the [Statement of Applicability](../05-risk-management/statement-of-applicability.md), reuse ISMS evidence where the population and period match, and keep PCI-specific parameters in the relevant procedure. Do not assume ISO certification demonstrates PCI compliance or vice versa.

## Sources

- [PCI Security Standards Council](https://www.pcisecuritystandards.org/)
- [PCI DSS document library](https://www.pcisecuritystandards.org/document_library/)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
