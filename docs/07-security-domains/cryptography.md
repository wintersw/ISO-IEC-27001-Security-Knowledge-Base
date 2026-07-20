---
title: Cryptography
description: Practical domain guidance for ISO 27001 security teams.
category: Security Domains
difficulty: Intermediate
reviewed_on: 2026-07-20
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Cryptography

Cryptography protects confidentiality, integrity, authenticity, and non-repudiation where appropriate.

## Key concepts

- encryption in transit
- encryption at rest
- key management
- certificate management
- secrets management

## Choosing algorithms and protocols

Cryptography relies on a few families, each with a purpose:

| Purpose | Family | Modern examples | Avoid |
|---|---|---|---|
| Confidentiality (bulk) | Authenticated symmetric encryption | AES-GCM with an approved key size, ChaCha20-Poly1305 | DES, 3DES, RC4; unauthenticated modes |
| Key establishment | Public-key or hybrid mechanisms | approved elliptic-curve or RSA schemes; standardized post-quantum or hybrid mechanisms where policy requires | ad hoc exchanges; obsolete parameters |
| Digital signatures | Public-key signatures | ECDSA P-256, Ed25519, RSA signatures with approved parameters; standardized post-quantum signatures where policy requires | RSA-1024; deprecated hashes |
| Integrity / fingerprint | Hashing | SHA-256, SHA-3 | MD5, SHA-1 |
| Passwords | Password hashing | Argon2id, bcrypt, scrypt | plain SHA/MD5 |
| Transport | Protocol | TLS 1.2 (hardened), TLS 1.3 | SSL, TLS 1.0/1.1 |

Select authenticated encryption (AEAD) for confidentiality with integrity, and never design your own algorithm or protocol. Prefer well-reviewed libraries and safe defaults.

There is no universal “strongest” algorithm table. Choose from the organization's approved profile using the data lifetime, threat model, interoperability, platform support, regulatory and national guidance, protocol construction, and transition plan. A larger key does not compensate for nonce reuse, exposed key material, insecure protocol design, or a flawed implementation.

## Crypto-agility and post-quantum readiness

Algorithms weaken over time, and large-scale quantum computing threatens today's asymmetric algorithms. Design for *crypto-agility*: keep an inventory of where cryptography is used, avoid hard-coding algorithms, and be able to swap them without redesigning systems. See [Post-Quantum Readiness](../29-emerging-data-security-trends/post-quantum-readiness.md).


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

Cryptography protects confidentiality, integrity, authenticity, and non-repudiation, but only when algorithms, keys, protocols, implementation, and lifecycle management are controlled.

A cryptographic standard should define approved algorithms, key lengths, protocols, certificate use, key ownership, rotation, recovery, revocation, storage, and retirement.

### Example

Sensitive backups are encrypted using centrally managed keys. Backup operators can run jobs but cannot extract keys. Key access is logged, recovery is tested, rotation is scheduled, and retired backups follow retention and destruction requirements.

### Best practices

- maintain a cryptographic inventory
- use approved modern algorithms and protocols
- separate key management from encrypted data
- restrict and log key access
- plan certificate and key rotation
- protect signing keys
- manage secrets outside source code
- prepare for post-quantum migration
- document exceptions and legacy dependencies

### Common weaknesses

Encryption may be enabled while keys are broadly accessible, certificates expire unexpectedly, legacy protocols remain active, or backups cannot be decrypted during recovery.

## Related chapters

- [Key Management](key-management.md)
- [Post-Quantum Readiness](../29-emerging-data-security-trends/post-quantum-readiness.md)
- [Post-Quantum Cryptography Inventory Template](../10-templates/post-quantum-crypto-inventory-template.md)

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Cryptography is addressed primarily through Annex A control A.8.24 (use of cryptography), which requires a policy on the use of cryptographic controls and key management. Related controls include A.5.14 (information transfer) for encryption in transit and A.8.10 (information deletion) for cryptographic erasure.
- **Implementation guidance:** Define cryptographic standards (algorithms, key lengths, TLS versions), certificate lifecycle management, key generation/rotation/revocation procedures, and an inventory of where cryptography is applied.
- **Best practice:** Cryptography policy should cover the full key lifecycle, not just algorithm selection. The most common audit finding is expired certificates and undocumented key-management procedures.

## Practical example

The platform team discovers several certificates expiring within 30 days across production services. The team inventories all TLS endpoints, assigns renewal ownership, sets automated expiry alerts at 60 and 30 days, and documents the key lifecycle including generation, rotation, and revocation procedures.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).

## Sources

- [NIST SP 800-131A Rev. 2](https://csrc.nist.gov/pubs/sp/800/131/a/r2/final)
- [NIST Post-Quantum Cryptography project](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [BSI Technical Guideline TR-02102](https://www.bsi.bund.de/EN/Service-Navi/Publications/TechnicalGuidelines/TR02102/BSITR02102.html)
