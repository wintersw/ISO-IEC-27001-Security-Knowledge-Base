---
title: A.8.24 Use of cryptography
description: Practical implementation, evidence, and audit guidance for A.8.24.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.24 Use of cryptography

## Overview

Cryptography protects confidentiality, integrity, authenticity, or proof of origin when selected and managed correctly. The organization needs rules for approved use, algorithms, protocols, keys, certificates, ownership, recovery, rotation, and retirement.

## Purpose

This control ensures that cryptographic controls are used appropriately — with approved algorithms, proper key management, and defined policies — to protect the confidentiality, integrity, and authenticity of information. Cryptography deployed without governance creates a false sense of security and can fail silently.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.24 when selected or otherwise committed to.
- **Implementation guidance:** Define **use of cryptography** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

Sensitive backups use approved encryption with keys stored separately under restricted roles. Key generation, rotation, recovery, use, and destruction are recorded, and a recovery exercise confirms data remains accessible to authorized staff.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Weak or deprecated algorithms (MD5, SHA-1, RC4) remain in use because no cryptographic inventory or migration plan exists.
- Encryption keys are stored alongside the data they protect — in the same database, config file, or repository.
- Certificates expire without warning because there is no automated expiry monitoring or renewal process.
- Cryptography is applied inconsistently — some services use TLS 1.3 while others still accept TLS 1.0.

## Auditor questions

- Where is the cryptographic policy documented, and what algorithms and key lengths are approved?
- How are cryptographic keys generated, stored, rotated, and destroyed?
- How are certificate expirations monitored, and what happens when a certificate expires unexpectedly?
- Show evidence that deprecated algorithms have been identified and a migration plan exists.

## Checklist

- [ ] cryptographic policy documented with approved algorithms and key lengths
- [ ] key management procedure defined (generation, storage, rotation, destruction)
- [ ] certificate inventory maintained with expiry monitoring
- [ ] deprecated algorithms identified and migration planned
- [ ] cryptographic controls applied consistently across services
- [ ] cryptographic implementation tested for correctness

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
