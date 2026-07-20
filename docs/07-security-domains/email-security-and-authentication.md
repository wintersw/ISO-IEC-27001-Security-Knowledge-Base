---
title: Email Security and Authentication
description: SPF, DKIM, DMARC, anti-phishing, and email protection under ISO 27001.
category: Security Domains
difficulty: Intermediate
reviewed_on: 2026-07-20
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Email Security and Authentication

Email is a frequent channel for phishing, business email compromise (BEC), malicious links, and malware delivery. Email security combines domain authentication, transport protection, content controls, identity safeguards, and human reporting. Because email crosses organizational boundaries, it depends on interoperable internet standards.

## Domain authentication: SPF, DKIM, DMARC

These three DNS-based standards work together to reduce spoofing of your domain:

- **SPF (Sender Policy Framework)** lets a domain publish which systems may use it in the SMTP envelope identity. A receiver evaluates that identity; SPF does not by itself authenticate the address visible to a user in the `From` header.
- **DKIM (DomainKeys Identified Mail)** lets a signing domain take responsibility for selected message content with a verifiable signature. Forwarding or message modification can affect validation, and a valid signature alone does not establish that the visible sender is trustworthy.
- **DMARC (Domain-based Message Authentication, Reporting, and Conformance)** requires an authenticated SPF or DKIM domain to align with the visible `From` domain, publishes receiver policy (`none`, `quarantine`, or `reject`), and enables aggregate and optional failure reporting.

Deploy them in order: publish SPF and DKIM, monitor with a DMARC `p=none` policy, then tighten to `quarantine` and finally `reject` once legitimate senders are aligned.

Inventory every sending service and protect non-sending and parked domains too. Use the DMARC subdomain policy where appropriate. Authenticated Received Chain (ARC) can preserve authentication results through intermediaries such as mailing lists, but it does not replace DMARC. MTA-STS with TLS reporting can strengthen mail-transport policy; DANE is another option where DNSSEC deployment and mail-system support make it appropriate.

## Inbound protection

- gateway filtering for spam, malware, and known-malicious URLs
- attachment sandboxing and link rewriting/time-of-click checks
- impersonation and lookalike-domain detection
- external-sender banners and BEC/wire-fraud controls
- authentication of privileged requests through a second channel

## Anti-phishing and awareness

Technical controls reduce volume, but some phishing always arrives. Combine:

- easy one-click reporting for suspicious messages
- rapid triage and takedown of confirmed phishing
- targeted awareness training and simulated phishing (see [Security Testing and Assurance](security-testing-and-assurance.md))
- measurement of report rates, not just click rates

## Evidence

- published SPF, DKIM, and DMARC records and policy level
- DMARC aggregate report review
- gateway configuration and quarantine logs
- phishing report and response metrics
- awareness training and simulation results

## Common mistakes

- believing SPF validates the address that a person sees in the message header
- moving to enforcement before third-party senders and forwarded-mail paths are understood
- publishing one permissive SPF record with excessive includes or more than the allowed DNS lookups
- protecting only the primary domain while leaving parked and lookalike domains unmanaged
- treating DMARC as protection against compromised legitimate accounts or display-name impersonation

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Email touches A.8.23 (web filtering), A.8.20/A.8.21 (network and network-service security), A.5.14 (information transfer), A.6.3 (awareness and training), and A.5.24–A.5.28 (incident management).
- **Implementation guidance:** Enforce domain authentication for all sending domains (including parked and third-party senders), filter inbound mail, and integrate phishing reporting with [security operations](security-operations-and-monitoring.md) and [incident response](incident-response.md).
- **Best practice:** Move DMARC to an enforcing policy; a monitor-only record does not stop spoofing. Track the report rate as a positive signal of a security-aware workforce.

## Practical example

A company publishes SPF and DKIM for all sending domains, starts DMARC at `p=none`, and uses aggregate reports to find an unauthorized marketing platform. After aligning it, the team moves DMARC to `p=reject`, deploys a report button, and runs quarterly phishing simulations that feed targeted training.

## Related chapters

- [Security Operations and Monitoring](security-operations-and-monitoring.md)
- [Incident Response](incident-response.md)
- [Endpoint Security](endpoint-security.md)

## Sources

- [RFC 7208 — Sender Policy Framework](https://datatracker.ietf.org/doc/html/rfc7208)
- [RFC 6376 — DomainKeys Identified Mail](https://datatracker.ietf.org/doc/html/rfc6376)
- [RFC 7489 — DMARC](https://datatracker.ietf.org/doc/html/rfc7489)
- [RFC 8617 — Authenticated Received Chain](https://datatracker.ietf.org/doc/html/rfc8617)
- [RFC 8461 — MTA-STS](https://datatracker.ietf.org/doc/html/rfc8461)
- [RFC 8460 — SMTP TLS Reporting](https://datatracker.ietf.org/doc/html/rfc8460)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
