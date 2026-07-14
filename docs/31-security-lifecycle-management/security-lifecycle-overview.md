---
title: Security Lifecycle Overview
description: Explains the common lifecycle pattern used across security domains.
category: Security Lifecycle Management
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-lifecycle
  - isms
---

# Security Lifecycle Overview

Most security activities follow a common lifecycle. The details vary, but the management pattern is consistent.

## The common lifecycle pattern

1. **Identify** a new asset, system, supplier, risk, vulnerability, change, or obligation.
2. **Assess** ownership, business impact, legal requirements, risk, and dependencies.
3. **Design** security requirements, controls, evidence, and monitoring.
4. **Implement** controls and communicate responsibilities.
5. **Operate** the control or process as part of normal work.
6. **Monitor** events, metrics, exceptions, and control performance.
7. **Assure** through testing, internal audit, self-assessment, or management review.
8. **Improve or retire** based on lessons learned, changing context, or end-of-life.

## Example

A department wants to use a new analytics data set. The lifecycle starts before the dataset exists in production. The data owner classifies it, security reviews access and transfer requirements, privacy reviews personal data use, and the ISMS team links the dataset to the risk register and evidence register. During operation, access reviews and export logs are monitored. At retirement, the dataset is deleted or archived according to retention rules.

## Common mistakes

- Treating go-live as the end of security work.
- Missing the mover phase of identity lifecycle.
- Keeping old suppliers, data sets, service accounts, and firewall rules indefinitely.
- Collecting evidence only before audits.
- Running controls without measuring whether they still reduce risk.
