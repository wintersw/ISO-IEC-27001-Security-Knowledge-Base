---
title: Accessibility and Inclusive Documentation
description: Practical rules for making security guidance understandable and usable by people with different abilities and experience levels.
category: Reference
difficulty: Beginner
reviewed_on: 2026-07-20
applies_to:
  - WCAG 2.2
  - ISO/IEC 27001:2022
tags:
  - reference
  - accessibility
  - plain-language
---

# Accessibility and Inclusive Documentation

Accessible documentation helps people perceive, navigate, understand, and apply security guidance. It is also a safety measure: an instruction that cannot be understood or operated reliably can create control failure.

## Authoring standard

- Explain the purpose before the detail and define specialist terms on first use.
- Use descriptive headings in a logical hierarchy and meaningful link text instead of “click here.”
- Give images useful alternative text. Mark decorative images as decorative.
- Introduce tables in prose, use header cells, and avoid using a table only for visual layout.
- Provide a text explanation of every Mermaid diagram's important relationships and sequence.
- Never communicate state or severity through color alone.
- Use numbered steps for ordered procedures and bullets for unordered choices.
- Expand abbreviations on first use and link to the [Abbreviations](abbreviations.md) reference.
- Prefer short sentences, concrete verbs, and role names over gendered or culture-specific language.

## Site and review checks

Test keyboard navigation, visible focus, zoom and reflow, color contrast, headings, landmarks, accessible names, and screen-reader output. Automated checks find only part of the problem; include manual keyboard and assistive-technology review for important workflows.

Security must not be used as a default reason to block accessibility features. Assess the risk and provide an equally effective accessible path—for example, an accessible authentication option that does not depend on a puzzle or a particular physical ability.

## Practical example

An incident runbook supplements a response flowchart with numbered actions, identifies each responsible role in text, defines acronyms on first use, and is tested at 200% zoom and with keyboard navigation before an exercise.

## Common mistakes

- adding alternative text that repeats the filename but not the image's meaning
- relying only on automated scores or color contrast checks
- placing essential instructions only inside diagrams, screenshots, or video
- using unexplained acronyms because the intended audience is assumed to be expert

## Sources

- [W3C Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/)
- [W3C Writing for Web Accessibility](https://www.w3.org/WAI/tips/writing/)
- [PlainLanguage.gov guidelines](https://www.plainlanguage.gov/guidelines/)

## Related chapters

- [Editorial Style Guide](editorial-style-guide.md)
- [How to Use This Knowledge Base](../00-getting-started/how-to-use.md)
- [Terminology Governance](terminology-governance.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](abbreviations.md).
