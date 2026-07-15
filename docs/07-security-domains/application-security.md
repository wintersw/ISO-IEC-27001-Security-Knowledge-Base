---
title: Application Security and Secure SDLC
description: Practical domain guidance for ISO 27001 security teams.
---

# Application Security and Secure software development lifecycle (SDLC)

Application security reduces risk in software requirements, design, implementation, testing, deployment, and maintenance.

## Key concepts

- security requirements
- threat modeling
- secure coding
- static application security testing (SAST)
- dynamic application security testing (DAST)
- software composition analysis (SCA)
- environment separation


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

A practical application-security program connects product requirements, architecture review, threat modeling, secure coding, dependency management, continuous integration and continuous delivery (CI/CD) controls, security testing, release decisions, vulnerability response, and operational monitoring.

### Example

A team develops a customer profile application programming interface (API). During design, it identifies tenant separation, authorization, rate limiting, input validation, audit logging, and data minimization requirements. Automated tests cover authorization and input handling. A pre-release review confirms that secrets are managed securely and that failed authorization attempts create monitoring signals. After release, API anomalies and vulnerability reports feed the incident and improvement processes.

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

### Defensive web-verification model

Testing should follow how an application can actually be discovered, reached, trusted, and misused. Use the following model to set requirements and test scope; it is defensive guidance, not an instruction to attack systems without authorization.

| Area | Security objective | Example verification evidence |
|---|---|---|
| External exposure | Only intended domains, services, interfaces, and administrative paths are reachable | approved inventory, domain ownership review, exposure scan, remediation ticket |
| Authentication and recovery | Credentials, account recovery, and automated-attack resistance protect account entry | design decision, rate-limit test, recovery-flow test, multifactor-authentication result |
| Sessions and requests | Session identifiers, cookies, logout, expiry, and state-changing requests resist reuse or forgery | test cases, configuration record, retest result |
| Authorization and business logic | Every request is checked against the user, tenant, object, action, and business state | negative authorization tests, abuse cases, tenant-isolation test |
| Input and output handling | Untrusted data cannot change commands, queries, page structure, or unintended file paths | validation rules, code review, automated and manual test results |
| File processing | Uploads are constrained by type, size, storage location, access, scanning, and execution policy | upload test matrix, storage design, malware-handling result |
| Detection and response | Security-relevant failures and suspicious behavior create usable, protected signals | logging requirements, alert test, response ticket |

Discovery and testing must have written scope, permitted methods, test accounts, data-handling rules, stop conditions, contacts, and a remediation-and-retest workflow. A scanner result alone does not prove that authorization, workflow abuse, tenant separation, or monitoring works.

### Typical evidence

Architecture decisions, threat models, security requirements, authorized test scope, code-review records, automated and manual test results, penetration-test reports, release approvals, dependency inventories, vulnerability tickets, retest results, and monitoring records.

### Common weaknesses

Application security fails when testing occurs too late, findings are accepted without ownership, production data is copied into test, shared libraries remain unpatched, and teams measure scan counts instead of escaped defects and customer exposure.

## Related chapters

- [Secure by Design](../34-secure-by-design/index.md)
- [Change and Release Lifecycle](../31-security-lifecycle-management/change-release-lifecycle.md)
- [Secure artificial intelligence (AI) Development Lifecycle](../29-emerging-data-security-trends/secure-ai-development-lifecycle.md)

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Application security is not a standalone clause in ISO/IEC 27001. It spans multiple Annex A controls — primarily A.8.25 (secure development life cycle), A.8.26 (application security requirements), A.8.27 (secure system architecture), A.8.28 (secure coding), A.8.29 (security testing), A.8.30 (outsourced development), A.8.31 (separation of environments), and A.8.32 (change management). Each must be selected through risk treatment and recorded in the Statement of Applicability.
- **Implementation guidance:** Embed security activities — threat modelling, SAST/DAST, dependency scanning, security code review — into the development lifecycle and CI/CD pipeline. Define security gates that must pass before promotion to production.
- **Best practice:** Treat application security as a continuous pipeline activity, not a pre-release checkpoint. Evidence of security activities should be generated automatically and retained as control operating records.

## Practical example

A development team adds a payment integration to the web application. Threat modelling identifies cardholder data in transit and at rest as key risks. The team applies input validation, TLS, parameterised queries, and SAST in CI/CD, then verifies findings before release.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
