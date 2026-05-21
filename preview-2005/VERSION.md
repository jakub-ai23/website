# Hill Digital Website — Versions-Log

*Append-only Log aller Etappen-Commits. Format: `vX.Y · YYYY-MM-DD HH:MM · Beschreibung`*

---

## v1.45 · 2026-05-21 13:10 · [K] · TEA-04 (Workshop wall) neben „Ein Tag im Leben Ihrer HR-Leitung."

Donnerstag-Section-Head auf zwei-spaltigen Grid umgestellt: links Eyebrow + h2 + Lead, rechts TEA-04 „Workshop wall, sticky notes" Foto in B&W (Aspect-Ratio 4/3, grayscale-Filter, leichter Shadow). Inline-Grid mit minmax-Columns für stabile Spaltenbreite.

---

## v1.44 · 2026-05-21 13:04 · [K] · Hero-Foto auf TEA-02 (Standing briefing) gewechselt.

Hero-Bild auf der Homepage neben Headline „Mehr Zeit für Menschen" von POR-04 (Frau am Fenster, `photo-1521737711867`) auf TEA-02 „Standing briefing" (`photo-1542744173`) aus dem Photo-Katalog gewechselt. Alt-Text mit angepasst.

---

## v1.43 · 2026-05-21 10:31 · [K] · Hero-Claim final: „Human in the Lead. AI in Support."

