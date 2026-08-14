---
title: "Styleguide: jedes Element"
slug: styleguide
date: 2026-07-05
draft: false
description: Referenzseite. Zeigt jeden erlaubten Baustein eines Artikels, damit alles einheitlich bleibt.
lede: Das ist der Untertitel (lede). Ein Satz, der reinzieht. Genau ein Standfirst pro Artikel.
hero: /images/blog/swat-butterfly.webp
caption: So sieht ein Hero-Bild mit Caption aus. Bild mit KI generiert.
---

Das ist **Fließtext**. Ein normaler Absatz in der Lesespalte mit `Inline-Code`, einem [Link](https://jakubpopluhar.com) und *kursiver* sowie **fetter** Betonung. So sieht der Standard aus, an dem sich alles orientiert.

## Titel 2 (H2, Sektion)

Nach einer H2 folgt wieder Fließtext. Jede Sektion sollte für sich verständlich sein, auch aus dem Zusammenhang gerissen (GEO: in sich geschlossene Passagen).

### Titel 3 (H3, Untersektion)

Eine Ebene tiefer. Nicht von H2 auf H4 springen, sonst warnt der Build.

> Das ist ein verbatim Zitat (blockquote). Wörtlich, mit Sprecher am Ende. (Jemand Konkretes)

>> Das ist ein Pull-Quote. Die eine Zeile, die hängen bleibt.

Eine Aufzählung, nur für konkrete Punkte:

- Erster konkreter Punkt
- Zweiter konkreter Punkt
- Dritter konkreter Punkt

Eine nummerierte Liste:

1. Schritt eins
2. Schritt zwei
3. Schritt drei

Eine Vergleichstabelle:

| Alt | Neu |
|---|---|
| Ein Modell frei laufen lassen | Klare Rolle plus Limits |
| Hoffen, dass es passt | Prüfen, im Urteil bleiben |

Ein Code- bzw. Datenblock:

```
python3 blog/build.py
```

Ein Trenner:

---

Und ein Bild mit Caption mitten im Text:

![Alt-Text](/images/blog/swat-butterfly.webp "Bildunterschrift im Fließtext. Bild mit KI generiert.")

Das war jeder Baustein. Mehr Elemente gibt es bewusst nicht, damit jeder Artikel gleich aussieht.
