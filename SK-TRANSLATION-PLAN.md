# SK Translation Plan — jakubpopluhar.com/sk/

Created: 2026-08-04 · Last updated: 2026-08-04
Owner: Commander (decisions) · Porygon + `translate-document` pipeline (execution)
Status: PLANNED — not started, awaiting the four blockers in §7

---

## 1 · Commander's Intent

Slovak-language outreach to Slovak training organisations, offering Jakub as a trainer,
goes out under Real Team SK. A Slovak-speaking recipient who clicks the signature link
must land on a Slovak page that sells the same thing the mail promised.

**The site is a blocker, not a support asset.** The first Slovak mail does not go out
before `/sk/` is live. (Commander, 2026-08-04.)

## 2 · Decisions taken (Commander, 2026-08-04)

| Question | Call |
|---|---|
| Hosting | **`/sk/` folder on `jakubpopluhar.com`.** Confirmed 2026-08-04 against `sk.jakubpopluhar.com`: a subdomain would need a second repo (GitHub Pages = one custom domain per repo), a second CNAME, a DNS record, duplicated assets and two deploys. `/sk/` is a folder in the existing repo — no DNS, no config, existing HTTPS cert. Registering `jakubpopluhar.sk` and 301-ing it onto `/sk/` stays available later and changes nothing about the build. |
| Positioning | **Faithful translation.** Same offers, same € prices, same Austrian proof (ARS, testimonials, logos). Only imprint + privacy adapt to the Slovak entity. |
| Legal entity | **REAL TEAM, s.r.o.** — commander, 2026-08-04. Legal pair adapted from the existing `rt-sport/pravne.html`. |
| Wave 1 scope | Outreach core: landing, `/trainings/` + 4 course pages, `/ki-personal-training/` — plus SK legal pair. `/ueber-mich/` deferred to wave 1b (§7.4). |
| Outreach language | Slovak. Site precedes the send. |

## 3 · Source state (FACT, verified 2026-08-04)

- Repo `jakub-ai23/website`, GitHub Pages, CNAME `jakubpopluhar.com`.
- **`jakubpopluhar.sk` is NOT registered.** whois: "Domain not found."
- Local working copy sits on branch `schatten-ki-uebung`, **behind `origin/main`**, 15 files
  modified, three parallel worktrees checked out by other windows. `/trainings/`,
  `/ki-personal-training/`, `/ueber-mich/` and the whole `/en/` track exist on `origin/main`
  but **not in the local folder**. Translating from the local copy would translate stale source.
- `/ueber-mich/` was de-linked from nav and dropped from the sitemap on `origin/main`
  ("wird noch überarbeitet", commits `ab5a666` / `08f0f71`). It is in wave-1 scope but its
  German source is explicitly mid-revision. See §7.4.

## 4 · The asset we are reusing

The DE→EN run of 2026-08-03 built a working translation pipeline:
`translate-document` skill → orchestrator → proofreader (iter 1) → gatekeeper (final),
with a locked-terminology glossary and automated verification (tag parity, dead links,
hreflang both directions, currency format, language remnants, testimonial fidelity).
Result on 7 pages / 610 units: 0 CRITICAL at the gate.

**The pipeline transfers to SK unchanged. What does not exist yet is `glossary_de_sk.md`.**
Building that glossary before the first page is translated is the whole difference between
this run and an ad-hoc one. Reference: `2026-08-03-translation-mission-report.md`,
`glossary_de_en.md`.

## 5 · Scope and volume

| German source | Slovak target | Est. units |
|---|---|---|
| `/` (landing, snap-scroll, 82 KB) | `/sk/` | ~300 |
| `/trainings/` | `/sk/trainings/` | 79 |
| `/trainings/copilot/` | `/sk/trainings/copilot/` | 52 |
| `/trainings/hr-kurs/` | `/sk/trainings/hr-kurs/` | 61 |
| `/trainings/ki-am-schreibtisch/` | `/sk/trainings/ki-am-schreibtisch/` | 62 |
| `/trainings/konsumentenpsychologie/` | `/sk/trainings/konsumentenpsychologie/` | 58 |
| `/ki-personal-training/` | `/sk/ki-personal-training/` | 156 |
| `/ueber-mich/` | `/sk/ueber-mich/` | 142 |
| Legal pair (not translation — see §7.2) | `/sk/impressum.html`, `/sk/datenschutz.html` | n/a |

