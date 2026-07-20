---
title: Identity Federation and Single Sign-On
description: OAuth 2.0, OpenID Connect, SAML, and SSO within an ISO 27001 ISMS.
category: Security Domains
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Identity Federation and Single Sign-On

Federation lets users authenticate once with a trusted identity provider (IdP) and access many applications (relying parties or service providers) without separate credentials. Single sign-on (SSO) is the user-facing result. Federation concentrates authentication into a well-protected system, but it also concentrates risk: the IdP becomes a high-value target.

## The core protocols

- **SAML 2.0** — an XML-based standard, widely used for enterprise web SSO. The IdP issues a signed assertion that the application trusts.
- **OAuth 2.0** — an authorization framework. It lets an application obtain delegated access (tokens) to resources without receiving the user's password. OAuth is about authorization, not authentication.
- **OpenID Connect (OIDC)** — an identity layer built on OAuth 2.0 that adds authentication and an ID token, now the common choice for modern web and mobile apps.
- **SCIM** — complements these by automating provisioning and deprovisioning of accounts between the IdP and applications.

A frequent mistake is using OAuth alone for login; use OIDC when you need to authenticate a user.

## How federation fits together

1. The user requests an application (relying party).
2. The application redirects to the IdP.
3. The IdP authenticates the user (ideally with phishing-resistant MFA).
4. The IdP issues a signed assertion or token.
5. The application validates the signature, issuer, audience, and expiry, then grants access.

## Security considerations

- Protect the IdP as a tier-0 system with strong administrative controls.
- Enforce MFA at the IdP, preferably phishing-resistant (FIDO2/passkeys).
- Validate token signature, issuer, audience, expiry, and nonce; reject unsigned or `alg:none` tokens.
- Use short token lifetimes and secure refresh-token handling.
- Automate joiner/mover/leaver through SCIM so deprovisioning is immediate.
- Log authentication events centrally and monitor for anomalies.

## Evidence

- federation trust configuration and certificate/key rotation records
- MFA enforcement policy and coverage
- token validation and session-timeout settings
- provisioning/deprovisioning (SCIM) records
- IdP administrative access reviews and logs

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Federation supports A.5.15–A.5.18 (access control, identity, authentication information, access rights) and A.8.2–A.8.5 (privileged access, restriction, secure authentication). See [Identity and Access Management](iam.md).
- **Implementation guidance:** Centralize authentication on a hardened IdP, enforce MFA, integrate applications through OIDC or SAML rather than local passwords, and automate lifecycle with SCIM. Treat federation trust certificates as managed keys — see [Key Management](key-management.md).
- **Best practice:** Prefer phishing-resistant MFA at the IdP and eliminate application-local passwords. Because SSO widens blast radius, invest proportionally in monitoring and rapid session revocation.

## Practical example

A company connects its SaaS applications to a single IdP using OIDC, enforces passkey-based MFA, and provisions accounts through SCIM tied to the HR joiner/leaver process. When an employee leaves, disabling the IdP account removes access to every connected application, and the deprovisioning event is logged for the access review.

## Related chapters

- [Identity and Access Management](iam.md)
- [Zero Trust](../01-fundamentals/zero-trust.md)
- [Key Management](key-management.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
