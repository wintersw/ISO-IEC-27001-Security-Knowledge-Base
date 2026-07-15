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
- endpoint detection and response (EDR)/extended detection and response (XDR)
- patching
- disk encryption
- local privilege restriction
- secure configuration
- remote wipe for mobile devices


## Evidence

- mobile device management (MDM)/EDR inventory
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

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Endpoint security is addressed through Annex A control A.8.1 (user endpoint devices), supported by physical controls A.7.7 (clear desk and clear screen), A.7.8 (equipment siting and protection), and A.7.9 (security of assets off-premises). The organisation must define and enforce a security baseline for all endpoint devices that access information assets.
- **Implementation guidance:** Define the endpoint security baseline (disk encryption, screen lock, minimum OS version, endpoint detection, patch compliance), enforce it through MDM or equivalent tooling, and monitor endpoint compliance continuously.
- **Best practice:** Treat endpoint compliance as a precondition for access, not a post-connection check. Non-compliant devices should be quarantined or denied access to corporate resources automatically.

## Practical example

The organisation rolls out a mobile-device-management profile for company laptops. The team defines the minimum OS version, enforces disk encryption and screen lock, deploys endpoint detection, and verifies compliance through a dashboard before allowing access to corporate resources.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
