---
title: Threat Modeling
description: A practical, repeatable method for identifying abuse paths and selecting security requirements before implementation.
category: Secure by Design
difficulty: Intermediate
reviewed_on: 2026-07-20
applies_to:
  - ISO/IEC 27001:2022
tags:
  - secure-by-design
  - threat-modeling
---

# Threat Modeling

Threat modeling is a structured conversation about what is being built, what must be protected, how it can be misused, and what will reduce the risk. It turns architecture and abuse cases into traceable security requirements early enough to influence design.

## Repeatable method

1. Define the decision, scope, assumptions, users, assets, trust boundaries, dependencies, and data flows.
2. Describe intended use and credible misuse or failure scenarios. Include malicious, accidental, supply-chain, privacy, safety, and availability impacts where relevant.
3. Identify threats systematically. STRIDE, attack trees, MITRE ATT&CK, privacy frameworks, or domain-specific methods can prompt analysis; none is a complete checklist.
4. Evaluate likelihood and consequence using the organization's risk method and existing controls.
5. Select design changes, preventive and detective controls, tests, owners, and due dates. Prefer removing a risky path over adding downstream monitoring.
6. Record accepted assumptions and residual risk, then review after architectural, exposure, dependency, or threat changes.

Keep the model proportionate. A whiteboard and short decision record may be enough for a small change; a safety-critical or internet-facing system may need formal diagrams, attack trees, and specialist review.

## Evidence and integration

Evidence includes scoped diagrams, assumptions, threat and abuse cases, linked requirements, control decisions, test results, exceptions, and review history. Link threats to the risk register, backlog, architecture decisions, security tests, and incident lessons.

## Practical example

A team modeling a document-sharing service identifies a trust boundary between public links and authenticated access. It adds expiring scoped tokens, download logging, rate limits, malware scanning, and a test that proves a revoked link cannot be reused.

## Common mistakes

- drawing a diagram without converting findings into owned requirements
- modeling only external attackers and ignoring mistakes, dependencies, and privileged misuse
- rating threats without the organization's business and safety context
- treating a one-time workshop as valid after the architecture changes

## Sources

- [NIST SP 800-154, Guide to Data-Centric System Threat Modeling](https://csrc.nist.gov/pubs/sp/800/154/ipd)
- [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)
- [MITRE ATT&CK](https://attack.mitre.org/)

## Related chapters

- [Security by Design](../01-fundamentals/security-by-design.md)
- [Application Security](../07-security-domains/application-security.md)
- [Secure by Design Principles](secure-by-design-principles.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
