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

## Best practices

- Segment critical environments.
- Restrict management interfaces.
- Review firewall rules periodically.
- Document network zones.
- Monitor high-risk network flows.
- Remove unused rules.

## Evidence

- network diagrams
- firewall rule reviews
- remote access logs
- segmentation design
- change records

## Detailed implementation guidance

Network security controls communication paths, trust boundaries, exposure, segmentation, and monitoring. Modern network security should not assume that internal location equals trust.

### Example

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

### Example

A small online retailer cannot fund multiple data centres. It uses a managed edge service, restricts direct access to the application origin, rate-limits expensive requests, defines a read-only degraded mode, and tests the provider escalation path before its seasonal sales event. This is proportionate resilience; it does not imply that every traffic surge can be prevented.

## Related chapters

- [Microsegmentation and Network Control](../27-zero-trust-and-data-centric-security/microsegmentation-and-network-control.md)
- [Application Access and secure access service edge (SASE)](../27-zero-trust-and-data-centric-security/application-access-and-sase.md)
- [Business Continuity](business-continuity.md)

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **Network Security** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Practical example

A growing software-as-a-service provider applies this guidance to a new customer-data feature. The service owner identifies the relevant risks, implements proportionate safeguards, and verifies them before release and during operation.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
