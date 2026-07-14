---
title: Risk Assessment Methodology Template
description: Tried-and-tested ISMS template: Risk Assessment Methodology Template.
category: Templates
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - template
  - isms-documentation
  - iso27001
---

# Risk Assessment Methodology Template

| Field | Content |
|---|---|
| Owner | [information security management system (ISMS) manager / risk function] |
| Approved by | [Top management / risk committee] |
| Version | [Version] |
| Review frequency | Annual or after significant change |

## 1. Purpose

This methodology defines how information security risks are identified, analyzed, evaluated, treated, accepted, monitored, and reviewed.

## 2. Scope

This methodology applies to information security risks within the ISMS scope.

## 3. Risk definition

Risk is the effect of uncertainty on information security objectives.

## 4. Risk scenario format

Use the following format:

> Threat actor or event causes an unwanted event affecting an asset or process, resulting in business impact.

Example:

> A compromised administrator account modifies production configuration, causing service outage and loss of customer trust.

## 5. Impact criteria

| Impact level | Description |
|---|---|
| 1 Very low | Limited inconvenience, no material business impact |
| 2 Low | Minor operational disruption or limited internal impact |
| 3 Medium | Noticeable business disruption, customer concern, or moderate compliance impact |
| 4 High | Significant operational, financial, legal, or reputational impact |
| 5 Very high | Severe business disruption, major legal exposure, or existential impact |

## 6. Likelihood criteria

| Likelihood level | Description |
|---|---|
| 1 Rare | Unlikely under current conditions |
| 2 Unlikely | Possible but not expected |
| 3 Possible | Could occur |
| 4 Likely | Expected to occur periodically |
| 5 Almost certain | Expected to occur frequently |

## 7. Risk rating

Risk rating = impact × likelihood.

| Score | Rating | Action |
|---|---|---|
| 1–4 | Low | Accept or monitor |
| 5–9 | Medium | Treat or justify acceptance |
| 10–16 | High | Treatment required unless formally accepted |
| 17–25 | Critical | Immediate management attention |

## 8. Treatment options

- avoid
- reduce
- transfer/share
- accept

## 9. Risk acceptance

Residual risks above tolerance must be approved by the accountable risk owner and reviewed at defined intervals.

## 10. Review triggers

Risks must be reviewed after:

- incidents
- major changes
- supplier changes
- new vulnerabilities
- audit findings
- legal or contractual changes
- changes in business objectives

## 11. Required records

- risk assessment worksheet
- risk register
- risk treatment plan
- risk acceptance records
- Statement of Applicability (SoA) updates

## Usage guidance

Use this template to document **Risk Assessment Methodology**. The owner defines its trigger and scope, uses authoritative sources, routes required approval, and tracks open items. Adapt the fields; this is guidance, not required ISO wording.

## Practical example

For one in-scope service, the owner completes the **Risk Assessment Methodology** record, links authoritative evidence, obtains review, and tracks rejected or incomplete items to closure.

## ISO requirement, implementation guidance, and best practice

This exact template is not an ISO requirement; it is guidance for recording **Risk Assessment Methodology** consistently. Controlled values, named owners, timestamps, approvals, and authoritative evidence improve assurance.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
