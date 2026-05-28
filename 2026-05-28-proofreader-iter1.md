# Proofreader Critique — Iteration 1 (DE→EN, en/index.html)

Date: 2026-05-28
Target dialect: Neutral EU business English
File: `en/index.html`  | Source: `index.html` | Glossary: `glossary_de_en.md`

## Verdict: NEEDS-FIX

Counts: CRITICAL 2 | HIGH 2 | MED 1 | LOW 0 blocking

---

## CRITICAL

**1. German string leaked in JS catch branch** — line 2430
- PROBLEM: `btn.textContent = 'Fehler - bitte erneut versuchen';` (network-error path; happy-path else was already English)
- FIX: `btn.textContent = 'Error - please try again';`
- STATUS: APPLIED

**2. Schema `url` not updated to /en/** — line 1768
- PROBLEM: `"url": "https://jakubpopluhar.com"` (og:url + canonical correctly read /en/, schema did not)
- FIX: `"url": "https://jakubpopluhar.com/en/"`
- STATUS: APPLIED

## HIGH

**3. Typewriter gold-highlight split** — lines 2245-2254
- PROBLEM (critic): glossary §4 said full completion should be gold; implementation golds only the tail.
- ORCHESTRATOR DECISION: OVERRULED / KEPT CURRENT. The German source uses white-lead-in + gold-tail (`white "was Sie " + gold "nicht wissen."`). The current EN split (`white "what " + gold "you don't know."`; `white "what your competitors " + gold "already use."`) faithfully mirrors that rhetorical device — the gold highlights the punch/echo. Glossary §4's instruction to gold the entire completion was over-prescriptive. No change.
- STATUS: NO CHANGE (intentional)

**4. "Course" undersells Lehrgang** — line 2100
- PROBLEM: `<span class="training-tag">Course</span>` — a 2-day ARS Lehrgang is a structured programme.
- FIX: `<span class="training-tag">Programme</span>` (matches "off-the-shelf programme" usage + EU/UK spelling lean)
- STATUS: APPLIED

## MED

**5. Translation-y calque** — line 2148
- PROBLEM: `for winning new members` (calque of "Mitgliedergewinnung")
- FIX: `for bringing in new members`
- STATUS: APPLIED

## CLEAN (verified)
- Em-dashes / en-dashes: zero in rendered body (only CSS/HTML comments, exempt).
- AI tics: none (no elevate/supercharge/leverage/unlock/empower/seamless/cutting-edge).
- Locked-rhythm §4 phrases: all verbatim correct (hero sub, "No lectures. No off-the-shelf programme.", "On stage with heads of state", CTA, "It works.").
- Semantic §5: "concrete output you can put to use immediately", "within 24 hours", "saves 40 minutes a day", "AI Literacy per EU AI Act Art. 4", "I come to you", "runs on my own machine first" — all preserved.
- Dates: 25 June 2026 / 6 July 2026 / 14-15 July 2026 — EU format, consistent.
- HTML structure: 9 slides, 3 training cards, 3 proof testimonials, nav, footer — intact.
- selectInterest() / option value= payloads unchanged. Footer Impressum/Datenschutz → German pages (correct).
- lang="en", og:locale="en_GB", schema addressLocality "Vienna".
