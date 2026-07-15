---
title: ISO/IEC 27002:2013 to 2022 Transition Guide
description: A copyright-safe method for migrating legacy control references, policies, contracts, and evidence to the 2022 structure.
category: ISO 27000 Family
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
  - ISO/IEC 27002:2022
tags:
  - iso27000-family
  - transition
  - legacy-mapping
---

# ISO/IEC 27002:2013 to 2022 Transition Guide

ISO/IEC 27002:2013 is withdrawn and was revised by ISO/IEC 27002:2022. Legacy policies, contracts, audit reports, risk treatments, control libraries, and customer questionnaires may still cite the 2013 structure. Treat those references as migration inputs, not as current control requirements.

This guide does not reproduce either standard's control text or provide a normative crosswalk. Use authorized copies of the applicable standards and approved mapping sources when exact correspondence matters.

## Why direct renumbering fails

A mechanical identifier replacement can hide important changes. During the revision, control organization, grouping, naming, scope, and implementation context changed. One legacy reference may correspond to several current controls; several legacy references may converge on one current control; and some 2022 topics have no simple predecessor.

Migration must preserve the intended security outcome and evidence, not merely the old number.

## Transition workflow

1. Inventory every legacy citation in policies, procedures, contracts, risk records, SoA versions, audit workpapers, control tools, metrics, training, and supplier questionnaires.
2. Record the business or security outcome that the legacy reference was intended to support.
3. Consult authorized editions and determine whether the relationship is one-to-one, one-to-many, many-to-one, changed in scope, newly introduced, or no longer relevant.
4. Reassess applicability against current scope, risk treatment, legal, regulatory, contractual, and interested-party requirements.
5. Update control design, ownership, evidence, measures, procedures, and test steps where the current outcome differs.
6. Update the SoA and linked risk-treatment records before changing downstream labels.
7. Retain an approved transition record so historical evidence remains interpretable.
8. Obtain confirmation from contract owners or customers before changing externally agreed control references.

## Legacy reference register

| Legacy reference | Source document / system | Intended outcome | Current reference(s) | Relationship | Design or evidence change | Owner | Approval / completion |
|---|---|---|---|---|---|---|---|
| [2013 identifier] |  |  | [2022 identifier(s)] | 1:1 / 1:many / many:1 / changed / none |  |  |  |

## Migration decisions

| Situation | Required treatment |
|---|---|
| Internal document cites 2013 only | Update the citation and verify the surrounding procedure still produces the current intended outcome. |
| Contract fixes a 2013 control reference | Preserve the contractual interpretation, map it to current operation, and obtain legal or commercial approval before changing the contract. |
| Audit evidence uses old identifiers | Retain the historical identifier and add the current relationship; never relabel old evidence as though it was created under the new criteria. |
| Current control has no simple predecessor | Perform fresh applicability, design, ownership, and evidence decisions. |
| One old control maps to several current topics | Assign and test each relevant current outcome; do not close the migration because one branch was implemented. |
| Legacy control is no longer relevant | Record the scope, risk, requirement, and approval basis rather than silently deleting it. |

## Completion criteria

- all legacy references have an owner and disposition;
- the current SoA is the authoritative applicability record;
- risks, controls, procedures, evidence, metrics, and tests use consistent current references;
- external obligations and historical evidence remain traceable;
- new or changed topics received fresh risk-based review; and
- the mapping source, edition, reviewer, approval, and date are retained.

## Common mistakes

- treating a public crosswalk as a substitute for reading the applicable standards;
- changing identifiers without reviewing control design and evidence;
- deleting legacy references needed to interpret historical audits or contracts;
- assuming that “not present in 2013” means “not applicable now”;
- publishing copied control wording inside the transition register; and
- mixing 2013 and 2022 identifiers without edition labels.

## Related pages

- [ISO/IEC 27002 Control Guidance](iso27002-control-guidance.md)
- [Statement of Applicability](../05-risk-management/statement-of-applicability.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Control Guidance Adaptation Checklist](../11-checklists/control-guidance-adaptation-checklist.md)
- [Terminology Governance](../15-reference/terminology-governance.md)
