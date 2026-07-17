---
title: Policy and Document Architecture Enhancement
description: Enhanced guidance for policy hierarchy, document control, review, distribution, classification, and terminology.
category: PDF Source Integration
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - source-integration
  - isms
  - iso27001
---

# Policy and Document Architecture Enhancement

The uploaded policy example reinforced the value of mature document control and a clear policy structure.

## Recommended policy document structure

- document title
- document type
- owner/editor
- reviewer
- approver
- version
- status
- classification
- effective date
- next review date
- distribution list
- change history
- purpose
- scope
- rules
- responsibilities
- references
- terms and definitions
- enforcement and violations
- approval record

## Policy hierarchy

| Level | Document type | Example |
|---|---|---|
| 1 | Policy / guideline | Information Security Policy |
| 2 | Standard | Logging and Monitoring Standard |
| 3 | Procedure | Incident Response Procedure |
| 4 | Work instruction | How to export security information and event management (SIEM) evidence |
| 5 | Record | Incident report, access review, audit report |

## Why terminology matters

Terms such as access, entry, availability, integrity, confidentiality, employees, contractors, third parties, and information owners should be harmonized across information security management system (ISMS) documents.

## Review triggers

- annual review date
- surveillance or certification audit findings
- changes to ISO/IEC 27000 family
- organizational changes
- scope changes
- legal or contractual changes
- incidents or control failures
- terminology changes

## Related templates

- [Document Control Procedure Template](../10-templates/document-control-procedure-template.md)
- [Policy Header and Version Control Template](../10-templates/policy-header-version-control-template.md)
- [Security Policy Review Record Template](../10-templates/security-policy-review-record-template.md)


## Practical example

A document controller audits the security policy set against the recommended structure and finds most documents lack a next-review date, classification, and distribution list, and that "third parties" means contractors in one policy but suppliers in another. The remediation adds the standard header block to every document, harmonizes the terminology section, and demotes two overly technical "policies" to standards in the hierarchy. At the next certification audit, the auditor samples three policies and verifies version history, approver, and review date without any follow-up requests.

## Evidence to retain

Retain records demonstrating document control maturity, such as:

- policy documents with complete header blocks (owner, version, approver, review date)
- change histories and approval records per document
- review records triggered by the defined review triggers
- distribution and acknowledgement records for applicable audiences


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
