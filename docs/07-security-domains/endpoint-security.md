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

## Best practices

- Enroll endpoints in management.
- Enforce baseline configuration.
- Monitor endpoint health.
- Restrict local administrator rights.
- Include endpoints in vulnerability management.
- Define lost-device response.

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

- **ISO requirement:** This chapter explains **Endpoint Security** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Practical example

A growing software-as-a-service provider applies this guidance to a new customer-data feature. The service owner identifies the relevant risks, implements proportionate safeguards, and verifies them before release and during operation.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
