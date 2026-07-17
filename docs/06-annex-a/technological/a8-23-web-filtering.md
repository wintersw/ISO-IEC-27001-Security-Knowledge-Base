---
title: A.8.23 Web filtering
description: Practical implementation, evidence, and audit guidance for A.8.23.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.23 Web filtering

## Overview

Web filtering reduces exposure to malicious or prohibited destinations while supporting legitimate work. Decisions should use risk, category, reputation, context, exceptions, privacy, logging, and response rather than opaque blanket blocking.

## Purpose

This control ensures that access to external websites is managed to reduce exposure to malicious, inappropriate, or prohibited content while enabling legitimate business use. Web filtering is a frontline defense against phishing sites, malware delivery, and command-and-control channels.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.23 when selected or otherwise committed to.
- **Implementation guidance:** Define **web filtering** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A newly registered domain hosting a credential-harvesting page is blocked across managed devices. A business exception requires owner approval and isolation, while detections are correlated with sign-in activity and investigated.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Filtering is configured as blanket allow-all or block-all without risk-based category decisions.
- Encrypted traffic (HTTPS) is not inspected — malware and phishing sites delivered over TLS bypass filtering entirely.
- There is no exception process — business-critical sites are blocked with no path to request access.
- Filtering is applied only on the corporate network — remote or mobile devices operate without web protection.

## Auditor questions

- What categories of websites are blocked, and how were those decisions made?
- How is encrypted (HTTPS) traffic handled by the web filtering solution?
- How are web filtering exceptions requested, approved, and periodically reviewed?
- Show evidence that web filtering is active and that blocked access attempts are logged and reviewed.

## Checklist

- [ ] web filtering categories defined based on risk assessment
- [ ] HTTPS inspection configured where appropriate
- [ ] filtering applied consistently across on-premises and remote endpoints
- [ ] exception process documented with approval and review
- [ ] blocked-access logs reviewed for patterns and incidents
- [ ] filtering rules reviewed and updated regularly

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
