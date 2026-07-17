---
title: Differential Privacy Overview
description: Conceptual introduction for security and data governance teams.
category: Privacy Engineering and Data Protection
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - differential-privacy
  - privacy-enhancing-technologies
---

# Differential Privacy Overview

Differential privacy is a mathematical privacy technique that limits how much the result of an analysis can reveal about any one individual.

## Where it can help

- statistical reporting
- aggregate analytics
- privacy-preserving dashboards
- data sharing with reduced individual exposure
- machine learning pipelines where aggregate signals are sufficient

## Practical governance questions

- What privacy budget is acceptable?
- Who decides privacy utility tradeoffs?
- Are outputs aggregate or record-level?
- Is repeated querying controlled?
- Are assumptions documented?
- Can stakeholders understand the limitations?
- Is the technique validated by competent specialists?

## Caution

Differential privacy is powerful but not a magic label. It requires correct design, governance, and validation.

## Typical evidence

- documented privacy budget decision and who approved the privacy-utility tradeoff
- design record describing where noise is applied and the assumptions made
- controls limiting repeated querying against the same data
- validation of the implementation by competent specialists
- documentation of limitations communicated to stakeholders

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

An HR team wants a public dashboard of salary statistics by department. Small departments would expose individuals, so the team applies differential privacy to the aggregates, has a specialist set and document the privacy budget, limits how often the queries can be re-run, and records the known limitations — rather than simply labeling the dashboard "anonymized" without analysis.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
