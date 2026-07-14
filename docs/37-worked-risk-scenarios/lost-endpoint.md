---
title: Lost Endpoint with Sensitive Data
description: Worked risk scenario: Lost Endpoint with Sensitive Data.
category: Worked Risk Scenarios
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - risk-scenario
  - worked-example
---

# Lost Endpoint with Sensitive Data

## Risk statement

> A laptop containing cached confidential data is lost during travel.

## Assets and context

Endpoint, cached files, credentials.

The assessor should identify a business owner, technical owner, affected services, data classification, dependencies, and existing recovery requirements.

## Threat and cause

The scenario may be initiated by loss or theft. The risk is increased by local data, weak encryption, persistent sessions.

## Business impact

Potential impacts include data exposure, account compromise. Impact should be assessed in the organization's own financial, operational, legal, safety, privacy, and reputational language.

## Existing-control review

Relevant controls may include device encryption, MDM, remote wipe, minimal local data, conditional access. The assessor should test whether these controls cover the complete population, operate at the required frequency, produce evidence, and address the actual scenario.

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

Useful indicators include encrypted-device coverage, unmanaged devices, remote wipe success, lost-device incidents. Metrics should be interpreted with scope and coverage information.

## Review triggers

Review after a related incident, major architecture change, supplier change, control failure, audit finding, new threat intelligence, or change in business impact.
