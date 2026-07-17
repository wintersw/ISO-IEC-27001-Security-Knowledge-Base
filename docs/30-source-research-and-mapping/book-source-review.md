---
title: Publication Resource Review
description: Review of publications previously provided as project resources, including adopted themes, exclusions, and project destinations.
category: Source Research and Mapping
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - source-mapping
  - editorial-assurance
---

# Publication Resource Review

## Overview

The following eight publications are included in the project's research resources. They were reviewed to identify useful concepts that were absent or too shallow in the knowledge base, and the resulting adoption decisions are recorded in this register. The publications inform original, independently maintained guidance; the project does not reproduce their prose, diagrams, tables, examples, standard definitions, or technical procedures.

## Purpose

This record makes adoption and rejection decisions visible. It helps maintainers distinguish “a source was reviewed” from “all of its content is current, authoritative, or suitable,” and prevents the same material from being repeatedly rediscovered or copied into multiple chapters.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** ISO/IEC 27001 does not require this particular source review. Applicable requirements must be determined from authorized editions of standards and binding legal, regulatory, contractual, and organizational sources.
- **Implementation guidance:** Use secondary sources to discover questions, examples, and implementation patterns; validate formal claims against authoritative sources before presenting them as requirements.
- **Best practice:** Record source age, authority, limitations, adopted themes, project destination, and reasons for exclusion. Prefer a link to a maintained destination page over repeating the theme here.

## Key concepts

- **Adopted:** the source exposed a useful gap and original guidance was added.
- **Already covered:** the theme was checked but did not justify more content.
- **Excluded:** the material was outdated, unreliable, overly product-specific, unsafe to reproduce, or less useful than existing guidance.
- **Source age:** older management ideas may remain useful, while legal, technical, threat, and standard-specific claims can expire quickly.

## Publication-by-publication assessment

| No. | Source reviewed | Decision | Useful themes and destination | Limitations applied |
|---:|---|---|---|---|
| 1 | *Enterprise-Grade IT Security for Small and Medium Businesses* (Denny Cherry, 2022) | Adopted selectively | Risk-based minimum viable security and explicit denial-of-service resilience were added to the [SME and Startup Implementation Guide](../16-implementation-guides/sme-startup-guide.md) and [Network Security](../07-security-domains/network-security.md). | Product and platform examples were not carried over; segmentation, firewalls, remote access, endpoints, multifactor authentication, zero trust, and awareness were already covered. |
| 2 | *Hacklog Volume 2: Web Hacking* (Stefano Novelli and Marco Silvestri, 2018) | Adopted as defensive objectives only | External exposure, authentication, session handling, authorization, input and file processing, logging, test authorization, and retesting strengthened [Application Security](../07-security-domains/application-security.md) and [A.8.29 Security testing](../06-annex-a/technological/a8-29-security-testing-in-development-and-acceptance.md). | Offensive procedures, payloads, commands, tool walkthroughs, and obsolete implementation details were excluded. |
| 3 | *Implementing the ISO/IEC 27001 ISMS Standard* (Edward Humphreys, second edition, 2016) | Adopted conceptually | Control dependencies, continuity of the ISMS itself, and decision-led measurement strengthened the [ISMS Operating Model](../04-isms/isms-operating-model.md) and [Metrics and Management Review](../04-isms/metrics-and-management-review.md). | It discusses an earlier ISO/IEC 27001 edition; it was not used as authority for 2022 requirements or Annex A structure. |
| 4 | *ISO/IEC 27000:2018 — Overview and vocabulary* | Adopted through paraphrased distinctions; legacy reference | The [Glossary](../15-reference/glossary.md) distinguishes related management-system, measurement, risk, and incident terms in original plain language, while [Terminology Governance](../15-reference/terminology-governance.md) controls edition-aware use. | Formal definitions were not copied. The 2018 edition was withdrawn and replaced by ISO/IEC 27000:2026, published on 3 July 2026. The sixth edition is an ISMS overview rather than primarily a vocabulary document; validate current terminology against applicable sources. |
| 5 | *ISO 27001:2022 Information Security Management System Guide* (Bruce Brown, 2024) | Limited adoption | Planning ISMS changes and executable communications strengthened [Clause 6](../03-iso27001/clause-6-planning.md) and [Clause 7](../03-iso27001/clause-7-support.md). | Most content restated material already present. It was treated as secondary commentary, not authority for ISO requirements. |
| 6 | *IT Security Governance Guidebook* (Fred Cohen, 2007) | Adopted selectively | Decision challenge and appeal, governance-forum mechanics, and whole-life security cost strengthened the [Security Governance Model](../02-grc/governance-model.md) and [Economic Use of Security Resources](../20-bsi-isms-enhancement/resource-economics.md). | Dated organization structures, technical architecture, and quantitative claims were not adopted. |
| 7 | *IT Security Management 100 Success Secrets* (Lance Batten, 2012) | Excluded | No unique destination. Its broad themes were already covered more accurately. | Repetitive promotional-style entries, obsolete standards and market references, and weak sourcing made it unsuitable for new guidance. |
| 8 | *IT Security Project Management Handbook* (Susan Snedaker, 2006) | Adopted as lifecycle guidance | Outcome framing, separate project and security risks, acceptance criteria, traceability, controlled change, operational transfer, closure, and benefit review produced the [Security Project Delivery Guide](../16-implementation-guides/security-project-delivery-guide.md) and strengthened A.5.8 and the certification plan. | Dated technology, product, United States legal, cost, and threat content was excluded. |

