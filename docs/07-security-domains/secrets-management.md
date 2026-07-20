---
title: Secrets Management
description: Lifecycle guidance for passwords, API tokens, credentials, and other non-cryptographic secrets.
category: Security Domains
difficulty: Intermediate
reviewed_on: 2026-07-20
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
  - secrets-management
---

# Secrets Management

A secret is information that grants authority or access, such as a password, API token, database credential, recovery code, or signing-service credential. Secrets management controls how secrets are created, stored, delivered, used, rotated, revoked, and monitored. It is related to—but distinct from—[cryptographic key management](key-management.md).

## Lifecycle and design

1. Inventory the systems and identities that use secrets; assign an owner and purpose.
2. Generate high-entropy secrets in an approved secrets manager and avoid shared human credentials.
3. Deliver secrets to workloads through authenticated, short-lived mechanisms rather than source code, images, tickets, or chat.
4. Grant least-privilege access, log retrieval and administrative changes, and prevent secret values from entering logs.
5. Rotate automatically where possible and immediately after suspected disclosure or ownership change.
6. Revoke, verify dependent services, and retain metadata—not secret values—as evidence.

Prefer workload identity and short-lived credentials over long-lived stored secrets. Scan source history, build artifacts, container images, and logs for accidental exposure. Treat a detected secret as compromised even when the current branch no longer contains it.

## ISO relevance and evidence

Secrets management supports A.5.15–A.5.18, A.8.2, A.8.4, A.8.5, A.8.9, A.8.12, and secure-development controls A.8.25–A.8.29. Evidence includes an inventory, access policy, manager configuration, access and rotation logs, scanning coverage, incident records, and time-bound exceptions.

## Practical example

A deployment platform exchanges its workload identity for a short-lived database credential. Developers cannot read production values, retrieval is logged, leaked-secret scanning blocks commits, and emergency rotation is rehearsed without rebuilding the application.

## Common mistakes

- treating environment variables as a secrets-management system
- rotating a secret without updating or testing every consumer
- storing bootstrap or recovery credentials beside the system they recover
- assuming encryption at rest compensates for broad read access

## Sources

- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [NIST SP 800-204A, Building Secure Microservices-based Applications](https://csrc.nist.gov/pubs/sp/800/204/a/final)

## Related chapters

- [Key Management](key-management.md)
- [Identity and Access Management](iam.md)
- [Software Supply Chain Security](../34-secure-by-design/software-supply-chain-security.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
