---
title: Lab 8 — Design a Zero Trust Roadmap
description: Create a staged Zero Trust roadmap for a hybrid organization.
category: Guided Labs
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - lab
  - workshop
  - practical
---

# Lab 8 — Design a Zero Trust Roadmap

## Scenario

A hybrid organization uses Active Directory, cloud SaaS, VPN, unmanaged contractor devices, and broad internal network access. Critical systems include finance, customer support, and source code.

## Tasks

1. Define protect surfaces.
2. Map identities and devices.
3. Identify major trust assumptions.
4. Select first-year priorities.
5. Define metrics.
6. Identify exceptions.

## Suggested priorities

1. enforce MFA for privileged and remote access
2. centralize contractor identity
3. restrict unmanaged-device access
4. move critical applications from broad VPN to application-specific ZTNA
5. segment source-code and finance services
6. monitor sensitive data export
7. review service identities

## Suggested metrics

- critical applications covered by MFA
- unmanaged-device access blocked
- privileged accounts reviewed
- broad VPN entitlements removed
- lateral movement paths reduced
- policy exceptions open

## Review questions

- Is the roadmap risk-based?
- Does it protect data and applications, not only networks?
- Can progress be measured?
- Are operational teams involved?
