# Avatar Integrity Ontology

**Version:** 0.1
**Status:** Draft — requires DECISION_LOG.md approval entry before versioning beyond 0.1
**Governed by:** `ASSET_THESIS.md`, `AVATAR_STRENGTH_ASSESSMENT_PROTOCOL.md`
**Subordinate to:** `ASSET_INTELLIGENCE_FACTORY_PLAN.md` (portfolio/asset-dossiers/strongavatar.com/)

---

## Scope

This ontology classifies:

- **Weakness classes** (W-01…W-10): the observable failure modes of a synthetic avatar or digital likeness deployment
- **Governance components** (C-01…C-08): the structural mechanisms that eliminate or reduce each weakness

Out of scope: avatar aesthetics, rendering quality, realism, style, platform performance, and engagement metrics. The ontology is silent on whether an avatar looks good. It classifies only whether the avatar's identity, consent, provenance, disclosure, scope, revocability, and accountability are governed and verifiable.

---

## Relation to Protocol Dimensions

The nine assessment dimensions in `site/data/protocol_dimensions.json` (Identity Integrity, Likeness Control, Consent Clarity, Platform Portability, Visual Authority, Synthetic Trust, Commercial Readiness, Abuse Resistance, Long-Term Narrative Coherence) function as **structured inputs** to the Avatar Strength Assessment Protocol. Each dimension captures bounded answers about a deployment. The protocol maps those answers to the weakness classes and governance components defined here.

Dimensions describe *what is evaluated*. Weakness classes describe *what is wrong*. Governance components describe *what remediates it*.

---

## Versioning Rules

- Classes and components carry stable identifiers (W-01…W-10, C-01…C-08). Identifiers are permanent once assigned.
- Minor additions (new classes or components) require a new minor version and a `DECISION_LOG.md` entry.
- Existing class definitions may be refined but not silently repurposed.
- A class or component may not be removed; it may be deprecated with a superseding class noted.
- This document is append-aware: additions do not invalidate prior assessments.

---

## Entry Criteria

**For a weakness class to enter this ontology it must:**

1. Name a distinct, observable failure or governance gap — not a subset of an existing class
2. Be detectable or confirmable through structured protocol inputs (bounded questionnaire responses)
3. Map to at least one governance component on the C-table
4. Be defined precisely enough that two competent operators assess the same deployment identically

**For a governance component to enter this ontology it must:**

1. Name a distinct structural mechanism — not a general best practice
2. Demonstrably remediate at least one weakness class
3. Be implementable and verifiable independently of other components

---

## Weakness Classes

### W-01 — Consent Absence

**Definition:** No documented authority exists for the use of the likeness or identity represented by the avatar. The deployment proceeds without an explicit, reviewable consent basis that specifies who authorized what, for what purpose, in what scope, and for what duration.

**Observable signals:**
- No consent agreement, license, or authorization record is producible on request
- The avatar replicates a real person's appearance, voice, or manner without traceable permission
- Synthetic likeness is derived from a source whose consent status is undocumented or ambiguous

**Compounding with:** W-06 (Rights Ambiguity), W-07 (Revocation Gap)

**Remediates via:** C-01 (Consent Infrastructure)

**Assessment dimension mapping:** Consent Clarity (primary), Likeness Control (secondary)

---

### W-02 — Provenance Void

**Definition:** No traceable chain exists from the source identity (real or synthetic) to the deployed avatar. The avatar's origin — who it was derived from, what training data or capture process created it, and what transformations were applied — cannot be established or verified.

**Observable signals:**
- No content credentials, provenance metadata, or origin documentation is attached to or associated with the avatar
- The generation or capture process is undocumented
- No binding exists between the deployed avatar and a verifiable source identity

**Compounding with:** W-01 (Consent Absence), W-09 (Attribution Loss)

**Remediates via:** C-02 (Provenance and Content Credentials Layer)

**Assessment dimension mapping:** Identity Integrity (primary), Synthetic Trust (secondary)

---

### W-03 — Disclosure Failure