**~910 translatable units, ~7,000–7,500 words.** Unit counts for the seven non-landing pages
are measured (from the EN run); the landing figure is an estimate and will be replaced by a
real extraction count at kickoff.

**URL convention: German slugs mirrored**, exactly as the EN track does (`/en/trainings/hr-kurs/`).
Keeps DE/EN/SK paths in structural parity, keeps hreflang trivial, keeps the build scripts honest.
Cost: Slovak URLs contain German words. Accepted — the EN track already made this trade.

## 6 · Slovak-specific rules to lock in the glossary before translating

These are the DE→SK equivalents of the traps the EN run actually hit. Each becomes a
numbered glossary entry, not a remembered convention.

1. **Register: vykanie throughout** (formal plural). The German source is Sie-Form; B2B
   Slovak matches it. No switching to tykanie anywhere, including CTAs.
2. **"KI" → "AI"**, with "umelá inteligencia" on first mention per page. *Not* "UI" — in
   Slovak that reads as user interface. This is the single highest-frequency term on the site.
3. **Currency format.** German `1.120 €` → Slovak `1 120 €` (space as thousands separator,
   non-breaking, € after the number). The EN run proved bare price strings fall through the
   extractor entirely because they carry no letters — a **dedicated currency pass** is mandatory,
   not optional. Ten prices in scope.
4. **`netto` → `bez DPH`.** Every occurrence. The EN run tracked this as a semantic-weight phrase.
5. **Date format.** DE `14.07.2026` → SK `14. 7. 2026` (spaces after the dots, no leading zero).
   Affects `/termine/` in wave 2, and any inline dates in wave 1.
6. **Quotation marks:** SK uses `„…"` — same convention as German. Unlike the EN run, no
   quote conversion is needed. The grep check inverts: German quotes are *correct* here.
7. **No em-dash / en-dash.** Carries over from the standing rule. Grep U+2014 and U+2013
   separately, as the EN run learned to.
8. **Proper nouns stay German:** ARS Akademie, tecTrain, REAL TEAM, Sport Union, FitRock,
   Innovatic Group. Course *titles* translate; institution names do not.
9. **Testimonials are quotes.** Katarzyna Pichler and Patrik Hubek gave those words in German.
   Translate for comprehension, mark as translated, add nothing. Same discipline as the EN run.
10. **Semantic-weight phrases** carried from `glossary_de_en.md` §10.3 (in-house-only exclusion,
    laptop *recommended not required*, free versions covering *all* content, both hedges). These
    are commercial commitments. They survive verbatim in meaning or the translation is wrong.

## 7 · Blockers

**7.1 · `jakubpopluhar.sk` — RESOLVED / DEFERRED.** Not registered, and not needed. The site
ships at `jakubpopluhar.com/sk/` and the outreach mails point there directly. Registering the
.sk and 301-ing it (never masked forwarding, which breaks canonical/hreflang) is a later
cosmetic upgrade, not a dependency.

**7.2 · SK legal pair — RESOLVED 2026-08-04.** Entity is **REAL TEAM, s.r.o.** (commander).
All identifiers verified on disk, nothing guessed:

| Field | Value | Source |
|---|---|---|
| Obchodné meno | REAL TEAM, s.r.o. (registered name; "REAL TEAM Sport s.r.o." is the trade name only) | `memory/real-team.md`, `real-team/CLAUDE.md` |
| IČO | 31 369 049 | both, plus `rt-sport/pravne.html` |
| DIČ / IČ DPH | SK2020873745 | both |
| Sídlo | Pri kríži 18, 841 02 Bratislava | both |
| Register | Mestský súd Bratislava III, Oddiel Sro, Vložka č. 6700/B | both |
| Konateľ | Jakub Popluhar (sole spoločník + konateľ since 2023) | `memory/real-team.md` |

