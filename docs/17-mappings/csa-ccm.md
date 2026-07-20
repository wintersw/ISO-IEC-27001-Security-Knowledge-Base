---
title: ISO 27001 and CSA Cloud Controls Matrix
description: How ISO/IEC 27001 relates to the Cloud Security Alliance Cloud Controls Matrix.
category: Mappings
difficulty: Intermediate
reviewed_on: 2026-07-20
applies_to:
  - ISO/IEC 27001:2022
  - CSA CCM 4.1
tags:
  - mapping
---

# ISO 27001 and CSA Cloud Controls Matrix

The Cloud Security Alliance (CSA) Cloud Controls Matrix (CCM) 4.1 contains 197 control objectives across 17 cloud-security domains. It is paired with the Consensus Assessments Initiative Questionnaire (CAIQ) and the STAR registry. ISO/IEC 27001 provides the certifiable management system into which cloud controls fit.

## Practical relationship

| CCM domain (examples) | ISO/IEC 27001 relationship | Example evidence |
|---|---|---|
| Identity & Access Management (IAM) | A.5.15–A.5.18, A.8.2–A.8.5 | access policy, federation configuration, reviews |
| Data Security & Privacy (DSP) | A.5.12, A.5.34, A.8.24 | classification, encryption, key management |
| Application & Interface Security (AIS) | A.8.25–A.8.29 | secure development, API security testing |
| Threat & Vulnerability Management (TVM) | A.8.7, A.8.8 | patching, vulnerability scans |
| Logging & Monitoring (LOG) | A.8.15, A.8.16 | log coverage, alerting, retention |
| Business Continuity (BCR) | A.5.29, A.5.30, A.8.13, A.8.14 | continuity and recovery tests |
| Supply Chain & Governance (STA, GRC) | A.5.19–A.5.23, Clauses 4–6 | supplier agreements, shared-responsibility records |

## Best practice

CCM already publishes an official mapping to ISO/IEC 27001 and 27017/27018; use that authoritative crosswalk rather than reproducing one. Combine CCM with [ISO/IEC 27017 and 27018](../03-iso27001/iso27000-family-detailed.md) for cloud scope, and record the [shared-responsibility](../07-security-domains/cloud-security.md) split so evidence ownership between customer and provider is unambiguous. A STAR entry is a supplier-assurance signal, not a substitute for your own control assessment.

## Sources

- [CSA Cloud Controls Matrix](https://cloudsecurityalliance.org/research/cloud-controls-matrix)
- [CSA STAR Registry](https://cloudsecurityalliance.org/star/registry)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
