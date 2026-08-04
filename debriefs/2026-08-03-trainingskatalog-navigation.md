# Debrief — Trainingskatalog öffentlich + Angebote-Navigation (jakubpopluhar.com)

**Created:** 2026-08-03 · **Last updated:** 2026-08-03
**Fenster:** 14:29–15:15 · **Persona:** Zoya → Jocko (Ausführung/Push)
**Einheit:** JT (AI Training / persönliche Marke) · **Typ:** Session-Debrief (volles Session-Ende)
**Zeit:** 14:29–15:15 (46 min Fenster, [NETTO siehe Daily Log], hands-on)

---

## 1. Auftrag

Commander wollte die Trainings, die er bisher nur in personalisierten, passwortgeschützten
Firmenseiten verschickt (BFI Vorarlberg, Digital Campus Vorarlberg), auch öffentlich unter
„Angebote" auf jakubpopluhar.com haben. Dazu eine Navigationslösung: beim Schweben über
„Angebote" sollen sich One-on-One-Coaching, Inhouse-Trainings und Standard-Trainings aufklappen
(Vorbild Cal.com).

## 2. Was geliefert wurde

**Neue öffentliche Seite `/trainings/`.** Die sechs Trainingskarten aus den Firmenseiten,
wortgleich übernommen, im Stil der Hauptseite: KI am Schreibtisch · KI im HR-Alltag ·
Copilot im Arbeitsalltag · ChatGPT, Gemini oder Claude · Konsumentenpsychologie ·
Maßgeschneiderte Trainings. Darüber die Angebotsleiter mit „Sie sind hier". JSON-LD-Liste,
canonical, og-Tags, Sitemap-Eintrag — Futter für Antwortmaschinen, der Kanal, über den
Rebecca Reinhold heute Vormittag hereinkam.

**Vier Kursbeschreibungen auf saubere URLs gezogen.** Sie lagen bereits öffentlich, aber unter
`/copilot-onepager/` und ähnlich, ohne Beacon, ohne Rechtslinks, ohne canonical. Jetzt
`/trainings/<slug>/`, jeweils mit Zurück-Link, canonical, Impressum/Datenschutz im Fuß und
Tracking-Beacon. Alte Pfade bleiben als Weiterleitung stehen. Damit sind drei Befunde aus
dem Vormittags-Audit erledigt (fehlender Beacon, fehlende Rechtslinks, ungelistete Seiten).

**Namensregel gesetzt.** Das eigene Grundlagentraining heißt überall „KI am Schreibtisch".
„KI im Büroalltag" ist der Titel der ARS und steht nur noch dort, wo die ARS gemeint ist
(Startseite, Terminseite). Umbenannt: Seitentitel, H1, Beschreibung, Katalogkarte,
Querverweis in der Copilot-Karte, JSON-LD, Sitemap, URL. PDF gegen die Schreibtisch-Fassung
getauscht.

**Angebote-Aufklappmenü** auf Startseite, `/trainings/`, `/ueber-mich/`,
`/ki-personal-training/` und `/termine/`. Öffnet per Hover, per Tastaturfokus (CSS) und per
Tippen auf Touchgeräten (Skript). Escape schließt.

**Angebote-Abschnitt der Startseite:** zwei schmale Verweise auf `/trainings/` und `/termine/`
unter dem KI-Personal-Training.

## 3. Entscheidungen

- **Trainingskatalog wird öffentlich** (nicht nur als passwortgeschützter Klon). Begründung:
  Antwortmaschinen können nur zitieren, was öffentlich steht, und genau darüber kam heute
  der erste belegte Lead. Die personalisierten Klone bleiben davon unberührt und behalten
  ihre Exklusivität, weil sie zusätzlich den Lebenslauf tragen.
- **Eigene URL-Ebene `/trainings/`** statt der bisherigen `-onepager`-Pfade, alte Pfade als
  Weiterleitung. Saubere, zitierfähige Adressen.
- **„KI am Schreibtisch" ist der eigene Produktname**, „KI im Büroalltag" gehört der ARS.
- **Nav-Punkt „Über mich" bleibt auf der Landingpage** (Commander-Rücknahme meiner Änderung).
  Die Seite `/ueber-mich/` bleibt bestehen und erreichbar über „Mein Weg, ausführlich".

