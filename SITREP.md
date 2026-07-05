# SITREP — jakubpopluhar.com Positioning + Website-Update

*Created: 2026-07-02 11:30 · Zweck: Wiedereinstieg. Lies das zuerst, dann mach genau hier weiter.*

## Lage in einem Satz
LinkedIn-Positioning ist FERTIG und locked (Headline + About, EN+DE, HD im Vordergrund); jetzt muss dieselbe gelockte Sprache auf jakubpopluhar.com runter, und die kaputten ARS-Trainings-Termine gehören gefixt, alles mit dem Commander im Loop (NICHT blind).

## Was erledigt wurde
- LinkedIn: Headline (EN+DE), About (EN+DE), Mindworx-Entry, alles locked + vom Commander live gesetzt.
- Working Plan komplett: `STANDING-ORDER-positioning-and-changes.md` mit ⭐ LOCKED COPY (Headline + About EN/DE) = die eine Quelle für alles Weitere.
- Fakten korrigiert + festgeschrieben: Staatsexamen (nicht 2 Master), 4. Sprache, 3. Generation Coach, Floorball/Roundnet/PADI, SURF raus, BJJ raus, "Hill compensation expertise" gekillt, PE-CEO-Coaching = getrennt von HD.
- Portrait-Empfehlung: 11.png (Profilbild) / 15.png (Banner).

## Aktueller Stand
- jakubpopluhar.com = NOCH ALT: Repo `jakub-ai23/website`, lokal `~/Projects/builds/websites/personal/`, live via GitHub Pages (CNAME). Positioning noch Mindworx/SURF, KEIN Hill Digital. 2 von 3 Trainings-Terminen falsch (Copilot 25.06 = vorbei, Konsum. 06.07 -> real 06.11), Claude-Seminar 16.10 fehlt ganz.
- Nichts an der Website angefasst/gepusht in dieser Session (bewusst: Commander will dabei sein).

## Blocker
- Läuft nur MIT dem Commander (er will folgen, nicht blind deployen). Darum als eigener Kalender-Block 17:30-18:30.
- ARS-Seminar-URLs müssen live verifiziert werden (ARS vergibt pro Termin neue ID; alte 25.06-IDs sind tot).

## Naechster Schritt (genauer Einstiegspunkt)
1. Öffne `STANDING-ORDER-positioning-and-changes.md`, Section 2c: die 3 Trainings-Termine in `index.html` (Z. 2117/2127/2137) fixen + Claude-Karte (16.10) ergänzen. ARS-URLs vorher read-only verifizieren (welche ID ist live).
2. Section 2a/2b: Positioning HD-foreground (title Z.6/9/16, JSON-LD Z.1805, Hero-Badge Z.1890, SURF-Badge Z.1936 RAUS, Credential Z.1961, about-stat Z.1948).
3. Section 2e: About-Slide-Text (Z.1956/1957) aus der DE LOCKED About kondensieren.
4. Preview lokal zeigen -> Commander-OK -> Mobil-Check (`infrastructure/website-mobile-check.sh` im HD-Repo-Muster; hier eigenes Repo) -> Push `jakub-ai23/website`.

## Offene Entscheidungen
- LinkedIn Education-Einträge (2× "Master of Education - MEd") vs. Staatsexamen: relabeln? (im Plan als Verify-Item).
- Website: HD-Tagline "Human in the Lead. KI im Hintergrund." auf der Personal-Site nutzen ja/nein (optional).

## Termine
- Do 02.07 17:30-18:30: dieser Website-Block (Kalender, colorId Peacock).
- Danach Ripple: ARS-Bio + tecTrain-Bio (DE medium master bio + Foto), Brevo-Auth jakubpopluhar.com.

## Datei-Quick-Ref
- Plan + LOCKED COPY: `STANDING-ORDER-positioning-and-changes.md`
- Website: `index.html` (Slide 2 About Z.~1929-1966, Slide 7 Trainings Z.~2096-2144)
- Debrief dieser Session: `~/Projects/ops/mission-reports/2026-07-02-linkedin-positioning-hd-foreground.md`

---
*Last updated: 2026-07-02 11:30*
