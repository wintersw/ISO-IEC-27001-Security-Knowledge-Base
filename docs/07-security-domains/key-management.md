---
title: Key Management
description: Cryptographic key lifecycle, HSMs, KMS, and PKI under ISO 27001.
category: Security Domains
difficulty: Advanced
reviewed_on: 2026-07-20
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Key Management

Key management covers the lifecycle of cryptographic keys—generation, distribution, storage, use, rotation, revocation, archival or recovery where justified, and destruction—and the systems and roles that protect them. Failures can arise from algorithms, protocols, implementations, random generation, access, or lifecycle management. This page complements [Cryptography](cryptography.md) and [Secrets Management](secrets-management.md).

## The key lifecycle

1. **Generation** — create keys with approved parameters and a suitable random source; use validated or high-assurance hardware where policy and risk require it.
2. **Distribution** — deliver keys to authorized parties over protected channels; never hard-code them in source or configuration.
3. **Storage** — protect keys at rest, separated from the data they protect.
4. **Use** — restrict who and what can use a key, and log usage.
5. **Rotation** — change keys on a defined schedule and after suspected compromise.
6. **Revocation** — invalidate keys and certificates that are no longer trusted.
7. **Destruction** — securely delete retired keys so recovery is infeasible.

## Protecting keys: HSM, KMS, and PKI

- **Hardware security module (HSM).** A tamper-resistant device that generates, stores, and uses keys so the private key never leaves the hardware in plaintext. Used for high-assurance keys such as certificate authority roots.
- **Key management service (KMS).** A managed service (often cloud-based) that centralizes key storage, access control, rotation, and audit logging, frequently backed by HSMs.
- **Public key infrastructure (PKI).** The certificate authorities, registration processes, and revocation mechanisms that bind public keys to identities. See its relationship to [identity federation](identity-federation.md).
- **Secrets management.** Passwords, API tokens, and database credentials have different lifecycle and exposure concerns. Manage them through the separate [Secrets Management](secrets-management.md) discipline; some platforms integrate both capabilities.

## Common weaknesses

- keys hard-coded in source control or container images
- shared keys with no rotation and no ownership
- encryption enabled but keys stored beside the data
- no separation between key administrators and data users
- certificates that expire unexpectedly because renewal is manual

## Evidence

- key inventory with owner, purpose, algorithm, and rotation schedule
- HSM/KMS configuration and access controls
- key rotation and revocation records
- certificate inventory and expiry monitoring
- separation-of-duties evidence for key administration

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A A.8.24 (use of cryptography) requires a policy on cryptographic controls and key management across the lifecycle. Supporting controls include A.5.15–A.5.18 (access control) and A.8.9 (configuration management).
- **Implementation guidance:** Define a key management policy covering algorithms, key lengths, lifecycle, and roles. Use an HSM or KMS rather than storing keys in application configuration, separate key-administration duties from data access, and monitor certificate expiry.
- **Best practice:** Centralize policy and inventory, automate safe rotation and certificate renewal, and use non-exportable hardware-backed keys for uses whose assurance needs justify it. Plan for crypto-agility so algorithms, formats, libraries, and protocols can be replaced without redesign.

## Practical example

A company moves database and storage encryption keys into a cloud KMS backed by HSMs, grants applications key-use permission without exposing the key material, and enables automatic annual rotation. TLS certificates are issued from an internal PKI with automated renewal and expiry alerting, ending a history of outages caused by lapsed certificates.

## Related chapters

- [Cryptography](cryptography.md)
- [Identity Federation and Single Sign-On](identity-federation.md)
- [Container and Cloud-Native Security](container-and-cloud-native-security.md)
- [Secrets Management](secrets-management.md)

## Sources

- [NIST SP 800-57 Part 1 Rev. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)
- [NIST SP 800-130](https://csrc.nist.gov/pubs/sp/800/130/final)
- [OWASP Key Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
