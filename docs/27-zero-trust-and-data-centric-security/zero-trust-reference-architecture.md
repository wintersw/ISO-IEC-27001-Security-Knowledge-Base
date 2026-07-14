---
title: Zero Trust Reference Architecture
description: Reference architecture for identity, device, network, application, data, and monitoring controls.
category: Zero Trust and Data-Centric Security
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - zero-trust
  - architecture
---

# Zero Trust Reference Architecture

## Logical components

```mermaid
flowchart TD
    U[User / Service Identity] --> PEP[Policy Enforcement Point]
    D[Device Posture] --> PEP
    C[Context and Risk Signals] --> PDP[Policy Decision Point]
    P[Policy Store] --> PDP
    R[Resource / Data] --> PEP
    PDP --> PEP
    PEP --> R
    PEP --> L[Logs and Monitoring]
    L --> A[Analytics and Improvement]
```

## Control domains

| Domain | Example controls |
|---|---|
| identity | MFA, identity governance, conditional access |
| device | endpoint compliance, EDR, patch posture |
| network | segmentation, encrypted transport, ZTNA |
| application | access proxy, API authorization |
| data | classification, DLP, masking, encryption |
| monitoring | SIEM, UEBA, alert triage, control metrics |
| governance | roadmap, risk register, exceptions |


## Typical evidence

- approved policy, standard, procedure, or architecture record
- risk assessment or design review
- owner and role assignment
- implementation plan
- operating records
- monitoring records
- exception or waiver decisions
- test results
- audit records
- management review decisions

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)
