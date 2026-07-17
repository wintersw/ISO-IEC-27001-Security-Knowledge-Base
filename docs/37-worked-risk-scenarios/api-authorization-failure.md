---
title: API Authorization Failure
description: "Worked risk scenario: API Authorization Failure."
category: Worked Risk Scenarios
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - risk-scenario
  - worked-example
---

# API Authorization Failure
## Risk statement

> An API fails to enforce object or tenant authorization and exposes another customer's data.

## Assets and context

API, customer records, tenant identifiers.

The assessor should identify a business owner, technical owner, affected services, data classification, dependencies, and existing recovery requirements.

## Threat and cause

The scenario may be initiated by external attacker or user. The risk is increased by inconsistent authorization, inadequate testing.

## Business impact

Potential impacts include cross-tenant breach, customer trust loss. Impact should be assessed in the organization's own financial, operational, legal, safety, privacy, and reputational language.

## Existing-control review

Relevant controls may include central authorization, tenant checks, security tests, logging, rate limits. The assessor should test whether these controls cover the complete population, operate at the required frequency, produce evidence, and address the actual scenario.

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

Useful indicators include authorization defects, cross-tenant test results, unusual API access. Metrics should be interpreted with scope and coverage information.

## Worked decision

| Field | Illustrative entry |
|---|---|
| Inherent | 3 × 5 = 15 (high): one defect could expose many customer tenants |
| Finding | Two legacy endpoints look up objects before checking tenant and lack negative-authorization tests |
| Treatment | Use shared middleware, add cross-tenant CI tests, inventory endpoints, and alert on tenant-ID mismatches |
| Target | 5 (moderate); API engineering lead; fix before the next release |
| Verification | Independent two-tenant test plus telemetry proving middleware coverage |

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
