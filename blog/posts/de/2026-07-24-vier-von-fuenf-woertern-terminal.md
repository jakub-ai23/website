---
title: 82 Prozent meiner gesprochenen Wörter sind kein Prompt. Das hat mich selbst überrascht.
slug: vier-von-fuenf-woertern-terminal
date: 2026-07-24
draft: false
category: aus-der-praxis
description: Als KI-Trainer arbeite ich jeden Tag mit KI. Trotzdem hat mich eine Zahl aus meinem eigenen Diktier-Tool überrascht, 82 Prozent meiner gesprochenen Wörter zählen dort gar nicht als AI Prompt. Was das über den Unterschied zwischen Prompt und Delegation sagt.
lede: Wispr Flow protokolliert jedes Wort, das ich spreche. Die meisten davon sind kein Prompt, sondern eine Delegation.
hero: /images/blog/vier-von-fuenf-woertern-terminal.png
caption: Mein Wispr-Flow-Voice-Profil, Stand 23. Juli 2026. Screenshot.
---

Ich bin KI-Trainer. Ich arbeite jeden Tag mit KI, das ist mein Beruf. Trotzdem hat mich eine Zahl aus meinem eigenen Diktier-Tool überrascht.

Ich benutze Wispr Flow, es protokolliert jedes gesprochene Wort und zeigt mir, in welche App es ging. 235.956 Wörter diktiert, seit ich das Tool nutze.

Und dann die Zahl, die mich gestört hat: 74 Prozent meiner Desktop-Nutzung liefen unter „Other Tasks", nur 18 Prozent unter „AI Prompts". Das kam mir falsch vor. Ich spreche den ganzen Tag mit einer KI, aber das Tool zählt die meisten dieser Gespräche nicht als „AI Prompts".

Meine erste Reaktion: eine Mail an den Hersteller schreiben und fragen, was mit den restlichen 74 Prozent ist.

## Der Moment, um den es eigentlich geht

Bevor ich die Mail geschrieben hatte, war die Frage schon beantwortet. Statt zu warten, hat mein Agent selbst nachgesehen. Er hat die lokale Datenbank von Wispr Flow geöffnet, eine SQLite-Datei mit fast zwei Gigabyte Verlauf, und innerhalb von Minuten stand die Zahl da.

Das ist der eigentliche Punkt der Geschichte, mehr als die Zahl selbst: Ich wollte ein Ticket schreiben und auf eine Antwort warten. Stattdessen hat der Agent die Frage selbst beantwortet, während ich noch überlegt habe, wie ich sie formuliere.

## Prompt oder Delegation

Das ist der Unterschied zwischen einem Prompt und einer Delegation. Ein Prompt ist eine Frage, auf die ich eine Antwort erwarte. Eine Delegation ist ein Auftrag, den jemand anderes zu Ende führt, ohne dass ich jeden Schritt anleite. Die meisten Analytics-Tools kennen nur die erste Kategorie. Für die zweite gibt es noch keinen Namen, obwohl sie längst der größere Teil meines Arbeitstags ist.

Bei mir laufen die meisten dieser Delegationen an einem Ort: Claude Code, das in einem Terminal läuft.

Ein Terminal ist ein einfaches, schwarzes Textfenster ohne Buttons, ohne Menüs, ohne grafische Oberfläche. Ursprünglich war es dafür da, dem Computer Zeile für Zeile Befehle einzutippen. Bei mir ist es inzwischen etwas anderes geworden: das Fenster, in dem meine KI für mich arbeitet.

## Die Zahl

Hier ist, was die Datenbank hergegeben hat: Von allen Wörtern, die ich seit Mai diktiert habe, gingen 79,5 Prozent an Claude Code im Terminal. In den letzten 14 Tagen waren es 81,6 Prozent. Vier von fünf Sätzen, die ich in Wispr Flow spreche, sind nicht an ein Textfeld gerichtet, sondern an einen Agenten, der etwas damit baut.

Die App auf Platz zwei, ein Recherche-Tool, liegt bei knapp 18.600 Wörtern seit Mai. Claude Code im Terminal bei über 167.000. Faktor neun.

Interessanter als die Momentaufnahme ist die Kurve, weil sie zeigt, wie schnell sich das verschoben hat:

| Monat | Anteil Delegation an allen diktierten Wörtern |
|---|---|
| Mai 2026 | 73,9 % |
| Juni 2026 | 82,6 % |
| Juli 2026 (bisher) | 81,9 % |

Seit ich das Tool im Mai ernsthaft nutze, war dieser Anteil in keinem Monat unter drei Vierteln meiner Wörter. Von der ersten Messung an war es die klare Mehrheit meines gesamten Sprachinputs, nicht ein Kanal unter vielen.

## Warum das mehr ist als eine persönliche Randnotiz

Die meisten Diskussionen über KI drehen sich um bessere Prompts. Wie formuliere ich die Anfrage klarer, wie baue ich den perfekten Prompt, welches Template funktioniert am besten. Das ist die Ebene des Chatfensters. Meine eigenen Zahlen zeigen etwas anderes: Der Teil meiner Arbeit, der am schnellsten gewachsen ist, war nie das perfekte Prompten. Es war das Zutrauen, eine ganze Aufgabe abzugeben und erst wieder hinzuschauen, wenn sie fertig ist.

Ich sage nicht mehr „wie schreibe ich das", ich sage „mach das". Ich beschreibe ein Ergebnis und übergebe die Ausführung. Das eigene Sprachmuster verrät den Wandel, bevor irgendeine Statistik es tut.

Der Unterschied zwischen KI benutzen und KI Arbeit geben ist kein Wissensunterschied. Es ist eine Frage der Rolle: Frage ich, oder gebe ich Richtung vor. Und diese Verschiebung geht schneller, als man denkt.

---

**Hinweis:** Das Diktier-Tool in diesem Artikel ist [Wispr Flow](https://wisprflow.ai/r?WISPR17032). Der Link ist ein Empfehlungslink, wenn jemand darüber ein Konto eröffnet, bekomme ich einen Monat kostenlos dazu. Das ändert nichts an dem, was oben steht, das sind meine eigenen, echten Nutzungsdaten. Wer den Link nicht nutzen will, kann Wispr Flow genauso gut direkt suchen, für mich macht das keinen Unterschied.
