# Hormozi-lens conversion critique — seven pages (DE structure, EN copy)

Created: 2026-08-04 · Reviewer: critic agent, briefed against
`~/Projects/content/voice-library/alex-hormozi-voice-profile.md`
Scope: the seven new pages. **Findings are about the OFFER, not the translation.**
Constraint given to the reviewer: Hormozi's mechanics, never his register. No invented claims.

## VERDICT: these pages do not convert as they stand

## Finding 1 — HIGHEST — four of seven pages have no booking CTA at all

`trainings/copilot/`, `trainings/hr-kurs/`, `trainings/ki-am-schreibtisch/`,
`trainings/konsumentenpsychologie/`: the only clickable action on the entire page is the PDF download.

**Independently verified by the orchestrator, and the reviewer understated it — this is true of the
GERMAN pages too, which are already live:**

| Page | cal.eu links, DE | cal.eu links, EN |
|---|---|---|
| `/trainings/` | 4 | 4 |
| `/trainings/copilot/` | **0** | **0** |
| `/trainings/hr-kurs/` | **0** | **0** |
| `/trainings/ki-am-schreibtisch/` | **0** | **0** |
| `/trainings/konsumentenpsychologie/` | **0** | **0** |
| `/ki-personal-training/` | 2 | 2 |
| `/ueber-mich/` | 1 | 1 |

A reader who consumes a full course description has no path to book. Proposed: add
`Book an intro call →` / `Vorgespräch buchen →` to `https://cal.eu/jakubpopluhar/erstgespraech`
in the hero next to the PDF button, plus a closing CTA band matching `/trainings/`.
NB `.btn-primary` is not defined in those four pages' stylesheets — they only have `.btn`.

## Finding 2 — the coaching guarantee is buried

"And if it does not help? Then tell me in the first hour and we stop." — currently FAQ #5 of 5,
far below the price grid. Proposed addition under the price grid (built from the existing guarantee,
nothing invented): "Every package is billed by the hour you actually use. If the first hour doesn't
work for you, say so and we stop there — you're never on the hook for hours you haven't had."

## Finding 3 — the sharpest proof on the site sits in one buried paragraph

"saved 40 minutes a day … around 18 working days [a year]" is sentence three of paragraph three on
`ki-personal-training`, and appears nowhere else. The catalogue and all four course pages carry no
hard numbers at all. Proposed: promote it within its own section, and distribute existing proof
(e.g. `hr-kurs`'s "two thirds of Austrian HR departments") to the catalogue hero.

## Other findings

- **Offer clarity on cost:** the catalogue and all four course pages state no price and no "on
  request" line. They fail the ten-second test on cost.
- **Price ladder:** naming (Starter / Recommended / Intensive) and "Most people choose this one" are
  working — keep. But the Starter anchor undercuts itself: "Individually that would be €1,160" against
  €1,120 is a 3.4% saving, next to 13.8% and 17.2% on the tiers above. Copy fix only (no price
  change): drop the comparison on Starter, give it a different reason ("Best if you have exactly one
  thing to fix").
- **Wrong place, right content:** the "book through a training provider" paragraph sits directly under
  the price grid, opening a fourth path at peak purchase intent. Move to the FAQ.
- **`ueber-mich`:** the warmed-up reader is sent to another page rather than offered the call directly.
- **Weakest passages to cut:** the catalogue's second hero paragraph (meta-description of the page
  itself); the `copilot` hero-sub (a features list wearing a subhead's clothes).

## NEEDS COMMANDER INPUT (reviewer refused to invent these)

1. A day rate or "from €X" for in-house trainings — nothing exists in the source.
2. A real number behind the `copilot` claim "changes daily work from the ground up".
3. Whether the Hubek / Pecija testimonials, given for 1:1 coaching, may be shown on in-house pages.
4. A measured result for `konsumentenpsychologie` beyond the qualitative claims.

## Status

**Nothing from this critique has been applied.** These are copy and offer changes to pages that are
already live in German; applying them is a business decision, not a translation fix.
