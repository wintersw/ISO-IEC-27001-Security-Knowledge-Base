---
title: EU Cybersecurity Regulatory Landscape
description: Applicability-oriented overview of GDPR, NIS2, DORA, and the Cyber Resilience Act alongside ISO/IEC 27001.
category: Mappings
difficulty: Intermediate
reviewed_on: 2026-07-20
applies_to:
  - ISO/IEC 27001:2022
  - GDPR
  - NIS2 Directive
  - DORA
  - Cyber Resilience Act
tags:
  - mapping
  - regulation
  - european-union
---

# EU Cybersecurity Regulatory Landscape

European Union instruments can apply because of an organization's activities, sector, size, location, customers, data, or products. ISO/IEC 27001 can organize governance, risk, controls, evidence, audit, and improvement, but certification does not by itself demonstrate legal compliance.

This page is orientation, not legal advice. Determine scope with qualified legal and regulatory owners, including national implementing law and supervisory guidance.

## Applicability map

| Instrument | Primary focus | Typical applicability question | ISMS integration |
|---|---|---|---|
| General Data Protection Regulation (GDPR) | personal-data processing and individual rights | Are personal data processed in an activity within territorial and material scope? | privacy risks, processor governance, security of processing, incidents, records, and rights workflows |
| NIS2 Directive | cybersecurity risk management and incident reporting for covered entities | Does national law classify the entity as essential or important, including supply-chain and jurisdiction rules? | leadership accountability, risk measures, supply chain, continuity, vulnerability handling, reporting |
| Digital Operational Resilience Act (DORA) | information and communication technology risk in the financial sector | Is the entity a covered financial entity or critical ICT third-party provider? | ICT risk framework, incident reporting, resilience testing, third-party risk, registers |
| Cyber Resilience Act (CRA) | products with digital elements placed on the EU market | Is the organization a manufacturer, importer, distributor, or open-source software steward in scope? | secure product lifecycle, vulnerability handling, conformity evidence, reporting, updates |

## Implementation method

1. Maintain an obligations register with instrument, article or national provision, entity/product/service scope, regulator, owner, deadline, and evidence.
2. Separate direct legal duties from contractual flow-down and voluntary guidance.
3. Map each obligation to implemented organizational controls and accountable processes—not merely to Annex A labels.
4. Reconcile incident definitions, materiality thresholds, recipients, and reporting clocks in one tested escalation matrix.
5. Track transition dates, delegated acts, national implementation, supervisory guidance, and product lifecycle milestones.
6. Record gaps and legal interpretations with owners and review dates.

## Practical example

A financial software provider finds that GDPR applies to its processing, DORA obligations flow down from regulated customers, NIS2 depends on national classification, and the CRA applies to a commercial product. One ISMS supplies access, supplier, incident, and development evidence, while separate registers retain each law's scope and specific duties.

## Common mistakes

- assuming an ISO/IEC 27001 certificate creates a compliance presumption for every instrument
- applying directive text without checking national implementing law
- combining distinct incident definitions and deadlines into one generic “72-hour” rule
- overlooking product, importer, distributor, open-source, or third-party-provider roles

## Sources

- [GDPR — Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [NIS2 — Directive (EU) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)
- [DORA — Regulation (EU) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)
- [Cyber Resilience Act — Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj)

## Related chapters

- [ISO 27001 and GDPR](gdpr.md)
- [Legal, Statutory, Regulatory, and Contractual Requirements](../06-annex-a/organizational/a5-31-legal-statutory-regulatory-and-contractual-requirements.md)
- [Software Supply Chain Security](../34-secure-by-design/software-supply-chain-security.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
