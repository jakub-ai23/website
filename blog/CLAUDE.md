# Blog (jakubpopluhar.com) — Projekt-Doku

Lebendes Steuerdokument für das Blog-Subsystem. Gilt vor dem Website-Top-Level-CLAUDE.md, wenn an `blog/` gearbeitet wird.

Created: 2026-07-05 · Owner: Jakub (Content) + Porygon (Build)

## Zweck
Content-Blog auf jakubpopluhar.com, gespeist aus Jakubs Content-Pipeline (seeds/Nuggets + Scene Protocol). Vorbilder: Tim Ferriss (content-first, understated) + Mark Manson (nach Themen sortiert). Zwei harte Prinzipien:
1. **Einheitliche Typografie**: immer klar, was Haupttitel, Untertitel, Titel 2/3, Zitat, Pull-Quote, Fließtext ist.
2. **GEO-first**: gebaut, damit LLMs (ChatGPT, Perplexity, Google AI, Claude) zitieren. Basis: `~/Projects/knowledge/geo/GEO-DOCTRINE.md`.
3. **Kein Verkauf** im Blog (Blog-Regel): informieren, keinen CTA/Preis/Pitch.

## Architektur (kurz)
Statischer Markdown zu HTML Generator, pure Python-stdlib, keine Dependencies. Ausgabe geht auf GitHub Pages (Repo `jakub-ai23/website`, **public**). Datenmodell + Entity-Graph: siehe `ARCHITECTURE.md`.

```
blog/build.py            Generator (Parser, Templates, GEO, Lints, robots/sitemap/llms)
blog/blog.css            Ein Stylesheet, dark, Marken-Tokens
blog/posts/de/*.md       DE-Artikel (source of truth)
blog/posts/en/*.md       EN-Artikel
blog/posts/_off/         inaktiv (nicht gebaut)
images/blog/             Hero-/Body-Bilder
  -> /blog/ + /blog/<slug>/            (DE)
  -> /en/blog/ + /en/blog/<slug>/      (EN)
  -> /robots.txt /sitemap.xml /llms.txt (Site-Root, generiert)
```

## Bauen + Prüfen (Befehle)
```
python3 blog/build.py            # baut alles, gibt Lint-Warnungen aus
python3 blog/build.py --drafts   # inkl. draft: true (nur Vorschau)
```
Vorschau (lokal, nie live ohne OK):
```
python3 -m http.server 8765 --bind 127.0.0.1   # dann http://127.0.0.1:8765/blog/
```
Headless-Screenshot-Check: siehe frühere Session (Chrome `--headless --screenshot`). **Preview vor Push, kein `git push` ohne explizites OK** (public Repo).

## SÄULE 1 — Typo-Vertrag (nur diese Bausteine, alles rendert gleich)
Referenzseite: `/blog/styleguide/` (Quelle `blog/posts/_styleguide.md`, unlisted).

| Element | Markdown | Regel |
|---|---|---|
| Haupttitel | Frontmatter `title` | genau 1 (H1) |
| Untertitel | Frontmatter `lede` | 0 bis 1 Standfirst |
| Titel 2 / 3 | `## ` / `### ` | keine Sprünge (Lint) |
| Zitat | `> ` | verbatim, Sprecher optional |
| Pull-Quote | `>> ` | eine Power-Line, gold, zentriert |
| Fließtext | Absatz | Standard |
| Fett-Label | `**...**` | Inline-Betonung |
| Liste | `- ` / `1.` | nur konkrete Punkte |
| Tabelle | `\| a \| b \|` + `\|---\|` | Vergleiche |
| Code/Daten | ``` Fences / `code` | Monospace |
| Bild + Caption | `![alt](src "caption")` | KI-Bilder: "Bild mit KI generiert" |
| Trenner | `---` | |

**Haus-Regel:** keine em/en-Dashes (Hook blockt; Build lintet). Kommas, Doppelpunkte, Punkte.

## SÄULE 2 — Content-Ingestion (Nugget/Scene zu Artikel)
Blog-Quelle bleibt `blog/posts/<lang>/*.md` mit sauberem Frontmatter:
```
title, slug, date (YYYY-MM-DD), category, lede, hero, caption, description, draft
```
Redaktions-Schritt aus `~/Projects/content/articles|posts/<file>.md`:
1. Interne Blöcke strippen: `META:`/SURF-Footer, Hashtags, "P.S."-CTA, `[ABOVE THIS LINE]`-Sentinel, Status/Voice-Italic-Zeile.
2. **Sensitivity-Gate:** nur ohne offene `[INTERN-*]`/Sensitivity-Flags, Status freigegeben (Scene-Protocol Paragraf 6).
3. Blog-Frontmatter setzen, in `blog/posts/<lang>/` ablegen, bauen.
Optionaler Helfer (Phase 2B): `blog/import.py <pfad>` erzeugt einen Blog-Ready-Stub (Mensch prüft, kein Auto-Publish).

Konventionen: Dateiname mit `_` Prefix = unlisted (immer gebaut, nie gelistet, nicht in Sitemap). `draft: true` = nur mit `--drafts`.

## SÄULE 3 — GEO-Checklist
**P1 (im Build, automatisch):** kein JS für Content · `robots.txt` (GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot, Google-Extended, Bingbot) · `sitemap.xml` · canonical · `<title>`+description (Build warnt bei fehlen) · Person-JSON-LD global · BlogPosting-JSON-LD pro Artikel · answer-first + saubere H-Hierarchie (Lint) · og:image · `llms.txt`.
**P2 (Autoren-Checklist, pro Artikel):** answer-first (Kernaussage in Satz 1 bis 3), inline-Quellenlinks, benannte Zitate, konkrete Zahlen, in sich geschlossene Sektionen, optional FAQ-Block.
**P3 (Owner, off-blog):** Bing Webmaster, **Wikidata-Eintrag Jakub**, Dritt-Erwähnungen, Share-of-Model-Messung (DE+EN), GA4 AI-Referral.

## SÄULE 4 — Kategorien (Phase 3, DE-first)
`aus-der-praxis` (was Jakub selbst baut) · `jakub-trainings` (Klienten/Firmen) · `ki-wissen` (Erklärendes, "Was ist ein LLM"). Hybrid-Index: Neueste oben, darunter Kategorie-Cluster; je Kategorie eigene Seite. Frontmatter `category:` schon aktiv.

## SÄULE 5 — Sharing
Share-Buttons pro Artikel (LinkedIn zuerst, X, Facebook, Link kopieren), reine Share-URLs, kein Backend. Kommentare = Phase 4 (Giscus, GitHub Discussions).

## Phasen-Status
- [x] Phase 1: flaches Gerüst, DE-Artikel, Hero+Caption, Nav
- [x] Phase 2A: Typo-Vertrag + Parser (Tabellen, Pull-Quote, Caption) + Styleguide + Share + GEO-P1 + Scaffolding
- [x] Phase 2B: Ingestion-Workflow + `import.py` (Dry-Run default, `--write` speichert draft-Stub)
- [x] Phase 3: Kategorien (Hybrid-Index + Kategorieseiten + Breadcrumbs, DE). `category`-Feld aktiv, CATEGORIES-Config in build.py
- [ ] Phase 4: EN-Mirror + Wikidata/Entity-Bridge, Kommentare, Start-Here, Newsletter, Messung

## Bekannte offene Punkte
- EN-Kategorie-Labels bei Phase 4 bestätigen.
- Autoren-Foto aktuell `images/profile/headshot.png` (Crop aus profile/9.png).
