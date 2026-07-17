---
title: A.8.11 Data masking
description: Practical implementation, evidence, and audit guidance for A.8.11.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.11 Data masking

## Overview

Data masking reduces exposure by replacing, obscuring, or transforming sensitive values while keeping data useful for an approved purpose. The method should match re-identification risk, context, access, and downstream use.

## Purpose

This control ensures that sensitive data is obscured, transformed, or replaced where masking is an appropriate way to reduce exposure while preserving required utility. Masking strength, reversibility, access to mapping data, and re-identification risk must match the use case; masking does not automatically make data anonymous.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.11 when selected or otherwise committed to.
- **Implementation guidance:** Define **data masking** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A test environment receives customer-like records with names and account numbers tokenized and rare attributes generalized. The team tests utility and re-identification risk and restricts the separately protected token mapping.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Production data is copied to test environments without masking, exposing real customer or employee information.
- Masking is applied only to direct identifiers (name, email) but rare combinations or quasi-identifiers enable re-identification.
- The mapping table or seed used for tokenization is stored alongside the masked data, defeating the purpose.
- Masking is treated as a one-time step — new fields, schema changes, or data sources are not added to the masking scope.

## Auditor questions

- Which data elements are subject to masking, and how was the scope determined?
- What masking techniques are used, and how is re-identification risk assessed?
- How is masking verified before non-production environments are released for use?
- Show evidence that masking rules are reviewed when schemas change or new data sources are added.

## Checklist

- [ ] masking scope defined based on data classification
- [ ] masking technique appropriate to re-identification risk
- [ ] masking verified before non-production use
- [ ] mapping tables/secrets stored separately from masked data
- [ ] masking rules reviewed on schema change
- [ ] exception process for unmasked data in non-production documented

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
