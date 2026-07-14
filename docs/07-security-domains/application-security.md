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

- **ISO requirement:** This chapter explains **Application Security and Secure SDLC** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Practical example

A growing software-as-a-service provider applies this guidance to a new customer-data feature. The service owner identifies the relevant risks, implements proportionate safeguards, and verifies them before release and during operation.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
