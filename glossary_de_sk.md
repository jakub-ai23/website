# Glossary DE → SK · jakubpopluhar.com/sk/

Created: 2026-08-04 · Last updated: 2026-08-04
Status: **LOCKED — commander signed off §1 on 2026-08-04.** All four decisions applied as
recommended: školenie/tréning split (§1.1), AI not UI (§1.2), Váš lektor (§1.3), vykanie (§1.4).
Companion to `glossary_de_en.md`. Same enforcement model: every entry below is *locked* —
the translator does not vary it for style, and the gatekeeper greps for violations.

Scope: wave 1, seven pages, 767 units / 5,272 words (measured 2026-08-04).

---

## 1 · The four decisions that need your call

These are load-bearing. Each one appears dozens of times; changing one later means
re-reading every page.

### 1.1 · "Training" — the product name itself

German uses *Training* for both the group courses and the 1:1 product. Slovak splits them:

| | Recommendation | Why |
|---|---|---|
| Group/corporate courses (`/trainings/` + 4 course pages) | **školenie** / **školenia** | This is the standard Slovak term for corporate training. A Slovak HR manager buying a course buys a *školenie*. *Tréning* in this slot reads as sport or soft-skills coaching. |
| The 1:1 product (`/ki-personal-training/`) | **AI osobný tréning** | Here *tréning* is correct and deliberate — the whole page runs on the personal-trainer metaphor ("Ein Seminar zeigt, was KI kann. Hier richten wir sie ein."). Keeping *tréning* keeps the metaphor. |

**This split is the single highest-impact choice in the document.** Alternative: use *tréning*
everywhere for brand consistency and accept that the course pages read slightly off-register.

### 1.2 · "KI" → **AI**, always. No "umelá inteligencia" anywhere.

**Revised by the commander 2026-08-04** (original rule glossed the first mention per page as
*umelá inteligencia*; that is now withdrawn). Every KI becomes **AI**, including first mention,
headlines, meta descriptions, course titles and JSON-LD. **Never "UI"** — that reads as
*užívateľské rozhranie*. Compounds follow: *KI-Trainer* → *AI tréner*, *KI-Helfer* →
*AI pomocníci*, *KI am Schreibtisch* → *AI pri stole*.

**AI is indeclinable in Slovak.** Every replacement is checked in context, never swept: the
surrounding preposition and verb must carry the case the noun used to. `pre umelú inteligenciu`
→ `pre AI`, `v ére umelej inteligencie` → `v ére AI`, `už umelú inteligenciu používajú` →
`už AI používajú`.

**Watch the density.** A literal swap can stack three `AI` in one sentence where the German had
two. The trainer bio is the known case: DE `KI-Trainer und Implementierungsberater mit Fokus auf
Künstliche Intelligenz und Konsumentenpsychologie` carries KI twice, so the Slovak carries AI
twice — `AI tréner a implementačný poradca so zameraním na AI a spotrebiteľskú psychológiu`.
Where the German itself repeats (`Grundlagen der Künstlichen Intelligenz: was KI ist`), the
Slovak repetition is faithful and stays.

### 1.3 · "Ihr Trainer" → **Váš lektor**

*Lektor* is the standard Slovak word for the person delivering a course. *Tréner* would pull
back toward sport. Appears as an h2 on all four course pages.

### 1.4 · Register: **vykanie** throughout

The German source is Sie-Form. B2B Slovak matches. No tykanie anywhere, including CTAs and
form labels. Consequence to watch: German *Sie* is number-neutral, Slovak *vy* + participle
must agree — singular decision-maker vs plural team is a real choice on every imperative.
Default: address one person (the decision-maker reading the page), not the team.

### 1.5 · Register: business-standard Slovak, **anglicisms kept** (commander, 2026-08-04)

Target dialect: standard Slovak (spisovná slovenčina), B2B, vykanie. The working vocabulary of
Slovak office life **stays English** where that is how people actually speak:

**Keep in English:** AI · prompt · workflow · e-mail · meeting · chatbot · Copilot · online ·
software · notebook / laptop · dashboard · tím (Slovak spelling of team)

**Still translate:** the surrounding prose, all headings, all commercial terms, all legal text.
The anglicism licence covers tooling vocabulary only — it is not a licence to leave German or
English sentences standing.

Target reader: an HR director or managing director in Bratislava. The page should read like a
Slovak consultancy wrote it, not like a translated textbook. **AI tic to avoid:** over-explaining
an anglicism in brackets on every use. First mention may gloss it; after that, use it bare.

---

## 2 · Locked terms

