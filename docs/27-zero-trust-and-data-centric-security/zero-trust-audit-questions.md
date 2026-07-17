---
title: Zero Trust Audit Questions
description: Audit questions for Zero Trust implementation and assurance.
category: Zero Trust and Data-Centric Security
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - zero-trust
  - audit
---

# Zero Trust Audit Questions

## Governance

- Is there a Zero Trust roadmap?
- Are protect surfaces defined?
- Are policies risk-based?
- Are exceptions time-limited and approved?

## Identity

- Is multifactor authentication (MFA) enforced for critical access?
- Are privileged identities reviewed?
- Are service identities owned and rotated?

## Device

- Is device posture evaluated?
- Are unmanaged devices restricted?

## Data

- Are sensitive data access attempts logged?
- Are downloads and exports monitored?
- Are data loss prevention (DLP) rules risk-based?

## Monitoring

- Are Zero Trust events integrated into security information and event management (SIEM)?
- Are policy violations reviewed?
- Are metrics reported to management?

## Typical evidence

- Zero Trust roadmap and defined protect surfaces
- MFA and privileged access review records sampled during the audit
- device posture and unmanaged-device restriction policies with enforcement logs
- sensitive data access, download, and DLP monitoring reports
- time-limited exception approvals and management metric reports

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

An internal auditor uses these questions in an ISMS audit and finds MFA enforced everywhere except six "temporary" service exceptions that are two years old and owned by nobody. The finding is raised as a nonconformity, exceptions get owners and expiry dates, and the exception register becomes a standing item in the quarterly security review.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
