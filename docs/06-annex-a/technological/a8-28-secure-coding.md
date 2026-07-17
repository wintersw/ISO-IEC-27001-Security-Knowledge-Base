---
title: A.8.28 Secure coding
description: Practical implementation, evidence, and audit guidance for A.8.28.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.28 Secure coding

## Overview

Secure coding turns security requirements and known failure patterns into everyday implementation practices. Standards, training, review, automated checks, dependency controls, secrets handling, testing, and remediation should fit the technologies used.

## Purpose

This control ensures that secure coding principles and practices appropriate to the languages, frameworks, and threat context are applied before, during, and after coding. Training, tooling, review, testing, and feedback can prevent or detect relevant defect classes, but their coverage and findings must be verified.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.28 when selected or otherwise committed to.
- **Implementation guidance:** Define **secure coding** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- high-risk changes with security review
- security defects escaped to production
- critical findings fixed before release
- emergency changes reviewed

## Practical example

A pull request handling file uploads is checked against language guidance, peer-reviewed for authorization and validation, scanned for secrets and vulnerable components, tested with malicious files, and blocked until findings are resolved.

## Evidence to retain

- security requirements
- architecture or threat-model review
- test results
- release/change approval
- defect and remediation records

## Common mistakes

- Secure coding standards exist but developers are not trained on them or held accountable.
- Only OWASP Top 10 issues are considered — language-specific and framework-specific vulnerabilities are ignored.
- Code review focuses on functionality and performance; security review is not explicitly required.
- Secrets (API keys, tokens, passwords) are hardcoded in source code and committed to repositories.

## Auditor questions

- What secure coding standards are in place, and how are developers trained on them?
- How are secure coding violations detected — static analysis, peer review, or both?
- How are secrets prevented from being committed to source code repositories?
- Show evidence that security findings from code review or static analysis are tracked to resolution.

## Checklist

- [ ] secure coding standards documented per language and framework
- [ ] developer security training completed and tracked
- [ ] static analysis integrated into development workflow
- [ ] peer review includes security checklist
- [ ] secret scanning prevents credential commits
- [ ] security findings tracked and remediated before release

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
