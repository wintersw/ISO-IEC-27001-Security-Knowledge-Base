---
title: A.8.12 Data leakage prevention
description: Practical implementation, evidence, and audit guidance for A.8.12.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.12 Data leakage prevention

## Overview

Data leakage prevention aims to detect or stop unauthorized movement of sensitive information across endpoints, messages, networks, cloud services, and removable media. Rules require accurate scope, context, response, and privacy-aware tuning.

## Purpose

This control ensures that measures are in place to detect and prevent unauthorized disclosure or extraction of sensitive information through endpoints, networks, email, cloud services, and removable media. DLP is not a single tool but a layered capability combining detection rules, user awareness, and response workflows.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.12 when selected or otherwise committed to.
- **Implementation guidance:** Define **data leakage prevention** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

This control identifies sensitive information and applies proportionate measures to detect or prevent unauthorized disclosure or extraction. Coverage should reflect information classification, approved transfer paths, user and service behaviour, privacy requirements, exception handling, and tested response workflows.

### Measures that support decisions

- sensitive repositories and transfer channels covered by approved rules
- confirmed leakage events and high-risk attempts by channel
- false-positive rate and rules overdue for tuning
- blocked or alerted events resolved within target

## Practical example

A rule detects a bulk export of classified customer records to an unapproved file-sharing service. The transfer is blocked, the user receives guidance, an analyst validates intent, and recurring false positives are tuned with owner approval.

## Evidence to retain

- sensitive-information and channel coverage record
- approved detection or blocking rules and test results
- leakage alerts, analyst decisions, and response records
- business exceptions with owner, safeguards, and expiry
- tuning changes, coverage gaps, and corrective actions

## Common mistakes

- DLP is deployed in monitor-only mode indefinitely — alerts are generated but never reviewed or acted upon.
- Rules are overly broad, generating excessive false positives that cause alert fatigue and ignored incidents.
- Coverage is limited to email while other channels (USB, web uploads, cloud sync, print) are unmonitored.
- Sensitive data is not classified or tagged, so DLP rules rely on fragile pattern matching that misses unstructured data.

## Auditor questions

- What channels are covered by DLP controls, and how was the scope determined?
- How are DLP alerts triaged, investigated, and resolved — and what is the mean time to respond?
- How are false positives tuned, and how often are rules reviewed for effectiveness?
- Show evidence that DLP incidents are escalated appropriately and that repeat offenders are addressed.

## Checklist

- [ ] sensitive data identified and classified for DLP rule creation
- [ ] DLP coverage defined across email, endpoint, network, and cloud channels
- [ ] alert triage and response process documented
- [ ] false-positive tuning performed regularly
- [ ] DLP rules reviewed and updated on a defined cadence
- [ ] DLP incident metrics tracked and reported

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
