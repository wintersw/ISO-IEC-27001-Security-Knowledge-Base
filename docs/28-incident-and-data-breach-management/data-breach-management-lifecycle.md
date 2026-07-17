---
title: Data Breach Management Lifecycle
description: Detailed breach lifecycle for readiness, investigation, notification, documentation, and improvement.
category: Incident and Data Breach Management
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - breach-lifecycle
---

# Data Breach Management Lifecycle

## Step 1 — Readiness

Define breach roles, notification decision process, evidence sources, legal/privacy escalation, and breach register.

## Step 2 — Identify

Determine whether data was accessed, disclosed, altered, lost, destroyed, or made unavailable.

## Step 3 — Investigate

Establish what happened, how it happened, what data was involved, who was affected, and whether the breach is ongoing.

## Step 4 — Respond

Contain the breach, stop data exposure, restore controls, and reduce impact.

## Step 5 — Preserve evidence

Preserve logs, images, system records, communications, and decision records.

## Step 6 — Notify and escalate

Use a jurisdiction-neutral decision record and obtain legal/privacy review.

## Step 7 — Document

Maintain a complete breach record.

## Step 8 — Improve

Update risks, controls, policies, training, monitoring, and supplier requirements.

## Typical evidence

- documented breach roles, escalation paths, and notification decision process
- investigation records showing what data was involved and who was affected
- containment and recovery action logs
- preserved evidence with chain-of-custody records
- breach register entries and post-breach improvement actions

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

An attacker abuses a leaked API key to pull customer records over three weeks. The team walks the lifecycle: readiness materials identify the log sources, investigation scopes which records were accessed, response revokes the key and rotates secrets, evidence is preserved with hashes, the jurisdiction-neutral decision record supports notification review, and improvement adds API-key expiry plus anomaly alerts on bulk reads.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
