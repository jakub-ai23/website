/* ============================================================================
   quiz.js — Mini-Checks für eine E-Learning-Seite.
   Einbinden: quiz.css im <head>, quiz.js vor </body>. Sonst nichts.
   Ein Check = EIN Block im HTML:

     <div class="quiz">
     <script type="application/json">
     { "id":"ue0-tipp", "typ":"tipp", "frage":"...", "optionen":["A","B"],
       "richtig":["A"], "hinweis":"...", "auflösen":"später" }
     </scr` + `ipt>
     </div>

   FELDER
     id         Pflicht, einmalig pro Seite. Schlüssel im Speicher, nie ändern.
     typ        "einfach" (eine Antwort) | "tipp" (mehrere) | "text" (freie Vorhersage)
     frage      Pflicht.
     hilfe      optional, kleine Zeile unter der Frage.
     optionen   bei einfach und tipp Pflicht.
     richtig    ANTWORTTEXT, nicht Position. Bei "einfach" ein String, bei "tipp" eine Liste.
                Entfällt bei "text".
     hinweis    was nach der Auflösung erscheint. Bei "text" die richtige Antwort.
     auflösen  "sofort" | "später" (Vorgabe) | "nie"
     mischen    true = Reihenfolge der Optionen zufällig. Der Schlüssel bleibt gültig,
                weil gegen den Text geprüft wird.
     etikett    Überschrift im Kästchen, Vorgabe "Kurzcheck".

   ABSCHLUSS (optional, einmal pro Seite):
     <div class="quiz-abschluss"></div>
   ========================================================================== */