Vom Hero-Claim-Label `.hero-claim` aus v1.42 („Human in the Lead. KI im Hintergrund.") auf den finalen Brand-Satz „Human in the Lead. AI in Support." umgestellt.

---

## v1.42 · 2026-05-21 10:10 · [K] · Hero-Claim umformuliert: „Human in the Lead. KI im Hintergrund." statt „Sovereign AI for HR · People First".

Index-Hero-Claim-Label oben im Hero (`.hero-claim`-Span) auf den Hill-Digital-Positionierungs-Refrain aus dem Briefing umgestellt.

---

## v1.41 · 2026-05-20 21:00 · [K] · Logo-Files freigestellt, plus Browser-basierter PNG/JPG-Exporter

- Neuer Ordner `assets/img/logo/` mit fünf freigestellten SVG-Varianten:
  - `hill-digital-mark.svg` (Mark only, Color, Berg Grau plus Bogen Yellow-zu-Orange)
  - `hill-digital-mark-white.svg` (Mark only, Berg Weiß für dunklen Hintergrund)
  - `hill-digital-mark-mono.svg` (Mark only, alles Charcoal für Einfarb-Druck)
  - `hill-digital-logo.svg` (Full Logo, Mark plus Wortmarke Source Sans 3 Bold)
  - `hill-digital-logo-white.svg` (Full Logo, Wortmarke Weiß)
- Alle SVG mit transparentem Hintergrund, viewBox sauber definiert, viewBox 100x100 für Marks und 360x100 für Full-Logos.
- `logo-export.html`: Browser-basierte Konverter-Seite, zeichnet jedes SVG via Canvas und exportiert als PNG oder JPG in mehreren Größen. Buttons triggern direkten Download. Funktioniert ohne externes CLI-Tool.
- Hinweis: Wortmarke aktuell als SVG-Text-Element mit Source-Sans-3-Fallback. Für Print-Output ohne Schrift-Abhängigkeit Wortmarke in Vektor-Tool in Pfade umwandeln.

---

## v1.40 · 2026-05-20 20:50 · [J] · AGB v1.0 publiziert, Footer-Sync, Nav "AI Trainings"

- `agbs.html`: Volltext AGB v1.0 B2B aus `Hill_Digital_AGB_B2B_v1.0.docx` publiziert. Alle `[●]`-Platzhalter mit HWDigital-Daten ersetzt (FN 537930z, ATU 75762667, GF Melanie Hill BA, Kölblgasse 2, 1030 Wien, office@hill-woltron-digital.com). Anlagen 1–4 referenziert (gesondert beizulegen, keine Subpages). Footer-Kontakt-Stubs gefüllt. Internen Hinweis entfernt.
- Footer-Spalte "Trainings" (mit Sub-Items) durch homogene "Leistungen"-Spalte ersetzt auf: `agbs.html`, `datenschutz.html`, `impressum.html`, `kontakt.html`, `news.html`, `trainings.html`, `ueber-uns.html`. Identisch zur Homepage: AI Recruiting · AI Onboarding · AI Enablement & Trainings · Suite (Phase 2).
- Nav-Header: "Trainings" → "AI Trainings" auf allen 11 live DE-Seiten. Recruiting + Onboarding bleiben generisch.
- Hinweis: EN-Seiten unverändert (eigener Footer mit alter Tuchlauben-Adresse, eigene Lane).

---

## v1.36 · 2026-05-19 01:05 · [K] · Logo-Konzepte Mood-Boards 3 und 4 dazu

- `logos-preview-3.html`: vier Outline-Varianten von Konzept A (Berg als reine Kontur statt gefüllt). Stroke-Width-Varianten 2px und 3px, Ridge-Only, Layered.
- `logos-preview-4.html`: drei Envelope-Arc-Varianten (E.1, E.2, E.3) nach Hill-Woltron-Original-Vorbild mit der langen Sweeping-Bogenlinie die den Berg umfasst. Plus Nav-Mockup-Zeile pro Variante.
- Mood-Boards, keine produktive Logo-Wahl getroffen. Stehen als Visual-Referenz bereit.
- Liegen analog zu `logos-preview.html` und `logos-preview-2.html`, schließen die Logo-Konzept-Galerie ab.

---

## v1.35 · 2026-05-19 00:55 · [K] · EN-Footer: „· Since 1975" raus aus Brand-Line in allen sieben EN-Files

- Alle EN-Files Footer-Heritage-Linie: „A Hill Woltron company · Since 1975" zu „A Hill Woltron company".
- Betroffene Files: `index-en.html`, `contact-en.html`, `imprint-en.html`, `heritage-en.html`, `standpunkte-en.html`, `privacy-en.html`, `suite-en.html`.
- Konsistent zur DE-Linie wo das Datum schon in v1.20+ aus dem Footer raus war.
- Mini-Ausnahme vom EN-Sperr-Constraint #1: einzelne Brand-Line-Korrektur auf Commander-Wunsch, kein voller EN-Sync.
- Nicht angefasst: `Since 1975` in Eyebrow- und Title-Tags (index-en, heritage-en), die warten auf v2.0-Vollsync. `photos-home.html` Slot-Label bleibt als Mood-Board-Kontext.
- DE-Footer-Zeile bleibt unverändert auf „Mitglied der Hill-Gruppe".

---

## v1.34 · 2026-05-19 00:45 · [K] · Methodik zu Expertise in Ueber-uns: Headline, Lead, Schule, Standort-Text, Statement

- `ueber-uns.html` Zeile 74: Headline „Methodik ist das, was bleibt." zu „Expertise ist das, was bleibt."
- Zeile 76: Lead „Methodik kommt vor Tool" zu „Expertise kommt vor Tool"
- Zeile 102: Timeline-Internationalisierung „mit klarer Methodik-Schule" zu „mit eigener Expertise" (Compound umgangen, klingt deutscher).
- Zeile 236: Hill-Standorte „Methodik fließt zwischen den Standorten" zu „Expertise fließt zwischen den Standorten"
- Zeile 261: Closing-Statement „Drei Generationen Methodik" zu „Drei Generationen Expertise"
- Stehen geblieben: „eine eigene Auditmethodik" auf Zeile 76 als geschlossener Fachterminus.
- Schließt v1.25/v1.30-Linie konsequent ab: „Hill-Methodik" raus, „HR-Expertise"/„Expertise" rein, jetzt auch auf der Ueber-uns-Seite.

---

## v1.33 · 2026-05-19 00:35 · [K] · „seit 1975" raus aus Ueber-uns Lead und Meta-Description

- `ueber-uns.html` Meta-Description (Zeile 7): „Drei Generationen Hill-Heritage seit 1975, das aktuelle Team" zu „Drei Generationen Hill-Heritage, das aktuelle Team".
- `ueber-uns.html` Lead-Paragraph (Zeile 56): „Drei Generationen Hill-Heritage seit 1975. Ein kleines, klares Team" zu „Drei Generationen Hill-Heritage. Ein kleines, klares Team".
- Heritage-Framing bleibt erhalten (drei Generationen), nur die Jahreszahl als Zeitanker raus. Timeline-Visual mit Jahr 1975 (Zeile 95) und englisches Quote „since 1975" (Zeile 138) bleiben unverändert.

---

## v1.32 · 2026-05-19 00:25 · [K] · Österreichisches Deutsch statt deutsches Deutsch: Feber statt Februar

- `news.html`: zwei Card-Meta-Zeilen „Februar 2026" zu „Feber 2026" (DACH-HR-Card und 20-bis-30-Prozent-Card).
- `trainings.html`: Zertifikat-Lead „seit Februar 2025" zu „seit Feber 2025" (Bezug EU AI Act Artikel 4).
- Ein klassisches DACH-vs-AT-Wortpaar. Alle anderen DE-Files sind bereits AT-konform (Wien, WKO, Firmenbuch, FN, UID-Nummer, GewO 1994, ECG, MedienG, DSG).
- `standpunkte-en.html` hat dieselbe Februar-Stelle, wird aber per Constraint nicht angefasst, kommt mit dem EN-Sync zu v2.0.
- Keine CSS-Änderung, keine Layout-Änderung.

---

## v1.31 · 2026-05-19 00:15 · [K] · CEE-Praxis statt DACH-Praxis in Drei-Pfeiler-Sektion

- `index.html` Pfeiler 02 (Heritage): „drei Generationen DACH-Praxis" zu „drei Generationen CEE-Praxis" geändert.
- Geografische Klarstellung: Hill-Gruppe (München, Wien, Warschau) reicht in CEE und nicht nur DACH, der Pfeiler-Text spiegelt das jetzt korrekt.
- Single-Word-Change, keine CSS-Änderung, keine anderen Files betroffen, kein EN-File angefasst.

---

## v1.30 · 2026-05-18 23:49 · [K] · Großer Visual-Polish-Sweep: Hill-Expertise, Schatierungen raus, Headlines, Team-Layout, Final-CTA-Iteration.

Lange iterative Etappe mit vielen kleinen Korrekturen auf Wunsch der Eigentümerin. Zusammengefasst:

**Sprache und Wording:**
- „Hill-Methodik" überall in `index.html` durch „Hill-Expertise" ersetzt (3 Stellen: Modul-Onboarding-Card, Promise-Section-Lead, Promise-Do-List-Item).
- Heritage-Pillar-Headline „50 Jahre HR-Expertise" zu „Erfahrung aus Jahrzehnten." geändert.
- Promise-Do-Bullet „Methodik schärfen: 50 Jahre Hill People-IP im Modell verankert." durch „Erfahrung aus Jahrzehnten. Strategien für morgen." ersetzt.
- Modul-Card-Labels umbenannt: „AI Recruiting" → „Recruiting", „AI Onboarding" → „Onboarding", „AI Enablement" → „AI Trainings". CTAs entsprechend.

**Headlines und Akzente:**
- Hero-h1-Underline-Akzent von „Weniger Zeit" auf „Mehr Zeit für Menschen" verlegt (umgesetzt schon in v1.29, hier nur Erwähnung).
- Pillars-Section-Headline „Drei Pfeiler, ein roter Faden: Human in the Lead." mit Zeilenumbruch vor „Human".
- ROI-Section-Head linksbündig statt zentriert.
- Final-CTA-Headlines: „Kein Sales-Pitch" auf index.html und „Ohne Verkaufsdruck" auf recruiting/onboarding in zweite Zeile mit Underline-Akzent verlegt.
- Modul-Section-Labels (Recruiting/Onboarding/AI Trainings auf Homepage) auf 1.35rem in Charcoal-Dunkel (initial Orange-d, dann auf Schwarz umgestellt).
- Persona-Section-Headlines auf recruiting/onboarding und Trainings-Karten-Titel auf trainings.html auf Schwarz-Charcoal-d statt Orange.

**Promise Do/Don't Section:**
- Spalten getauscht: „Was wir nicht tun" jetzt links, „Was wir tun" jetzt rechts.

**Über uns Team-Layout:**
- Reihenfolge der Featured-Team-Karten getauscht: Franz Hill links, Jakub Popluhar rechts.
- Franz-Eyebrow „Co-Founder, Heritage-Anker" → „CEO".
- Jakub-Eyebrow „CEO Hill Digital" → „Business Lead". Image-Alt und Final-CTA-Signatur auf index.html entsprechend angepasst.
- Franz-Foto auf `object-fit: contain` zentriert statt Cover-Crop.
- Jakub-Foto mit `transform: scale(1.5) origin top center` damit Kopf/Oberkörper größer im Frame.
- Erweitertes-Team-Heading „Hill-Gruppe Wien" mit Beschreibungs-Absatz entfernt. Drei-Frauen-Foto-Grid rückt direkt unter Franz/Jakub.

**Trainings-Subpage:**
- EN-Stamp („Also Available in English") rechts oben entfernt.

**Hero-Section:**
- „Drei Module ansehen" Ghost-Button entfernt (v1.29).
- Hero-Trust-Punkte EU AI Act / DSGVO / Plattform-Hill-Recruiter entfernt.

**Sub-Page Final-CTA:**
- „Was kommt"/Suite-Phase-2-Preview-Sektion auf `recruiting.html` und `onboarding.html` entfernt. Section springt direkt auf Final-CTA.

**Orange/Yellow-Schatierungen (Sub-Background-Gradients) global entfernt:**
9 Stellen in `hill.css`:
- `.section-cream::before` reduziert auf nur subtilen Grau-Schatten.
- `.page-header::before`, `.page-header::after` (Orange-Orb top-right 520×520px), `.hero::before`, `.hero-image::after`, `.philosophy::before`, `.module-detail-visual::before`, `.insight-feature-aside::before`, `.final-cta::before`, `.final-cta.with-bg-image::before` alle auf transparent gestellt oder Orange/Gelb-Anteile entfernt.

**ROI-Metric-Werte:**
- Farbe von Orange-Dunkel auf Charcoal `#575756` (Hill-CD-Grau).

**Footer-Newsletter:**
- Titel „Hill Digital Praxis-Notizen" auf 9 DE-Seiten zu „Hill Digital Newsletter" geändert.
- Beschreibungs-Absatz „Einmal im Monat. Werkstattnotizen…" auf 9 DE-Seiten komplett entfernt. Nur Headline und Form bleiben.
- Footer-Top-Padding von 4rem auf 1.5rem reduziert, Newsletter rückt näher an Final-CTA.

**Final-CTA-Background-Iteration (mehrere Zwischenschritte, Endstand):**
- War `--charcoal-d`, dann `--charcoal-x` (zu schwarz), dann `--charcoal` (grau), dann `--grey` (#B0B0B0 zu hell), dann `--white` (zu weiß), dann `--bg` (off-white), dann `--cream` (#F5F2EA, warmer Cream-Ton), final wieder `--charcoal-d` (dunkel).
- Final-CTA-Bottom-Padding von 4-6rem auf 1.5rem reduziert (Newsletter rückt enger heran).
- Dot-Konstellation-Overlay (`.final-cta::after`) per `display: none` deaktiviert.

**Über-uns Final-CTA-Button:**
- „Auf die Warteliste"-Ghost-Button entfernt, nur orange „Trainings ansehen" zentriert.

**Neue CSS-Komponenten (ergänzt zu v1.28):**
- `#module .training-card-tag` und `#wie .training-card .h3` / `#uebersicht .training-card .h3` als gescopte Regeln für Business-Area-Labels und Card-Titel.

**Was NICHT angefasst:**
- Archive (`_archive-*.html`) unverändert.
- EN-Files unverändert.
- Photographie-Regel (B&W, niemals Sepia) gilt weiter.

---

## v1.29 · 2026-05-18 21:30 · [K] · Hero-Polish: Underline auf „Mehr Zeit für Menschen", Ghost-Button und Trust-Punkte raus.

**Eigentümer-Feedback nach v1.28:**

- **Underline-Wechsel:** Gelb-Akzent sitzt jetzt unter „Mehr Zeit für Menschen" statt unter „Weniger Zeit". Der erste Halbsatz ist das Versprechen, der bekommt den Anker.
- **Hero-CTA-Stripped:** „Drei Module ansehen" Ghost-Button entfernt. Hero hat jetzt einen einzigen klaren Primary-CTA „60-Min. Discovery-Call buchen".
- **Hero-Trust-Punkte entfernt:** Die drei Punkte EU AI Act-ready / DSGVO by Design / Plattform plus Hill-Recruiter im Managed Service sind aus dem Hero raus. Inhalt taucht weiter unten in der Promise- und Warum-jetzt-Section auf, wo er kontextuell besser sitzt.

Stand nach dieser Etappe: Hero ist ruhiger, weniger Konkurrenz im First-Fold, klarer Single-CTA. Nur `index.html` angefasst.

---

## v1.28 · 2026-05-18 21:24 · [K] · Index neu: Reference-Content im Orange/Yellow Hill-CD. Sechs neue Sektionen, fünf neue CSS-Komponenten.

**Auftrag vom Eigentümer:** „Use the content from this index file AND apply Orange/Yellow corporate design. Take from this version logo, fonts, colors, photography and look & feel."

Heißt: Inhaltliche Struktur und Copy aus der ZIP-Referenz (`e60aeae2-...`), aber visuell komplett im bestehenden Hill-CD (Source Sans 3, Orange `#FFA014`, Yellow `#FAE600`, Charcoal, Cream-Background, B&W-Photography, Mountain-SVG-Logo).

**`index.html` komplett neu geschrieben (498 Zeilen):**

Sektionsfolge (gleich Referenz):
1. Hero (`.hero` `.hero-with-image`) — Logo + Nav mit 6-Link multi-page, Hero-Claim „Sovereign AI for HR · People First", H1 mit Yellow-Underline-Akzent „Weniger Zeit", Lead über 50 Jahre Hill People-Expertise plus AI-Module, zwei CTAs (60-Min Discovery-Call primary, Drei Module ansehen ghost), Hero-Trust-Punkte (EU AI Act-ready, DSGVO by Design, Plattform plus Hill-Recruiter), B&W-Foto rechts.
2. Pillars (`.pfeiler-grid`) — Drei Pfeiler People First / Heritage / Sovereign mit Hill-Methodik-Heritage-Erwähnung.
3. Pain Story (`.philosophy` + neuer `.pain-story` + `.pain-pullquote`) — dunkle Sektion, „Donnerstag, 14:30 Uhr · Sie kennen das Gefühl", zwei Narrative-Absätze, Pullquote mit Yellow-Border.
4. Modules (`.trainings-grid` + `.training-card`) — Drei Service-Cards AI Recruiting, AI Onboarding, AI Enablement, verlinken auf `recruiting.html`, `onboarding.html`, `trainings.html`.
5. Vorher/Nachher (`.day-grid` neu) — Drei-Spalten-Layout mit Pfeil dazwischen, Vorher-Karte grau, Nachher-Karte mit Orange-Border-Left und Orange-Bullet-Dots.
6. Promise Do/Don't (`.promise-grid` neu) — Zwei-Spalten-Karten, Do mit Orange-Check, Don't mit Grey-X, beide mit Orange-Border-Left bzw Grey-Border-Left.
7. ROI Metriken (`.metrics-grid` neu) — Vier Karten mit großen Orange-Werten und animierten Countern (IntersectionObserver-basiert), Indikative-Werte-Disclaimer drunter.
8. Warum jetzt (`.warum-grid`) — Drei Karten Demografischer Druck / EU AI Act / Agentic AI.
9. Final CTA (`.final-cta` + neuer `.cta-form` + `.cta-meta` + `.cta-signature`) — Dunkle Sektion mit Email-Form, Form-Action mailto an `digital@hill-woltron.com`, „Jakub Popluhar, CEO Hill Digital" als Signatur.
10. Footer — Bestehender Hill-Footer mit Newsletter, Footer-Inner-Grid, Hill-Woltron-Adresse Tuchlauben 17/10 Wien, alle Legal-Links.

**Em-Dashes aus Referenz durch Kommas ersetzt:** Diese SITREP-Regel wurde nicht überschrieben.

**`assets/css/hill.css` erweitert um neue Komponenten (~250 Zeilen append):**
- `.hero-trust` — Trust-Punkte-Zeile unter Hero-CTAs
- `.pain-story`, `.pain-narrative`, `.pain-pullquote` — Donnerstag-Sektion auf dunklem Background
- `.day-grid`, `.day-card`, `.day-vorher`, `.day-nachher`, `.day-arrow` — Vorher-Nachher-Layout mit Orange-Bullet-Dots
- `.promise-grid`, `.promise-card`, `.promise-do`, `.promise-dont` — Do/Don't mit Check und X-Icons
- `.metrics-grid`, `.metric-card`, `.metric-value`, `.metric-label`, `.metric-disclaimer` — ROI-Kachel-Layout
- `.cta-form`, `.cta-meta`, `.cta-signature` — Form-Layout für die Final-CTA-Sektion

**Counter-Animation** als IIFE im Inline-Script: IntersectionObserver lädt die Counter, sobald die Metrics-Section in den Viewport kommt. Easing-Funktion ist cubic-out.

**Form-Submit** öffnet `mailto:digital@hill-woltron.com` mit vorbefülltem Subject und Body.

**Stand:**
- index.html: neu im Hill-CD mit Referenz-Content
- Subpages (recruiting, onboarding, trainings, ueber-uns, news, kontakt, suite, impressum, datenschutz, agbs): unverändert in ihrem v1.25-Stand
- hill.css: erweitert um die neuen Komponenten, alle Bestandsklassen unverändert
- Keine fabrizierten Cases oder Personen. Alle Aussagen entweder direkt aus der Referenz oder dokumentierte indikative ROI-Spannweiten mit Disclaimer.

**Bekannte Open Loops:**
- Subpages haben die neuen Komponenten (Pain-Story, Day-Grid, Promise, Metrics, CTA-Form) noch nicht im Einsatz. Können in v1.29 nach Bedarf integriert werden.
- `recruiting.html` und `onboarding.html` verlinken zwar von der neuen Module-Section, ihr Inhalt ist aber noch der v1.24-Stand (Hill-Recruiting-Methodik-Sprache schon aktualisiert in v1.25). Wenn nötig: nächste Etappe Inhalt der Subpages aufs Module-Pattern ziehen.

---

## v1.27 · 2026-05-18 21:00 · [K] · REVERT v1.26 Brand-Pivot. Orange/Yellow Hill-CD bleibt die kanonische CDCI.

**Eigentümerin-Klarstellung:** „I want that Home and all the subpages are in the same corporate design! Exactly in this one" mit Screenshot der Orange/Yellow-Cream-Variante (Source Sans 3 Sans, Orange-Akzent, Yellow-Underline, B&W-Fotos auf cream-Background).

**Ich hatte die Anweisung „take the corporate design from localhost:8090/index.html?v=1779136336" falsch interpretiert** und das Navy/Gold-Inline-CSS aus der ZIP-Referenz als CDCI extrahiert. Tatsächlich gemeint war der v1.25-Stand der index.html, den die Eigentümerin in ihrem Browser-Tab vor sich hatte. Cache-Verzögerung im Edge hat den Missverstand begünstigt.

**Was diese Etappe macht:**
- `index.html` per `git checkout v1.25 -- index.html` zurück auf den Orange/Yellow-Stand (mit Säulen-Section, Personas-Section, Hebel 1 Underline, AT-Tonalität, HR-Expertise-Schliff)
- `assets/css/cdci.css` gelöscht. Die Navy/Gold-CSS war ein Sackgassen-Artefakt.

**Was bleibt kanonisch:**
- `assets/css/hill.css` ist die CDCI (Orange `#FFA014`, Yellow `#FAE600`, Charcoal `#575756`, Grey `#B0B0B0`, Source Sans 3).
- Alle Subpages waren in v1.26 nicht angefasst worden, sie sind also auch im Orange/Yellow-Stand.
- Die SITREP-Hard-Bans (Source Sans 3 only, Orange-Gold-Palette, max zwei dunkle Sektionen, keine Em-Dashes) sind wieder voll aktiv.

**Brand-Stand nach diesem Revert:**
Hill Digital Website ist v1.25-Stand auf allen Seiten:
- Index mit Hero, Drei-Säulen, Personas, Philosophy, Pfeiler (50 Jahre HR-Expertise als kanonische Setzung), Warum-jetzt, Vergleichstabelle, Pillars-Grid, Heritage-Block, Bewertungs-Layer, Final-CTA, Footer
- Recruiting, Onboarding, Trainings, Über uns, News, Kontakt, Suite, Impressum, Datenschutz, AGB alle in Orange/Yellow plus Source Sans 3

---

## v1.26 · 2026-05-18 20:54 · [K] · Brand-Pivot: Komplett neue index.html im Navy/Gold Premium-Look. CDCI extrahiert als assets/css/cdci.css.

**Auftrag vom Eigentümer:** „Stop. Wir starten mit dem Content von vorne. Nimm den kompletten Inhalt und die Struktur aus dieser Referenz-Datei und wende unser neues CDCI an."

Die Referenz war eine Single-Page-Landing im Navy-und-Gold-Premium-Look mit Cormorant Garamond Serif-Headlines, dunkelblauen Backgrounds, Gold-Akzenten, animierten Counter-Metriken und einer rotierenden SVG-People-First-Visualisierung.

**Brand-Override (bewusst von der Eigentümerin entschieden):**
Die SITREP-Hard-Bans aus dem v1.0-Briefing werden mit dieser Etappe formell überschrieben:
- Schrift: Cormorant Garamond Serif für Headlines zusätzlich zur Sans erlaubt, nicht mehr Source Sans 3 only.
- Palette: Navy 950 bis 600 plus Gold 500 bis 300 ist die neue CD, Orange-Yellow-Hill-CD wird zur Legacy.
- Dunkle Sektionen: nicht mehr max zwei, die ganze neue Landing ist Navy-Dark by Design.
- Discovery-Call wieder als CTA erlaubt, die alte „CTA muss auf Trainings zeigen"-Regel ist nicht mehr aktiv.

**`index.html` komplett ersetzt:**
- Gesamter Inhalt und Struktur aus der Eigentümerin-Referenz übernommen
- Inline-CSS mit den neuen Design-Tokens, Komponenten und Animationen
- Sektionen: Nav, Hero mit SVG-Orbit-Visual, Pillars, Pain-Story Donnerstag, Module 01-03 (AI Recruiting, Onboarding, Enablement), Vorher/Nachher Donnerstag-Tag, Promise Do/Don't, ROI-Metriken mit animiertem Counter, Warum jetzt, Final-CTA mit Email-Form, Footer
- E-Mail im Footer und CTA: `jakub@hill-digital.eu`
- Domain-Referenz: `hill-digital.eu`
- Em-Dashes aus dem Original-Reference durch Kommas ersetzt, weil diese eine SITREP-Regel nicht explizit überschrieben wurde
- Footer-Legal-Links zeigen auf existierende `impressum.html`, `datenschutz.html`, `agbs.html`, statt `[NACHTRAGEN]`-Anker

**Neu: `assets/css/cdci.css`**
- Komplettes Design-Token-Set: Navy-Skala, Gold-Skala, Cream, Off-White, Text-Muted, Border-Soft, Border-Gold, Shadow-Glow, Shadow-Card, Radius-Skala, Font-Stacks Serif und Sans, Container-Größen
- Komponenten-CSS: `.nav`, `.logo`, `.hero`, `.hero-eyebrow`, `.hero-trust`, `.btn .btn-primary .btn-ghost`, `.section-eyebrow`, `.section-heading`, `.section-lead`, `.pillar`, `.pain`, `.module`, `.day-card .day-vorher .day-nachher`, `.promise-card .promise-do .promise-dont`, `.metric`, `.now-card`, `.cta-form`, `.footer`, `.reveal`
- Single Source of Truth für Subpage-Umbau in folgenden Etappen

**Was NICHT in dieser Etappe ist:**
- Subpages (`recruiting.html`, `onboarding.html`, `trainings.html`, `ueber-uns.html`, `news.html`, `kontakt.html`, `impressum.html`, `datenschutz.html`, `agbs.html`, `suite.html`) bleiben in v1.25-Stand mit Orange/Yellow + Source Sans 3 + `hill.css`
- Visueller Bruch zwischen neuer Landing und Subpages besteht, bis die Subpages umgezogen sind
- `hill.css` (das alte Stylesheet) bleibt parallel zu `cdci.css` aktiv, weil die Subpages sie noch brauchen

**Nächste Etappen (geplant, jeweils nach Eigentümer-Freigabe):**
- v1.27: Subpages Hero, Nav und Footer auf Navy/Gold umstellen (Hülle-Refactor)
- v1.28: Service-Subpages (`recruiting.html`, `onboarding.html`, `trainings.html`) inhaltlich auf das Module-Pattern ziehen
- v1.29: `ueber-uns.html`, `news.html`, `kontakt.html` auf neues Layout
- v1.30: Legal-Seiten (`impressum.html`, `datenschutz.html`, `agbs.html`) auf neuen Stil
- v2.0: EN-Sync mit Translation-Glossary

---

## v1.25 · 2026-05-18 20:14 · [K] · Hill-Methodik raus, HR-Expertise rein. Nav-Reihenfolge Recruiting/Onboarding/Trainings. 50-Jahre-Dominanz entschärft.

**Auftrag vom Eigentümer:**
1. „Hill-Methodik" als Brand-Vokabel raus, ersetzt durch „HR-Expertise" oder kontextpassende Variante. Eine kanonische „50 Jahre HR-Expertise"-Setzung als Pfeiler-Headline behalten.
2. „50 Jahre" nicht mehr dominant, weniger Hero-Heritage-Lastigkeit.
3. Business-Areas konsistent in Reihenfolge Recruiting, Onboarding, Trainings (vorher oft Trainings-zuerst).

**Nav-Reihenfolge umgestellt (11 Files):**
Alle DE-Seiten plus die zwei neuen Service-Seiten von `Trainings · Recruiting · Onboarding · …` auf `Recruiting · Onboarding · Trainings · Über uns · News · Kontakt`.

**Footer-Tagline auf 9 DE-Seiten:**
`Gebaut auf 50 Jahren Hill-Methodik` → `Gebaut auf tiefer HR-Expertise`

**`index.html`, Content-Schliff in 19 Stellen:**
- Meta-Description: Reihenfolge der Areas umgestellt, „50 Jahre" rausgenommen, Personas eingebaut.
- Hero-Strong: `50 Jahre Hill People-Expertise` → `Tiefe HR-Expertise`. „Seit 1975 surfen wir" abgemildert zu „Wir haben Internet, Email und Cloud im HR mitgemacht".
- Hero-Second-Lead: Reihenfolge der Werkzeuge geändert, Recruiting zuerst.
- Hero-Stat-Label: `Drei Generationen Hill-Recruiting-Methodik` → `Tiefe HR-Expertise`.
- Säulen-Section-Lead: ohne „50 Jahre" und „Drei Generationen Hill-Methodik".
- Säulen-Recruiting-Card: ohne „Hill-Recruiting-Methodik aus 50 Jahren".
- Persona HR-Leiter-Links: umsortiert auf Recruiting, Onboarding, Trainings.
- Philosophy-Sub: ohne „Drei Generationen Hill-Recruiting-Methodik seit 1975".
- Pfeiler-Lead: ohne „50 Jahre Hill-Methodik", dafür einfach „HR-Expertise".
- **Pfeiler-H3: bleibt `50 Jahre HR-Expertise`. Das ist die einzige bewusst stehengelassene 50-Jahre-Setzung, als kanonische Pfeiler-Aussage.**
- Pfeiler-Card-Texte (Trainings): `drei Generationen Hill-Methodik` → `echter HR-Erfahrung`.
- AI-Trainings-Sektion-Lead: ohne „50 Jahre Hill-Recruiting-Praxis".
- Comparison-HD: ohne „Drei Generationen Hill-Methodik. 50 Jahre HR-Erfahrung".
- Heritage-Text: ohne „bauen daraus die Hill-Methodik weiter".
- Img-Alt: Em-Dash entfernt, „Hill-Methodik analog" → „HR-Expertise analog".
- Heritage-Caption: `Jahre Hill-Recruiting-Methodik` → `Jahre HR-Expertise`. „50+" Heritage-Number bleibt als einziger visueller Anker.
- Bewertungs-Layer-H3: ohne „50 Jahre Hill-Methodik".
- Recruiting-Pillar-Card-Text: `auf 50 Jahren Hill-Bewertungsmethodik` → `trainiert auf tiefer HR-Bewertungsexpertise`.
- **Zweites Drei-Säulen-Section (Pillars-Grid) umstrukturiert:** Headline `AI-Trainings, Recruiting, Onboarding` → `Recruiting, Onboarding, AI-Trainings`. Pillar-Cards 01/02/03 entsprechend umsortiert (Recruiting, Onboarding, AI-Trainings) inklusive Bildern. Lead-Text spiegelt neue Reihenfolge.

**Weitere DE-Seiten:**
- `trainings.html`: Vergleichstabelle-Item ohne „50 Jahren Hill-Recruiting-Praxis".
- `recruiting.html`: Meta-Description und Hero-Lead ohne „Drei Generationen Hill-Recruiting-Methodik seit 1975".
- `ueber-uns.html`: Heritage-Caption + ein Absatz im Heritage-Block ohne „50 Jahren Bewertungslogik".
- `impressum.html`: Methodische-Grundlage-Statement von „Hill-Methodik aus 50 Jahren" auf „tiefe HR-Expertise" umgestellt, Schwerpunkte-Liste auf Reihenfolge Recruiting/Onboarding/Trainings.
- `suite.html`: Meta + Recruiting-Modul-Lead ohne „Hill-Methodik" und Em-Dash.

**Was bewusst nicht angefasst:**
- Archive-Files (`_archive-*.html`): unverändert per Konvention.
- EN-Files: unverändert per SITREP-Regel, EN-Sync wartet auf v2.0.
- `photos-preview.html`: Kaska-Mood-Board, lokal-only, ein „Hill-Bewertungsbogen"-Verweis bleibt als interne Notiz.
- `ueber-uns.html` Eyebrow „Seit 1975" auf dem Heritage-Block: bleibt als ein Heritage-Anker, das ist eine Datumsangabe, keine „50-Jahre"-Wiederholung.

---

## v1.24 · 2026-05-18 19:55 · [K] · Drei-Säulen-Foundation: Recruiting + Onboarding als eigene Seiten, Persona-Pfade auf der Landing

**Auftrag vom Eigentümer:** Recruiting, Onboarding und Trainings gleich gewichten. Zielgruppe HR-Leiter, Geschäftsführung und KMU-Inhaber ohne HR. AT-Tonalität. Modernes Look-and-Feel innerhalb der bestehenden Brand-Constraints.

**Neue Seiten:**
- `recruiting.html` (komplett, 250+ Zeilen): Hero, Lage-in-Österreich-Sektion (Demografie, EU AI Act, AT-Spezifika mit Kollektivvertrag und AMFG-Konzession), Drei-Wege-Sektion (Trainings für HR-Leiter, Vorgespräch für Geschäftsführung, Sprechstunde für Inhaber ohne HR), Suite-Phase-2-Preview, Final-CTA, Footer. Keine fabrizierten Cases oder Zahlen.
- `onboarding.html` (komplett, 250+ Zeilen): Gleiche Struktur. Lage-Sektion mit Frühfluktuations-Pain, KMU-Realität-Beobachtung, EU-AI-Act-Kompetenz-Pflicht.

**Navigation auf 6 Links erweitert (9 DE-Seiten):**
- Trainings, Recruiting (neu), Onboarding (neu), Über uns, News, Kontakt
- Suite bleibt aus dem Nav raus (Phase-2-Reserve, SITREP §6 respektiert)
- `suite.html` selbst verwendet ab v1.24 ebenfalls den Standard-Nav (Suite-Eintrag nicht mehr Self-Reference)
- EN-Files und Archiv unverändert

**`index.html` umstrukturiert:**
- Hero-CTA-Buttons von Trainings-only umgestellt: primary `Unsere drei Säulen` (Scroll zu `#saeulen`), secondary `Vorgespräch buchen` (`kontakt.html`)
- Neue Section `#saeulen` direkt nach Hero: drei gleich gewichtete Service-Cards (Recruiting, Onboarding, Trainings) mit `.text-accent`-Headline `Alle aus einer Hand`
- Neue Section `#personas`: drei Persona-Cards (HR-Leiter:in / Geschäftsführung / Inhaber:in ohne HR), jede mit drei spezifischen Eingangs-Links

**AT-Tonalität durchgezogen:** „Inhaber:in" statt „Owner", „Geschäftsführung" statt „Leadership", Kollektivvertrag und AMFG-Konzessionspflicht explizit benannt, „Kein HR-Team" als Persona-Realität abgebildet, „Sprechstunde" und „Stundenweise abrechenbar, ohne Rahmenvertrag" als ehrliches KMU-Angebot.

**Ehrlichkeit zu Phase 1 vs Phase 2:** Recruiting- und Onboarding-Seiten zeigen klar, was heute live ist (Trainings + Beratung + Vorgespräch) und was im Aufbau ist (Suite-Module). Keine Fabrikation von Pilotkundenzahlen, Preisen, KI-Tools die es noch nicht gibt.

**Bewusst nicht umgesetzt in dieser Etappe (kommt in v1.25 ff.):**
- Visueller Hebel 2 (Karten entboxen) und Hebel 3 (Foto bricht aus Grid)
- Voice-Schliff auf bestehenden Sektionen (`philosophy`, `pfeiler`, `unterschied`)
- Heritage-Relocation aus Hero in Footer-Vertrauenslayer
- EN-Sync (`recruiting-en.html`, `onboarding-en.html`) wartet auf v2.0 EN-Etappe

**Bekannte offene Punkte (Eigentümer/Karl/Jakub müssen klären):**
- Konzessionsstatus für Recruiting in AT (eigene AMFG-Konzession oder via Hill-Gruppe-Partner). Aktuelle Formulierungen auf `recruiting.html` sind Beratungs-formuliert, keine Vermittlungs-Versprechen.
- KMU-Sales-Funnel: Wer beantwortet die Sprechstunden-Anfragen vom Tischlerei-Inhaber? Aktuell Default `kontakt.html`.
- Preisrange Trainings/Recruiting/Onboarding: Aktuell auf allen Seiten `Auf Anfrage`. Wenn öffentlich, dann eintragen.

---

## v1.23 · 2026-05-18 15:16 · [K] · Logo-Refresh, Trainings-Polish, Akzent-Headlines entgiftet

- **Logo (Nav, alle DE-Seiten):** Icon von 34px auf 64px, Text von 1.12rem auf 1.6rem, `/ HR-OS`-Suffix entfernt im HTML der 9 DE-Seiten (index, trainings, ueber-uns, suite, news, kontakt, impressum, datenschutz, agbs) und zusätzlich global per CSS gehidet (`.nav-logo-sub { display: none }`). EN-Files und Archiv unverändert.
- **Trainings Karte 07 (Büroalltag):** auf gleiche Breite wie 01 bis 06 gesetzt. `.trainings-grid-office` bekommt jetzt `repeat(3, 1fr)` Grid statt `max-width: 760px`. Yellow-Border-Akzent links bleibt. Media-Queries für 920px und 600px erweitert.
- **Trainings Header:** `shape-growth-tr` Punkt-Linien-Grafik rechts oben aus `trainings.html` entfernt. EN-Stamp (`.en-stamp`) bleibt.
- **Nav-Links:** per `margin-left: auto` nach rechts an Lang-Switcher und Button geschoben. Vorher `margin-right: auto; margin-left: 2.4rem`, jetzt `margin-left: auto; margin-right: 2rem`.
- **Hebel 1, `.text-accent`:** Gelb-Orange-Gradient als Textfarbe raus, dafür Charcoal-Text plus 0.08em Gelb-Underline mit `text-decoration-skip-ink: none`. Wirkt auf Index, Trainings, Über uns, Suite, News, Kontakt. Headlines lesen sich editorial statt Textmarker, Gelb behält den Hill-Moment als Akzent.

**Brand-Rule notiert für die Session:** Fotos bleiben `filter: grayscale(100%)`, niemals `sepia()`, keine warmen Duotones, keine orange/gelben Tint-Overlays auf Fotos.

**Note zur Versionslücke:** v1.20 bis v1.22 (Jakubs Commits, im git-Log dokumentiert) wurden in VERSION.md nicht eingetragen. Lücke ist Jakubs Baustelle, hier nicht angefasst.

---

## v1.19 · 2026-05-15 18:18 · [J] · Trainings-Subpage Aufbau: Übersicht-Grid + neues Trainer-Foto

**Aufbau-Logik überarbeitet:**

- **Header klarer:** "Vier KI-Trainings. Drei für HR. Eines für den Büroalltag." (vorher unklar wie viele)
- **Neue Sektion `#uebersicht`** ganz oben: Karten-Grid mit allen vier Trainings auf einem Level sichtbar
  - **3 HR-Karten in einer Row** (HR allgemein, Energie, Logistik) mit Orange-Akzent
  - **4. Karte (Büroalltag) separat darunter**, abgesetzter Yellow-Akzent (border-left), max-width 760px, klar als „branchenneutral, auch über ARS" markiert
  - Klick auf Karte → smooth scroll zur jeweiligen Detail-Sektion (Anker-Navigation, scroll-behavior global aktiv)
  - Karten zeigen Nummer (groß, Orange), Tag, Titel, Kurz-Beschreibung, Status "Warteliste" + CTA "Mehr Infos"
- **Trainer-Block nach oben verschoben** (nach Übersicht, vor Detail-Sektionen) — Authority vor Details
- **Trainer-Foto neu:** `assets/img/team/jakub-popluhar-trainer.png` (aus `/Users/mr.magico/Documents/Media/Fotoshooting May 25/after photoshop/no background png/15.png`, freigestelltes PNG)
  - Neue CSS-Klasse `.trainer-photo-cutout`: kein Crop, kein Border, transparente Darstellung mit drop-shadow für Tiefe
- **Trainer-Bio neu formuliert:** weniger US-Pitch, mehr deutsche Sachlichkeit. „Ludwig-Maximilians-Universität München" ausgeschrieben. „Didaktik aus dem Lehramt, nicht aus dem Marketing." statt „Didaktik ist Handwerk, nicht Folie."
- **Tonalität entdeutscht** an mehreren Stellen:
  - „Workflows aus dem Maschinenraum, dokumentierte Misserfolge" → „Werkstattnotizen, dokumentierte Lernkurven"
  - „Wie KI hilft, ohne die Personalentscheidung zu automatisieren" → „KI als Werkzeug, nicht als Ersatz für die Personalentscheidung"
  - Diverse weitere Schliffe
- **Status-Wording präziser:** "Aktuelle Runde voll. Anmeldung nur über Warteliste." (vorher nur „Nur über Warteliste" — die neue Formulierung erklärt warum)

**CSS-Erweiterung `assets/css/hill.css`:**

- `.trainings-grid` (3-col → 2-col → 1-col responsive)
- `.trainings-grid-office` (max-width 760px, abgesetzt)
- `.training-card` (Hover-Lift, Orange-Border bei Hover, große Nummer)
- `.training-card-office` (Yellow-Border-Left, leichter Yellow-Gradient)
- `.training-card-status` mit Pulse-Dot, `.training-card-cta` mit gap-Animation bei Hover
- `.trainer-photo-cutout` (transparente Darstellung mit drop-shadow für PNG-Freisteller)
- `.trainer-quote`

**Photo-Source-of-Truth-Memory:** `~/.claude/projects/-Users-mr-magico/memory/hill-digital.md` erweitert mit Pfad zu Jakubs Fotoshooting-Ordner (`/Users/mr.magico/Documents/Media/Fotoshooting May 25/after photoshop/no background png/`).

**Pre-Deploy-TODO:** jakub-popluhar-trainer.png ist 5.7MB unkomprimiert. Vor Live-Deploy auf <500KB komprimieren (zusammen mit jakub-popluhar.png 7MB von Hero-Bereich).

**EN-Files unverändert.** Lokal committed, KEIN Push.

---

## v1.18 · 2026-05-15 18:03 · [J] · Trainings-Subpage Inhalt + Landing-Vergleichstabelle

**Trainings-Subpage `trainings.html` komplett überarbeitet:**

- **HARD-FIX:** ARS-Akkreditierungs-Claims überall raus. Nichts ist akkreditiert. Nur "KI für den Büroalltag" wird zusätzlich über die ARS Akademie angeboten (Jakub dort als Trainer gelistet).
- **4 Trainings** statt 3 + Keynote:
  - 01 · KI im HR-Büroalltag (HR allgemein, branchenneutral) · #hr-allgemein
  - 02 · KI für HR · Energiebranche · #energie
  - 03 · KI für HR · Logistikbranche · #logistik
  - 04 · KI für den Büroalltag (branchenneutral, Nicht-HR, auch via ARS) · #bueroalltag
- **Keynote raus** (Commander-Entscheidung).
- **Trainer-Bio-Block neu** (#trainer): Jakub Popluhar, CEO und Trainer. Master of Education in English Language and Literature, LMU München. Staatlich geprüfter Lehrer. Sprache/Semantik/Linguistik als Brücke zu Prompting. "Ich trainiere nichts, was ich nicht selbst täglich nutze."
- **Zertifikat-Block neu** (#zertifikat): jeder Teilnehmer erhält Hill-Digital-Zertifikat als KI-Kompetenz-Nachweis im Sinne Artikel 4 EU AI Act. Mit Goldenem Trophy-Icon.
- **Schmerz-Querthema in jedem Training:** "Kein Frontalunterricht. Wir arbeiten mit." (im Page-Header und in Trainer-Block)
- **Scarcity-Logik:** Jedes Training zeigt Status "Aktuelle Runde voll. Nur über Warteliste." mit orangem Pulse-Dot. CTA "Auf die Warteliste setzen" pro Training.
- **Warteliste-Form zentral** (#warteliste) mit Dropdown-Auswahl (alle 4 Trainings). JS belegt Dropdown automatisch vor wenn von Training-Karte geklickt (data-training Attribute).
- Final-CTA umgestellt: nicht mehr Demo, sondern "Inhouse-Anfrage ab 8 Personen".

**Landing-Page `index.html` Trainings-Sektion umgebaut:**

- Statt 3-Card-Teaser + Keynote-Card: **5-Achsen-Vergleichstabelle** "Generelle HR-Trainings am Markt vs. Hill Digital"
- Headline: "Was unsere HR-Trainings anders machen."
- 5 Achsen: Format · Trainer · Wissen dahinter · Branchen-Tiefe · Was bleibt
- Hill-Digital-Spalte mit Orange-Akzent-Border und Cream-Tönung
- Mobile: Stacked Layout mit Marktstandard- / Hill-Digital-Prefix
- CTA-Doppel unten: "Alle vier Trainings im Detail" (primary → trainings.html) + "Auf die Warteliste" (ghost → trainings.html#warteliste)

**CSS-Erweiterung `assets/css/hill.css`:**

- Neue Komponenten: `.training-cta-row` (mit Pulse-Dot-Status), `.trainer-block` (2:1 Grid), `.trainer-photo`, `.cert-block` (Icon + Content), `.cert-block-icon` (Yellow-Orange-Gradient), `.waitlist-block` (Card mit Form), `.waitlist-form`/`.waitlist-row`, `.comparison-table` mit Header/Row/Label/Other/Hd-Klassen
- Vollständig responsive (mobile breakpoints bei 760px / 640px / 560px)

**EN-Files unverändert** (Massen-Sync später als v2.0).

---

## v1.17 · 2026-05-15 17:37 · [J] · Trainings als eigene Subpage (trainings.html)

- **Neue Datei:** `trainings.html` — Standalone-Subpage für Trainings + Keynote
  - Struktur wie `suite.html` (page-header + 3 module-detail Sektionen + Keynote-Card + Final-CTA)
  - 3 Detail-Blöcke mit Anker-IDs: `#energie`, `#logistik`, `#bueroalltag`
  - Keynote-Block mit Anker `#keynote`
  - Eigener "ARS-akkreditiert. Inhouse buchbar."-Block mit Doppel-CTA (Inhouse-Anfrage + Newsletter)
- **Nav auf allen 6 DE-Pages** umgestellt: `index.html#trainings` → `trainings.html`
- **index.html Hero-CTA** umgestellt: `#trainings` → `trainings.html`
- **index.html Landing-Trainings-Sektion** behält 3-Card-Teaser + Keynote, neuer Doppel-CTA unten: "Alle Trainings im Detail" (primary → trainings.html) + "Newsletter abonnieren" (ghost)
- **index.html Final-CTA-Sekundär-Button:** "Erst die Suite ansehen" (→ suite.html) → "Trainings im Detail" (→ trainings.html)
- **heritage.html Final-CTA-Sekundär-Button:** "Die Suite ansehen" (→ suite.html) → "Trainings im Detail" (→ trainings.html)
- **Footer Suite-Spalte → Trainings-Spalte** auf allen 6 DE-Pages: Recruit/Onboard/Develop/Assess/Listen → Energie/Logistik/Büroalltag/Keynote (links auf `trainings.html#anchor`)
- **EN-Files NICHT angerührt** (Massen-Sync später als v2.0)
- **`suite.html` bleibt unverändert stehen** (separate Entscheidung, derzeit nicht von Navigation erreichbar)

---

## v1.16 · 2026-05-15 17:16 · [J] · Nav "Suite" → "Trainings", offizielle Präsentation, Workshop-Foto wandert

- **Nav-Menü auf allen 6 DE-Pages** (index, heritage, standpunkte, kontakt, impressum, datenschutz): "Suite" → "Trainings" mit Anker `index.html#trainings`
- **Hero-CTA** auf `index.html` umgestellt: "Die Suite entdecken" → "Trainings ansehen" → `#trainings` Anker
- **Trainings-Sektion id="trainings"** + scroll-margin-top für sauberen Anker
- **"Phase 1"-Badge raus** — wir präsentieren als offiziell-bereit, nicht als "kommt noch"
- **"Konkrete Termine ab Q4 2026"-Framing raus** → "Inhouse buchbar, offene Termine über den Newsletter"
- **Bottom-CTA-Text raus:** "Termine ab Q4 2026. Auf dem Laufenden bleiben:" → "Offene Termine und neue Workshops zuerst erfahren:"
- **Workshop-Wall-Foto (photo-1551836022-d5d88e9218df) wandert** vom verschwundenen Suite-Banner zur "KI für den Büroalltag"-Karte (passt zur Methodik-im-Büro-Botschaft)
- EN-Pages noch nicht angefasst (Constraint #1)
- `suite.html` Sub-Page bleibt vorerst stehen (separate Entscheidung)

---

## v1.15 · 2026-05-15 17:06 · [J] · Jakub-Bio Variant C + Suite raus + Trainings neu (3 + Keynote)

**Bio (Variant C, Format konsistent zum Team):**
- `heritage.html` Jakub-Karte: "Master of Education · AI Practitioner" Nickname + Tagline "Wir trainieren nichts, was wir nicht selbst nutzen."
- `index.html` Brücke-Story Jakub-Karte: gleiche Erweiterung

**Suite-Sektion (5 Module) entfernt von Landing:**
- "Die Hill Digital Suite — Fünf Module" Sektion komplett aus `index.html` raus
- Begründung: Produkt existiert noch nicht (Phase 2), unehrliche Positionierung
- Workshop-Wall-Foto (Unsplash photo-1551836022-d5d88e9218df) zu Content/seeds.md gesichert für späteren Blog-Artikel "Was & Warum"
- `suite.html` Detail-Seite bleibt stehen (separates File, später entscheiden)

**Trainings-Sektion neu (ersetzt v1.2 generic 3):**
- Eyebrow "Phase 1 · Trainings + Keynote"
- H2: "Drei Trainings. Eine Keynote. Für HR, Führung und Konferenzen."
- Sub mit ARS-Akkreditierung erwähnt + Termine ab Q4 2026
- 3 Training-Karten mit Branchen-Fokus:
  1. KI für HR im Energiebereich · Inhouse · ARS-akkreditiert
  2. KI für HR in der Logistik · Inhouse · ARS-akkreditiert
  3. KI für den Büroalltag · ½-Tages-Workshop oder Inhouse · ARS-akkreditiert
- Keynote-Karte (eigene Styling, dark-warm Hintergrund):
  - "Sie wissen nicht, was Sie nicht wissen."
  - Impulsvortrag · 30-60 Min · Live oder Hybrid · DE oder EN
  - Format Tag in Gold-Akzent
- Bottom-CTA: kein Calendly mehr (kein hartes Produkt), stattdessen "Newsletter abonnieren" → springt zum Footer-Newsletter-Band
- Newsletter-Band hat jetzt `id="newsletter"` + `scroll-margin-top: 100px` für sauberen Anker
- Trainings-Sales-Page (separate Seite, später) als TODO eingetragen

---

## v1.14 · 2026-05-15 16:49 · [J] · Team-Bios verifiziert (Franz, Roswitha, Melanie, Doris)

- `heritage.html` Team-Sektion:
  - **Franz Hill** Featured-Card: erweitert um Eigentümer · Chief Inspiration Officer · Dr. Network + Tagline "Putting clients & applicants first since 1975."
  - **Roswitha Hill-Feichtl** (vorher Platzhalter): Prokuristin & General Manager Salzburg · Feel Good Manager · Tagline "Heart of the Company."
  - **Melanie Hill, BA** (vorher Platzhalter): General Manager · Aspiring Novelist · Queen of Cake · Tagline "Soon to be Bestselling Author."
  - **Mag. Doris Weis-Burger** (vorher nur "Doris"): Senior Consultant · Head of all things awesome · Tagline "Leaving a bit of sparkle everywhere I go."
- `index.html` Brücke-Story-Sektion Franz-Karte: gleiche Erweiterung (Eigentümer · Chief Inspiration Officer · Dr. Network + Tagline)
- Alt-Texte der Fotos auf vollständige Namen + Rollen aktualisiert
- Verifizierte Inhalte direkt vom Commander, keine Fabrikation

---

## v1.13 · 2026-05-15 16:29 · [J] · README: "Uncle-Jake-Mode" Begriff entfernt

- README.md: Begriff "Uncle-Jake-Mode" durch neutrale "So läuft eine Session" ersetzt
- VERSION.md: gleiche Korrektur retroaktiv in v1.12 Eintrag
- Kein inhaltlicher Wechsel, nur Sprach-Bereinigung

---

## v1.12 · 2026-05-15 16:25 · [J] · README Klartext: Lanes sind nur AI-Tool-Empfehlung, Menschen machen alles

- README.md zwei wichtige Änderungen:
  - NEUER Abschnitt oben: "💬 TL;DR — Für Menschen" mit Session-Workflow in einfacher Sprache (pull → arbeiten → push → WhatsApp-Ping)
  - "👥 Schwerpunkt-Empfehlung" Sektion klargestellt: **TECHNISCH für Claude Codes**, NICHT Rollen-Lock für Menschen. Kaska kann Texte ändern, Jakub kann Bilder tauschen, beide dürfen alles.
  - "📁 File-Schwerpunkte" (vorher "File-Ownership Lanes") umformuliert: keine Eigner-Sprache, sondern Empfehlung. Mensch-Regel ergänzt: "Wenn du etwas siehst, das verbessert werden muss, mach es. Egal welcher Schwerpunkt."
- Hintergrund: Kaska fand die starre Lane-Definition zu restriktiv. Realität ist: Lanes sind nur AI-Hilfe für Konflikt-Reduktion, kein Rollenkorsett für die Menschen.
- Mission bleibt: eine richtig gute Hill-Digital-Webseite. Wer was macht, ist Mittel zum Zweck.

---

## v1.11 · 2026-05-15 16:10 · [J] · Migration auf EINE Branch: `main`

- **Ab jetzt: nur noch `main` als gemeinsame Arbeits-Branch.** v0.5-relaunch wird Legacy, Branch bleibt vorerst stehen (bei Gelegenheit löschen).
- `main` ist auf v1.10 fast-forwarded (enthält Kaskas Logo-Konzepte v1.10)
- README.md aktualisiert:
  - Branch-Tabelle: `main` ist jetzt "Die EINE gemeinsame Arbeits-Branch"
  - Pre-Edit-Pull-Befehl auf `main` geändert
  - Konflikt-Resolution-Pull-Befehl auf `main` geändert
- v0.5-relaunch bleibt vorerst, wird nicht mehr gepusht von beiden
- Beide Claude Codes arbeiten ab jetzt: `git checkout main && git pull --rebase`

---

## v1.10 · 2026-05-15 14:35 · [K] · Logo-Konzepte Preview-Seiten

- Zwei neue Visual-Preview-Pages für die Logo-Refresh-Suche:
  - `logos-preview.html`: drei klar verschiedene Logo-Richtungen für Hill Digital nebeneinander. A · Refined Heritage, B · Peak Monogramm, C · Wordmark-Forward. Jede Direktion auf hell und dunkel, plus Compact-, Icon-Only- und Mono-Versionen. Referenz Hill-Woltron-Original neben erster Ziel-Übersetzung oben auf der Seite.
  - `logos-preview-2.html`: vier Sub-Varianten von Konzept A nach Commander-Auswahl der Refined-Heritage-Linie. Verfeinerter Berg mit drei differenzierten Gipfeln nach Hill-Woltron-Vorbild, stärkerer Yellow-zu-Orange-Bogen-Gradient, vier Wortmarken-Layouts (A.1 stacked, A.2 inline horizontal, A.3 mit "HR-BETRIEBSSYSTEM"-Subline, A.4 dramatic peaks).
- Alle SVG inline, alle Source Sans 3, alle Hill-CD-Farben (#FAE600 zu #FFA014, Charcoal #575756, Grey #B0B0B0).
- Reine Preview-Files: keine `hill.css`-Änderung, keine bestehenden HTML-Seiten editiert, keine Content-Edits, kein EN-File angefasst.
- Finale Logo-Auswahl wartet auf Commander-Entscheidung. Sobald gewählt: Integration in `assets/css/hill.css` für `.nav-logo` SVG und `.footer-brand` SVG.

---

## v1.9 · 2026-05-15 14:18 · [J+K] · kaska-fusion-1 — Diffusion Visual ↔ Content

- **Merge `origin/main` (d28af1c + c5435b4 + ddccbc3) in `v0.5-relaunch`**
- Kaskas Visual-Schicht übernommen:
  - Hero: `.hero-with-image` Wrapper + Unsplash-Foto (HR-Verantwortliche am Fenster)
  - 3 Säulen Recruiting/Onboarding/Weiterbildung mit Bild-Headern + `Säule 01/02/03` Tags
  - Suite-Sektion mit `.suite-banner` (Workshop-Wall) oben
  - Heritage-Block mit `.heritage-visual-stack` (Hands-Writing-Image über 50+ Number)
  - Insight-Cards Standpunkte mit Header-Bildern
  - Final-CTA mit `.with-bg-image` Backdrop
- Neue Pages: 5 `campaign*.html` + 6 `photos-*.html` Mood-Boards
- +117 Zeilen CSS in `hill.css` für `.hero-with-image`, `.pillar-card.with-image`, `.suite-banner`, `.heritage-visual-stack`, `.insight-card.with-image`, `.final-cta.with-bg-image`
- **Hero-Konflikt manuell gelöst:** Kaskas `.hero-with-image` Wrapper trägt Jakubs v1.4 Surfer-Welle-Text (2 Lead-Paragraphe mit "Die KI-Welle ist nicht unsere erste.")
- **Trainings-Sektion (v1.2) bekommt Bild-Header** konsistent zu Kaskas neuem `.pillar-card.with-image` Pattern — Tags "Training 01/02/03", 3 Unsplash-Platzhalter (workshop / recruiter-screen / strategy-team)
- Jakubs Content bleibt komplett: Brücken-Statement (v1.1), Trainings-Sektion (v1.2 mit neuen Bildern), Newsletter-Footer (v1.3), Hero-Welle-Text (v1.4), Standpunkte-Korn-Ferry-Fix (v1.5), Team-Sektion Heritage (v1.6), Brücke-Story-Sektion mit Franz+Jakub-Fotos (v1.7), README-Protokoll (v1.8)
- EN-Files: `index-en.html` übernimmt Kaskas Visual-Edits automatisch. Andere EN-Files unverändert (Constraint #1).
- Lokal-only Commit. Push erst auf Commander-Befehl.

---

## v1.8 · 2026-05-15 13:57 · [J] · README als Kollaborations-Protokoll

- `README.md` komplett neu geschrieben als Single Source of Truth für beide Claude-Code-Instanzen (Jakubs + Kaskas)
- Definiert: File-Ownership-Lanes (Jakub Content / Kaska Visual), Branch-Struktur (v0.5-relaunch shared, main stable-only), Versions-Tag-Schema (vX.Y, jakub-fusion-N, kaska-fusion-N, latest, stable), VERSION.md-Format mit [J|K]-Author-Markern, Pull-Rebase-Disziplin, Push-on-Command-Regel
- Pflicht-Lektüre-Reihenfolge: README → STRATEGY-v2.0.md → VERSION.md
- Format-Hard-Bans dokumentiert (Source Sans 3, max 2 dunkle Sektionen, Orange-Gold, em-dashes raus, "Hill International"/"Korn Ferry"/"KI-Agenten"-Bans)
- Conflict-Resolution-Protokoll für parallele Edits
- Notfall-Protokoll bei kaputten Commits
- Begründung jeder Regel ("Warum dieser Aufbau") für beide Claude-Instanzen

---

## v1.7 · 2026-05-15 13:25 · [J] · Brücke-Story-Sektion auf Landing (Franz + Jakub)

- Neue Section "Die Geschichte hinter Hill Digital — Zwei Welten. Eine Brücke." auf `index.html` zwischen Heritage-Block und Standpunkte (cream)
- Lead-Narrative: "Hill Digital lebt vom Treffen zweier Welten. Franz Hill trägt seit 1988 die Hill-Recruitment-Praxis durch jede Welle, die kam. Jakub Popluhar bringt Didaktik und KI-Praxis aus dem Maschinenraum. Vom Berg auf die Welle."
- Featured-Row mit 2 Foto-Karten (Franz + Jakub) — gleichwertig 50/50
- Franz-Karte: Eyebrow "Heritage · Der Berg" + Kurz-Bio (40 Jahre Wellen-Navigator)
- Jakub-Karte: Eyebrow "CEO · Wasser und Wind" + Kurz-Bio (M.Ed. TUM+LMU, Sunshine Coast, Mindworx, April 2026, "wir trainieren nichts, was er nicht selbst nutzt")
- Closer-Paragraph: "Der Berg trägt. Die Welle treibt. Der Wind hebt. Hill Digital verbindet, was Franz seit 40 Jahren weiß, mit dem, was Jakub heute baut. Das ist nicht Tech gegen Tradition. Das ist Tradition, die mit der Zeit fliegt."
- CTA "Das ganze Team kennenlernen" → heritage.html
- Hintergrund weiß (zwischen Heritage white und Standpunkte cream)
- Inline-Styles, kein CSS-File-Touch
- Selbe Fotos wie Heritage-Page (assets/img/team/franz-hill.png + jakub-popluhar.png)

---

## v1.6 · 2026-05-15 13:21 · Team-Sektion auf Heritage (mit echten Fotos)

- Neuer `<section class="section-cream">` Block auf `heritage.html` zwischen "Drei Grundsätze" und Final-CTA
- Section-Headline: "Das Team — Wer Hill Digital trägt."
- Lead: "Drei Generationen Hill-Recruitment-Heritage trifft auf Lehramt, Didaktik und KI-Praxis aus dem Maschinenraum. Vom Berg auf die Welle."
- **Featured-Row (2 große Karten, gleichwertig):**
  - Franz Hill (FIRST, Heritage-Anchor): "Heritage · Partner Hill Woltron" + Bio mit "Wellen navigiert"-Narrative
  - Jakub Popluhar (SECOND, CEO): "CEO Hill Digital" + Bio mit verifizierten Fakten (TUM, LMU, Sunshine Coast, Mindworx, M.Ed., CEO April 2026)
- **Team-Row (3 kleinere Karten, weniger dominant):**
  - Roswitha Hill (Hill Woltron) — Platzhalter-Bio mit TODO-Comment
  - Melanie Hill (Geschäftsführerin Hill Woltron, Dritte Generation) — Platzhalter-Bio
  - Doris (Hill Digital) — Platzhalter-Bio
- Fotos kopiert nach `assets/img/team/`:
  - `franz-hill.png` (184KB)
  - `jakub-popluhar.png` (7MB — TODO: optimieren)
  - `roswitha-hill.png` (294KB)
  - `melanie-hill.png` (194KB)
  - `doris.png` (249KB)
- Inline-Styles (kein CSS-File-Touch)
- Detail-Bios (besonders Sunday-Session-Output für Jakub) kommen in v1.7+

---

## v1.5 · 2026-05-15 13:08 · Blog-Stub-Update Standpunkte + Hard-Ban-Fix

- **KRITISCH:** standpunkte.html Card 5 hatte "Korn Ferry, Heidrick und Randstad" extern erwähnt — Hard-Ban-Verletzung (Strategy v2.0 §5)
- Card 5 ersetzt durch AI-First-Praxis Card: "Sechs Workflows, die ich als CEO automatisiert habe."
- Body: "Plus zwei, bei denen ich gescheitert bin. Konkret, ungeschönt, mit echten Prompts. Walk the walk, talk the talk: wir trainieren nichts, was wir nicht selbst nutzen."
- Andere 5 Cards bleiben (sind Strategy-aligned)
- ⚠️ standpunkte-en.html hat dieselbe Verletzung — NICHT angefasst per Constraint #1, MUSS bei v2.0 EN-Translation mit-gefixt werden

---

## v1.4 · 2026-05-15 13:07 · Surfer-Welle Mini-Integration im Hero (Option 4A)

- `index.html` Hero Lead-Text aufgesplittet in zwei Absätze
- Neuer erster Lead-Absatz mit Brand-Metapher: "**Die KI-Welle ist nicht unsere erste.** Seit 1975 surfen wir die Veränderungen im HR. Internet. Email. Cloud. Jetzt KI."
- Zweiter Lead-Absatz: bestehender Produkt-Sub-Text (HR-Betriebssystem etc.), em-dash zu Komma korrigiert
- Hero-Claim "Human in the Lead. KI im Hintergrund." bleibt unverändert (locked Tagline)
- H1 "Wir starten beim Menschen, nicht bei der Plattform." bleibt unverändert (locked Stance-Hook)
- KEIN Hero-Background-Foto, KEIN Visual-Break — Option 4A reine Text-Integration
- Original-Hero-Format bewahrt, Schrift + Akzent unverändert

---

## v1.3 · 2026-05-15 13:06 · Newsletter-Band im Footer aller DE-Pages

- Neues `.footer-newsletter` Grid-Band oberhalb der bestehenden 4-Spalten im Footer
- Headline: "Hill Digital Praxis-Notizen"
- Sub: "Einmal im Monat. Workflows aus dem Maschinenraum, EU-AI-Act-Updates, dokumentierte Misserfolge. Kein Marketing."
- Form-Stub: Email-Input + "Abonnieren"-Button mit `action="#"` Placeholder
- HTML-Kommentar `<!-- TODO: MailerLite Embed-Code von Jakub ergänzen, derzeit nur HTML-Stub -->`
- Inline-Styles (kein CSS-File-Touch, keine neue Klasse globalisiert)
- Sync auf 7 DE-Pages: index, heritage, suite, standpunkte, kontakt, impressum, datenschutz
- 6 EN-Files NICHT angefasst (Constraint #1)

---

## v1.2 · 2026-05-15 13:04 · Trainings-Phase-1-Sektion (NEU)

- Neue Section in `index.html` zwischen Suite (cream) und Heritage (white)
- Eyebrow: "Phase 1 · Trainings für HR-Profis" mit Accent-Highlight
- H2: "Drei Trainings, die wir gerade entwickeln. Mit HR-Profis. Für HR-Profis."
- Lead-Text mit Q4-2026-Hinweis + "wir bauen das beste HR-Training im DACH-Raum, gemeinsam mit den HR-Leuten"
- 3 Karten im bestehenden `.pillar-card` Pattern:
  - HR-Profi 2026 (½-Tag · Wien · max. 8)
  - Recruiting mit KI (1 Tag · Wien + Online · max. 12)
  - HR-Abteilung KI-fit (90-Tage Inhouse)
- Keine Preise sichtbar (per Decision §12.5 #3)
- CTA "Termin anfragen" → Calendly-Placeholder mit TODO-Comment
- Heritage-Page nicht angefasst (eigener Scope)
- Keine CSS-Änderung (reuse vorhandene Klassen)
- EN-Files nicht angefasst (Constraint #1)

---

## v1.1 · 2026-05-15 13:02 · Brücken-Statement in Philosophy

- `index.html` Philosophy-Sektion (Z. 86-99): neue Headline "Wir leben Recruiting. Wir leben Technologie. Wir bauen die Brücke zwischen zwei Welten."
- Bestehender "Andere starten bei Tech…"-Text rückt nach unten als Sub
- 20-30%-Zeit-Aussage rückt als dritter Absatz
- Em-dash zu Komma (DACH-Regel)
- Heritage-Page Philosophy unverändert (separater Scope)
- Dunkle Section bleibt by-design

---

## v1.0 · 2026-05-15 13:00 · Setup: Strategie-Anker + Versions-Log

- `STRATEGY-v2.0.md` als 1-Seite-Strategie-Kondensat für Kaska im Repo angelegt
- `VERSION.md` (diese Datei) als Versions-Log angelegt
- Quelle: Master-Strategy in personal repo unter `~/Projects/Hill Digital/strategy/2026-05-15-hill-digital-strategy-v2.md`
- Basis: `4d564dd` (Original main + strategisches-Denken-Fix)

---

## Kommende Etappen (geplant)

| Version | Beschreibung | Status |
|---|---|---|
| v1.1 | Brücken-Statement in Philosophy | geplant |
| v1.2 | Trainings-Phase-1-Sektion (neu) | geplant |
| v1.3 | MailerLite Newsletter-Form im Footer | geplant |
| v1.4 | Surfer-Welle Mini-Integration im Hero | geplant |
| v1.5 | Blog/Content-Hub Stub-Update | geplant |
| v1.6 | Jakub Authority Block + Heritage-Bio | wartet auf Sunday-Bio-Session 17.05 |
| v2.0 | EN-Translation aller DE-Änderungen (Massen-Sync) | wartet auf expliziten Befehl |

---

## Regeln

1. **NUR DE editieren.** EN-Files werden bei v2.0 in einem Rutsch synchronisiert.
2. **Lokal-only.** Push erst auf expliziten Befehl.
3. **Versions-Tag in jedem Commit-Message.** Format: `vX.Y · YYYY-MM-DD HH:MM · Kurz`
4. **Diese Datei mit jedem Commit ergänzen.**
5. **Original-Format bewahren:** Source Sans 3, max 2 dunkle Sektionen (Philosophy + Final-CTA), Orange-Gold-Akzent.
