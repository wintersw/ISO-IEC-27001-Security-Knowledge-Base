---
title: Zero Trust Monitoring and Metrics
description: Measuring Zero Trust implementation and effectiveness.
category: Zero Trust and Data-Centric Security
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - zero-trust
  - metrics
---

# Zero Trust Monitoring and Metrics

Zero Trust should be measured by outcomes, not tool deployment alone.

## Suggested metrics

| Metric | Purpose |
|---|---|
| multifactor authentication (MFA) coverage for critical apps | identity control coverage |
| unmanaged-device access blocked | enforcement strength |
| privileged sessions monitored | sensitive activity visibility |
| policy exceptions open | risk exposure |
| lateral movement paths reduced | attack surface reduction |
| high-risk access denied | policy effectiveness |
| sensitive data downloads by role | behavioral monitoring |
| time to revoke access | identity lifecycle performance |

## Dashboard view

Group metrics by identity, device, network, application, data, monitoring, and exceptions.

## Typical evidence

- Zero Trust metric dashboard grouped by identity, device, network, application, and data
- MFA and EDR coverage reports with trend history
- open policy-exception counts and aging reports
- blocked high-risk access and unmanaged-device statistics
- management review records showing metric-driven decisions

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

A security team reports "Zero Trust is deployed" but the metrics tell a sharper story: MFA coverage on critical apps is 98%, yet 40 open policy exceptions bypass device checks and the median time to revoke leaver access is nine days. Management uses the dashboard to fund identity-lifecycle automation — a decision driven by outcome metrics rather than tool inventory.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
