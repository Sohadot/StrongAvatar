# Regulatory and Standards Alignment

**Status:** Internal governance analysis — not a public page, not registered for publication
**Discipline:** Governed by `SOURCE_AND_CLAIM_DISCIPLINE.md`. This document is conceptual analysis, not legal advice, not regulatory guidance, and not a claim of endorsement by or affiliation with any body named below.
**Publication rule:** No statement in this document may appear on a public page until each framework reference is verified against the primary source current at publication time and the page carries a reference-only / not-legal-advice disclaimer.

---

## Purpose

The Avatar Strength Protocol becomes structurally hard to bypass when it is the practical crosswalk between what regulators and standards bodies require and what an avatar deployment must actually implement. This document maps the ontology's governance components (C-01…C-08) and weakness classes (W-01…W-10) to the external frameworks most relevant to synthetic likeness, so that alignment is inferred by institutional readers from the mapping itself rather than claimed rhetorically.

The positioning rule: StrongAvatar.com does not compete with these frameworks and does not restate them. It translates them into one deterministic, auditable assessment for a single deployment context — which none of them provide on their own.

---

## Alignment Map (Analysis)

Each row states the *conceptual* correspondence. Framework descriptions are directional summaries for internal planning; exact obligations must be confirmed against primary sources before public use.

| Framework | Nature | Corresponding components | Corresponding weakness classes | Correspondence (analysis) |
|---|---|---|---|---|
| C2PA / Content Credentials | Industry technical standard for tamper-evident content provenance | C-02 | W-02, W-10 | The protocol's B2 input ("content credentials or provenance metadata in tamper-evident form") is directly satisfiable by a C2PA-conformant implementation. The Sovereign band's tamper-evident provenance criterion is the band-level expression of the same property. |
| EU AI Act — transparency obligations for AI systems and synthetic content | Regulation (EU), phased applicability | C-03, C-02 | W-03, W-02 | Disclosure of synthetic origin in contexts where a viewer would need to know (input C1, component C-03) is the deployment-level control an operator would point to when demonstrating synthetic-content transparency. The unconditional Ungoverned rule for W-03 encodes the position that undisclosed synthetic likeness is indefensible. |
| GDPR — lawful basis, consent, and withdrawal | Regulation (EU) | C-01, C-07 | W-01, W-07 | Documented, scoped, dated consent (inputs A1/A2) and a defined revocation path (input A3, component C-07) mirror the consent-quality and withdrawal expectations that apply where a likeness involves personal data. The protocol does not determine lawful basis; it verifies that the documentation an operator would rely on exists and is producible. |
| US federal and state likeness legislation (e.g., proposed NO FAKES Act; state right-of-publicity and voice/likeness statutes such as Tennessee's ELVIS Act) | Statutes and proposals, jurisdiction-specific and evolving | C-01, C-06, C-05 | W-01, W-06, W-05 | Rights-chain documentation (E1/C-06), consent records (A1/C-01), and anti-impersonation controls (E2/C-05) are the operational artifacts a deployer would need to produce when a likeness claim is asserted. Legislative status must be re-verified at publication time. |
| NIST AI Risk Management Framework | Voluntary US framework | C-08, C-04, C-07 | W-09, W-04, W-08 | Accountable-owner binding (D2/C-08), documented scope boundaries (D1/C-04), and tested revocation (C-07) express the govern/map/manage posture at the granularity of a single avatar deployment. |

---

## What the Protocol Adds That the Frameworks Do Not

- A **single deterministic determination** per deployment: frameworks state obligations; the protocol resolves any deployment to exactly one band with a machine-verified rule table (see `spec/`).
- A **cross-framework vocabulary**: one weakness taxonomy (W-01…W-10) that an operator, a platform trust-and-safety team, and a rights holder can use consistently regardless of jurisdiction.
- A **remediation order**: ranked components and a minimum band-elevation path, which no transparency or provenance framework provides at deployment granularity.

This additive framing is the acquisition-relevant claim, and it is defensible because it is structural, not comparative marketing.

---

## Constraints

- No public page may assert that a band determination constitutes compliance with any law, regulation, or standard. Bands assess governance documentation and controls, not legal conformity.
- No framework name may be used on a public page in a way that implies endorsement, certification, or partnership.
- Every framework reference on a future public page requires a primary-source citation and a dated verification note, per `SOURCE_AND_CLAIM_DISCIPLINE.md`.
- This mapping must be reviewed whenever the ontology adds a weakness class or a framework named here changes materially.
