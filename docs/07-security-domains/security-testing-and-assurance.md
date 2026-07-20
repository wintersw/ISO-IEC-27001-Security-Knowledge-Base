---
title: Security Testing and Assurance
description: Penetration testing, red teaming, and phishing simulation under ISO 27001.
category: Security Domains
difficulty: Advanced
reviewed_on: 2026-07-20
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Security Testing and Assurance

Security testing provides evidence that controls actually work, rather than assuming they do because they are documented. It ranges from automated vulnerability scanning to adversary simulation. Do not test a system without explicit authorization from an accountable owner, an agreed scope and rules of engagement, and review of applicable law, contract, safety, privacy, and provider policies.

## Types of security testing

- **Vulnerability scanning** — automated identification of known weaknesses across systems and applications. Frequent and broad, but shallow. See [Vulnerability Management](../11-checklists/vulnerability-management.md).
- **Penetration testing** — authorized, goal-oriented testing that exploits weaknesses to demonstrate real impact. Deeper but point-in-time.
- **Red teaming** — objective-based adversary simulation across people, process, and technology, testing detection and response as well as prevention.
- **Purple teaming** — red and blue (defensive) teams working together to improve detections in real time.
- **Bug bounty and vulnerability disclosure** — structured channels for external researchers to report weaknesses safely.

## A penetration testing methodology

A typical engagement follows recognized methodologies (for example, PTES, the OWASP testing guides, or NIST SP 800-115):

1. **Scoping and authorization** — define targets, rules of engagement, timing, and written approval.
2. **Reconnaissance** — gather information about the target.
3. **Scanning and enumeration** — identify services, versions, and weaknesses.
4. **Exploitation** — attempt to exploit weaknesses within scope.
5. **Post-exploitation** — assess the impact and potential for lateral movement.
6. **Reporting** — document findings, severity (for example, using CVSS), evidence, and remediation advice.
7. **Retesting** — confirm fixes after remediation.

## Phishing simulation

Simulated phishing tests workforce resilience and reinforces awareness training. Do it constructively:

- obtain management authorization and define objectives before running campaigns;
- avoid deceptive themes that damage trust (for example, fake bonuses or layoffs);
- measure and celebrate the report rate, not only the click rate; and
- route results into targeted training rather than punishment.

See [Email Security and Authentication](email-security-and-authentication.md) for the technical controls that complement awareness.

## Evidence

- authorization and rules-of-engagement records
- test reports with findings, severity, and evidence
- remediation tracking and retest results
- phishing simulation results and follow-up training
- trend of findings over time

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A A.8.8 (technical vulnerability management), A.8.29 (security testing in development and acceptance), A.6.3 (awareness), and Clause 9.1 (performance evaluation) drive testing. A.5.36 supports compliance review.
- **Implementation guidance:** Combine continuous scanning with periodic penetration testing of high-risk systems, feed findings into the [risk register](../05-risk-management/risk-register.md) and remediation tracking, and retest to confirm closure. Always secure written authorization first.
- **Best practice:** Test detection and response, not just prevention — purple-team exercises turn a point-in-time test into improved [security operations](security-operations-and-monitoring.md). Track time-to-remediate by severity as a program metric.

## Practical example

A company scans continuously, commissions an annual external penetration test of its customer platform, and runs a purple-team exercise where the SOC tunes detections against the tester's techniques. Findings are risk-rated, assigned owners, tracked to closure, and retested; quarterly phishing simulations feed targeted awareness training, and report rates are trended for management review.

## Common mistakes

- treating a vulnerability scan as a penetration test or a penetration test as complete assurance
- accepting a broad authorization that does not identify systems, techniques, data handling, stop conditions, and contacts
- testing production availability or social-engineering scenarios without business, safety, privacy, and human-resources safeguards
- closing findings from a ticket status without retesting the affected condition
- publishing sensitive exploit evidence more broadly or retaining it longer than needed

## Sources

- [NIST SP 800-115, Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [Penetration Testing Execution Standard](http://www.pentest-standard.org/)

## Related chapters

- [Application Security](application-security.md)
- [Security Operations and Monitoring](security-operations-and-monitoring.md)
- [Incident Response](incident-response.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
