---
title: Secure by Default
description: How to design default configurations that reduce customer risk.
category: Secure by Design
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - secure-by-design
  - product-security
  - devsecops
---

# Secure by Default

Secure by default means that a product starts in a reasonably protected state without requiring extensive customer configuration.

## Example: cloud storage

An insecure product may create storage that is publicly accessible unless the customer changes permissions. A secure-by-default product blocks public access, warns clearly before exposure, logs changes, and allows policy-level prevention.

## Example: administrative access

A secure product should not ship with shared administrator credentials. It should require unique identity, strong authentication, controlled recovery, and audit logging.

## Design checklist

- strong authentication
- least privilege
- secure network exposure
- logging enabled
- encryption enabled
- safe session settings
- secure API configuration
- automatic updates
- recovery controls
- visible warnings for risky changes

## Common mistakes

- marketing “secure by default” while leaving key controls optional
- providing logs only in expensive tiers
- relying on customers to disable legacy protocols
- shipping broad roles for convenience
- making secure configuration operationally difficult
