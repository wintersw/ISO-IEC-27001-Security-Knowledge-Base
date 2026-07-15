---
title: Worked Risk Assessment Example
description: Practical guidance for Worked Risk Assessment Example.
---

# Worked Risk Assessment Example

This page demonstrates a complete risk assessment walkthrough — from scenario identification through treatment to residual risk acceptance — using a realistic example.

## Scenario

**Organization:** A mid-sized SaaS company (200 employees) providing a customer data analytics platform.

**ISMS scope:** The analytics platform, supporting infrastructure (AWS-hosted), corporate IT, and the engineering and customer support functions.

**Risk methodology:** 5×5 matrix (impact 1–5, likelihood 1–5). Acceptance threshold: risks rated ≤6 are within appetite; risks rated 7–12 require treatment or documented acceptance; risks rated ≥13 require mandatory treatment.

## Step 1: Identify the risk scenario

**Risk ID:** RISK-2025-022

**Scenario:** An attacker gains access to the production AWS environment through a compromised developer credential that has excessive IAM permissions. The attacker exfiltrates customer analytics data from S3 buckets and deletes resources, causing a data breach and service outage.

**Asset:** Production AWS environment (EC2, S3, RDS) containing customer analytics data

**Threat:** External attacker targeting cloud infrastructure credentials

**Vulnerability:** Developer IAM users have broad permissions not limited to their role; no MFA enforced on all IAM users; no monitoring of anomalous API calls

## Step 2: Identify existing controls

- IAM roles for service-to-service authentication (reduces use of long-lived access keys)
- CloudTrail logging enabled
- Annual penetration test includes cloud infrastructure

## Step 3: Assess inherent risk

| Dimension | Rating | Rationale |
|---|---|---|
| Impact | 5 (Critical) | Breach of customer data could cause contractual penalties, reputational damage, and customer churn; depending on the nature of the personal data and the risk to data subjects, it may trigger regulatory notification obligations under GDPR |
| Likelihood | 3 (Moderate) | Credential compromise is a common attack vector; broad IAM permissions increase the blast radius; existing controls provide partial mitigation |

**Inherent risk level:** 5 × 3 = **15 (High — mandatory treatment required)**

## Step 4: Determine risk treatment

| Treatment option | Actions |
|---|---|
| **Modify** (primary) | Enforce MFA for all IAM users; implement least-privilege IAM policies using access advisor; deploy IAM Access Analyzer; configure GuardDuty alerts for anomalous API activity; implement S3 bucket policies preventing public access and requiring encryption |
| **Modify** (supporting) | Reduce session duration for privileged roles; implement just-in-time access for production environment changes |
| **Share** | Verify that cyber insurance covers cloud credential compromise and data breach response costs |

**Linked Annex A controls:** A.5.15 (Access control), A.5.16 (Identity management), A.5.17 (Authentication information), A.8.2 (Privileged access rights), A.8.5 (Secure authentication)

## Step 5: Assess residual risk

After treatment is implemented and verified:

| Dimension | Rating | Rationale |
|---|---|---|
| Impact | 4 (High) | Data exfiltration impact remains high because the compromised credentials legitimately authorize read access regardless of server-side encryption; treatment reduces the data an attacker can reach but does not eliminate exfiltration risk entirely |
| Likelihood | 2 (Low) | MFA and least privilege reduce the attack surface for initial compromise; anomaly detection and GuardDuty improve the speed of detection and containment, which limits blast radius — but they do not make the initial credential compromise itself harder. Residual likelihood is lowered because the attacker must now defeat multiple independent controls to achieve material impact. |

**Residual risk level:** 4 × 2 = **8 (Medium — requires risk owner acceptance)**

## Step 6: Accept residual risk

**Risk owner:** CTO

**Acceptance decision:** Residual risk level 8 is outside the routine acceptance threshold (≤6) but is accepted by the risk owner with the documented treatment in place, subject to verification of treatment effectiveness through control testing before the next management review. Review trigger: any cloud security incident, IAM architecture change, or at next annual risk reassessment.

**Approval:** CTO, 2025-06-15

## Step 7: Monitor and review

- Monthly review of IAM Access Analyzer findings
- Quarterly review of GuardDuty alerts and anomalous API activity
- Annual reassessment as part of the ISMS risk review cycle
- Immediate reassessment if a cloud credential incident occurs

## Evidence to retain

- Risk register entry RISK-2025-022 with all fields completed
- Treatment plan showing actions, owners, and target dates
- IAM policy changes and MFA enforcement records
- GuardDuty and Access Analyzer configuration evidence
- Residual risk acceptance record signed by CTO
- SoA showing applicable controls with implementation status

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **Worked Risk Assessment Example** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
