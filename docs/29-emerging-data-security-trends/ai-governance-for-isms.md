---
title: AI Governance for ISMS
description: How the ISMS should govern AI systems and AI-enabled data processing.
category: Emerging Data Security Trends
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - AI
  - governance
---

# AI Governance for ISMS
AI governance should be integrated into the ISMS rather than managed as a separate blind spot.

## Governance questions

- Which AI systems are in scope?
- Which datasets are used?
- Who owns the model?
- Who owns training data?
- Are outputs used for decisions?
- Are personal or confidential data involved?
- Are suppliers involved?
- Are risks assessed before deployment?
- Is monitoring in place?
- Can the system be disabled or rolled back?

## Governance artifacts

- AI system inventory
- AI data inventory
- AI risk assessment
- model card or system factsheet
- supplier assessment
- testing report
- approval record
- monitoring dashboard
- incident playbook

## Typical evidence

- AI system and AI data inventories with named owners
- pre-deployment AI risk assessments and approval records
- model cards or system factsheets for deployed AI systems
- supplier assessments for external model providers
- monitoring dashboards and rollback capability test records

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

An ISMS review discovers three departments already use external AI services that never went through any assessment — a classic governance blind spot. The organization creates an AI system inventory, assigns owners, and runs a lightweight risk assessment on each: two services are approved with monitoring conditions, and one that sent customer data to an unvetted provider is replaced. New AI use now enters through the same intake instead of appearing unannounced.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
