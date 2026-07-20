---
title: Authenticity, Accountability, and Non-Repudiation
description: Explains additional security properties beyond confidentiality, integrity, and availability.
category: Fundamentals
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - fundamentals
---

# Authenticity, Accountability, and Non-Repudiation

The [CIA triad](cia-triad.md) is fundamental, but security teams often need additional properties.

## Authenticity

Authenticity means that an entity or message is genuine. Authentication, certificates, [digital signatures](../07-security-domains/cryptography.md), and signed artifacts support authenticity.

## Accountability

Accountability means actions can be traced to responsible identities. Unique user accounts (see [Identity and Access Management](../07-security-domains/iam.md)), audit logs, approval workflows, and change records support accountability.

## Non-repudiation

Non-repudiation means a party cannot credibly deny an action or transaction. Digital signatures, tamper-resistant logs, timestamping, and strong identity controls may support this requirement.

## Practical example

A production database change should be linked to an approved change ticket, a named engineer, a privileged access session, and a timestamped log entry. This supports accountability and investigation.

## Common mistakes

- Shared administrator accounts
- Missing timestamps
- Weak log retention
- Uncontrolled service accounts
- Manual approvals without traceability

## Evidence

- identity and access management (IAM) records
- privileged session logs
- change tickets
- signed approvals
- audit logs


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
