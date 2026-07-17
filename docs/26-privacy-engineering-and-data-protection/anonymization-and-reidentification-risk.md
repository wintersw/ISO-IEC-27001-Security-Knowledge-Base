---
title: Anonymization and Re-identification Risk
description: Limits of anonymization and how to assess re-identification risk.
category: Privacy Engineering and Data Protection
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - anonymization
  - re-identification
---

# Anonymization and Re-identification Risk

Anonymization attempts to remove the ability to identify individuals. In practice, re-identification risk depends on context, auxiliary datasets, uniqueness, and attacker capability.

## Risk drivers

- rare attributes
- geographic precision
- timestamps
- linkage across datasets
- small groups
- public auxiliary data
- persistent identifiers
- high-dimensional data
- model outputs

## Review questions

- Is the dataset truly anonymous or only pseudonymized?
- Which quasi-identifiers remain?
- Can records be linked to public datasets?
- Can an attacker infer sensitive attributes?
- Is data released once or repeatedly?
- Are small cohorts suppressed?
- Is aggregation sufficient?
- Is re-identification tested?

## Typical evidence

- re-identification risk assessment for each released or shared dataset
- documented decision on whether data is anonymous or only pseudonymized
- records of quasi-identifier analysis and small-cohort suppression
- linkage or re-identification test results before release
- release approvals noting auxiliary-data and repeated-release risk

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

An analytics team wants to publish "anonymized" ride data with pickup points and timestamps. The review finds that rare routes plus precise timestamps make many riders unique and linkable to public social media posts. The team coarsens locations to zones, buckets times, suppresses cohorts under 10 records, and runs a linkage test against public data before approving the release.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
