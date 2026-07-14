---
title: Endpoint Security
description: Endpoint security practices for user devices and servers.
category: Security Domains
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Endpoint Security

Endpoint security protects laptops, desktops, mobile devices, and servers.

## Core capabilities

- device inventory
- hardening
- EDR/XDR
- patching
- disk encryption
- local privilege restriction
- secure configuration
- remote wipe for mobile devices

## Best practices

- Enroll endpoints in management.
- Enforce baseline configuration.
- Monitor endpoint health.
- Restrict local admin rights.
- Include endpoints in vulnerability management.
- Define lost-device response.

## Evidence

- MDM/EDR inventory
- compliance reports
- encryption reports
- patch reports
- incident tickets

## Detailed implementation guidance

Endpoints are where users access data, identities, cloud services, and business applications. Endpoint security should balance prevention, detection, usability, remote work, and recovery.

### Example

A managed laptop baseline requires encryption, EDR, supported operating system, automatic patching, screen lock, restricted local administration, secure browser configuration, and remote-wipe capability. Conditional access blocks non-compliant devices from restricted data.

### Best practices

- maintain endpoint ownership and inventory
- define secure configuration baselines
- use full-disk encryption
- deploy EDR and verify coverage
- remove unnecessary local privilege
- patch operating systems and applications
- control removable media
- enforce device posture
- protect remote administration
- define lost-device response
- monitor exceptions

### Common weaknesses

Coverage reports may omit unmanaged devices, EDR agents may be unhealthy, and encrypted devices may still expose active sessions or cached data.

## Related chapters

- [Device Trust and Endpoint Posture](../27-zero-trust-and-data-centric-security/device-trust-and-endpoint-posture.md)
- [Remote Work Data Security](../29-emerging-data-security-trends/remote-work-data-security.md)