## Practical implementation

For each future publication provided as a project resource, record its bibliographic identity, publication date, themes, authority level, version-sensitive claims, candidate gaps, existing destinations, adoption decision, and verification status. Add content to the smallest number of durable destination pages, then link back to this register.

## Practical example

A source contains a long chapter about a particular web-testing tool. The reviewer does not reproduce its commands or create a product chapter. Instead, the reviewer extracts the durable defensive question—whether test scope covers authentication, authorization, sessions, inputs, uploads, and logging—checks current project coverage, adds original vendor-neutral acceptance guidance, and records the source limitation here.

## Evidence to retain

- source inventory and bibliographic metadata;
- extraction or review log kept outside published content where licensing requires it;
- theme-to-destination gap notes;
- authoritative verification for formal requirements;
- editorial review showing original wording and safe level of detail;
- changed-file list, link check, and successful site build; and
- explicit rejection rationale for sources or themes not adopted.

## Common mistakes

- treating every publication as equally authoritative;
- importing an older standard structure into current requirements;
- copying definitions, examples, tables, screenshots, or step-by-step procedures;
- adopting dated product, legal, cost, or threat claims without verification;
- adding a new chapter when an existing page is the natural destination;
- equating a source's table of contents with a project gap; and
- failing to record why a reviewed source produced no changes.

## Auditor questions

- How were formal requirements separated from secondary guidance?
- Which source themes were rejected, and why?
- How was copyrighted wording avoided?
- Can each adopted theme be traced to an original destination and evidence of review?
- How are version-sensitive statements identified for future revalidation?

## Checklist

- [ ] Source identity, date, authority, and version recorded
- [ ] Source reviewed chapter by chapter or theme by theme
- [ ] Existing project coverage checked before adding content
- [ ] Formal claims verified against authoritative material
- [ ] Adopted guidance is original, vendor-neutral, and safely scoped
- [ ] Outdated, duplicative, product-specific, or unreliable material excluded
- [ ] Destination pages, examples, evidence, and related links updated
- [ ] Abbreviations expanded and registered where introduced
- [ ] Copyright, links, and strict site build checked

## Related controls, clauses, templates, and checklists

- [Research and Topic Mapping](index.md)
- [Topic and Reference Inventory](source-inventory.md)
- [Source Theme Register](source-theme-register.md)
- [Source-to-Project Map](source-to-project-map.md)
- [PDF Source Integration Review Checklist](../11-checklists/pdf-source-integration-review-checklist.md)
- [Editorial Style Guide](../15-reference/editorial-style-guide.md)
- [Abbreviations](../15-reference/abbreviations.md)
