/* jakubpopluhar.com · site-weite Skripte
   Zentral, damit JEDE Seite die dieses File laedt automatisch getrackt wird
   (Hauptseiten + alle Blog-Artikel, aktuell und kuenftig).
   Vorher: Beacon inline pro Seite verstreut, Blog-Artikel komplett vergessen. */

/* ===== Schicht 1: Analytics-Beacon (cookieless, IP wird serverseitig gehasht) ===== */
(function () {
  try {
    // Lokale Previews (127.0.0.1 / localhost / file://) nicht tracken -> kein Datenmuell.
    var h = location.hostname;
    if (h === 'localhost' || h === '127.0.0.1' || location.protocol === 'file:') return;
    var i = new Image(1, 1);
    i.src = 'https://deflifeos.popluhar.at/t.gif?site=jakubpopluhar&path=' +
      encodeURIComponent(location.pathname + location.search) +
      '&ref=' + encodeURIComponent(document.referrer);
  } catch (e) {}
})();

/* ===== Schicht 2: Microsoft Clarity (Heatmaps/Recordings) =====
   NOCH NICHT SCHARF. Clarity setzt Cookies + zeichnet Verhalten auf -> braucht
   Consent-Banner + Datenschutz-Passus (siehe infrastructure/analytics-clarity/).
   Wird erst geladen, wenn (a) Project-ID gesetzt und (b) Besucher zugestimmt hat.
   Aktivierung: CLARITY_ID unten setzen + Consent-Gate scharf schalten. */
var CLARITY_ID = ''; // <- Clarity Project-ID hier eintragen, wenn Consent steht
(function () {
  try {
    if (!CLARITY_ID) return;                                   // nicht konfiguriert -> nichts laden
    if (localStorage.getItem('jp_consent_stats') !== 'yes') return; // kein Opt-in -> nichts laden
    (function (c, l, a, r, i, t, y) {
      c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
      t = l.createElement(r); t.async = 1;
      t.src = 'https://www.clarity.ms/tag/' + i;
      y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
    })(window, document, 'clarity', 'script', CLARITY_ID);
  } catch (e) {}
})();
