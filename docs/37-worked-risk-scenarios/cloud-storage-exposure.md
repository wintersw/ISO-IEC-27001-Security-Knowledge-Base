---
title: Cloud Storage Exposure
description: "Worked risk scenario: Cloud Storage Exposure."
category: Worked Risk Scenarios
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - risk-scenario
  - worked-example
---

# Cloud Storage Exposure

## Risk statement

> A storage resource is made publicly accessible and confidential records become discoverable.

## Assets and context

Cloud storage, customer records.

The assessor should identify a business owner, technical owner, affected services, data classification, dependencies, and existing recovery requirements.

## Threat and cause

The scenario may be initiated by misconfiguration or unauthorized change. The risk is increased by unsafe defaults, weak change control, missing monitoring.

## Business impact

Potential impacts include data breach, customer harm, regulatory and contractual impact. Impact should be assessed in the organization's own financial, operational, legal, safety, privacy, and reputational language.

## Existing-control review

Relevant controls may include public-access prevention, policy-as-code, data classification, logging, alerting. The assessor should test whether these controls cover the complete population, operate at the required frequency, produce evidence, and address the actual scenario.

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

Useful indicators include public resources detected, drift age, remediation time, repeat configuration failures. Metrics should be interpreted with scope and coverage information.

## Worked decision

| Field | Illustrative entry |
|---|---|
| Inherent | 4 × 5 = 20 (very high): storage is created frequently and may hold customer records |
| Finding | Preventive policy covers managed accounts, but an acquired account is outside the hierarchy |
| Treatment | Enrol all accounts, enforce preventive policy, scan continuously, classify stores, and test response |
| Target | 4 (low); cloud platform owner; acquired account enrolled in ten business days |
| Boundary | Public content uses a separate publishing path; no sensitive-data exception is permitted |

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
