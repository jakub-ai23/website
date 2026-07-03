# Translation Mission Report — EN page mirror of repositioned DE

*Created: 2026-07-03 · Skill: translate-document · Direction: DE → EN (Neutral EU business English)*

## Task
Mirror the freshly-repositioned German `index.html` into the English `en/index.html`: Business Lead @ Hill Digital foreground, SURF/Mindworx removed, 6-item trainings agenda, roundnet/PADI facts, individual-appointment prompt.

## Files
- Source (DE, finalised this session): `index.html`
- Target (EN, edited): `en/index.html`
- Glossary (updated §0 for 2026-07-03 positioning): `glossary_de_en.md`
- Proofreader critique: returned inline (SHIP-READY)

## Sections mirrored
1. `<head>` — title, meta description, og + twitter title/description
2. JSON-LD — `jobTitle` + new `worksFor` (Hill Digital); valid JSON confirmed
3. Hero badge — "Business Lead at Hill Digital · AI Trainer"
4. About slide — SURF badge/stat/credential removed; About text leads with HD identity (locked EN copy); stat "HD / Business Lead"; roundnet + former national floorball player + PADI Divemaster; no BJJ
5. Trainings slide — card grid → agenda (6 live trainings, English copy) + individual-appointment prompt ("Request an appointment" → `cal.eu/hilldigital/consulting`)
6. CSS — agenda + prompt styles; mobile breakpoint rewritten; dead `.surf-badge-overlay` CSS stripped (both files)

## QA results
- **Proofreader (native Neutral-EU EN):** VERDICT SHIP-READY. 0 CRITICAL, 0 HIGH. 1 MED applied ("People work with AI" → "HR work with AI"). LOW items (dead SURF CSS) cleared.
- **Parity scan:** 6/6 trainings identical DE↔EN (order, dates, providers, all 7 hrefs). 6 `.ag` entries each.
- **Positioning:** no SURF/Mindworx anywhere (both files); Business Lead @ Hill Digital leads title/meta/og/twitter/hero/jobTitle/About/first credential.
- **Glossary:** "member of Hill Woltron" (with O), tagline exactly "Human in the Lead. AI in Support.", GDPR for DSGVO — all verbatim.
- **Dash sweep:** 0 em/en dashes in visible copy (2 hits are in code comments only).
- **JSON-LD:** valid in both files.

## VERDICT: SHIP-READY (both DE + EN)
Layout verified on desktop (hero, About, trainings agenda) and mobile (forced 390px). Nothing pushed — awaiting commander's explicit go to publish `jakub-ai23/website`.
