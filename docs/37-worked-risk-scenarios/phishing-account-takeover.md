---
title: Phishing Leads to Account Takeover
description: Worked risk scenario: Phishing Leads to Account Takeover.
category: Worked Risk Scenarios
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - risk-scenario
  - worked-example
---

# Phishing Leads to Account Takeover

## Risk statement

> A user approves a fraudulent authentication request and the attacker accesses cloud services.

## Assets and context

User identity, email, software as a service (SaaS) data.

The assessor should identify a business owner, technical owner, affected services, data classification, dependencies, and existing recovery requirements.

## Threat and cause

The scenario may be initiated by phishing and multifactor authentication (MFA) fatigue. The risk is increased by weak authentication design, insufficient detection.

## Business impact

Potential impacts include data access, fraud, lateral movement. Impact should be assessed in the organization's own financial, operational, legal, safety, privacy, and reputational language.

## Existing-control review

Relevant controls may include phishing-resistant MFA, conditional access, user reporting, session monitoring. The assessor should test whether these controls cover the complete population, operate at the required frequency, produce evidence, and address the actual scenario.

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

Useful indicators include account takeovers, risky sign-ins, phishing reports, phishing-resistant MFA coverage. Metrics should be interpreted with scope and coverage information.

## Review triggers

Review after a related incident, major architecture change, supplier change, control failure, audit finding, new threat intelligence, or change in business impact.


## Practical example

A risk owner adapts this scenario to a real service, validates the assets, threats, and impacts with relevant stakeholders, and records a treatment and residual-risk decision.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- validated scenario and affected assets
- likelihood and impact rationale
- treatment decision and owner
- residual-risk approval and review trigger

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
