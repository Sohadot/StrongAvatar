# Indexing Readiness Report — 2026-07-14

**Sprint:** 19 — Post-Launch Indexing Readiness
**Scope:** Live verification of the 22-route foundation launch set on the production domain, sitemap submission status, and indexing posture.
**Method:** `site/scripts/verify_live_routes.py` (network verification against https://strongavatar.com) plus manual redirect and parity checks. All observations dated 2026-07-14.

---

## Summary

The deployed foundation set is fully indexing-ready. All 22 registered routes serve correctly with exact canonical URLs, the live sitemap is byte-identical to the governed repository sitemap, redirect consolidation funnels every URL variant to a single canonical form, unregistered routes hard-404, and the sitemap has been submitted to and successfully processed by Google Search Console with all 22 pages discovered.

---

## Live Route Verification — 22/22 PASS

Every route in `site/data/launch_set.json` was fetched on the production domain and verified for:

| Check | Result |
|---|---|
| HTTP status 200 | 22/22 |
| `<link rel="canonical">` exactly matching `https://strongavatar.com{route}` | 22/22 |
| `<title>` present and page-specific | 22/22 |
| `<meta name="robots" content="index, follow">` | 22/22 |

## Canonical Consolidation — PASS

| Variant | Behavior |
|---|---|
| `http://strongavatar.com/` | 301 → `https://strongavatar.com/` |
| `https://www.strongavatar.com/` | 301 → `https://strongavatar.com/` |
| Route without trailing slash (e.g. `/standard`) | 301 → trailing-slash canonical (`/standard/`) |

One canonical form per page; no duplicate-content surface.

## Unregistered Route Behavior — PASS

`/not-a-page/` returns a hard HTTP 404. No soft-404 behavior; the indexable surface is exactly the registered launch set.

## Sitemap — PASS

- `https://strongavatar.com/sitemap.xml` serves HTTP 200 and is **byte-identical** to the governed `output/sitemap.xml` (22 URLs).
- **Google Search Console:** sitemap submitted 2026-07-14, status *success* ("Opération effectuée"), **22 pages discovered** — exact parity with the registered launch set. Submission performed by the owner from the verified property.

## Robots — PASS, with one observation

The repo-governed `robots.txt` section (Allow /, internal-path disallows, sitemap directive) is served intact on the live domain.

**Observation (owner-level policy, no action taken):** the CDN (Cloudflare) prepends a managed content-signals block to the live `robots.txt`: `Content-Signal: search=yes, ai-train=no, use=reference`, plus `Disallow: /` for AI-training crawlers (GPTBot, ClaudeBot, CCBot, Google-Extended, Bytespider, Amazonbot, Applebot-Extended, meta-externalagent, CloudflareBrowserRenderingCrawler). Consequences to weigh:

- **Protective reading:** reference content is shielded from uncompensated model training — consistent with the asset's likeness-governance posture and rights discipline.
- **Reach reading:** AI assistants and AI-grounded search answers are a growing discovery channel for exactly the institutional audience this asset targets; `ai-train=no` with per-bot disallows also blocks some retrieval/grounding access, which can reduce the protocol's citation surface in AI-generated answers.

This is a strategic trade-off between content protection and reference reach. It is CDN-managed (not repository-governed), so any change is made in the Cloudflare dashboard, not in this repository. Flagged for an explicit owner decision; either choice should then be recorded in `DECISION_LOG.md` so the posture is deliberate rather than default.

## Classic search indexing — unaffected

Googlebot (search) and Bingbot are **not** blocked; `search=yes` is explicitly signaled. Standard search indexing of the 22 pages proceeds normally.

---

## Verification Tooling

`site/scripts/verify_live_routes.py` added as a repeatable post-deployment verifier. It is intentionally **excluded** from `site/scripts/quality_gate.py`, which must remain deterministic and offline; run it manually after any deployment and record results in a dated report in this directory.

## Next Signals to Watch (no action required yet)

- Google Search Console **Pages / Indexing** report: expect the 22 discovered pages to move to *indexed* over the coming days-to-weeks; investigate any excluded pages.
- First impressions/queries in the **Performance** report establish the baseline for reference-authority growth.
