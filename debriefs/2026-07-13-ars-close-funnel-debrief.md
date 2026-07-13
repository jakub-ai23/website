# Mission Debrief — ARS 14.07 Close-Funnel finalisiert

*Created: 2026-07-13 · Persona: Jocko (execution) · Fenster: Website/ARS-Funnel (parallel zu einem Life-OS-Session-Ende-Fenster)*

## Commander's Intent
Den ARS-14.07-Lead-Funnel vor dem Event morgen (14.07) vollständig funktionsfähig und sauber machen: Formular, das Leute anklicken lässt was sie wollen → getailorte Sofort-Mail → funktionierende Ressourcen-Seite. Nichts darf ins Leere laufen.

## Ergebnis: Kette komplett dicht + live
**Formular (mit Haken) → Brevo (Liste 14) → getailorte Sofort-Mail → „Alle Tools ansehen" → Ressourcen-Seite (200).** End-to-end getestet und in Gmail verifiziert.

---

## Was gemacht wurde (3 Workstreams)

### 1. Website `/weiter/` ARS-Formular (jakubpopluhar.com, Branch main)
- **Anforderungs-Haken zurück** (Reversal von `7b10035`, das sie entfernt hatte). Commander-O-Ton: „ohne Haken katastrophal, Leute müssen anklicken können, was sie anfordern". 4 Optionen unter „Was darf ich Ihnen schicken?": Ressourcen · Strategiegespräch · Training für mich/Team/weitere · Rechtskonforme KI-Lösungen.
- **Training-Haken** umbenannt zu „Training für mich, mein Team oder weitere Trainings".
- **Consent-Text** → „…dürfen mich per E-Mail bezüglich Angeboten in der Zukunft kontaktieren." (HWD als „Hill Digital" gerendert = öffentlicher §8-Markenname.)
- **Neuer Titel** „Was möchten Sie, dass nach dem Training passiert?"; Hero-Badge/Subtitle/Typewriter raus → direkt zu den Feldern.
- **Veraltete Konsumentenpsychologie-Kurs-Box** (Vergangenheitsdaten) entfernt — Fokus nur E-Mail-Erfassung.
- **Consent-Fehlermeldung** differenziert: „Bitte kreuzen Sie das Kästchen an…" statt generischem „schiefgelaufen"; Pflichtfeld-Meldung eigen; generische Meldung nur noch bei echten Netzwerk-/Serverfehlern.
- Commits: `9010599` (Rework), `85aafd4` (Consent-Meldung), `21b1352` (Ressourcen-Restore). Alle auf `main` gepusht = live.

### 2. Brevo-Proxy — Sofort-Mail an die Haken gekoppelt (HD-Infra)
- `infrastructure/brevo-proxy/server.js` (`kind=ars`): baut den Mail-Inhalt aus `d.interesse`. Ressourcen-/Training-/Strategiegespräch-Block je nach Haken. **Rechtskonforme KI-Lösungen → Strategiegespräch-Block** (Commander-Entscheid). Dedup (Strategie+Rechtskonforme = 1 Block). Fallback ohne Haken = Ressourcen. Reihenfolge Ressourcen → Training → Strategiegespräch.
- **BUG gefunden & gefixt:** Brevo **escaped** HTML, das über Template-Parameter `{{ params.X }}` reinkommt (Empfänger sahen rohe `<p>`-Tags). Fix: komplette Mail-HTML **im Code** bauen und als `htmlContent` senden (ohne templateId). Absender explizit `jakub.popluhar@hill-digital.at`.
- Deployed auf VPS (pm2 `brevo-proxy`, rsync, health 200). Commit `ec94028` im HD-Repo (`jakub-ai23/hd`) — Push läuft übers parallele Session-Ende-Fenster.
- Ungenutztes Brevo-Template 9 auf Original zurückgesetzt (kein kaputter Platzhalter-Rest).

### 3. Ressourcen-Seite 404 gefixt
- Ursache: Commit `f7ff23a` hatte `ars14072026/ressourcen/index.html` gelöscht (gleichzeitig die Karte aus dem E-Learning genommen). Sofortmail-CTA lief ins 404.
- Fix: Datei aus `f7ff23a^` wiederhergestellt (1:1 die vorher-live „Ressourcen & Tools"-Seite). E-Learning `index.html` behält **0** Verweise → Seite über URL erreichbar (für die Mail), im E-Learning **unsichtbar** (Commander-Wunsch). Live 200 verifiziert (~30s nach Push).

---

## Verifikation (nicht geraten — geprüft)
- Block-Logik gegen 8 Ankreuz-Szenarien standalone getestet (inkl. Dedup + Fallback).
- 4 echte Test-Submits über den Proxy an jakub@popluhar.at, **in Gmail selbst gelesen**: alle 4 rendern korrekt, jede zeigt genau ihre Blöcke (Ressourcen-only / Training-only / Strategie-only / alle-in-Reihenfolge). Bug wurde durch dieses direkte Reinschauen erst gefunden.
- Ressourcen-URL live 200 + korrekter Titel.
- Newsletter-DOI: als **nicht kaputt** verifiziert (Log-Fehler war alt/stale). Live-Test `ok:true`, Bestätigungs-Mail zugestellt + korrekt gerendert.

## Aufräumen
- Test-Kontakt `jakub@popluhar.at` aus Liste 14 entfernt (3 → 2).
- Template 9 restauriert, temporäre Dateien entfernt, lokale + VPS-Backups behalten (server.js + template-9).

## Multi-Fenster-Git-Hygiene
Drei parallele Linien: `main` (live) · `schatten-ki-uebung` (ARS-PM-Übungen, Hauptdir) · `blog-hd-restyle` (Blog, Worktree `.wt-blog-mobile`). Für alle main-Edits einen isolierten Worktree `.wt-formfix-main` benutzt, um kein aktives Parallelfenster zu stören. Vor jedem main-Edit `git pull`.

---

## Offene Punkte
- **Liste 14:** noch 2 Test-Adressen drin (`payments@jakubpopluhar.com`, `popluhar@futureroundnet.com`). Vor Event auf 0 — wartet auf Commander-„die zwei auch raus".
- **HD-Repo-Push** `ec94028`: übers parallele Session-Ende-Fenster (Commander hält meinen eigenen Push zurück).
- **Pre-existing (SITREP):** Formspree-SPOF, Clarity-Read (96% Startseiten-Absprung), Mi 15.07 ARS-Drip-Mail 2 + Brevo-Automation.

## Lessons
1. **Brevo escaped HTML in Template-Parametern (`{{ params.X }}`).** Für getailortes HTML: im Code bauen + als `htmlContent` senden, NICHT über Template-Param. (Annahme aus dem entgelt/aifluency-Muster war falsch — Rendering real prüfen, nicht annehmen.) → gilt für Selina/Proxy-Arbeit.
2. **Outputs direkt verifizieren.** `HTTP 200` / `ok:true` heißt nur „angenommen", nicht „rendert korrekt". Der Bug fiel erst auf, als die Mails in Gmail wirklich angeschaut wurden. Bei Mailversand: echten Client prüfen. → Zoya/Jocko/Selina.
3. **Multi-Fenster:** vor jedem Edit an einem geteilten Repo pullen; Worktrees zur Isolation nutzen; nie den Branch unter einem aktiven Fenster wegziehen.
