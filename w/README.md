# Workshop-Seiten-System (`/w/`)

**Created:** 2026-06-19 · **Last updated:** 2026-06-19

Ein Dach für alle Workshop-/Trainings-Auslieferungsseiten von Jakub Popluhar.
Statt jede Seite als 600-Zeilen-Copy-Paste zu bauen, teilen sich alle Seiten
**ein** Design-System und **ein** Verhaltens-Skript. Neue Seite = 5-Minuten-Klon.

Live-Übersicht (intern, noindex): **https://jakubpopluhar.com/w/**

## Was hier liegt

```
w/
├── index.html        Private Übersicht aller Workshops (noindex). Nur für Jakub.
├── README.md         Diese Datei.
├── assets/
│   ├── style.css     Gemeinsames Design-System (Gold/Charcoal, alle Komponenten).
│   └── workshop.js   Copy-to-Clipboard, Akkordeon (1 offen), Sidebar-Scroll-Spy.
└── _template/
    └── index.html    Klon-Vorlage für jede neue Seite.
```

Alle Asset-Pfade in `style.css` sind **absolut** (`/fonts/...`, `/images/...`),
damit eine Seite an jedem Pfad funktioniert.

## Neue Workshop-Seite bauen

```bash
cp -r w/_template w/<neuer-name>
```

Dann `w/<neuer-name>/index.html` öffnen und alle `[[...]]`-Platzhalter ersetzen:
Titel, Badge, Hero, Sidebar-Links, Sektionen. **Wichtig:** Die Sidebar-Links
(`href="#xy"`) müssen den Sektions-IDs (`id="xy"`) entsprechen, daran hängt der
Scroll-Spy. CSS oder JS werden **nie** kopiert, sie kommen aus `/w/assets/`.

URL der neuen Seite: `jakubpopluhar.com/w/<neuer-name>/`

## Komponenten (CSS-Klassen)

| Klasse | Zweck |
|---|---|
| `.site-header` / `.header-badge` | Sticky-Header mit Logo + Kunden-/Datums-Badge |
| `.hero` / `.badge` | Titelblock |
| `.doc-callout` | Großer Link aufs gemeinsame Google-Doc-Arbeitsblatt |
| `.page-layout` + `.sidebar-nav` | Zweispaltig: Sticky-Sidebar (Scroll-Spy) + Inhalt |
| `.section-divider` (`.time-tag`) | Abschnitts-Überschrift mit optionaler Zeitangabe |
| `.exercise` | Übungs-/Inhaltskarte |
| `.prompt-block` | Kopierbarer Prompt (Klick kopiert; `white-space: pre-line`) |
| `.compare-table` | Vergleichs-/Framework-Tabelle (z.B. CITER) |
| `.magic-box` (`.quote`) | Hervorgehobener Merksatz / Formel |
| `details` + `.collapsible-content` | Aufklappbare Schritte (pro `.exercise` nur einer offen) |
| `.llm-grid` / `.llm-card` | Tool-Karten (ChatGPT/Gemini/Claude, "Im Browser öffnen") |
| `.links` / `.link-card` | Link-Karten für Index-/Landing-Seiten |

## Regeln

- **Bestehende ausgelieferte Seiten nicht verschieben.** Ihre URLs stehen auf
  verteilten QR-Codes/Flyern (ars140426, viennaup2205, viennaupagents, hw190526).
  Die Konvention gilt ab jetzt für **neue** Seiten. Eine Umstellung der Alten auf
  das geteilte CSS ist ein separater, vorsichtiger Durchgang (Regressionsrisiko live).
- **Immer `noindex`** auf Auslieferungsseiten (Kundennamen, Einmal-Lieferung).
- **Kein öffentliches Hub**, das die Kundenseiten verlinkt (Kunden-Leak). Die
  Übersicht hier ist `noindex` und nur intern.
- **Kein em/en-Dash** im deutschen Text (Projekt-Standard).
- Analytics-Beacon (`site=jakubpopluhar`) ans Seitenende, wie in der Vorlage.

## Status der bestehenden Seiten (Stand 2026-06-19)

Alle noindex außer wo vermerkt. Noch **selbstständig** (eigenes Inline-CSS), nicht
aufs geteilte System umgestellt: `ars140426`, `viennaup2205`, `viennaupagents`,
`hw190526`, `techtrain0306`, `sportunionm2`, `pmi` (öffentlich).
Doppelt vorhanden: `training/` und `weiter/` (beide "Nach dem Training") - bei
Gelegenheit zusammenführen.
