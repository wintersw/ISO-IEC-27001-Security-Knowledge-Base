---
title: Privacy by Design for Security Teams
description: Workflow for embedding privacy controls in project and security reviews.
category: Privacy Engineering and Data Protection
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - privacy-by-design
  - security-review
---

# Privacy by Design for Security Teams

Privacy by design means considering privacy before data is collected or processed, not only after a legal review.

## Workflow

1. identify personal data
2. confirm purpose and necessity
3. map data flows
4. classify sensitivity
5. minimize data elements
6. define retention and deletion
7. select protection controls
8. assess re-identification and misuse risk
9. document decisions
10. monitor operation and exceptions

## Security review questions

- Is all personal data necessary?
- Can data be aggregated, masked, tokenized, or pseudonymized?
- Are access and logging appropriate?
- Can test systems avoid production personal data?
- Are exports controlled?
- Does the breach team know where data flows?
- Are artificial intelligence (AI) or analytics uses reviewed?

## Typical evidence

- completed privacy-by-design checklist or review record per project
- data flow map and classification produced before build
- documented minimization decisions (fields removed, masking, synthetic test data)
- retention and deletion design agreed before release
- release approval showing privacy risks and safeguards were assessed

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

A team building a chat-support feature runs the privacy-by-design workflow at design time: it maps that transcripts flow to a third-party analytics tool, discovers full transcripts are unnecessary, and ships with redacted transcripts, 90-day retention, and masked support views. The privacy decisions cost days at design time instead of a costly retrofit after launch.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
