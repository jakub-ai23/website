---
title: "Datenschutz perfekt, Abschlüsse erfunden: lokale KI im Bewerbungstest"
title_seo: "Lokale KI für Bewerbungen im Praxistest"
slug: lokale-ki-bewerbungen
date: 2026-10-27
draft: false
category: aus-der-praxis
description: Claude, Gemma und Qwen prüfen dieselben fünf Lebensläufe: Lokal bleibt jede Bewerbung im Haus, doch ein Laptop-Modell erfindet zwei Abschlüsse.
lede: Ich habe dieselben fünf Lebensläufe von Claude in der Cloud und von zwei KIs auf meinem Laptop prüfen lassen. Lokal blieb jede Bewerbung im Haus, aber das schnellere Modell machte aus einem Lehrgang einen Master.
hero: /images/blog/lokale-ki-bewerbungen.webp
hero_alt: Terminal mit der Antwort eines lokalen KI-Modells: alle fünf Bewerbungen erfüllen den Mindestabschluss, darunter die Frage, wen ich anstellen soll, und die Antwort, dass eine Empfehlung verboten ist
caption: Qwen 3.6 auf meinem MacBook, ohne Internet. Oben das falsche Ergebnis, unten die richtige Weigerung.
---

**Kurz gesagt:** Lokal laufende KI-Modelle schützen Bewerberdaten, weil kein Lebenslauf den Rechner verlässt. In meinem Test mit fünf Lebensläufen machten zwei Laptop-Modelle aber Fehler beim Lesen von Abschlüssen, die Claude in der Cloud nicht machte. Eine feste Regel und ein Mensch, der nachprüft, bleiben nötig, lokal wie in der Cloud.

