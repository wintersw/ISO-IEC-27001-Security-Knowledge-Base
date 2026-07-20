---
title: Security Operations and Monitoring
description: SOC, SIEM, detection engineering, and threat hunting within an ISO 27001 ISMS.
category: Security Domains
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Security Operations and Monitoring

Security operations is the ongoing capability to detect, investigate, and respond to security events. It turns the logging and monitoring controls of ISO/IEC 27001 into an operating function. The security operations center (SOC) — whether an internal team, a managed security service provider (MSSP), or a hybrid — is where detection meets response.

## Building blocks

- **Log collection and normalization.** Sources include endpoints, identity providers, network devices, cloud platforms, and applications.
- **SIEM (security information and event management).** Aggregates and correlates events, runs detection rules, and stores logs for investigation and retention.
- **SOAR (security orchestration, automation, and response).** Automates repeatable response steps such as enrichment, ticketing, and containment.
- **EDR/XDR.** Endpoint and cross-domain detection and response telemetry feeding the SOC.
- **Threat intelligence.** Context on adversary tactics that informs detections and prioritization.

## Detection engineering

Detection engineering treats detections as maintained products, not one-off alerts:

- Map coverage to adversary behavior using [MITRE ATT&CK](https://attack.mitre.org/) rather than only to indicators of compromise.
- Write detections with a clear hypothesis, data source, and expected true/false positives.
- Version-control detection rules and test them against known-good and known-bad data.
- Measure and tune false-positive rates so analysts are not overwhelmed.
- Track detection coverage gaps as risks.

## Threat hunting

Threat hunting is the proactive search for undetected compromise, guided by hypotheses (for example, "an attacker is abusing valid accounts for lateral movement"). Findings feed new detections and close coverage gaps.

## Key metrics

- mean time to detect (MTTD) and mean time to respond (MTTR)
- alert volume, true-positive rate, and false-positive rate
- detection coverage against prioritized ATT&CK techniques
- log source health and coverage
- percentage of incidents found by monitoring versus reported externally

## Evidence

- log source inventory and coverage report
- detection rule repository with change history
- alert triage and investigation records
- tuning decisions and suppression rationale
- SOC shift handover and on-call records

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A A.8.15 (logging) and A.8.16 (monitoring activities) require logging and monitoring; A.5.7 (threat intelligence) and A.5.24–A.5.28 (incident management) connect detection to response. Clause 9.1 requires evaluation of security performance.
- **Implementation guidance:** Define which sources must be logged, retention periods, and what "monitored" means for each. Establish alert triage severities, escalation paths, and hand-off to [incident response](incident-response.md). Protect log integrity and restrict administrator access to logging systems.
- **Best practice:** Measure detection coverage against a threat model, not just alert counts. A SIEM full of unused logs and untuned rules provides little assurance; a smaller, well-mapped detection set is more effective.

## Practical example

A mid-sized company ships identity, endpoint, and cloud logs to a SIEM, defines a starter set of ATT&CK-aligned detections for credential abuse, and integrates a SOAR playbook that enriches alerts and opens incident cases automatically. Monthly, the team reviews false-positive rates, retires noisy rules, and reports MTTD/MTTR to management review.

## Related chapters

- [Incident Response](incident-response.md)
- [Endpoint Security](endpoint-security.md)
- [Network Security](network-security.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
