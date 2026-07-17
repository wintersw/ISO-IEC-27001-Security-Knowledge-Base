---
title: Ransomware Affecting a Critical Service
description: "Worked risk scenario: Ransomware Affecting a Critical Service."
category: Worked Risk Scenarios
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - risk-scenario
  - worked-example
---

# Ransomware Affecting a Critical Service

## Risk statement

> Ransomware encrypts production systems and accessible backups, interrupting customer service and creating recovery uncertainty.

## Assets and context

Critical customer service, production servers, backup platform.

The assessor should identify a business owner, technical owner, affected services, data classification, dependencies, and existing recovery requirements.

## Threat and cause

The scenario may be initiated by phishing or exposed service. The risk is increased by weak segmentation, excessive privilege, accessible backups.

## Business impact

Potential impacts include service outage, lost revenue, contractual penalties, recovery cost. Impact should be assessed in the organization's own financial, operational, legal, safety, privacy, and reputational language.

## Existing-control review

Relevant controls may include multifactor authentication (MFA), endpoint detection and response (EDR), segmentation, immutable backups, restore tests, incident playbook. The assessor should test whether these controls cover the complete population, operate at the required frequency, produce evidence, and address the actual scenario.

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

Useful indicators include restore success, privileged access anomalies, critical EDR coverage, recovery test findings. Metrics should be interpreted with scope and coverage information.

## Worked decision

| Field | Illustrative entry |
|---|---|
| Inherent | 4 × 5 = 20 (very high): one identity tier reaches production and online backups |
| Finding | EDR coverage is 98%, but backup operators use corporate identity and clean-room recovery misses its objective |
| Treatment | Isolate backup identity and copies, close EDR gaps, reduce privilege paths, and repeat recovery |
| Interim residual | 12 (high); executive risk owner accepts for no more than 60 days |
| Exit | Independent restore meets objectives and identity-path testing proves separation |

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
