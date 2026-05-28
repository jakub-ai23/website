# Translation Mission Report — DE → EN

**Date:** 2026-05-28
**Source:** `index.html` (German, Austrian, Sie-Form)
**Target:** `en/index.html` (Neutral EU business English)
**Pipeline:** translate-document skill — glossary → translator x2 → proofreader x2 → gatekeeper

## Decisions locked
- **Dialect:** Neutral EU business English (spelling-neutral, UK lean: personalise, programme, behaviour, cooperation)
- **Scope:** Main page only (`index.html`). Legal pages (Impressum, Datenschutz) stay German; footer links point to `../impressum.html` / `../datenschutz.html`.
- **Output:** `/en/` subfolder mirror. Asset/font/icon paths rewritten to `../`. Internal anchors unchanged.
- **Date format:** EU business style — "25 June 2026", "6 July 2026", "14-15 July 2026".

## Files produced
- `en/index.html` — translated page (working artefact)
- `glossary_de_en.md` — reusable DE→EN term map (the asset)
- `2026-05-28-proofreader-iter1.md`
- `2026-05-28-proofreader-iter2-final.md`
- `2026-05-28-gatekeeper-final.md`
- this report

## Issue counts
| Pass | CRITICAL | HIGH | MED | LOW |
|---|---|---|---|---|
| Proofreader iter 1 | 2 | 2 | 1 | 0 |
| Proofreader iter 2 | 0 | 0 | 0 | 0 |
| Gatekeeper | 0 | 0 | 0 | 0 |

### Fixes applied (iter 1)
1. German error string in JS catch branch → "Error - please try again" (CRITICAL)
2. Schema `url` → `https://jakubpopluhar.com/en/` (CRITICAL)
3. Training tag "Course" → "Programme" (HIGH)
4. Testimonial "winning new members" → "bringing in new members" (MED)

### Orchestrator override
- Typewriter gold-highlight split: kept the white-lead-in / gold-tail pattern. It mirrors the German source's rhetorical device (the gold highlights the repeated punch). Glossary §4 was over-prescriptive; not changed.

## Final verification
- Structural parity vs source: identical (9 slides, 3 training cards, 3 testimonials, nav, footer, credentials, podium, transform rows, CTA cards).
- Names / degrees / dates / coords / emails / URLs: preserved.
- Em-dash AND en-dash: zero in rendered body (only HTML/CSS comments, exempt).
- German leakage in body: zero. German remains only in `value=`/`selectInterest()` form payloads (intentional, stable form data) and institution names (TU München, LMU München).
- AI-tells: none. Locked-rhythm phrases: verbatim. `lang="en"`, `og:locale="en_GB"`.
- Asset paths use `../` correctly for `/en/` depth.

## VERDICT: SHIP-READY

## Layout-risk flags (visual check before publish)
- Hero typewriter longest line: "what your competitors already use." — confirm single-line on mobile.
- Training-card row, nav bar labels — confirm no overflow.
- Confirm self-hosted fonts load via `../fonts/` and snap-scroll renders from `/en/`.
- Preview: `http://localhost:8791/en/index.html` (local server, port 8791).

## Open decision before launch
- No language switcher exists yet (DE ↔ EN). The `/en/` page is live-able standalone, but visitors have no link between versions. Add a DE/EN toggle in nav when ready, and set `hreflang` alternates in both pages' `<head>`.
