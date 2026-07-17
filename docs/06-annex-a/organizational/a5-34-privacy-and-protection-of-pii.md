---
title: A.5.34 Privacy and protection of PII
description: Practical implementation, evidence, and audit guidance for A.5.34.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.34 Privacy and protection of PII

## Overview

Privacy and personally identifiable information protection require the organization to understand whose data it uses, for what purpose, under which obligations, and with which safeguards throughout the data lifecycle.

## Purpose

This control ensures that personally identifiable information (PII) is identified, and that privacy principles — purpose limitation, data minimization, transparency, access rights, and accountability — are applied throughout its lifecycle. Privacy is not a feature that can be bolted on; it must be designed into how data is collected, used, stored, and deleted.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.34 when selected or otherwise committed to.
- **Implementation guidance:** Define **privacy and protection of pii** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

Before adding call transcripts to analytics, the owner documents purpose and necessity, limits collected fields, assesses access and retention, informs affected parties where required, and tests deletion and rights-request handling.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- PII inventory is incomplete — only customer databases are considered while logs, backups, emails, and test data containing PII are ignored.
- Privacy notices are copied from a template without reflecting actual data practices.
- Data subject access and deletion requests are handled ad-hoc with no process, SLAs, or verification.
- Privacy impact assessments are performed only for new systems — changes to existing systems that increase PII exposure are not reassessed.

## Auditor questions

- How is PII identified and inventoried across systems, including logs, backups, and test environments?
- How are data subject rights (access, correction, deletion, portability) handled?
- When is a privacy impact assessment required, and who must approve it?
- Show evidence that privacy controls are tested and that PII handling matches the stated privacy notice.

## Checklist

- [ ] PII inventory maintained and reviewed
- [ ] privacy notice accurate and accessible
- [ ] data subject request handling process defined
- [ ] privacy impact assessment process documented
- [ ] PII minimization applied at collection
- [ ] privacy controls tested and verified

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