## 4. Eigene Fehler

**(a) Eine mehrdeutige Ansage einseitig gelesen.** Der Commander diktierte: „und wo ist
komplett die Über mich seite? Die ist gar nicht verlinkt, weil alles in der Navigation Bar,
was verlinkt ist, landet auf der Landingpage und das ist nicht richtig." Das lässt zwei
Deutungen zu: der Navigationspunkt soll auf die Seite zeigen, oder er wundert sich, wo die
Seite geblieben ist, will den Punkt aber auf der Landingpage lassen. Ich habe die erste
gewählt, umgebaut und live gepusht, ohne die Mehrdeutigkeit zu benennen. Seine nächste
Nachricht war die zweite Deutung. Zurückgenommen in `286db48`, geloggt als D-0539. Kosten
gering (drei Minuten, ein Commit), weil die Änderung klein und reversibel war. Richtig
gewesen wäre eine Rückfrage von fünf Sekunden.

**Nachtrag, zweite Fehlerebene:** die erste Fassung der Lesson in `lessons-learned.md`
beschrieb diesen Vorgang falsch. Sie stellte es so dar, als hätte ich ungefragt geändert,
obwohl der Commander das Thema selbst aufgebracht hatte. Aufgefallen beim Gegenlesen der
Originalnachrichten für das Scene Protocol, korrigiert am selben Tag. Ursache: aus der
Erinnerung geschrieben statt aus der Quelle, dasselbe Muster wie im Vormittags-Debrief.

**(b) Menü hinter dem Foto.** Das Aufklappmenü lag auf den Unterseiten hinter dem Hero-Bild
und die Navigationspunkte waren vertikal versetzt. Beides erst nach dem Push aufgefallen,
weil ich die Unterseiten nach dem Einbau nicht angesehen habe, nur die Startseite. Vorschau
gehört auf jede geänderte Seite, nicht auf die repräsentative.

## 5. Was das System gelernt hat

- Fix an der Vorlage, nicht am Klon: die vier Kursseiten existierten dreifach (Root plus zwei
  Firmenordner). Der öffentliche Satz ist jetzt der kanonische; die Firmenordner behalten
  bewusst eigene Kopien, weil sie selbsttragend sein müssen.
- Der Snap-Scroll-Aufbau der Startseite begrenzt, was in einen Abschnitt passt. Die zwei
  Verweiszeilen mussten zweimal verkleinert werden und liegen jetzt bei 778 px gegen
  740 px Fensterhöhe im Testfenster. Auf normalen Bildschirmen passt es, auf sehr flachen
  Laptop-Fenstern rutschen sie unter die Kante.
- Kein `hide-until-active`-Muster verwendet (Projekt-CLAUDE.md): das Einblenden auf
  `/trainings/` läuft zeitbasiert beim Laden, der Inhalt ist ab dem ersten Frame sichtbar,
  auch ohne JavaScript.

## 6. Offen

- **Hero-Text auf `/ki-personal-training/` kürzen** (Commander, ausdrücklich für später).
  Einstiegspunkt steht im SITREP.
- **Blognavigation** zeigt weiter auf `/#about` und `/#services`. Gehört in `blog/build.py`
  (Zeilen 376–378), danach Neubau aller Artikel. Bewusst nicht von Hand editiert.
- **Englische Strecke:** kein `/en/trainings/`, kein Aufklappmenü auf `/en/`.
- **`/ueber-mich/`** steht weiter in Sitemap und Index. Ob die Seite wirklich versteckt
  werden soll, ist offen.
- **Startseite wiegt weiter rund 20 MB** (drei Profil-PNGs), Worktree `bilder-optimieren`
  liegt bereit, nicht auf main.

## Verweise

- SITREP-Strang: `~/Projects/builds/websites/personal/SITREP.md` → `trainings-katalog-nav`
- Commits auf `main`: `93c4ff8` (Katalog + Menü) · `276d691` (Nav-Korrekturen) · `286db48` (Rücknahme)
- Vormittags-Audit: `~/Projects/ops/website-audit/reports/2026-08-03-jakubpopluhar.md`
