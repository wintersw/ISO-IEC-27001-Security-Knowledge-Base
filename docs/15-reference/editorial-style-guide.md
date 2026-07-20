---
title: Editorial Style Guide
description: Plain-language, copyright-aware, vendor-neutral writing rules for the knowledge base.
category: Reference
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - reference
---

# Editorial Style Guide

## Voice

Use plain English. Explain concepts before terminology. Be precise without sounding academic.

Use American English for project prose (`organization`, `program`, `analyze`) while preserving official titles, names, and quotations. Prefer inclusive, role-based language and short sentences. Follow [Accessibility and Inclusive Documentation](accessibility-and-inclusive-documentation.md).

## Distinguish

- ISO perspective
- legal or contractual obligation
- organization-specific requirement
- implementation guidance
- best practice

## Avoid

- copying official standard text
- vendor lock-in
- unsupported claims
- long pages without examples or checklists
- unsupported superlatives and universal claims such as “always,” “never,” or “most common” unless an authoritative source and scope support them
- unexplained version-sensitive, legal, cryptographic, quantitative, or protocol claims

## Sources and review dates

- Link directly to primary sources: the issuing standards body, regulator, specification publisher, or project documentation.
- Add a `## Sources` section for mappings and for claims whose correctness depends on an edition, protocol, law, algorithm transition, or current project release.
- Add `reviewed_on: YYYY-MM-DD` to edition-sensitive pages and recheck them after a material source change.
- State the exact edition or release where it changes scope or meaning. Do not imply that a mapping proves equivalence or conformity.
- Use secondary sources for explanation only when a primary source is unavailable or insufficient, and label interpretation clearly.

## Accessible structure

Use one descriptive H1, nested headings without skipped levels, meaningful link text, table headers, and text alternatives for diagrams. Do not rely on color alone. Explain specialist terms on first use and give procedures in numbered steps.

## Terminology and definitions

- Follow the [Terminology Governance](terminology-governance.md) source hierarchy.
- Record the standard edition when terminology is version-sensitive.
- Treat licensed standards as validation sources, not reusable text.
- Write original plain-language explanations and link readers to authorized sources when exact wording matters.
- Do not place ISO/IEC PDFs or extracted definition catalogs in the repository.
- Revalidate affected terminology when a referenced standard is amended, withdrawn, or replaced.

## Abbreviations

Write the full term before an abbreviation on first use when practical. Add each abbreviation and its full written form to the [Abbreviations](abbreviations.md) reference so readers can check terminology from any article. Treat record prefixes and priority labels as codes and document their meaning separately.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](abbreviations.md).
