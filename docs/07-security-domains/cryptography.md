---
title: Cryptography
description: Practical domain guidance for ISO 27001 security teams.
---

# Cryptography

Cryptography protects confidentiality, integrity, authenticity, and non-repudiation where appropriate.

## Key concepts

- encryption in transit
- encryption at rest
- key management
- certificate management
- secrets management

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

- [Post-Quantum Readiness](../29-emerging-data-security-trends/post-quantum-readiness.md)
- [Post-Quantum Crypto Inventory Template](../10-templates/post-quantum-crypto-inventory-template.md)
