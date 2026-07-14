---
title: Content Depth Quality Standard
description: Editorial standard to avoid keyword-only documentation and require examples, explanations, best practices, and cross-links.
category: Reference
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - editorial-quality
  - content-depth
---

# Content Depth Quality Standard

This standard addresses a quality problem identified during review: many documentation pages used lists and keywords but lacked enough explanation, examples, and best-practice guidance.

## Required page structure for substantive chapters

Every substantive page should include:

1. **Purpose** — why the topic exists.
2. **Plain-language explanation** — what it means in practice.
3. **ISO/ISMS relevance** — how it supports the management system.
4. **Example** — realistic scenario or implementation pattern.
5. **Best practices** — practical guidance from experience.
6. **Typical evidence** — what proves it operates.
7. **Common mistakes** — what usually goes wrong.
8. **Related documents** — links to avoid duplicating content.

## Example quality test

A weak page says:

> Access reviews: review access quarterly, remove unused users, keep evidence.

A stronger page explains:

> Access reviews confirm that users and accounts still have a legitimate business need for their access. The review should start from a complete population exported from the authoritative identity or application source. The data owner should verify whether each account is still needed, whether privilege is appropriate, and whether service accounts still have an owner. Removal decisions should become tracked tickets, and the review is not complete until remediation is verified.

## Project-wide writing rule

Use lists for clarity, but do not let lists replace explanation. Each important list should be introduced with context and followed by implementation guidance or an example.

## Cross-link rule

If a page touches a topic covered elsewhere, link to the detailed chapter rather than rewriting it. Use the [Related Document Map](related-document-map.md) as the central cross-reference guide.

## Readability improvement priorities

Repository reviews should prioritize pages where tables, headings, or checkboxes carry most of the meaning. Improve them in this order:

1. **Landing and mapping pages:** explain who should use the section, what question it answers, and how its pages relate.
2. **Examples:** explain the reasoning behind populated values, assumptions, and the next decision—not only the completed fields.
3. **Reference tables:** introduce what the table is for and explain how to interpret or apply it after the table.
4. **Checklists:** state the trigger, accountable role, completion evidence, and what happens when an item fails.
5. **Templates:** describe when to use the record, how detailed entries should be, and which fields require controlled values or approval.

Do not add prose merely to increase page length. Useful explanation resolves ambiguity, connects an activity to risk or business outcomes, distinguishes similar concepts, provides decision criteria, or shows what adequate implementation and evidence look like.

## Reader-comprehension test

A reader unfamiliar with the page should be able to answer four questions after one pass:

- Why does this matter?
- What must be decided or done?
- Who is accountable, and when does the activity occur?
- What result or evidence shows that it worked?

If the page cannot answer these questions, add a short explanation or worked example before adding more list items.
