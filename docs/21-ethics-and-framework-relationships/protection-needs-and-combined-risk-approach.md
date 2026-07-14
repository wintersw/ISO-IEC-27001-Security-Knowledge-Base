---
title: Protection Needs and Combined Risk Approach
description: Generic protection-needs analysis and combined baseline/detailed risk approach.
category: Ethics and Framework Relationships
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
  - ISO/IEC 27000 family
tags:
  - ethics
  - standards
  - isms
---

# Protection Needs and Combined Risk Approach

The German paper demonstrates a useful implementation pattern: determine protection needs first, then decide whether baseline controls are enough or whether detailed risk analysis is required.

## Protection-needs categories

A simple model can use:

| Level | Meaning |
|---|---|
| Normal | Harm is limited and manageable |
| High | Significant business, legal, customer, or operational impact |
| Very high | Severe, existential, safety, regulatory, or major trust impact |

## Assessment dimensions

- confidentiality
- integrity
- availability
- privacy relevance
- misuse potential
- legal or contractual impact
- reputational impact

## Inheritance rules

Protection needs often propagate:

- applications influence systems
- systems influence rooms or cloud environments
- dependencies influence connected systems
- communication links inherit data and availability requirements
- cumulative low risks can create higher overall risk

## Combined approach

| Situation | Recommended analysis |
|---|---|
| Normal protection needs | baseline control set may be sufficient |
| High protection needs | baseline plus targeted risk assessment |
| Very high protection needs | detailed risk analysis and enhanced assurance |

## Evidence

- protection-needs analysis
- dependency map
- data flow diagram
- risk register
- control selection rationale
- SoA updates
