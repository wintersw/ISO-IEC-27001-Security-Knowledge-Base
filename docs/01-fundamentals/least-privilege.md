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

Least privilege means users, services, and administrators receive only the access needed to perform approved tasks, for only as long as necessary.

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

- “Admin by default” culture
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
