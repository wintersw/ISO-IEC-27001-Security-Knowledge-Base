---
title: Identity and Access Lifecycle
description: Joiner, mover, leaver, privileged access, service accounts, and access reviews.
category: Security Lifecycle Management
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-lifecycle
  - isms
---

# Identity and Access Lifecycle

Identity and access lifecycle management is one of the clearest examples of security lifecycle management.

```mermaid
flowchart LR
    A[Joiner] --> B[Identity Created]
    B --> C[Access Approved]
    C --> D[Access Used and Logged]
    D --> E[Mover / Role Change]
    E --> F[Access Re-certified]
    F --> G[Leaver]
    G --> H[Access Removed]
    H --> I[Evidence Retained]
```

## Practical example

An engineer moves from product development to security operations. Old repository access is no longer needed, new monitoring access is needed, privileged access requires approval and session logging, and service accounts owned by the engineer must be reassigned. Access review must verify that old access was removed.

## Best practices

- Integrate HR events with identity and access management (IAM) workflows.
- Use role-based access where practical.
- Treat privileged access as a separate lifecycle.
- Assign owners for service accounts and application programming interface (API) keys.
- Review movers with the same seriousness as leavers.
- Define emergency access with expiry and review.
- Monitor access to sensitive data, not just system login.

## Related chapters

- [Zero Trust Identity-Centric Security](../27-zero-trust-and-data-centric-security/identity-centric-security.md)
- [Access Review Template](../10-templates/access-review-template.md)
- [Quarterly Access Review Checklist](../11-checklists/quarterly-access-review.md)


## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- lifecycle record with owner and scope
- stage approvals and operating records
- exceptions and remediation actions
- closure and retained-evidence record

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
