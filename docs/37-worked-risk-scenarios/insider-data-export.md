---
title: Insider Data Export
description: "Worked risk scenario: Insider Data Export."
category: Worked Risk Scenarios
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - risk-scenario
  - worked-example
---

# Insider Data Export

## Risk statement

> An employee with legitimate access exports sensitive data for unauthorized personal or commercial use.

## Assets and context

Customer database, reports, intellectual property.

The assessor should identify a business owner, technical owner, affected services, data classification, dependencies, and existing recovery requirements.

## Threat and cause

The scenario may be initiated by malicious insider or coerced user. The risk is increased by broad access, weak export monitoring, poor segregation.

## Business impact

Potential impacts include confidentiality loss, fraud, competitive damage. Impact should be assessed in the organization's own financial, operational, legal, safety, privacy, and reputational language.

## Existing-control review

Relevant controls may include least privilege, data loss prevention (DLP), export approval, monitoring, access review, investigation process. The assessor should test whether these controls cover the complete population, operate at the required frequency, produce evidence, and address the actual scenario.

## Treatment approach

A complete treatment plan should:

1. reduce the most important causal weaknesses
2. assign owners and dates
3. define compensating controls where immediate remediation is impossible
4. update the Statement of Applicability if control implementation changes
5. define residual-risk approval
6. specify verification evidence

## Example evidence

- asset and owner record
- risk assessment and treatment plan
- architecture or data-flow record
- policy and procedure
- technical configuration
- operating logs or tickets
- control test
- exception or risk acceptance
- management decision

## Monitoring indicators

Useful indicators include bulk exports, unusual access, high-risk users, DLP incidents. Metrics should be interpreted with scope and coverage information.

## Worked decision

| Field | Illustrative entry |
|---|---|
| Inherent | 3 × 5 = 15 (high): analysts can export the complete customer dataset |
| Finding | Bulk export uses the viewing permission and alerts lack out-of-hours review |
| Treatment | Separate export privilege, require approval, watermark files, and monitor volume and destination |
| Target | 6 (moderate); data platform owner; privilege split due in 30 days |
| Safeguard | Monitoring is proportionate, access-controlled, time-limited, and privacy-reviewed |

## Review triggers

Review after a related incident, major architecture change, supplier change, control failure, audit finding, new threat intelligence, or change in business impact.


## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- validated scenario and affected assets
- likelihood and impact rationale
- treatment decision and owner
- residual-risk approval and review trigger


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
