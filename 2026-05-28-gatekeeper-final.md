# Gatekeeper Critique — Third-Pass Independent Review (en/index.html)

Date: 2026-05-28 | Target: Neutral EU business English | **VERDICT: SHIP**

Independent third pass after translator + proofreader (both SHIP). Evaluated fresh against source + glossary. **Zero CRITICAL, zero HIGH findings.**

## 1. Structural parity — PASS
All counts identical src/tgt: training-card 14/14, testimonial-card 11/11, proof-grid 3/3, about-credentials 6/6, podium-list 4/4, cta-offer-card 10/10, nav `<li>` 25/25, `<tr>` 10/10, `<section>` 9/9. No structural drift.

## 2. Number/name/date parity — PASS
- Names exact: Katarzyna Renata Pichler (2/2), Katalin Novák, Djordjija Petkoski, Gjorge Ivanov (2/2), M.Ed. — all preserved.
- Email jakub@popluhar.at present.
- Dates localised correctly: 25.06.2026→25 June 2026; 06.07.2026→6 July 2026; 15.07.2026→15 July 2026.
- **Number-set diff (1618 vs 1614) fully explained, NOT a defect:** leading zeros in DE dates (06/07) dropped on localisation; DE "45 Minuten" rendered as spelled "Forty-five minutes" (intentional English style). All semantic numbers preserved.

## 3. Dash grep — PASS
Both `—` and `–` sweeps: only HTML/CSS comments (lines 1579, 1938). Zero in rendered body. Body uses " - " spaced hyphen (Austrian-syntax carry-over, consistent).

## 4. Semantic shifts (§5) — PASS
Commercial weight preserved with natural wording (literal grep missed them, manual read confirmed):
- "Every session delivers a concrete output you can put to use immediately" (= konkreter Output, sofort einsetzbar).
- "40 minutes saved a day" (= 40 Minuten pro Tag gespart).
- "I come to you", "your office, your machine, your data security", AI Literacy / EU AI Act Art. 4 all intact.

## 5. Locked phrases (§4) — PASS
All verbatim, 1 occurrence each: hero sub, "No lectures. No off-the-shelf programme.", "On stage with heads of state", CTA "How can your company adopt AI if you haven't done it yourself?", "It works.", "You don't know what you don't know", "runs on my own machine first", "within 24 hours".

## 6. AI-tells — PASS
Zero hits for elevate/unlock/supercharge/leverage/empower/seamless/cutting-edge/"in today's".

## 7. German fragments — PASS
Zero German stopwords in body. Exempt payloads correctly German: `value="Keynote / Impulsvortrag"`, `value="Inhouse-Training (Team)"` (selectInterest() backend strings — must stay German). Footer "Impressum"/"Datenschutz" labels German by design.

## 8. Fixes verification — PASS
iter-1+2 fixes all live: EN error string "Error - please try again" (2426, 2430); schema/og/canonical → https://jakubpopluhar.com/en/ (12, 19, 1768); training tag "Programme"; testimonial "bringing in new members" (2148). No nearby grammar/markup breakage.

## 9. Asset path sanity — PASS
All fonts use ../ (lines 25-29); images src use ../ ; data:/SVG-fragment url() and #goldGlow refs correct; og:image/twitter:image use absolute https (correct). Internal anchors (#about/#services/#proof/#contact) unchanged. Footer legal → ../impressum.html / ../datenschutz.html.

## 10. HTML validity + extras — PASS
Tags balanced: section 9/9, div 86/86, ul 5/5, table 2/2. **`<html lang="en">` correctly set** (was `de` in source — confirmed flipped).

## Summary
| Severity | Count |
|---|---|
| CRITICAL | 0 |
| HIGH | 0 |
| MED | 0 |
| LOW | 0 |

No findings. The two prior agents' SHIP verdicts hold under adversarial third-pass review. **Recommend final visual eyeball** (render /en/index.html in browser) to confirm font loading via ../ paths and snap-scroll behaviour — the only thing static analysis cannot verify.
