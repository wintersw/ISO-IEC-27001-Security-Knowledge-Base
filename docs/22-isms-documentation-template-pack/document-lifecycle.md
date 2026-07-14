---
title: ISMS Document Lifecycle
description: How ISMS documents should move from draft to approved, reviewed, archived, and retired.
category: ISMS Documentation Templates
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - template
  - isms
  - iso27001
---

# ISMS Document Lifecycle

## Lifecycle stages

```mermaid
flowchart LR
    A[Draft] --> B[Review]
    B --> C[Approved]
    C --> D[Published]
    D --> E[In Use]
    E --> F[Periodic Review]
    F --> C
    F --> G[Superseded]
    G --> H[Archived]
    H --> I[Retired]
```

## Document metadata

Every controlled ISMS document should include:

- title
- document ID
- version
- owner
- reviewer
- approver
- approval date
- next review date
- classification
- retention period
- change history

## Review triggers

Review a document when:

- the ISMS scope changes
- the organization changes
- technology changes
- incidents reveal weakness
- internal audits identify gaps
- legal or contractual requirements change
- suppliers or critical dependencies change

## Audit evidence

Auditors may sample:

- whether documents are approved
- whether versions are controlled
- whether employees can access current documents
- whether old versions are archived
- whether review dates are followed
- whether documents match actual practice

## Related policy and document architecture

For enhanced policy hierarchy, version-control, terminology, distribution, classification, and review guidance, see:

- [Policy and Document Architecture Enhancement](../24-pdf-source-integration/policy-document-architecture.md)
- [Policy Header and Version Control Template](../10-templates/policy-header-version-control-template.md)
