---
title: Confidentiality, Integrity, and Availability
description: The CIA triad and how security teams apply it.
category: Fundamentals
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - fundamentals
---

# Confidentiality, Integrity, and Availability

## Confidentiality

Information is accessible only to authorized entities. Typical safeguards include [identity management](../07-security-domains/iam.md), [access restriction](least-privilege.md), [encryption](../07-security-domains/cryptography.md), classification, secure transfer, and physical access control.

## Integrity

Information and processing remain accurate, complete, authentic where required, and protected from unauthorized or accidental change. Typical safeguards include change control, validation, digital signatures, version control, checksums, separation of duties, and audit logging.

## Availability

Information and supporting services are accessible when required by authorized users and processes. Typical safeguards include resilient architecture, capacity planning, tested backups, redundancy, [incident response](../07-security-domains/incident-response.md), and [business continuity](../07-security-domains/business-continuity.md).

## Balancing objectives

Controls can conflict. Very restrictive access may reduce operational availability; excessive availability may expose confidential data. Risk owners must approve an appropriate balance through [risk management](../05-risk-management/index.md).


## Practical example

An online retailer's customer order database requires all three CIA properties. Confidentiality: order data is encrypted at rest, access is restricted to authorized customer service and fulfillment roles, and database firewall rules limit network access. Integrity: all changes to order status are logged with the user ID and timestamp, and a daily reconciliation detects discrepancies between the order system and payment processor. Availability: the database runs in a multi-AZ configuration with automated failover, and backup restore is tested quarterly. When an operations engineer accidentally runs a destructive script during maintenance, integrity controls detect the anomaly within the reconciliation window, and availability controls enable point-in-time recovery within the RPO.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- documented design or risk decision
- implemented safeguard or configuration record
- test, review, or monitoring result showing the intended outcome


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