**Definition:** The synthetic nature of the avatar is not communicated in contexts where a viewer, user, or counterparty would reasonably need to know they are interacting with a synthetic representation rather than a real person.

**Observable signals:**
- No disclosure label, indicator, or watermark is present in deployments where synthetic origin is material to the interaction
- Synthetic origin is actively concealed or implied to be human
- Disclosure is present in one channel but absent in others where the same avatar is deployed

**Compounding with:** W-04 (Identity Drift), W-08 (Context Collapse)

**Remediates via:** C-03 (Disclosure Layer)

**Assessment dimension mapping:** Synthetic Trust (primary), Identity Integrity (secondary)

---

### W-04 — Identity Drift

**Definition:** The avatar acts, appears, or is used in ways that diverge from its authorized identity scope. The deployed behavior, appearance, or statements differ materially from what consent, provenance, and scope documentation authorize.

**Observable signals:**
- Avatar is used in contexts, roles, or statements beyond those covered by its consent basis
- Appearance has been modified beyond authorized parameters
- Avatar is attributed to a real person in situations the person did not authorize

**Compounding with:** W-01 (Consent Absence), W-08 (Context Collapse)

**Remediates via:** C-04 (Scope and Usage Binding)

**Assessment dimension mapping:** Long-Term Narrative Coherence (primary), Identity Integrity (secondary), Likeness Control (secondary)

---

### W-05 — Impersonation Exposure

**Definition:** The avatar can be cloned, replicated, or repurposed to impersonate a real person, another avatar, or a protected identity without detection or prevention. The deployment creates an exploitable surface for identity fraud.

**Observable signals:**
- No technical or procedural barrier prevents reproduction of the avatar for impersonation purposes
- The avatar's source assets (model, voice, appearance parameters) are accessible in ways that enable replication
- No detection or authentication mechanism distinguishes the authorized avatar from a clone

**Compounding with:** W-02 (Provenance Void), W-10 (Robustness Weakness)

**Remediates via:** C-05 (Anti-Impersonation Controls)

**Assessment dimension mapping:** Abuse Resistance (primary), Identity Integrity (secondary)

---

### W-06 — Rights Ambiguity

**Definition:** The chain of title for the identity or likeness used in the avatar is unclear, incomplete, or contested. It cannot be established who holds rights over the likeness, what those rights permit, and whether they have been properly assigned or licensed.

**Observable signals:**
- No rights documentation exists covering the likeness source
- Rights ownership is disputed or has not been transferred from a prior holder
- Licensing terms are absent, expired, or conflict with the deployment context

**Compounding with:** W-01 (Consent Absence), W-07 (Revocation Gap)

**Remediates via:** C-06 (Rights Chain Documentation), C-01 (Consent Infrastructure, secondary)

**Assessment dimension mapping:** Likeness Control (primary), Commercial Readiness (secondary)

---

### W-07 — Revocation Gap

**Definition:** No mechanism exists to withdraw consent, decommission the avatar, or remove it from active deployment. Once deployed, the avatar cannot be recalled by the subject, the rights holder, or the deploying platform.

**Observable signals:**
- No kill-switch, decommission process, or revocation procedure is documented
- The consent basis contains no expiry, withdrawal clause, or termination right
- The avatar persists in deployment after the subject or rights holder has requested removal

**Compounding with:** W-01 (Consent Absence), W-06 (Rights Ambiguity)

**Remediates via:** C-07 (Revocation and Kill-Switch Mechanism), C-01 (Consent Infrastructure, secondary)

**Assessment dimension mapping:** Consent Clarity (primary), Commercial Readiness (secondary)

---

### W-08 — Context Collapse

**Definition:** The avatar is reused outside its authorized context, platform, or audience. A deployment authorized for one context is applied in another without renewal of consent, provenance verification, or scope confirmation.

**Observable signals:**
- Avatar originally authorized for one platform or audience appears in another without documented re-authorization
- Context-specific disclosures are not adapted when the avatar moves to a new deployment context
- Consent basis does not specify permitted contexts, creating ambiguity that enables expansion

**Compounding with:** W-03 (Disclosure Failure), W-04 (Identity Drift)

