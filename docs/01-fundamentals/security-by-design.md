---
title: Security by Design
description: Explains how to build security into systems and processes from the start.
category: Fundamentals
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - fundamentals
---

# Security by Design

Security by design means considering security requirements, risks, and controls early in business processes, projects, systems, and software development.

## Why this matters

Security added late is usually more expensive, less effective, and more disruptive.

## Practical implementation

1. Include security requirements in project initiation.
2. Perform risk assessment or [threat modeling](../07-security-domains/security-testing-and-assurance.md).
3. Define data classification and privacy needs.
4. Review architecture before implementation.
5. Automate security checks in delivery pipelines (see [DevSecOps](../16-implementation-guides/devsecops-guide.md)).
6. Validate controls during acceptance.
7. Update documentation and operational processes before go-live.

## ISO relevance

Security by design supports information security in project management, secure development lifecycle, application security requirements, secure architecture, change management, and risk assessment.

## Evidence

- project security checklist
- architecture review
- threat model
- risk assessment
- security test results
- change approval


## Practical example

A product team is building a new customer payment portal. During the design phase, the security architect facilitates a threat modeling session that identifies three high-priority risks: payment data interception, session hijacking, and SQL injection. Security requirements are added to the product backlog before development starts: TLS 1.3 enforcement, secure session management with HTTP-only cookies and short timeouts, and parameterized queries with input validation. Architecture review confirms the design before coding begins. SAST and DAST are integrated into the CI/CD pipeline. Before go-live, a penetration test validates the controls. The threat model, architecture review sign-off, security test results, and pen test report become auditable evidence.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
