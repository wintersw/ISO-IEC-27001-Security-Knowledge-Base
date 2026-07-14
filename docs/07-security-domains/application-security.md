---
title: Application Security and Secure SDLC
description: Practical domain guidance for ISO 27001 security teams.
---

# Application Security and Secure SDLC

Application security reduces risk in software requirements, design, implementation, testing, deployment, and maintenance.

## Key concepts

- security requirements
- threat modeling
- secure coding
- SAST
- DAST
- SCA
- environment separation

## Best practices

- Define ownership and scope.
- Integrate with risk management.
- Document minimum requirements.
- Automate evidence collection where practical.
- Review exceptions and control performance.
- Link operational practices to Annex A and the SoA.

## ISO relevance

This domain supports multiple ISO/IEC 27001 clauses and Annex A controls. Use the domain guidance to implement controls in a practical, operationally sustainable way.

## Evidence

- policy or standard
- process documentation
- configuration evidence
- logs or reports
- review records
- exceptions
- remediation tickets

## Detailed implementation guidance

Application security protects software behavior, data processing, interfaces, and dependencies throughout the product lifecycle. It should begin when the business use case is defined, not when code is ready for penetration testing.

A practical application-security program connects product requirements, architecture review, threat modeling, secure coding, dependency management, CI/CD controls, security testing, release decisions, vulnerability response, and operational monitoring.

### Example

A team develops a customer profile API. During design, it identifies tenant separation, authorization, rate limiting, input validation, audit logging, and data minimization requirements. Automated tests cover authorization and input handling. A pre-release review confirms that secrets are managed securely and that failed authorization attempts create monitoring signals. After release, API anomalies and vulnerability reports feed the incident and improvement processes.

### Best practices

- define security acceptance criteria with business requirements
- perform threat modeling for high-risk changes
- use reusable secure design patterns
- scan dependencies and source code, but verify tool coverage
- test authorization and business logic, not only common injection flaws
- separate development, testing, and production
- protect build pipelines and signing keys
- record security debt and release exceptions
- monitor production behavior
- analyze repeated vulnerability classes

### Typical evidence

Architecture decisions, threat models, security requirements, code-review records, automated test results, penetration-test reports, release approvals, dependency inventories, vulnerability tickets, and monitoring records.

### Common weaknesses

Application security fails when testing occurs too late, findings are accepted without ownership, production data is copied into test, shared libraries remain unpatched, and teams measure scan counts instead of escaped defects and customer exposure.

## Related chapters

- [Secure by Design](../34-secure-by-design/index.md)
- [Change and Release Lifecycle](../31-security-lifecycle-management/change-release-lifecycle.md)
- [Secure AI Development Lifecycle](../29-emerging-data-security-trends/secure-ai-development-lifecycle.md)
