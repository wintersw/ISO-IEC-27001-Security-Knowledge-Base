---
title: Network Security
description: Network security concepts and ISO 27001 implementation guidance.
category: Security Domains
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Network Security

Network security protects communication paths, boundaries, and network-access patterns.

## Core capabilities

- network segmentation
- firewall policy management
- secure remote access
- network service control
- Domain Name System (DNS) security
- ingress/egress filtering
- network monitoring
- secure network architecture
- denial-of-service resilience


## Evidence

- network diagrams
- firewall rule reviews
- remote access logs
- segmentation design
- change records

## Detailed implementation guidance

Network security controls communication paths, trust boundaries, exposure, segmentation, and monitoring. Modern network security should not assume that internal location equals trust.

### Segmentation example

A critical database is reachable from broad internal networks. The organization maps required application flows, limits access to approved workloads and administration paths, logs denied connections, and verifies that emergency support access is controlled.

### Best practices

- map data and service flows
- segment by risk and function
- restrict administration paths
- use secure protocols
- protect DNS and remote access
- monitor east-west traffic
- review firewall and security-group rules
- use application-specific access where possible
- document exceptions and expiry
- test containment

### Common weaknesses

Rules accumulate without owners, broad “any” access remains, temporary rules never expire, and segmentation is documented but not verified.

## Availability and denial-of-service resilience

A network can enforce access correctly and still fail when legitimate demand, malicious traffic, or a dependency overloads a constrained component. Treat distributed denial-of-service (DDoS) protection as a service-resilience problem, not only as a firewall feature.

For internet-facing services:

- identify externally reachable domains, addresses, interfaces, and upstream dependencies;
- estimate normal demand, credible peaks, bottlenecks, and business impact;
- decide where traffic can be absorbed, filtered, rate-limited, queued, degraded safely, or failed over;
- protect origin systems so that an intermediary cannot simply be bypassed;
- define provider contacts, escalation thresholds, communications, and recovery authority;
- exercise the response using safe load tests or tabletop scenarios; and
- retain capacity trends, architecture decisions, provider commitments, alert records, exercise results, and improvement actions.

### Denial-of-service resilience example

A small online retailer cannot fund multiple data centres. It uses a managed edge service, restricts direct access to the application origin, rate-limits expensive requests, defines a read-only degraded mode, and tests the provider escalation path before its seasonal sales event. This is proportionate resilience; it does not imply that every traffic surge can be prevented.

## Related chapters

- [Microsegmentation and Network Control](../27-zero-trust-and-data-centric-security/microsegmentation-and-network-control.md)
- [Application Access and secure access service edge (SASE)](../27-zero-trust-and-data-centric-security/application-access-and-sase.md)
- [Business Continuity](business-continuity.md)

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Network security is addressed through Annex A controls A.8.20 (networks security), A.8.21 (security of network services), A.8.22 (segregation of networks), and A.8.23 (web filtering). The organisation must manage network security through defined controls that protect information in transit and restrict network access to authorised devices and services.
- **Implementation guidance:** Define network zones based on data classification and risk, implement segregation through firewalls or SDN, manage firewall rules through a documented change process, and monitor network traffic for anomalies.
- **Best practice:** Every firewall allow rule should reference a documented business justification and an expiry or review date. Rules without justification accumulate over time and become a significant audit finding.

## Practical example

The network team segments the cardholder data environment from the corporate LAN. Firewall rules are defined from a deny-all baseline, each allow rule is linked to a documented business justification, rule changes follow the change-management process, and the configuration is reviewed quarterly.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
