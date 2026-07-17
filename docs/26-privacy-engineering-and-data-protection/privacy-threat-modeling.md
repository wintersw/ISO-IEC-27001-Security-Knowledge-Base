---
title: Privacy Threat Modeling
description: Threat modeling methods for personal data and data subject harms.
category: Privacy Engineering and Data Protection
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - privacy
  - threat-modeling
---

# Privacy Threat Modeling

Privacy threat modeling identifies how data processing can harm people, not only how attackers can compromise systems.

## Threat categories

- excessive collection
- unexpected secondary use
- unauthorized disclosure
- re-identification
- inference of sensitive attributes
- inaccurate data affecting decisions
- exclusion or discrimination
- retention beyond need
- lack of transparency
- weak consent or choice
- surveillance creep

## Practical model

For each processing activity, ask:

- who is the data subject?
- what data is collected?
- what can be inferred?
- who receives the data?
- how could the data be misused?
- what would harm look like?
- which controls reduce harm?
- how will controls be tested?

## Typical evidence

- privacy threat model per processing activity covering harm scenarios
- documented inference and secondary-use threats, not only breach threats
- identified harms mapped to mitigating controls
- review records for changes that alter data collection or sharing
- test plans showing harm-reducing controls are verified

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

A fitness app plans to share "activity heatmaps". Security threat modeling finds no attacker path, but privacy threat modeling asks what can be inferred: regular routes reveal home addresses and daily schedules of individual users in sparse areas. The team suppresses low-density areas and delays data publication — a harm no confidentiality control would have caught.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