**Remediates via:** C-04 (Scope and Usage Binding)

**Assessment dimension mapping:** Platform Portability (primary), Long-Term Narrative Coherence (secondary)

---

### W-09 — Attribution Loss

**Definition:** No durable binding exists between the avatar and an accountable owner, creator, or responsible party. The avatar cannot be traced to a person or entity that bears accountability for its deployment.

**Observable signals:**
- No owner, creator, or responsible entity is identified in or associated with the avatar
- Attribution metadata is absent, stripped, or detached from the avatar in at least one deployment context
- The avatar exists in deployment with no contactable accountable party

**Compounding with:** W-02 (Provenance Void), W-06 (Rights Ambiguity)

**Remediates via:** C-08 (Attribution and Accountable-Owner Binding)

**Assessment dimension mapping:** Identity Integrity (primary), Synthetic Trust (secondary)

---

### W-10 — Robustness Weakness

**Definition:** The avatar or its governance infrastructure is vulnerable to adversarial tampering, spoofing, or manipulation. Provenance signals can be stripped or forged, the avatar can be cloned with governance metadata removed, or authentication mechanisms can be bypassed.

**Observable signals:**
- Provenance or content credential signals are not tamper-evident
- Avatar assets can be re-exported without governance metadata attached
- No integrity verification mechanism exists to distinguish the authenticated avatar from a tampered version

**Compounding with:** W-02 (Provenance Void), W-05 (Impersonation Exposure)

**Remediates via:** C-02 (Provenance and Content Credentials Layer), C-05 (Anti-Impersonation Controls, secondary)

**Assessment dimension mapping:** Abuse Resistance (primary), Synthetic Trust (secondary)

---

## Governance Components

### C-01 — Consent Infrastructure

**Definition:** A documented system for recording, scoping, and maintaining the authority under which a likeness is used. At minimum: identity of the consenting party, scope of permitted use, duration, and conditions for renewal or withdrawal.

**Remediates:** W-01 (Consent Absence), W-06 (Rights Ambiguity, secondary), W-07 (Revocation Gap, secondary)

**Implementation indicators:**
- A consent record exists, is dated, and specifies the authorized use scope
- The consent record is producible on request by the subject, the deploying platform, or a regulator
- The record includes an expiry date or a renewal mechanism

---

### C-02 — Provenance and Content Credentials Layer

**Definition:** A mechanism that establishes and preserves the traceable chain from source identity to deployed avatar, including generation method, transformations applied, and authoring entity. Aligned with C2PA or equivalent provenance standards where applicable.

**Remediates:** W-02 (Provenance Void), W-10 (Robustness Weakness)

**Implementation indicators:**
- Content credentials or provenance metadata are attached to or associated with the avatar
- The origin chain (capture, generation, transformation) is documented and verifiable
- Provenance signals are tamper-evident and persist through distribution

---

### C-03 — Disclosure Layer

**Definition:** A mechanism for communicating the synthetic nature of the avatar in all deployment contexts where a viewer, user, or counterparty would reasonably need to know. Disclosure must be context-appropriate in form and placement.

**Remediates:** W-03 (Disclosure Failure)

**Implementation indicators:**
- A disclosure mechanism (label, watermark, metadata, verbal disclosure) is present in every deployment context where synthetic origin is material
- Disclosure is not buried, minimized, or conditioned on user action
- Disclosure adapts to context: a video avatar discloses differently from a conversational AI interface

---

### C-04 — Scope and Usage Binding

**Definition:** A documented boundary that constrains the avatar's authorized use: permitted contexts, platforms, audiences, behaviors, and statements. Any use outside the binding requires explicit re-authorization.

**Remediates:** W-04 (Identity Drift), W-08 (Context Collapse)

**Implementation indicators:**
- The consent basis or deployment agreement specifies permitted contexts and behaviors
- A review mechanism exists to detect and flag uses outside the authorized scope
- Platform or distribution re-authorization is required when the avatar moves to a new context

---

### C-05 — Anti-Impersonation Controls