**Template:** `~/Projects/builds/websites/rt-sport/pravne.html` is a live Slovak legal page for
this exact entity. The SK pair is adapted from it, not written from scratch.
**Still to confirm at build time:** whether the SK pages carry the same data flows as the DE
privacy page (Formspree, Brevo, Clarity, cal.eu). If the Slovak track uses the same tooling,
the DE privacy content translates and only the controller block swaps to REAL TEAM.

**7.3 · Prices.** Faithful translation keeps €1,120/day and the rest unchanged on the Slovak
pages. Flagging once, not arguing it: those are Austrian day rates shown to Slovak buyers.
You chose faithful — noted and executed as chosen. Say the word if that flips.

**7.4 · `/ueber-mich/` — DEFERRED to wave 1b.** It is de-linked from the German nav and out of
the sitemap because it is being reworked; translating it now means translating it twice.
Wave 1 ships **seven** pages (~770 units). The outreach click path is landing → trainings →
coaching, and about-me is not on it. Default applied 2026-08-04, reversible on one word.

## 8 · Execution sequence

**Phase 0 — clean ground (before any translation)**
1. Register `jakubpopluhar.sk`, configure 301 → `jakubpopluhar.com/sk/`.
2. Fresh branch `sk-uebersetzung` off `origin/main` in an **isolated worktree** — parallel
   windows are live on this repo and the local copy is stale and dirty. Non-negotiable.
3. Register the strand in `SITREP.md` so the other windows see it.

**Phase 1 — glossary first**
4. Extract all translatable units from the eight German sources; get the real landing count.
5. Build `glossary_de_sk.md` from §6 plus a terminology sweep of the extracted set.
   Commander signs off on the ~40 locked terms **before** a single page is translated.
   This is the step that makes passes 2 and 3 cheap.

**Phase 2 — translate**
6. Run `translate-document` per page, source of truth = the German page, glossary enforced.
7. Dedicated currency + date pass (they bypass the extractor).
8. JSON-LD / structured data pass — the EN run found six course names sitting inside a
   `<script>` block that the extractor masks by design. Same trap here.

**Phase 3 — verify**
9. Proofreader pass (iter 1), then gatekeeper pass. Report both, apply or overrule with reasoning.
10. Automated checks: tag parity DE/SK per pair, 0 dead internal links, hreflang in all
    directions, no German remnants in SK body text, price arithmetic, testimonial fidelity.
11. Mobile check at 390px. SK runs roughly level with German in length, but German compounds
    become Slovak multi-word phrases — nav items and the price grid are the wrap candidates.

**Phase 4 — wire up**
12. **Language switcher becomes three-way (DE/EN/SK) — but only on pages that have a Slovak twin.**
    Eight pages get SK in the switcher; the blog, `/termine/` and `/ki-check/` keep DE/EN.
    hreflang must only ever point at pages that exist.
13. `sitemap.xml` + `robots.txt` + `llms.txt` updated. Canonical tags on every new page.
14. Preview to commander. **No push before explicit sign-off** (`feedback_preview-before-push`).
15. Push, verify live, run `website-health-check`.

## 9 · Wave 2 (after outreach is running)

`/termine/`, `/ki-check/`, then the blog (13 articles). The blog is a trust engine but no
first-contact outreach click lands there, and the articles are Austrian-context-heavy.
Deliberately deferred, not forgotten.

## 10 · PACE

- **Primary:** full pipeline as above, eight pages, glossary-first.
- **Alternate:** if the domain stalls at the registrar — build `/sk/` anyway, ship it under
  the .com URL, point the outreach mails at `jakubpopluhar.com/sk/` directly. The site is
  the blocker; the domain is cosmetics on top of it.
- **Contingency:** if time compresses before the first send — landing + `/trainings/` +
  `/ki-personal-training/` only (four pages, ~590 units). That is a complete click path.
- **Emergency:** landing page alone in Slovak, everything else linking to the German pages
  with an honest "in German" label — the pattern already used for the German course PDFs
  on the English track.