| German | Slovak | Note |
|---|---|---|
| KI | AI | §1.2 |
| Künstliche Intelligenz | umelá inteligencia | first mention per page |
| KI-Trainer & Konsumentenpsychologe | AI tréner a spotrebiteľský psychológ | badge, appears in title + meta |
| Konsumentenpsychologie | spotrebiteľská psychológia | also the course title |
| Training (group) | školenie | §1.1 |
| Trainings (plural, catalogue) | školenia | §1.1 |
| KI-Personal-Training | AI osobný tréning | §1.1, product name |
| Ihr Trainer | Váš lektor | §1.3 |
| Teilnehmende / Teilnehmer | účastníci | |
| Führungskräfte | manažéri | not *vodcovia* |
| Unternehmen | firma / spoločnosť | *firma* in body copy, *spoločnosť* in legal |
| Team | tím | |
| Erstgespräch | úvodný rozhovor | booking CTA |
| Strategiegespräch | strategický rozhovor | booking CTA |
| Session | sedenie | on `/ki-personal-training/` |
| Warum dieses Training? | Prečo toto školenie? | h2, all four course pages |
| Kursinhalte | Obsah kurzu | h2 |
| Das Format | Formát | h2 |
| Was lernen die Teilnehmenden? | Čo sa účastníci naučia? | h2 |
| Für wen eignet sich dieses Training? | Pre koho je toto školenie vhodné? | h2 |
| Häufige Fragen | Časté otázky | h2 |
| Neueste Beiträge | Najnovšie články | h2, landing |
| Vorher vs. Nachher | Predtým vs. potom | h2, landing |
| netto | bez DPH | 8 occurrences |
| Impressum | Impressum → **Kontaktné údaje / Prevádzkovateľ** | not a Slovak legal category; see §5 |
| Datenschutz | Ochrana osobných údajov | |

## 3 · Names that do NOT translate

ARS Akademie · tecTrain · REAL TEAM · Sport Union · FitRock · Innovatic Group ·
YouKnowMeBest · ZR Team Vienna · became ai · Microsoft 365 Copilot · SURF

Course *titles* translate. Institution names do not. The EN run locked the same rule.

## 4 · Formatting rules (mechanical, gatekeeper-enforced)

1. **Currency.** German `1.120 €` → Slovak `1 120 €` — space as thousands separator
   (non-breaking), € after the number with a space. **13 price strings in scope; six carry the
   German thousands dot** (1.120 ×2, 2.320, 1.920, 1.740, 1.500, 1.160) and would otherwise read
   as 1.12 euros. The EN run proved bare price strings bypass the text extractor entirely
   because they contain no letters → **dedicated currency pass, mandatory.**
2. **Dates.** `30.09.2026` → `30. 9. 2026` (space after each dot, no leading zero).
   `10. Juli` → `10. júla` (genitive, lowercase month).
3. **Quotation marks.** SK uses `„…"` — identical to German. **No conversion.** Unlike the EN
   run, German-style quotes in the Slovak files are *correct*; the grep check inverts.
4. **No em-dash (U+2014) or en-dash (U+2013).** Standing rule. Grep the two separately.
5. **Slugs mirror the German**, as the EN track does: `/sk/trainings/hr-kurs/`,
   `/sk/ki-personal-training/`. Slovak URLs will contain German words. Accepted trade —
   it keeps DE/EN/SK structurally parallel and hreflang trivial.
6. **JSON-LD.** Structured data sits inside `<script>` blocks that the extractor masks by
   design. The EN run found six German course names and six German URLs left behind there.
   Separate pass, every page.

## 5 · Legal pair — REAL TEAM, s.r.o.

Verified identifiers (`memory/real-team.md`, `real-team/CLAUDE.md`, `rt-sport/pravne.html`):

- Obchodné meno: **REAL TEAM, s.r.o.** (registered name — *not* "REAL TEAM Sport s.r.o.",
  which is the trade name used on the sport site's footer)
- IČO **31 369 049** · DIČ/IČ DPH **SK2020873745**
- Sídlo **Pri kríži 18, 841 02 Bratislava**
- Mestský súd Bratislava III, Oddiel Sro, Vložka č. **6700/B**
- Konateľ: Jakub Popluhar

Template: `~/Projects/builds/websites/rt-sport/pravne.html` — a live Slovak legal page for this
exact entity. Adapt, do not rewrite. Note that *Impressum* is an Austrian/German legal category;
the Slovak page is structured as prevádzkovateľ + kontaktné údaje.

**Open at build time:** whether the SK pages carry the same data flows as the DE privacy page
(Formspree, Brevo, Clarity, cal.eu). If yes, the DE privacy content translates and only the
controller block swaps to REAL TEAM.

## 6 · Semantic-weight phrases — meaning survives or the translation is wrong

Carried from `glossary_de_en.md` §10.3. These are commercial commitments, not copy:

1. The in-house-only exclusion.
2. Laptop **recommended, not required**.
3. Free versions cover **all** content.
4. Both hedges (the two qualifying statements the EN gatekeeper tracked).
5. Testimonials — given in German. Translate for comprehension, **add nothing**.
   **Speaker gender is locked (commander-confirmed 2026-08-04).** Slovak past tense encodes
   the speaker's gender where German does not, so every testimonial forces a choice. These are
   real people; the forms below are confirmed, not inferred, and must not be changed:
   - **Tea Shashaj** — feminine (`Myslela som si`)
   - **Katarzyna R. Pichler** — feminine (`zmenila`, `objednala`, `Angel investorka roka 2025`)
   - **Patrik Hubek** — masculine (`som mal`)
   - **Petar Pecija** — masculine (`Nevedel som`)
   Any future SK page carrying a new named testimonial: make the choice, flag it, get it
   confirmed. Never infer gender from a given name.
6. Price arithmetic must survive: 4 × 280 = 1 120 against 4 × 290 = 1 160.

## 7 · Layout risk

Slovak runs roughly level with German in length, occasionally shorter. The wrap candidates are
where German compounds become Slovak multi-word phrases — nav items, the six catalogue cards,
and the price grid. Check at 1440px and 390px, same as the EN run.
