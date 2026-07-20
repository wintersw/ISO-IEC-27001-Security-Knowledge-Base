---
title: DevSecOps Implementation Guide
description: Integrating ISO 27001 controls into software delivery.
category: Implementation
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - implementation
---

# DevSecOps Implementation Guide
DevSecOps integrates security into development and operations workflows.

## Security activities by stage

| Stage | Security activities |
|---|---|
| Plan | security requirements, risk assessment |
| Design | architecture review, threat modeling |
| Code | secure coding, code review, secrets scanning |
| Build | dependency scanning, static application security testing (SAST) |
| Test | dynamic application security testing (DAST), security acceptance testing |
| Deploy | change control, approval, segregation |
| Operate | logging, monitoring, vulnerability response |

## ISO relevance

DevSecOps supports secure development lifecycle, secure coding, testing, change management, environment separation, access control, logging, and vulnerability management.

## Pipeline security gates

DevSecOps works best when security checks run automatically in the pipeline and can block a release. Define each gate as pass/fail with an owner and a documented exception path:

| Gate | Tool type | Fails the build when |
|---|---|---|
| Secrets scanning | pre-commit / CI | a credential or key is committed |
| Static analysis (SAST) | CI | a high-severity code weakness is introduced |
| Dependency / SCA | CI | a known-vulnerable component above threshold is used |
| Container image scan | CI | a critical image vulnerability is present |
| IaC / policy-as-code | CI | infrastructure violates a security policy |
| DAST | pre-release | a serious runtime vulnerability is found |

A gate that only warns is quickly ignored. Start with a small number of enforced gates and expand as the team matures.

## Software supply chain security

Modern attacks target the build pipeline and dependencies, not just the running application:

- generate a software bill of materials (SBOM) for each build;
- pin and verify dependencies, and monitor for newly disclosed vulnerabilities;
- sign build artifacts and verify signatures before deployment;
- protect the pipeline itself with least-privilege service accounts and protected branches; and
- keep provisioning credentials in a secrets manager, never in code.

See [Container and Cloud-Native Security](../07-security-domains/container-and-cloud-native-security.md) for image and Kubernetes specifics, and [Security Testing and Assurance](../07-security-domains/security-testing-and-assurance.md) for how testing depth complements automated gates.

## Threat modeling

Threat modeling in the design stage asks four questions: what are we building, what can go wrong, what will we do about it, and did we do a good enough job. Lightweight methods (for example, STRIDE) applied to significant changes catch design flaws that scanning cannot.

## Evidence

- security requirements
- threat models
- pipeline results
- code review records
- release approvals
- vulnerability tickets
- SBOMs and artifact signatures
- pipeline gate configuration and exception approvals

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** DevSecOps operationalizes Annex A A.8.25 (secure development lifecycle), A.8.26 (application security requirements), A.8.27 (secure architecture), A.8.28 (secure coding), A.8.29 (security testing), A.8.31 (separation of environments), A.8.32 (change management), and A.8.8 (technical vulnerability management).
- **Implementation guidance:** Encode these controls as automated pipeline gates with defined ownership and exception handling, so evidence is produced by the pipeline rather than assembled manually. Link findings to the [risk register](../05-risk-management/risk-register.md) and track remediation to closure.
- **Best practice:** Make the secure path the easy path. When secure defaults, templates, and gates are built into the pipeline, developers meet control requirements without extra effort, and conformity evidence is a by-product of normal delivery.


## Practical example

A program manager uses this guide to turn a broad security objective into owned work packages, milestones, evidence requirements, and review points suited to the organization's size and risk.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
