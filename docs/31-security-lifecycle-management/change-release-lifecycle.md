---
title: Change and Release Security Lifecycle
description: How security should be embedded into change, release, and DevSecOps workflows.
category: Security Lifecycle Management
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-lifecycle
  - isms
---

# Change and Release Security Lifecycle

Change is one of the most important security lifecycle triggers. A well-controlled change process prevents security drift and ensures that risks are reassessed before systems move into production.

```mermaid
flowchart TD
    A[Change Proposed] --> B[Security Impact Assessment]
    B --> C{Risk Significant?}
    C -->|No| D[Standard Approval]
    C -->|Yes| E[Risk / Architecture Review]
    E --> F[Security Testing]
    F --> G[Release Approval]
    G --> H[Post-Implementation Review]
    H --> I[Update Evidence and Risks]
```

## Example

A development team adds a new application programming interface (API) endpoint that exposes customer data to a partner. Security review should check data classification, authentication, authorization, rate limiting, logging, monitoring, supplier obligations, breach impact, data loss prevention (DLP)/export control, testing, and rollback.

## Best practices

- Use lightweight review for low-risk changes and deeper review for high-risk changes.
- Make security requirements part of the change form.
- Integrate security testing into continuous integration and continuous delivery (CI/CD) where possible.
- Require risk updates when changes affect sensitive data or critical services.
- Keep release evidence linked to the asset and service records.
- Use post-implementation review for failed or emergency changes.

## Related chapters

- [development, security, and operations (DevSecOps) Guide](../16-implementation-guides/devsecops-guide.md)
- [Change Security Assessment Template](../10-templates/change-security-assessment-template.md)
- [A.8.32 Change Management](../06-annex-a/technological/a8-32-change-management.md)


## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- lifecycle record with owner and scope
- stage approvals and operating records
- exceptions and remediation actions
- closure and retained-evidence record

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
