---
title: A.5.11 Return of assets
description: Practical implementation, evidence, and audit guidance for A.5.11.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.11 Return of assets

## Overview

When employment, a contract, or an assignment ends, organizational assets and information must be returned or otherwise accounted for. The process should cover physical items, copies, credentials, records, and assets held by third parties.

## Purpose

This control ensures that all organizational assets — physical devices, information, credentials, and access — are returned or accounted for when personnel, contractors, or third parties end their engagement. Unreturned assets represent a persistent data leakage and access risk that outlives the working relationship.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.11 when selected or otherwise committed to.
- **Implementation guidance:** Define **return of assets** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

At a contractor's final handover, the manager reconciles assigned equipment and documents, revokes remote access, transfers owned service accounts, records one missing token, and follows the loss procedure before closing the offboarding task.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Offboarding focuses on HR paperwork but neglects asset return — laptops, tokens, and access cards are never collected.
- Digital assets (files, credentials, certificates, cloud access) are overlooked while physical assets are tracked.
- No inventory exists of what was issued, so it is impossible to confirm that everything has been returned.
- Contractors and third parties are excluded from the asset return process.

## Auditor questions

- What is the process for ensuring all assets are returned when someone leaves?
- How are digital assets, credentials, and access rights addressed during offboarding?
- How are lost or unreturned assets handled — is there an investigation and risk assessment?
- Show evidence from recent departures that asset return was completed and verified.

## Checklist

- [ ] asset issuance recorded at onboarding
- [ ] asset return process defined and triggered at offboarding
- [ ] digital assets and credentials included in return scope
- [ ] contractors and third parties included in return process
- [ ] lost/unreturned asset procedure defined
- [ ] return verification evidence retained

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