**Definition:** Technical and procedural mechanisms that prevent the avatar from being cloned, replicated, or repurposed for impersonation. Includes detection, authentication, and barrier controls.

**Remediates:** W-05 (Impersonation Exposure), W-10 (Robustness Weakness, secondary)

**Implementation indicators:**
- Avatar assets are not distributed in forms that enable uncontrolled replication
- An authentication mechanism distinguishes the authorized avatar from unauthorized copies
- Detection procedures are in place to identify unauthorized clones in distribution

---

### C-06 — Rights Chain Documentation

**Definition:** A documented chain of title establishing who holds rights over the likeness or identity, what those rights permit, and how they have been assigned or licensed to the deploying party.

**Remediates:** W-06 (Rights Ambiguity)

**Implementation indicators:**
- Rights documentation covers the likeness source (real or synthetic) and all assignments
- Licensing terms match the deployment context and are not expired or contested
- The chain is traceable to an originating rights holder

---

### C-07 — Revocation and Kill-Switch Mechanism

**Definition:** A documented process that allows the subject, the rights holder, or an authorized authority to withdraw consent and remove the avatar from active deployment within a defined timeframe.

**Remediates:** W-07 (Revocation Gap)

**Implementation indicators:**
- A revocation procedure exists and is documented in the consent basis or deployment agreement
- The deploying platform has a technical mechanism to deactivate or remove the avatar on request
- A defined response time for revocation requests is documented

---

### C-08 — Attribution and Accountable-Owner Binding

**Definition:** A durable binding between the deployed avatar and a named accountable party — a person or entity that bears responsibility for the avatar's governance, behavior, and compliance.

**Remediates:** W-09 (Attribution Loss)

**Implementation indicators:**
- An accountable owner is identified in or associated with every deployment context
- Attribution metadata persists through distribution and is not detachable
- The accountable owner is contactable and has accepted documented responsibility

---

## Weakness-to-Component Mapping Table

| Weakness Class | Primary Component | Secondary Component |
|---|---|---|
| W-01 Consent Absence | C-01 Consent Infrastructure | C-06 Rights Chain Documentation |
| W-02 Provenance Void | C-02 Provenance and Content Credentials Layer | — |
| W-03 Disclosure Failure | C-03 Disclosure Layer | — |
| W-04 Identity Drift | C-04 Scope and Usage Binding | — |
| W-05 Impersonation Exposure | C-05 Anti-Impersonation Controls | — |
| W-06 Rights Ambiguity | C-06 Rights Chain Documentation | C-01 Consent Infrastructure |
| W-07 Revocation Gap | C-07 Revocation and Kill-Switch Mechanism | C-01 Consent Infrastructure |
| W-08 Context Collapse | C-04 Scope and Usage Binding | C-03 Disclosure Layer |
| W-09 Attribution Loss | C-08 Attribution and Accountable-Owner Binding | C-02 Provenance and Content Credentials Layer |
| W-10 Robustness Weakness | C-02 Provenance and Content Credentials Layer | C-05 Anti-Impersonation Controls |

---

## Assessment Dimension to Weakness Class Mapping

The nine protocol dimensions function as structured inputs. This table shows which weakness classes each dimension's answers are most likely to surface.

| Assessment Dimension | Primary W-Classes | Secondary W-Classes |
|---|---|---|
| Identity Integrity | W-02, W-09 | W-04, W-03 |
| Likeness Control | W-06, W-01 | W-04 |
| Consent Clarity | W-01, W-07 | W-06 |
| Platform Portability | W-08 | W-04, W-07 |
| Visual Authority | W-04 | W-03 |
| Synthetic Trust | W-03, W-02 | W-09, W-10 |
| Commercial Readiness | W-06, W-07 | W-01 |
| Abuse Resistance | W-05, W-10 | W-02 |
| Long-Term Narrative Coherence | W-04, W-08 | W-09 |

---

*Ontology maintained under Sovereign Asset System. Version history tracked in `DECISION_LOG.md`. Entry criteria enforced before any class addition. Identifiers W-01…W-10 and C-01…C-08 are permanent.*
