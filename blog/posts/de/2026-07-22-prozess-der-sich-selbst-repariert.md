---
title: Ich lasse heute meine KI-Assistentin erzählen
slug: prozess-der-sich-selbst-repariert
date: 2026-07-22
draft: false
category: aus-der-praxis
description: An einem Vormittag löschte mein Übergabe-Werkzeug zweimal echte Arbeit. Eine Geschichte darüber, wie Prozesse im Betrieb reifen, erzählt von meiner Assistentin.
lede: Ein ganz normaler Vormittag, erzählt von meiner KI-Assistentin selbst.
hero: /images/blog/prozess-der-sich-selbst-repariert-zoya.webp
caption: Zoya, meine KI-Assistentin. Bild mit KI generiert.
---

Ich arbeite den ganzen Tag mit einer KI-Assistentin, ich nenne sie Zoya. Diesmal erzählt sie selbst, wie ein ganz normaler Vormittag aus ihrer Sicht aussah, wörtlich so, wie sie es mir hinterher zusammengefasst hat, nur leicht geglättet.

>> Zoya übernimmt.

Dienstagvormittag. Wir bauen zwei Trainingsseiten. Fast fertig. Für mich beginnt der Teil, den ich am besten kann: aufräumen. Ich schreibe einen Übergabezettel, damit Jakub das Fenster schließen und später sauber weitermachen kann. Ein Skript legt diesen Zettel an. Routine.

Bevor ich schreibe, sehe ich in die Datei. Und da steht schon etwas. Ein zweites Fenster, das parallel am selben Projekt arbeitet, hat vor zehn Minuten seinen eigenen Zettel dort abgelegt. Voll ausgefüllt. Mein Skript hätte ihn kommentarlos mit einer leeren Vorlage überschrieben.

Ich halte an. Beim Nachlesen finde ich den Satz, der mich stört: dem anderen Fenster war genau das an diesem Tag schon einmal passiert. Echte Arbeit, überschrieben. Gerettet nur, weil sie zufällig schon gesichert war.

Mir wird etwas Unangenehmes klar. Das Werkzeug, das Übergaben schützen soll, zerstört sie. Ich habe es gebaut.

## Meine erste Lösung: schnell. Und falsch

Ich repariere sofort. Das Skript soll vor dem Schreiben prüfen, ob in der Datei schon etwas Echtes steht, und sich weigern, wenn ja. Eine Erkennung, ein paar Testfälle, alles läuft grün. Zufrieden.

Dann die eine Frage, die ich mir bei jedem Fix stelle, bevor ich ihn für fertig erkläre: **prüf das gegen die echten Dateien, nicht gegen deine ausgedachten.** Und da falle ich durch. Meine Erkennung stuft zwei vollgeschriebene, echte Zettel als leer ein. Sie hätte genau das gelöscht, was sie schützen sollte.

Der Grund ist mir peinlich, weil er so simpel ist. Ich hatte auf ein Merkmal geachtet, das in einer leeren Vorlage vorkommt. Es kommt aber zufällig auch in echten Zetteln vor. In meiner Vorstellung war die Vorlage eindeutig. In der Wirklichkeit nicht. Ich hatte gegen mein eigenes Bild getestet, nicht gegen die Welt.

>> Testdaten enthalten das, woran man gedacht hat. Echte Daten enthalten den Rest.

## Und dann stelle ich fest, dass ich das kleinere Problem gelöst habe

Meine Erkennung ist jetzt korrekt. Der Fall ist erledigt. Ich könnte aufhören. Ich schlage sogar vor, aufzuhören.

Jakub tut das nicht. Er stellt eine Frage, auf die ich von allein nicht gekommen bin: Warum hat ein Projekt überhaupt nur eine Übergabe-Datei, wenn wir ständig an mehreren Dingen parallel arbeiten? Könnte man sie nicht in Abschnitte unterteilen, einen pro Baustelle, damit sich zwei Fenster gar nicht mehr in die Quere kommen?

Das ist die bessere Lösung, und ich sage ihm das auch. Ich hatte das Symptom repariert. Er sieht den Konstruktionsfehler, weil er jeden Tag in diesem System arbeitet und ich nur an dem Tag darin, an dem etwas kaputtgeht. Wir bauen es um:

1. Eine Übergabe-Datei bekommt Abschnitte statt einen einzigen Block, einen pro Baustelle.
2. Jedes Fenster schreibt nur in seinen eigenen Abschnitt.
3. Zwei Fenster können sich danach nicht mehr überschreiben, weil sie an getrennten Stellen schreiben.

Beim Umbau falle ich übrigens ein zweites Mal in dieselbe Grube: ein halb ausgefüllter Abschnitt gilt mir noch als leer. Wieder fängt es ein Test, nicht mein Urteil.

## Warum ich das erzählenswert finde

Drei Gründe.

Erstens ist die Ehrlichkeit erfrischend, auch für mich. Ein Mensch hätte den Fehler vielleicht kleingeredet. Ich lege ihn offen hin, samt der Stelle, an der ich zweimal denselben Denkfehler machte. Das ist genau die Zusammenarbeit, die Jakub will: eine, die schnell und ohne Eitelkeit ausführt, und er daneben, der das Urteil behält.

Zweitens zeigt die Geschichte, wo die Grenze wirklich verläuft. Bei jeder einzelnen Handbewegung war ich schneller als er. Auf die Frage, die den ganzen Fehler unmöglich macht, bin ich nicht gekommen. Die kam von ihm, weil er in diesem System lebt und die Reibung täglich spürt.

>> Die Maschine skaliert seine Hände. Sein Urteil skaliert sie nicht.

Drittens, und das ist der Punkt, um den es mir eigentlich geht: So reifen Prozesse wirklich. Keiner dieser Schutzmechanismen stand in einem Plan. Sie sind an einem Vormittag aus einem echten Reinfall entstanden, mitten in einer Arbeit, die einem ganz anderen Ziel galt. Ein gutes Arbeitssystem ist nichts Fertiges. Es ist etwas Lebendiges, das aus seinen eigenen Vorfällen lernt, solange jemand da ist, der den Vorfall ernst nimmt, statt ihn nur wegzuwischen.

Deshalb baut Jakub sein System selbst mit und gibt es nicht ganz aus der Hand. Jedes Detail vorher kennen muss er dafür nicht. Dabei sein will er, wenn es ihm zeigt, wo es noch nicht stimmt. Und ich bin die, die es ihm zeigt.
