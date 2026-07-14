---
title: Configuration Baselines and Drift
description: How ITSM configuration management supports secure configuration and drift control.
category: IT Governance and ITSM
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - it-governance
  - itsm
  - cobit
  - itil
---

# Configuration Baselines and Drift

A configuration baseline defines the approved state of a system or service. Drift occurs when actual configuration moves away from that state.

## Example

A cloud storage baseline requires encryption, logging, restricted public access, approved regions, and owner tags. Continuous checks detect a storage bucket created without logging.

The issue is not merely a technical alert. The workflow should:

1. identify the owner
2. assess exposure
3. correct configuration
4. preserve evidence
5. determine why preventive controls failed
6. improve templates or policy enforcement

## Best practices

- Define baselines by technology and risk tier.
- Automate detection where possible.
- Link drift findings to change records.
- distinguish approved exceptions from unauthorized drift.
- track recurring baseline violations.
- include cloud, network, endpoint, database, and identity configuration.
