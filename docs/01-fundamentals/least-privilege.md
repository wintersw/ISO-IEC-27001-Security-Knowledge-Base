---
title: Least Privilege
description: Explains least privilege as a practical access-control principle.
category: Fundamentals
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - fundamentals
---

# Least Privilege

Least privilege means users, services, and administrators receive only the access needed to perform approved tasks, for only as long as necessary. It is a core principle of both [Zero Trust](zero-trust.md) and [Identity and Access Management](../07-security-domains/iam.md).

## Why this matters

Excessive access increases the blast radius of mistakes, compromised accounts, malicious insiders, and misconfigured integrations.

## Practical implementation

1. Define job roles and access bundles.
2. Avoid direct assignment of broad permissions.
3. Use groups or roles instead of individual exceptions where possible.
4. Require approval for privileged access.
5. Use just-in-time access for high-risk operations where feasible.
6. Review access periodically.
7. Remove access when roles change.

## Common mistakes

- “Administrator access by default” culture
- Permanent emergency access
- Service accounts with excessive permissions
- Access reviews that approve everything without challenge
- Lack of ownership for legacy permissions

## Evidence

- role model
- access request records
- privileged access approvals
- review records
- remediation tickets


## Practical example

A developer accumulated broad IAM permissions across three AWS accounts over two years through role changes and project migrations. During routine work, a misconfigured Terraform apply drops a production DynamoDB table — the developer had delete permissions that were never needed. The organization introduces just-in-time access for privileged operations, role-based permission sets tied to job function, and automated quarterly permission reviews that flag unused grants.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