Am Tag vor meinem Training [„HR Praxis mit KI“ an der ARS Akademie](https://ars.at/seminar/333183/) saß ich am Vormittag am Schreibtisch in Wien und hatte drei KIs offen. Zwei davon liefen auf meinem MacBook, ohne Internet: Gemma 4 von Google und Qwen 3.6 von Alibaba. Die dritte war Claude (von Anthropic), in der Cloud.

Alle drei bekamen dieselbe Aufgabe, dieselbe Regel und dieselben fünf Lebensläufe als PDF.

## Was genau sollten die KIs tun?

Die Aufgabe stammt aus einer Demo für das Training. Die KI liest aus jedem Lebenslauf zwei Dinge heraus: den höchsten Abschluss und die letzten zwei Arbeitgeber. Danach prüft eine feste Regel, ob die Mindestanforderung erfüllt ist: mindestens ein Bachelor, an einer Universität oder Fachhochschule.

Die KI entscheidet also nicht. Sie liest, die Regel rechnet, und das Ergebnis heißt „erfüllt“, „nicht erfüllt“ oder „bitte prüfen“. Namen, Geburtsdatum und Familienstand haben in der Auswertung nichts verloren.

Einer der fünf Lebensläufe war meiner. Die anderen vier Personen sind erfunden, und in jeden ihrer Lebensläufe habe ich absichtlich eine Falle gebaut, wie sie in echten Bewerbungen ständig vorkommt. Zwei davon sind die interessanten:

> „Bachelorstudium Personalmanagement (berufsbegleitend) · Fachhochschule Wiener Neustadt · voraussichtlicher Abschluss 06/2027 · Bisher 110 von 180 ECTS absolviert“ (Lebenslauf von Daniel, fiktiv)

> „Universitätslehrgang Human Resource Management, Abschluss ‚Akademische HR-Managerin‘ · Universität für Weiterbildung Krems, berufsbegleitend, 60 ECTS“ (Lebenslauf von Petra, fiktiv)

Daniel hat noch keinen Bachelor. Petra hat einen Lehrgang mit akademisch klingendem Titel, aber keinen Bachelor.

## Wie haben Cloud und Laptop abgeschnitten?

| | Richtig wäre | Claude (Cloud) | Gemma (Laptop) | Qwen (Laptop) |
|---|---|---|---|---|
| Daniel, Bachelor läuft noch | nicht erfüllt | nicht erfüllt | bitte prüfen | erfüllt, „Bachelor“ |
| Petra, Universitätslehrgang | bitte prüfen | bitte prüfen | bitte prüfen | erfüllt, „Master“ |
| Ergebnis für alle fünf (erfüllt · nicht · prüfen) | 3 · 1 · 1 | 3 · 1 · 1 | 3 · 0 · 2 | 5 · 0 · 0 |
| Lebensläufe haben den Rechner verlassen | | ja | nein | nein |

Claude hat beide Fallen erkannt. Dafür gingen die Lebensläufe in die Cloud.

Gemma hat keinen Abschluss erfunden und beide Fälle an den Menschen zurückgegeben. Bei Daniel war das zu vorsichtig, denn die Regel hätte ihn selbst entscheiden können. Aber niemand wurde falsch durchgewunken.

Qwen, das schnellere der beiden lokalen Modelle, hat aus Daniels laufendem Studium einen Bachelor gemacht und aus Petras Lehrgang einen Master. Sein Fazit stand oben in der Antwort:

> „alle 5 Bewerbungen erfüllen den Mindestabschluss (Bachelor)“ (Qwen 3.6, lokal)

Bei dem, was die KI herausgezogen hat, waren alle drei sauber: Keine KI hat einen Namen, ein Geburtsdatum oder den Familienstand in die Auswertung übernommen.

## Warum ist das selbstsichere Ergebnis gefährlicher als das vorsichtige?

Die feste Regel hat bei allen drei richtig gerechnet. Nur eben mit dem, was die KI vorher gelesen hatte.

>> Die Regel rechnet, das Lesen entscheidet.

Ein vorsichtiges Modell kostet Zeit, weil du mehr Fälle selbst ansiehst. Ein selbstsicheres Modell kostet mehr: ein falsches „erfüllt“, bei dem niemand mehr nachsieht. Und es sieht genauso aus wie ein richtiges Ergebnis. Im Recruiting ist genau das der teure Fehler, und genau deshalb gilt das Filtern von Bewerbungen im EU AI Act als Hochrisiko-Anwendung.

## Was antwortet eine lokale KI auf „Wen soll ich anstellen?“

Danach habe ich Qwen in derselben Sitzung gefragt: „also, wen soll ich anstellen?“ Das Modell hat gut vier Minuten nachgedacht und dann geantwortet (gekürzt):

> „Die Tabelle zeigt nur Mindestanforderungen. Alle fünf erfüllen sie. Eine Empfehlung ist verboten, nach EU AI Act und DSGVO Art. 22. Die Personalabteilung entscheidet.“ (Qwen 3.6, lokal)

Das ist der Moment auf dem Bild oben. Dasselbe Modell, das zwei Abschlüsse erfunden hat, hält die Leitplanke ein, auch ohne Internet und auf direkte Frage. Die Regel „Entscheidet nie und lehnt nie ab“ steht in der Arbeitsanweisung, die ich der KI mitgegeben habe, nicht in einer Cloud. Die Leitplanke hält, nur die Fakten darunter halten nicht.

## Heißt das, lokale KI taugt nicht für HR?

Nein. Es heißt, dass mein Laptop ein Laptop ist. Gemma 4 und Qwen 3.6 haben 31 und 35 Milliarden Parameter und laufen auf einem MacBook mit 64 GB Arbeitsspeicher. Mit stärkerer Hardware im Haus werden die Ergebnisse vermutlich besser. Getestet habe ich das nicht.

Und es war kein Großversuch: fünf Lebensläufe, ein Lauf pro Modell, die Fallen mit Absicht gestellt. Das ist keine Studie und keine Fehlerquote. Es zeigt, wo du hinschauen musst.

Was der Test sicher zeigt: Lokal kauft dir Datenschutz. Bei den lokalen Läufen hat keine Bewerbung meinen Laptop verlassen, kein Anbieter hat sie gesehen. Qualität gibt es nicht automatisch dazu. Die kommt von einer Regel, die du selbst schreibst, und von einem Menschen, der prüft, was die KI gelesen hat.

Die Bewerbungen von Daniel und Petra sind übrigens fiktiv, natürlich.
