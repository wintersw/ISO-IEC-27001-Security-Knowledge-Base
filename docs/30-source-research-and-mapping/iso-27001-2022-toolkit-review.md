---
title: ISO 27001:2022 Toolkit Source Review
description: Adoption, correction, attribution, and exclusion decisions for the MIT-licensed PehanIn toolkit.
category: Source Research and Mapping
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - source-mapping
  - open-source
  - attribution
---

# ISO 27001:2022 Toolkit Source Review

## Source and license

The local source reviewed was [PehanIn/ISO-27001-2022-Toolkit](https://github.com/PehanIn/ISO-27001-2022-Toolkit), copyright (c) 2024 Pehan Gunasekara, licensed under the MIT License. The complete retained notice is in `THIRD_PARTY_NOTICES.md` at the repository root.

The review covered its gap assessment, Statement of Applicability, risk register, context and scope, asset inventory, business continuity and disaster recovery, policy, awareness, management review, checklists, internal audit, and return-on-investment files.

## Adoption decisions

| Source area | Decision | Destination and adaptation |
|---|---|---|
| Scope and context | Adopted and expanded | [Clause 4](../03-iso27001/clause-4-context.md) and the [scope statement template](../10-templates/isms-scope-statement-template.md) now cover processes, locations, technology, exclusions, interfaces, context, and maintenance. |
| Asset inventory and classification | Adopted selectively | The [asset inventory template](../10-templates/asset-inventory-template.md) adds lifecycle, required controls, retention, and a policy-driven handling profile. Example assets were not copied. |
| Internal audit plan | Adopted and strengthened | The [internal audit plan](../10-templates/internal-audit-plan-template.md) adds timetable, roles, independence, evidence, reporting, and effectiveness follow-up. |
| Awareness plan | Adopted and strengthened | The [training and awareness plan](../10-templates/training-awareness-plan-template.md) adds delivery scheduling, feedback, knowledge checks, and behavior-based effectiveness. |
| Management-review measurement | Adopted selectively | The [management review template](../10-templates/management-review-template.md) adds traceable measures, thresholds, observations, decisions, owners, and review dates. |
| Return on investment | Corrected and reframed | The new [ISMS investment case](../10-templates/isms-investment-case-template.md) corrects the ROI formula, separates costs from uncertain benefits, adds scenarios, and states that this document is optional. |
| Risk register, SoA, continuity, disaster recovery, policy, and checklists | Already covered or excluded | Existing project templates were more complete. Useful generic themes were already present, so importing them would add duplication. |

## Corrections and exclusions

The source is useful as an implementation starter but is not treated as normative authority. Several checklist mappings use obsolete or incorrect control identifiers, the gap questionnaire samples only a small part of the clauses and Annex A, the ROI formula is displayed incorrectly, and the documentation checklist labels optional artifacts as mandatory. Those details were not imported. Any control or clause mapping must be checked against an authorized edition of ISO/IEC 27001:2022 and the organization's applicable obligations.

Source tables and document structures that materially influenced a destination carry a local “based on” notice. Global copyright and MIT License terms are retained in `THIRD_PARTY_NOTICES.md`.

## Related pages

- [Research and Topic Mapping](index.md)
- [Book Source Review](book-source-review.md)
- [Editorial Style Guide](../15-reference/editorial-style-guide.md)
- [Template Catalog](../10-templates/index.md)