(function () {
  "use strict";

  var SEITE = (document.body && document.body.dataset.quizSeite) || location.pathname;
  var KEY = "quiz:" + SEITE;
  var reg = [];          // alle Checks der Seite
  var neuzeichner = [];  // Neuzeichner der Abschlussblöcke
  var stand = laden();   // { id: {antwort, offen} }

  function laden() {
    try { return JSON.parse(localStorage.getItem(KEY)) || {}; }
    catch (e) { console.warn("[quiz] Speicher nicht lesbar:", e); return {}; }
  }
  function sichern() {
    try { localStorage.setItem(KEY, JSON.stringify(stand)); }
    catch (e) { console.warn("[quiz] Speicher nicht schreibbar, Antworten gehen beim Schließen verloren:", e); }
    neuzeichner.forEach(function (f) { f(); });
  }
  function el(t, k, txt) {
    var n = document.createElement(t);
    if (k) n.className = k;
    if (txt != null) n.textContent = txt;
    return n;
  }
  // Ein Bild, das niemals kaputt aussieht: fehlt die Datei oder ist der Pfad leer,
  // steht ein sichtbarer Platzhalter da, kein zerbrochenes Symbol.
  function bild(pfad, alt, marke, klasse) {
    var rahmen = el("figure", "quiz-bild" + (klasse ? " " + klasse : ""));
    function platzhalter(grund) {
      rahmen.innerHTML = "";
      var ph = el("div", "quiz-bild-platzhalter");
      ph.appendChild(el("span", "quiz-bild-marke", "Bild"));
      ph.appendChild(el("span", null, marke || alt || "noch kein Bild"));
      if (grund) ph.appendChild(el("span", "quiz-bild-grund", grund));
      rahmen.appendChild(ph);
      return rahmen;
    }
    if (!pfad) return platzhalter(null);
    var i = el("img");
    i.alt = alt || "";
    i.onerror = function () { platzhalter("nicht gefunden: " + pfad); };
    i.src = pfad;                       // src zuletzt, damit onerror sicher hängt
    rahmen.appendChild(i);
    return rahmen;
  }

  function unterschrift(rahmen, text) {
    if (text) rahmen.appendChild(el("figcaption", "quiz-unterschrift", text));
    return rahmen;
  }

  function fehler(wo, text) {
    wo.innerHTML = "";
    wo.appendChild(el("div", "quiz-fehler", "Quiz-Block kaputt:\n" + text));
    console.error("[quiz]", text);
  }
  function mischen(a) {
    a = a.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  /* ---------------------------------------------------- ein Check zeichnen */
  function bauen(wo, c) {
    var s = stand[c.id] || (stand[c.id] = { antwort: c.typ === "tipp" ? [] : null, offen: false });
    if (s.versuche == null) s.versuche = 0;
    if (s.geschafft == null) s.geschafft = false;
    var reihenfolge = c._reihenfolge;
    c._wo = wo;

    // Alles oder nichts. Halb richtig ist nicht richtig, dafür sind Versuche frei.
    function korrekt() {
      if (c.typ === "text" || c.auflösen === "nie") return null;
      if (c.typ === "tipp") {
        if (s.antwort.length !== c.richtig.length) return false;
        return c.richtig.every(function (r) { return s.antwort.indexOf(r) >= 0; });
      }
      return s.antwort === c.richtig;
    }

    function beantwortet() {
      if (c.typ === "tipp")  return s.antwort.length > 0;
      if (c.typ === "text")  return !!(s.antwort && String(s.antwort).trim());
      return s.antwort !== null;
    }
    function aufgelöst() {
      if (c.auflösen === "nie") return false;
      if (c.auflösen === "sofort") return beantwortet();
      return !!s.offen;
    }

    function zeichnen() {
      wo.innerHTML = "";
      wo.appendChild(el("span", "quiz-pill", c.etikett || "Kurzcheck"));
      var zeile = el("p", "quiz-frage", c.frage);
      if (c.pflicht) zeile.appendChild(el("span", "quiz-pflicht", " *"));
      wo.appendChild(zeile);
      if (c.hilfe) wo.appendChild(el("p", "quiz-hilfe", c.hilfe));
      if ("bild" in c) wo.appendChild(unterschrift(bild(c.bild, c.bildAlt, c.id), c.bildUnterschrift));
      var offen = aufgelöst();
      if (offen && !s.gewertet) {          // genau einmal pro Versuch zählen
        s.gewertet = true;
        s.versuche += 1;
        if (korrekt()) s.geschafft = true;
        sichern();
      }

      if (c.typ === "text") {
        if (offen) {
          var eig = el("div", "quiz-eigen", "Ihre Vorhersage: " + s.antwort);
          wo.appendChild(eig);
        } else {
          var ta = el("textarea");
          ta.value = s.antwort || "";
          ta.oninput = function () {
            s.antwort = ta.value; sichern();
            var k = wo.querySelector(".quiz-btn");      // nicht neu zeichnen, sonst springt der Fokus
            if (k) k.disabled = !beantwortet();
          };
          wo.appendChild(ta);
        }
      } else {
        var mitBild = reihenfolge.some(function (o) { return "bild" in o; });
        var liste = mitBild ? el("div", "quiz-optionen raster") : wo;
        reihenfolge.forEach(function (o) {
          var txt = o.text;
          var b = el("button", "quiz-opt" + ("bild" in o ? " mit-bild" : ""));
          if ("bild" in o) b.appendChild(bild(o.bild, o.bildAlt || txt, txt));
          b.appendChild(el("span", "quiz-opt-text", txt));
          var markiert = c.typ === "tipp" ? s.antwort.indexOf(txt) >= 0 : s.antwort === txt;
          var richtig  = c.typ === "tipp" ? c.richtig.indexOf(txt) >= 0 : c.richtig === txt;
          if (offen) {
            b.disabled = true;
            if (o._wn) { if (markiert) b.classList.add("unsicher"); }
            else if (markiert && richtig) b.classList.add("richtig");
            else if (markiert && !richtig) b.classList.add("falsch");
            else if (!markiert && richtig) b.classList.add(c.typ === "tipp" ? "verpasst" : "richtig");
          } else if (markiert) {
            b.classList.add("markiert");
          }
          b.onclick = function () {
            if (offen) return;
            if (c.typ === "tipp") {
              if (o._wn) {
                s.antwort = s.antwort.indexOf(txt) >= 0 ? [] : [txt];   // schließt alles andere aus
              } else {
                var wn = c.weissNicht ? s.antwort.indexOf(c.weissNichtText) : -1;
                if (wn >= 0) s.antwort.splice(wn, 1);
                var k = s.antwort.indexOf(txt);
                if (k >= 0) s.antwort.splice(k, 1); else s.antwort.push(txt);
              }
            } else {
              s.antwort = txt;
            }
            sichern(); zeichnen();
          };
          liste.appendChild(b);
        });
        if (mitBild) wo.appendChild(liste);
      }

      if (offen) {
        if ("hinweisBild" in c) wo.appendChild(unterschrift(bild(c.hinweisBild, c.hinweisBildAlt, c.id + " \u00b7 Auflösung"), c.hinweisBildUnterschrift));
        if (c.hinweis) wo.appendChild(el("p", "quiz-hinweis", c.hinweis));

        if (c.punkte > 0) {
          wo.appendChild(el("p", s.geschafft ? "quiz-punkte" : "quiz-punkte offen",
            s.geschafft
              ? "+" + c.punkte + (c.punkte === 1 ? " Punkt" : " Punkte")
                + (s.versuche > 1 ? ", im " + s.versuche + ". Versuch" : "")
              : "Noch keine Punkte. Ein weiterer Versuch kostet nichts."));
        }
        if (!s.geschafft && c.nochmal !== false && c.typ !== "text" && korrekt() === false) {
          var nb = el("button", "quiz-btn leer", "Nochmal versuchen");
          nb.onclick = function () {
            s.antwort = c.typ === "tipp" ? [] : null;
            s.offen = false; s.gewertet = false;
            sichern(); zeichnen();
          };
          wo.appendChild(nb);
        }
      } else if (c.auflösen !== "nie") {
        // Bei Auswahlfragen erscheint der Knopf erst mit einer Antwort, beim Textfeld steht er
        // von Anfang an da und ist gesperrt, sonst taucht er während des Tippens neu auf.
        if (c.typ === "text" || beantwortet()) {
          var ab = el("button", "quiz-btn leer", c.knopf || "Auflösung zeigen");
          ab.disabled = !beantwortet();
          ab.onclick = function () { if (!beantwortet()) return; s.offen = true; sichern(); zeichnen(); };
          wo.appendChild(ab);
        }
      }
    }
    zeichnen();
  }

  /* ------------------------------------------------------------ einlesen */
  function prüfen(c) {
    if (!c.id) return "Feld \"id\" fehlt.";
    if (!c.frage) return "Feld \"frage\" fehlt bei id \"" + c.id + "\".";
    c.typ = c.typ || "einfach";
    // Alte Schreibweise ohne Umlaut wird still angenommen, damit ein Tippfehler
    // nicht heimlich auf die Vorgabe zurückfällt.
    if (c.aufloesen && !c.auflösen) c.auflösen = c.aufloesen;
    c.auflösen = c.auflösen || "später";
    if (c.auflösen === "spaeter") c.auflösen = "später";
    if (["sofort", "später", "nie"].indexOf(c.auflösen) < 0)
      return "\"auflösen\" kennt nur \"sofort\", \"später\" und \"nie\". Hier steht: " + c.auflösen;
    // Punkte gibt es nur, wo es etwas zu wissen gibt. Reine Vorhersagen: "punkte": 0 setzen.
    if (c.punkte == null) c.punkte = (c.typ === "text" || c.auflösen === "nie") ? 0 : 1;
    if (typeof c.punkte !== "number" || c.punkte < 0) return "\"punkte\" muss eine Zahl ab 0 sein.";
    if (["einfach", "tipp", "text"].indexOf(c.typ) < 0) return "typ \"" + c.typ + "\" gibt es nicht.";
    // Alle Fragen sind Pflicht, wie bei Google Forms. "pflicht": false nimmt eine heraus.
    c.pflicht = c.pflicht !== false;
    if (c.typ === "text") { c.weissNicht = false; return null; }
    // Ein ehrlicher Ausweg gehört dazu, sonst erzeugt die Pflicht Zufallsklicks.
    c.weissNicht = c.weissNicht !== false;
    c.weissNichtText = c.weissNichtText || "Ich weiß nicht";
    if (!Array.isArray(c.optionen) || c.optionen.length < 2) return "\"optionen\" fehlt oder hat weniger als 2 Einträge.";
    // Eine Option ist entweder ein Text oder { "text": "...", "bild": "...", "bildAlt": "..." }
    var kaputt = null;
    c._opt = c.optionen.map(function (o, i) {
      if (typeof o === "string") return { text: o };
      if (o && typeof o.text === "string" && o.text) return o;
      kaputt = "Option " + (i + 1) + " ist weder ein Text noch ein Objekt mit \"text\".";
      return { text: "" };
    });
    if (kaputt) return kaputt;
    c.optionen = c._opt.map(function (o) { return o.text; });
    var doppelt = c.optionen.filter(function (t, i) { return c.optionen.indexOf(t) !== i; });
    if (doppelt.length) return "Zwei Optionen haben denselben Text:\n  " + doppelt.join("\n  ")
      + "\nDer Schlüssel geht über den Text, deshalb muss jeder Text einmalig sein.";
    if (c.weissNicht && c.optionen.indexOf(c.weissNichtText) >= 0)
      return "\"" + c.weissNichtText + "\" steht schon in den Optionen und wird zusätzlich automatisch"
        + " angehängt.\nEntweder die Option streichen oder \"weissNicht\": false setzen.";
    if (c.auflösen === "nie") { c.richtig = c.typ === "tipp" ? [] : null; return null; }
    if (c.typ === "tipp") {
      if (!Array.isArray(c.richtig) || !c.richtig.length) return "\"richtig\" muss eine Liste von Antworttexten sein.";
    } else {
      if (typeof c.richtig !== "string") return "\"richtig\" muss der Antworttext sein, nicht eine Zahl.";
      c.richtig = [c.richtig];
    }
    var fremd = c.richtig.filter(function (r) { return c.optionen.indexOf(r) < 0; });
    if (fremd.length) return "In \"richtig\" steht Text, der in \"optionen\" nicht vorkommt:\n  " + fremd.join("\n  ")
      + "\nDer Schlüssel wird gegen den TEXT geprüft, nicht gegen die Position. Tippfehler zählen.";
    if (c.typ !== "tipp") c.richtig = c.richtig[0];
    return null;
  }

  function starten() {
    var gesehen = {};
    [].forEach.call(document.querySelectorAll(".quiz"), function (wo) {
      var roh = wo.querySelector('script[type="application/json"]');
      if (!roh) { fehler(wo, "Kein <script type=\"application/json\"> im Block."); return; }
      var c;
      try { c = JSON.parse(roh.textContent); }
      catch (e) { fehler(wo, "JSON ist ungültig.\n" + e.message + "\n\nHäufigste Ursache: ein \" mitten im deutschen Text. Als \\\" schreiben."); return; }
      var m = prüfen(c);
      if (m) { fehler(wo, m); return; }
      if (gesehen[c.id]) { fehler(wo, "Die id \"" + c.id + "\" kommt auf dieser Seite zweimal vor."); return; }
      gesehen[c.id] = true;
      c._reihenfolge = (c.mischen && c.typ !== "text") ? mischen(c._opt || []) : (c._opt || []);
      // "Ich weiß nicht" steht immer unten und wird nie mitgemischt.
      if (c.typ !== "text" && c.weissNicht)
        c._reihenfolge = c._reihenfolge.concat([{ text: c.weissNichtText, _wn: true }]);
      reg.push(c);
      bauen(wo, c);
    });
    [].forEach.call(document.querySelectorAll(".quiz-abschluss"), abschluss);
    [].forEach.call(document.querySelectorAll(".quiz-punktestand"), punkteAnzeige);
    sichern();
  }

  /* ------------------------------------------------------ Pflichtfragen */
  function offeneFragen() {
    return reg.filter(function (c) {
      if (!c.pflicht) return false;
      var s = stand[c.id];
      if (!s) return true;
      if (c.typ === "tipp") return !(s.antwort && s.antwort.length);
      if (c.typ === "text") return !(s.antwort && String(s.antwort).trim());
      return s.antwort === null || s.antwort === undefined;
    });
  }

  /* ---------------------------------------------------------- Punktestand */
  function punktestand() {
    var e = 0, m = 0, v = 0;
    reg.forEach(function (c) {
      if (!c.punkte) return;
      m += c.punkte;
      var s = stand[c.id] || {};
      if (s.geschafft) e += c.punkte;
      v += s.versuche || 0;
    });
    return { erreicht: e, maximum: m, versuche: v };
  }

  function punkteAnzeige(wo) {
    function zeichnen() {
      var p = punktestand();
      wo.textContent = p.erreicht + " von " + p.maximum + " Punkten";
    }
    zeichnen();
    neuzeichner.push(zeichnen);
  }

  /* ----------------------------------------------------------- Abschluss */
  function bewertung(c) {
    var s = stand[c.id]; if (!s) return null;
    if (c.typ === "text" || c.auflösen === "nie") return null;
    if (c.typ === "tipp") {
      var tr = s.antwort.filter(function (x) { return c.richtig.indexOf(x) >= 0; }).length;
      var daneben = s.antwort.length - tr;
      return { ok: tr === c.richtig.length && daneben === 0,
               text: tr + " von " + c.richtig.length + (daneben ? ", " + daneben + " daneben" : "") };
    }
    return { ok: s.antwort === c.richtig, text: s.antwort === c.richtig ? "richtig" : "daneben" };
  }

  function abschluss(wo) {
    function zeichnen() {
      wo.innerHTML = "";
      wo.appendChild(el("span", "quiz-pill", "Ihr Stand"));
      var t = el("table"), n = 0, g = 0;
      reg.forEach(function (c) {
        var b = bewertung(c), s = stand[c.id];
        var tr = document.createElement("tr");
        var beantwortet = s && (Array.isArray(s.antwort) ? s.antwort.length : s.antwort !== null && s.antwort !== "");
        var zeichen = !beantwortet ? "·" : (b ? (b.ok ? "✓" : "✗") : "•");
        tr.appendChild(el("td", null, zeichen));
        tr.appendChild(el("td", null, c.frage));
        tr.appendChild(el("td", null, b && beantwortet ? b.text : (beantwortet ? "notiert" : "offen")));
        t.appendChild(tr);
        if (b) { n++; if (b.ok) g++; }
      });
      wo.appendChild(t);
      var pp = punktestand();
      wo.appendChild(el("p", "quiz-bilanz",
        g + " von " + n + " bewertbaren Checks sitzen."
        + (pp.maximum ? "  " + pp.erreicht + " von " + pp.maximum + " Punkten in " + pp.versuche + " Versuchen." : "")));

      var kopieren = el("button", "quiz-btn leer", "Antworten kopieren");
      kopieren.onclick = function () {
        navigator.clipboard.writeText(JSON.stringify(Quiz.paket(), null, 2))
          .then(function () { st.textContent = "In der Zwischenablage."; })
          .catch(function () { st.textContent = "Kopieren hat nicht geklappt, Konsole: Quiz.paket()"; });
      };
      wo.appendChild(kopieren);

      var offene = offeneFragen();

      var senden = el("button", "quiz-btn", offene.length
        ? "Noch " + offene.length + (offene.length === 1 ? " Pflichtfrage offen" : " Pflichtfragen offen")
        : "An den Trainer schicken");
      senden.disabled = offene.length > 0;
      senden.onclick = function () {
        senden.disabled = true;
        Quiz.senden().then(function (r) { st.textContent = r; senden.disabled = false; });
      };
      wo.appendChild(senden);

      if (offene.length) {
        var hin = el("button", "quiz-btn leer", "Zur ersten offenen Frage");
        hin.onclick = function () { Quiz.zeigeOffene(); };
        wo.appendChild(hin);
      }

      var st = el("p", "quiz-status", offene.length
        ? "Alle Fragen sind Pflicht. Wenn Sie etwas nicht wissen, ist \u201eIch weiß nicht\u201c eine gültige Antwort."
        : "Noch nichts gesendet. Alles liegt nur in diesem Browser.");
      wo.appendChild(st);
    }
    zeichnen();
    neuzeichner.push(zeichnen);
  }

  /* --------------------------------------------- der einzige Weg nach draussen */
  var Quiz = {
    ZIEL: "lokal",     // "lokal" | "endpoint"
    ENDPOINT: "",
    stand: function () { return stand; },
    offen: function () { return offeneFragen().map(function (c) { return { id: c.id, frage: c.frage }; }); },
    zeigeOffene: function () {
      var off = offeneFragen();
      if (!off.length || !off[0]._wo) return false;
      var wo = off[0]._wo;
      wo.scrollIntoView({ behavior: "smooth", block: "center" });
      wo.classList.add("fehlt");
      setTimeout(function () { wo.classList.remove("fehlt"); }, 2500);
      return true;
    },
    paket: function () {
      return {
        seite: SEITE,
        person: (stand.__id || (stand.__id = "tn-" + Math.random().toString(36).slice(2, 8))),
        zeit: new Date().toISOString(),
        punkte: punktestand(),
        antworten: reg.map(function (c) {
          var b = bewertung(c);
          var s = stand[c.id] || {};
          return { id: c.id, typ: c.typ, antwort: s.antwort, richtig: b ? b.ok : null,
                   punkte: s.geschafft ? c.punkte : 0, versuche: s.versuche || 0 };
        })
      };
    },
    senden: function () {
      var off = offeneFragen();
      if (off.length) {
        Quiz.zeigeOffene();
        return Promise.resolve("Nicht gesendet: " + off.length + " Pflichtfrage"
          + (off.length === 1 ? "" : "n") + " noch offen.");
      }
      var p = Quiz.paket();
      sichern();
      if (Quiz.ZIEL !== "endpoint" || !Quiz.ENDPOINT) {
        return Promise.resolve("Nichts gesendet. ZIEL steht auf \"lokal\".");
      }
      return fetch(Quiz.ENDPOINT, {
        method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(p)
      }).then(function (r) {
        return r.ok ? "Übermittelt." : "Übermittlung fehlgeschlagen (" + r.status + "). Die Antworten bleiben lokal gespeichert.";
      }).catch(function () {
        return "Kein Netz. Die Antworten bleiben lokal gespeichert, später nochmal schicken.";
      });
    },
    zurücksetzen: function () {
      stand = {};
      try { localStorage.removeItem(KEY); } catch (e) {}
      location.reload();
    }
  };
  window.Quiz = Quiz;

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", starten);
  else starten();
})();
