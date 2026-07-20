---
title: Terminology Governance
description: Copyright-safe source hierarchy and maintenance process for consistent ISMS terminology.
category: Reference
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - reference
---

# Terminology Governance

This project uses authoritative standards to validate terminology, but writes explanations in original plain language. Licensed ISO/IEC publications are reference authorities; they are not content repositories from which definitions, notes, examples, tables, or diagrams may be copied into this public knowledge base.

## Source hierarchy

When terms conflict or change, use this order:

1. the current standard that governs the specific subject or requirement;
2. a current referenced vocabulary or terminology source identified by that standard;
3. applicable law, regulation, or contract for terms used in that legal or contractual context;
4. an approved organization-specific definition for local methods, roles, ratings, and records;
5. this project's glossary as a plain-language reader aid.

Specific standards take precedence within their scope. Do not force one definition onto privacy, resilience, risk, audit, or legal contexts when the governing source defines the term differently.

## ISO/IEC 27000 edition handling

ISO/IEC 27000:2018 was the fifth-edition *Overview and vocabulary*. It was withdrawn and replaced by ISO/IEC 27000:2026, published on 3 July 2026. The sixth edition is an ISMS overview rather than primarily a vocabulary document. A licensed 2018 copy may still be used to:

- interpret terminology used by documents written against the 2018 edition;
- trace why older project wording or mappings used a particular distinction;
- compare terminology during an edition transition; and
- identify terms that require validation against current applicable sources.

It must not be labeled the current single source of truth. Before approving new or revised terminology, check the current ISO catalog entry, the current applicable standard, and any referenced terminology source. Record the edition used.

## Copyright-safe workflow

1. Identify the term, its context, and the decision that depends on it.
2. Consult an authorized copy of the applicable source and record its identifier, edition, clause or term number, and access date in private review notes.
3. Compare related terms and preserve distinctions that affect requirements or implementation.
4. Write a fresh plain-language explanation without copying the formal definition, notes, examples, tables, or diagrams.
5. Add a source pointer by standard identifier and edition; do not attach or redistribute the licensed publication.
6. Review the wording for semantic accuracy, copyright safety, and consistency with project usage.
7. Trigger revalidation when a source is revised, amended, corrected, withdrawn, or replaced.

Short standard titles, identifiers, clause references, and term numbers may be used for traceability. Avoid presenting a close paraphrase as though it were the normative definition. When exact wording matters, direct the reader to the authorized source.

## Terminology decision record

| Field | Record |
|---|---|
| Term and context |  |
| Decision owner |  |
| Governing source and edition |  |
| Clause / term reference |  |
| Other sources compared |  |
| Project explanation |  |
| Distinctions and usage rules |  |
| Copyright review |  |
| Approved date and next review trigger |  |

## Writing and naming rules

- Use the official standard identifier and edition when version matters.
- Preserve established distinctions such as requirement versus guidance, risk assessment versus risk analysis, and correction versus corrective action.
- Define organization-specific rating labels and workflow statuses locally rather than implying that ISO prescribed them.
- Expand abbreviations on first use where practical and maintain the abbreviation register.
- If a word has a legal, contractual, or sector-specific meaning, state that context explicitly.
- If the project explanation intentionally simplifies a concept, say so and link to the authoritative source.

## Evidence to retain

- terminology decision records;
- authorized-source access and edition information;
- reviewer and approval history;
- affected-page list;
- edition-change impact assessments; and
- evidence that copied normative wording was not published.

## Related pages

- [Glossary](glossary.md)
- [Abbreviations](abbreviations.md)
- [Editorial Style Guide](editorial-style-guide.md)
- [References](references.md)
- [ISO/IEC 27000 Family Detailed Guide](../03-iso27001/iso27000-family-detailed.md)
