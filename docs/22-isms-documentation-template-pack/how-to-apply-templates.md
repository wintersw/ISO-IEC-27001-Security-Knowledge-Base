---
title: How to Apply the Templates
description: Practical instructions for tailoring, approving, linking, and maintaining ISMS templates.
category: ISMS Documentation Templates
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - template
  - isms
  - iso27001
---

# How to Apply the Templates

## 1. Copy the template

Copy the template from `docs/10-templates/` into your working documentation area.

Recommended naming pattern:

```text
YYYY-MM-DD-document-name-owner-status.md
```

Example:

```text
2026-07-14-risk-methodology-isms-approved.md
```

## 2. Replace placeholders

Replace placeholders such as:

- `[Organization name]`
- `[Scope]`
- `[Owner]`
- `[Review frequency]`
- `[Approval authority]`
- `[Risk criteria]`

Do not leave generic text in approved documents.

## 3. Tailor to the ISMS scope

A document should match the scope of the ISMS. Avoid including controls, systems, sites, or processes that are outside the certification scope unless clearly marked as dependencies or interfaces.

## 4. Assign ownership

Each document should have:

- document owner
- reviewer
- approval authority
- review frequency
- retention requirement

## 5. Link to other ISMS records

Use links in the documentation portal:

| Document | Link to |
|---|---|
| Risk register | asset inventory, treatment plan, SoA |
| SoA | risk register, control evidence, policy documents |
| Policy | procedures, checklists, training material |
| Audit report | findings, corrective actions, evidence |
| Management review | dashboards, audit results, incidents, risks |

## 6. Approve and publish

Approved documents should be stored in a controlled location. Readers must know which version is current.

## 7. Operate the document

Documents must be used. For example:

- risk methodology guides risk assessments
- incident procedure is used during incidents
- supplier procedure is used before onboarding suppliers
- access review template is completed quarterly

## 8. Retain evidence

Keep completed templates as evidence. Keep superseded versions where they explain historical audit periods or decisions.

## 9. Review and improve

Review documents after:

- major incidents
- internal audits
- external audit findings
- major organizational changes
- new legal or contractual requirements
- major technology changes
