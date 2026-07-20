---
title: ISO 27001 and GDPR
description: How ISO 27001 supports but does not replace GDPR compliance.
category: Mappings
difficulty: Intermediate
reviewed_on: 2026-07-20
applies_to:
  - ISO/IEC 27001:2022
  - GDPR
tags:
  - mapping
---

# ISO 27001 and GDPR
ISO/IEC 27001 can support GDPR compliance by providing security governance, risk management, access control, supplier management, incident response, and evidence discipline.

## Important distinction

ISO 27001 certification does not automatically mean GDPR compliance. GDPR includes legal requirements such as lawful basis, data subject rights, transparency, controller/processor obligations, and breach notification.

## Useful overlaps

- security of processing
- access control
- encryption
- supplier security
- incident response
- records and evidence
- risk assessment
- privacy and personally identifiable information (PII) protection

## Illustrative relationship table

| GDPR obligation area | ISO/IEC 27001 support | Important gap to manage separately |
|---|---|---|
| Principles and accountability | Clauses 4–10 and A.5.31 support governance and evidence | lawful basis, fairness, transparency, purpose limitation, and data-subject rights |
| Data protection by design and default | A.5.34 and secure-development controls support engineering discipline | the controller's Article 25 legal assessment and defaults |
| Processor management | A.5.19–A.5.23 support supplier lifecycle controls | Article 28 contract content and controller/processor allocation |
| Security of processing | risk treatment plus relevant organizational and technical controls | Article 32 proportionality and the specific processing context |
| Personal-data breach response | A.5.24–A.5.28 support detection, decisions, and evidence | legal notification thresholds, content, and deadlines under Articles 33 and 34 |
| Data protection impact assessment | Clause 6 risk methods can provide inputs | the Article 35 trigger, privacy impacts, consultation, and required content |

Use the [official consolidated GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj) and qualified legal/privacy advice for legal conclusions.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).


## Practical example

A cloud-service supplier assessment can support both A.5.19 and processor due diligence. The GDPR review must still verify the processing agreement, subprocessor terms, transfer mechanism, assistance duties, and deletion arrangements rather than treating the ISO evidence as a complete Article 28 assessment.

## Sources

- [GDPR — Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
