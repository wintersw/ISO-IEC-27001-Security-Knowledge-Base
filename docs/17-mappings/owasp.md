---
title: ISO 27001 and OWASP
description: How OWASP resources support application security controls.
category: Mappings
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - mapping
---

# ISO 27001 and OWASP

OWASP resources help implement application security controls, especially secure development lifecycle, application security requirements, secure coding, and security testing.

## Useful OWASP resources

- OWASP Top 10
- OWASP Application Security Verification Standard (ASVS)
- OWASP Software Assurance Maturity Model (SAMM)
- OWASP Testing Guide
- OWASP Cheat Sheet Series

## Practical use

Use OWASP resources to define application security requirements, coding standards, developer training, test cases, and maturity targets.

| OWASP resource | Appropriate use | ISO/IEC 27001 relationship |
|---|---|---|
| ASVS | verifiable application security requirements and test coverage | A.8.25–A.8.29 and project-specific controls |
| SAMM | software-assurance capability assessment and roadmap | clauses 6, 7, 8, 9, and continual improvement |
| Top 10 | awareness and risk-conversation starter | risk identification; not a complete test standard |
| Testing Guide and Cheat Sheet Series | test design and implementation guidance | secure coding, testing, configuration, authentication, and logging controls |

Record the OWASP project version used. Do not claim that a Top 10 scan demonstrates secure-development conformity or complete application coverage.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).


## Practical example

A team derives release-gate requirements from scoped ASVS controls, links each requirement to tests and exceptions, and uses the results as evidence for A.8.26 and A.8.29. It separately evaluates governance, supplier, operational, and ISMS requirements that ASVS does not address.
