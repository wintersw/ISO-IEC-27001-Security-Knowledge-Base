---
title: AI Risk Landscape
description: Organisational risk categories introduced by AI systems and the distinction between attacks on AI and attacks using AI.
category: AI Governance and Security
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - AI
  - risk
  - bias
  - deepfakes
---

# AI Risk Landscape

AI systems introduce risks that are different in character from traditional IT risks. Understanding these categories helps an organisation decide what belongs in the risk register, what controls apply, and where governance attention is most needed.

## Risk categories

### Privacy misuse

AI systems consume vast amounts of data. Without controls, they can collect, retain, or repurpose personal data in ways the data subjects never consented to. Training data may contain personal information that the model later reveals through its outputs (memorisation). Biometric data, health records, and behavioural profiles are especially sensitive. Even anonymised datasets can sometimes be re-identified when combined with other data.

### Bias and unfair outcomes

Machine learning models learn from historical data. If that data reflects existing societal or organisational biases, the model will reproduce and potentially amplify them. A hiring model trained on past hiring decisions may discriminate against certain groups. A credit-scoring model may systematically disadvantage applicants from specific postcodes. Unlike human bias, algorithmic bias scales instantly and invisibly across every decision the model makes.

### Deepfakes and disinformation

AI-generated audio, video, and images can now be indistinguishable from authentic recordings. This creates risks of impersonation, fabricated evidence, reputational damage, and social engineering at a scale not previously possible. A deepfake of a senior executive giving fraudulent instructions could bypass controls that rely on voice or video verification.

### AI-enabled cybercrime

Attackers use AI to increase the speed, scale, and sophistication of their operations. Examples include: AI-generated phishing emails that adapt to the target's writing style, automated vulnerability discovery, intelligent credential-stuffing, and malware that modifies its behaviour to evade detection. AI also lowers the skill barrier: tools that once required expertise are becoming accessible to less-capable adversaries.

### Unintended misuse

Even well-intentioned deployment can produce harmful outcomes. A conversational AI chatbot deployed without adequate content filters may generate offensive or dangerous responses (the Microsoft Tay incident illustrates this risk). An AI system used in recruitment or benefits decisions may make consequential errors if users over-trust its outputs without human review.

### Autonomous action risk

AI systems granted agency -- the ability to take actions without human approval -- can cause harm if their decision-making is compromised or poorly bounded. An AI agent authorised to send emails could forward confidential messages if prompt-injected. An autonomous system controlling physical equipment could cause safety incidents if its inputs are manipulated.

## Two distinct problem spaces

It is useful to separate AI risk into two categories:

1. **Attacks on AI**: The AI system itself is the target. Attackers poison training data, extract models, craft adversarial inputs, or compromise the infrastructure hosting the model. These are covered in detail by [AI Security and Data Risk](../29-emerging-data-security-trends/ai-security-and-data-risk.md) and [Adversarial ML and Model Abuse](../29-emerging-data-security-trends/adversarial-ml-and-model-abuse.md).
2. **Attacks using AI**: AI is the tool, not the target. Attackers use AI to automate, scale, or refine traditional attacks. The victim may have no AI systems at all and still be affected.

Both categories belong in the ISMS risk assessment process. The asset inventory should identify which AI systems the organisation builds or buys (category 1) and the threat assessment should consider AI as an enabler for adversaries (category 2).

## Typical evidence

- AI risk categories documented in the organisation's risk assessment methodology
- Risk register entries that distinguish AI-specific risks from general IT risks
- Threat assessment updates that include AI-enabled attack techniques
- Records of management review discussions covering AI risk exposure

## Practical example

A mid-sized organisation identifies three AI risk areas during an ISMS risk review: a third-party recruitment tool uses an opaque ML model that may introduce hiring bias, a customer-service chatbot has no prompt-injection testing, and the security team notes that phishing simulations are becoming harder to distinguish from real attacks because attackers now use AI-generated content indistinguishable from legitimate communications. Each is entered into the risk register with an assigned owner and treatment plan.

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
