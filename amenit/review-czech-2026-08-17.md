Created: 2026-08-17
Reviewer: Lapras (critic agent)
Reviewed: `amenit/index.html` (CZ translation of `ewi-cv-v2-sk/index.html`) — pre-call to Jan Klanica, Školicí středisko Amenit, 13:00 today.

# Findings

## 1. `Viedeň` left untranslated in the CV — BLOCKER
- **Location:** line 355, `<div class="o">Viedeň</div>` (job entry "Samostatný školitel", 01/2025–současnost).
- **Current:** `Viedeň`
- **Replace with:** `Vídeň`
- **Reason:** `Viedeň` is the Slovak spelling. Every other occurrence of the city on this page is correctly `Vídeň` (line 366, line 554) — this is the one spot the translation pass missed. This is the single most literal version of the exact risk you named in the brief: a Czech reader hits a Slovak word inside a Czech CV line. It sits directly under the greeting where he's most likely to read carefully (he's a training-center director, CVs are his job).
- **Confidence:** High. Not a judgment call — `Viedeň` is not a Czech word under any spelling convention.

## 2. Recipient's surname declension — internally inconsistent, BLOCKER (needs a decision, not just a fix)
- **Location A (vocative):** line 583 (`<script>`), `var text = 'Dobrý den, pane Klanico';`
- **Location B (genitive):** line 279, `<p class="eyes-only">Jen pro oči <strong>pana Klanici</strong></p>`
- **Problem:** these two forms come from two *different* declension paradigms and contradict each other. If "Klanica" is declined as a regular Czech noun ending in -a (the "žena" pattern — žena/ženy/ženě/ženu/**ženo**/ženě/ženou, the pattern that produces the vocative "Klanico" the page already uses), the genitive under that same pattern is **"Klanicy"**, not "Klanici". "Klanici" is not a genitive ending that exists for any noun ending in -a in standard Czech declension — it reads like a leftover "-ice" pattern (ulice-type) that doesn't apply here, or a Slovak-influenced instinct, either way it doesn't match the paradigm the vocative already commits to.
- **My confidence on the fix is medium, not high** — because the harder question is whether "Klanica" should be declined at all. It's an unusual surname for a Czech ear (looks Slovak/Balkan in origin), and standard Czech practice for surnames whose declension is unclear or contested is to leave them **undeclined** and carry the case entirely on "pan/pana/pane": "pane Klanica" (vocative), "pana Klanica" (genitive). That's not a cop-out, it's the recommended move specifically to avoid the trap this page is currently in — guessing wrong at two different endings for the same name in front of the man himself.
- **Two ways to fix, pick one, don't leave it split:**
  - (a) Safe/recommended: `pane Klanica` (line 583) and `pana Klanica` (line 279) — surname undeclined both times.
  - (b) If you're confident he'd expect it declined: `pane Klanico` (line 583, already correct) and `pana Klanicy` (line 279, fix from "Klanici").
- **I cannot verify with certainty which the man himself would consider correct for his own name** — that's genuinely knowable only by him or someone who's seen his name declined before (an email signature, a colleague addressing him). If there's any way to check that before 13:00, do it; otherwise take option (a), it cannot be wrong.

## 3. Closing quotation mark is a straight ASCII quote, not Czech typography — SHOULD-FIX
- **Location:** line 513, `Navazuje na základy z „AI za pracovním stolem".`
- **Current:** opens with the correct Czech low quote `„` but closes with a plain straight `"` (U+0022).
- **Replace with:** `„AI za pracovním stolem"` — closing character should be `"` (U+201C), which is the correct Czech **closing** quote glyph (Czech convention: „text" — opens low-9, closes with what looks like an English opening curly quote).
- **Reason:** small but a native reader's eye catches mismatched quote glyphs, and it's the only piece of directly-quoted title text on the page, so it's visible.
- **Confidence:** High on what's wrong (mismatched glyph), high on the fix.

## 4. "Moje školení" language claim vs. the email — compliant, no fix needed
- **Text checked:** *"Každé školení vedu prezenčně, online i hybridně, německy, anglicky a slovensky, na přání i česky."*
- **Against his email:** *"Školím hlavně v němčině a angličtině, mateřským jazykem je slovenština, a pokud budete chtít, odškolím i v češtině."*
- **Verdict:** does not overstate. Czech ("na přání i česky") stays conditional/on-request, matching "pokud budete chtít" in the email. Nothing invented.
- **One soft note (NICE-TO-HAVE, not a fix):** the page lists German, English, and Slovak as three co-equal delivery languages, while the email put German+English as "hlavně" (mainly) with Slovak framed differently (mateřský jazyk). This isn't a fabrication — the page's phrasing is inherited near-verbatim from the Slovak original's own service list, it's just a slightly different emphasis than the specific email he sent this specific contact. Not worth blocking on; flagging only so you're aware if Klanica compares the two.

## 5. AI-tell / voice check — clean
Scanned "Moje školení", the six training cards, the "tři silné stránky" block, and the jump-section copy against Jakub's established voice (direct, concrete, states limits). No hollow triads, no "nejen... ale i", no inflated adjectives, no generic consultant filler found. Lines like *"Kde je Copilot spolehlivý, kde ne, a kde reálně ušetří čas místo toho, aby jen blikal"* and *"Žádný standardní program z police"* are his voice and should stay untouched. The slightly odd phrase *"jeho zvláštnosti, jeho hranice, jeho cesty"* (ChatGPT/Gemini/Claude card) reads a touch awkward in both languages, but it's a faithful carry-over from the Slovak original, not a new AI-sounding insertion — leaving it is defensible, tightening it is optional (NICE-TO-HAVE, not flagging a replacement since it's not broken, just slightly loose).

## 6. Register and other grammar spot-checks — clean
- `školení` used consistently and correctly for corporate training throughout; `trénink` (sport-register) never misapplied.
- `Vídeň`/`Vídni` case forms elsewhere on the page are correct Czech.
- No other slovakisms or false friends found in the visible copy I could confidently judge.
- Could not fully verify: idiomatic naturalness of every single sentence at native-speaker fluency — I flagged everything I have concrete grounds to flag; anything not listed above I'm not raising, but I'm not a substitute for a native Czech proofread on a page this consequential.

# Verdict: **FIX-FIRST**

Two BLOCKERs, both small, both fast to fix, both exactly in the two places Klanica is most likely to notice (the greeting with his own name, and the CV line right below it):
1. `Viedeň` → `Vídeň` (line 355)
2. Resolve the Klanica vocative/genitive mismatch — recommend undeclined `Klanica` in both spots (lines 279 and 583) unless you have a way to confirm he expects it declined before 13:00.

Everything else (quote glyph, language-claim nuance, "jeho cesty") is SHOULD-FIX or NICE-TO-HAVE and does not block sending once the two BLOCKERs are closed.
