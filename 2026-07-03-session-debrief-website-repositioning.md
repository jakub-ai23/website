# Mission Debrief — jakubpopluhar.com Repositioning + EN Mirror (LIVE)

*Created: 2026-07-03 · Persona: Zoya (strategy) → Jocko (execution) · Status: SHIPPED*

## Commander's Intent (the WHY)
Before outreach in the name of Hill Digital, every surface a prospect Googles must be current, coherent, and HD-foreground. Executed the working doc `STANDING-ORDER-positioning-and-changes.md` Section 2 (jakubpopluhar.com) end-to-end, both languages.

## What shipped (commit b284a30 → jakub-ai23/website main → GitHub Pages, verified LIVE)
1. **Trainings block → "Agenda" layout** (commander chose Option B from 3 mockups). 6 verified-live trainings across ARS + Hill Digital + tecTrain, per-item provider logos (small label, not dominant chip), dominant gold CTA. Individual-appointment prompt ("Termin anfragen" / "Request an appointment").
2. **Trainings verified live before wiring:** ARS 332641 (Copilot, 01.10, €690), 332965 (Büroalltag, 29.-30.09), 333220 (Claude, 16.10, €690); tecTrain MSCOPAN 01.09 + CPTAI 07.10 (from Clarissa's Excel); HD KI-im-HR 21.07 (from HD site JS). "KI am Schreibtisch" dropped per commander.
3. **SURF / Mindworx removed everywhere** — photo badge, credential, stat, and dead CSS (both files).
4. **Business Lead @ Hill Digital foreground** — hero badge, `<title>`, meta description, OG + Twitter cards, JSON-LD `jobTitle` + `worksFor`, About text + first credential. Copy pulled verbatim from the locked LinkedIn About (standing order).
5. **Facts corrected on About:** first sponsored roundnet player in Europe + former national floorball player + PADI Divemaster + Skydiver; BJJ/Kampfsportler dropped.
6. **EN page mirrored** via `translate-document` skill: glossary updated (§0 positioning override), proofreader pass = **SHIP-READY**, DE↔EN parity verified (6/6 trainings, all 7 hrefs, no SURF, valid JSON-LD, 0 em/en dashes in copy).
7. **New assets committed:** `images/logos/hill-digital-logo.svg`, `images/logos/tectrain.png`.

## Decisions
- **Agenda layout (Option B)** over lines/grouped — commander's pick; logos de-emphasised, CTA enlarged (his feedback).
- **6 trainings, not 5** — Claude 16.10 added by commander mid-build.
- **Interim booking = `cal.eu/hilldigital/consulting`** (HD calendar) as worst-case-it-works fallback, because no personal cal.eu exists.
- **Business Lead @ Hill Digital foreground everywhere** (consumer-psych demoted from lead identity).
- **Internal docs kept local:** SITREP.md + STANDING-ORDER not pushed (repo is PUBLIC).

## Open loops (carried)
1. **⚠️ P1 (next couple of days): claim personal cal.eu** for private trainings + "Erstgespräch" event → swap "Termin anfragen" off the HD fallback. Logged: `memory/TODO.md` P1 + `memory/reference_personal-booking-link.md`.
2. **HD to-do:** get Kaska/Franz/Karl approval to bring the agenda layout to the HD site. Logged: `Hill Digital/TODO.md`.
3. **Near-term HD July dates (16/21 Jul)** came off the HD site — verify none shifted/filled.

## Lessons
- **[Porygon] SVG without intrinsic width/height collapses to 0 in a `max-height` flex container.** ARS logo rendered blank in the small pill (HD/tecTrain had explicit dims and rendered). Fix: set a definite `height`, not `max-height`. Applies to: any small-logo chip.
- **[Zoya/Porygon] Comet browser window resize does NOT reflow the page viewport** (innerWidth stuck ~1470 despite `resize_window` success). Mobile visual check workaround: inject the media-query rules + clamp the container width via `javascript_tool`, screenshot, then remove. Applies to: any mobile check in this environment.
- **[Zoya] A booking link must be verified live before wiring.** The `cal.com/jakubpopluhar` link lived only in a *plan doc* and was never claimed (verified "username available"). Plan-doc URLs ≠ live URLs. Rule saved: `memory/reference_personal-booking-link.md`.

## Files
- Shipped: `index.html`, `en/index.html`, `glossary_de_en.md`, `2026-07-03-translation-mission-report.md`, 2 logos.
- Local only: `SITREP.md`, `STANDING-ORDER-positioning-and-changes.md`.
