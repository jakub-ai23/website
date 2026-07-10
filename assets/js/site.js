/* jakubpopluhar.com · site-weite Skripte
   Zentral, damit JEDE Seite die dieses File laedt automatisch getrackt wird
   (Hauptseiten + alle Blog-Artikel, aktuell und kuenftig).
   Vorher: Beacon inline pro Seite verstreut, Blog-Artikel komplett vergessen. */

/* ===== Schicht 1: Analytics-Beacon (cookieless, IP wird serverseitig gehasht) =====
   Braucht KEIN Consent (cookielose Reichweitenmessung, berechtigtes Interesse). */
(function () {
  try {
    var h = location.hostname;
    if (h === 'localhost' || h === '127.0.0.1' || location.protocol === 'file:') return; // lokale Previews nicht tracken
    var i = new Image(1, 1);
    i.src = 'https://deflifeos.popluhar.at/t.gif?site=jakubpopluhar&path=' +
      encodeURIComponent(location.pathname + location.search) +
      '&ref=' + encodeURIComponent(document.referrer);
  } catch (e) {}
})();

/* ===== Schicht 2: Microsoft Clarity (Heatmaps/Recordings) — NUR nach Opt-in =====
   Clarity setzt Cookies + zeichnet Verhalten auf -> DSGVO-Einwilligung noetig.
   Laedt ausschliesslich, wenn der Besucher im Consent-Banner zugestimmt hat. */
var JP_CLARITY_ID = 'xk7y1dwu8h';
var JP_CONSENT_KEY = 'jp_consent_stats';

function jpLoadClarity() {
  try {
    if (!JP_CLARITY_ID || window.__jpClarityLoaded) return;
    window.__jpClarityLoaded = true;
    (function (c, l, a, r, i, t, y) {
      c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
      t = l.createElement(r); t.async = 1;
      t.src = 'https://www.clarity.ms/tag/' + i;
      y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
    })(window, document, 'clarity', 'script', JP_CLARITY_ID);
  } catch (e) {}
}

/* ===== Consent-Banner (DE/EN, Zustimmen gleichwertig zu Ablehnen, kein Dark-Pattern) ===== */
(function () {
  try {
    var isLocal = location.hostname === 'localhost' || location.hostname === '127.0.0.1';
    var EN = (document.documentElement.lang || '').toLowerCase().indexOf('en') === 0
             || location.pathname.indexOf('/en/') === 0;
    var T = EN ? {
      msg: 'We use optional analytics (Microsoft Clarity) to understand how this site is used. Only with your consent.',
      ok: 'Accept', no: 'Decline', more: 'Privacy', moreHref: '/datenschutz.html'
    } : {
      msg: 'Wir nutzen optionale Analyse-Werkzeuge (Microsoft Clarity), um zu verstehen, wie die Seite genutzt wird. Nur mit Ihrer Zustimmung.',
      ok: 'Zustimmen', no: 'Ablehnen', more: 'Datenschutz', moreHref: '/datenschutz.html'
    };

    function set(v) { try { localStorage.setItem(JP_CONSENT_KEY, v); } catch (e) {} }
    function get() { try { return localStorage.getItem(JP_CONSENT_KEY); } catch (e) { return null; } }

    function removeBanner() { var b = document.getElementById('jp-consent'); if (b) b.remove(); }

    function showBanner() {
      if (document.getElementById('jp-consent')) return;
      var css = document.createElement('style');
      css.textContent =
        '#jp-consent{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);z-index:9999;' +
        'max-width:640px;width:calc(100% - 32px);background:#161616;color:#eee;border:1px solid #333;' +
        'border-radius:12px;padding:16px 18px;box-shadow:0 8px 30px rgba(0,0,0,.5);' +
        'font:14px/1.5 Inter,system-ui,sans-serif;display:flex;flex-wrap:wrap;gap:12px;align-items:center}' +
        '#jp-consent p{margin:0;flex:1 1 260px}' +
        '#jp-consent a{color:#d4a017;text-decoration:underline}' +
        '#jp-consent .jp-btns{display:flex;gap:8px;flex:0 0 auto}' +
        '#jp-consent button{cursor:pointer;border-radius:8px;padding:8px 16px;font:inherit;font-weight:600;border:1px solid #444}' +
        '#jp-consent .jp-no{background:transparent;color:#ccc}' +
        '#jp-consent .jp-ok{background:#d4a017;color:#111;border-color:#d4a017}' +
        '@media(max-width:520px){#jp-consent .jp-btns{flex:1 1 100%}#jp-consent button{flex:1}}';
      document.head.appendChild(css);
      var d = document.createElement('div');
      d.id = 'jp-consent';
      d.setAttribute('role', 'dialog');
      d.setAttribute('aria-label', T.more);
      d.innerHTML =
        '<p>' + T.msg + ' <a href="' + T.moreHref + '">' + T.more + '</a></p>' +
        '<div class="jp-btns">' +
        '<button class="jp-no" type="button">' + T.no + '</button>' +
        '<button class="jp-ok" type="button">' + T.ok + '</button></div>';
      d.querySelector('.jp-ok').addEventListener('click', function () { set('yes'); removeBanner(); jpLoadClarity(); });
      d.querySelector('.jp-no').addEventListener('click', function () { set('no'); removeBanner(); });
      document.body.appendChild(d);
    }

    // Widerruf/Aenderung: window.jpCookieSettings() ODER Klick auf Link mit href="#cookie-settings"
    window.jpCookieSettings = function () { showBanner(); };
    document.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('a[href="#cookie-settings"],[data-cookie-settings]');
      if (a) { e.preventDefault(); showBanner(); }
    });

    function init() {
      if (location.search.indexOf('consent=preview') !== -1) { showBanner(); return; } // Vorschau-Schalter
      var c = get();
      if (c === 'yes') { jpLoadClarity(); return; }     // frueheres Opt-in -> Clarity laden
      if (c === 'no') return;                            // frueheres Opt-out -> nichts
      if (isLocal) return;                               // lokal keinen Banner spammen
      showBanner();                                      // noch keine Entscheidung -> fragen
    }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
    else init();
  } catch (e) {}
})();

/* ===== Schicht 3: Conversion-Events (Clarity Custom Events) =====
   Feuert nur, wenn Clarity geladen ist (= Besucher hat zugestimmt). Ohne Consent no-op.
   Taxonomie ist gelockt -> siehe cta-erd. Reine Klick-/Submit-Delegation, kein Per-Seite-Edit. */
(function () {
  function jpTrack(name) {
    try { if (window.clarity) window.clarity('event', name); } catch (e) {}
  }
  try {
    // 1) Formspree-Absenden = Haupt-Conversion. submit-Event feuert auch bei fetch/preventDefault.
    document.addEventListener('submit', function (e) {
      var f = e.target;
      if (!f || f.tagName !== 'FORM') return;
      var action = (f.getAttribute('action') || '') + (f.action || '');
      if (action.indexOf('formspree.io') === -1) return;
      jpTrack('jp_form_submit');
      // Interesse-Checkboxen (Lead-Qualitaet) mitlesen
      try {
        f.querySelectorAll('input[type=checkbox]:checked').forEach(function (cb) {
          var v = ((cb.value || '') + ' ' + (cb.name || '')).toLowerCase();
          if (/erstgespr/.test(v)) jpTrack('jp_form_interest_erstgespraech');
          if (/1:1|coaching|executive/.test(v)) jpTrack('jp_form_interest_1on1');
          if (/ressourc|ki-stack|newsletter/.test(v)) jpTrack('jp_form_interest_ressourcen');
        });
      } catch (e2) {}
    }, true);

    // 2) Ausgehende Money-/Kontakt-Klicks -> je nach Ziel gelocktes Event
    document.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('a[href]');
      if (!a) return;
      var href = (a.getAttribute('href') || '').toLowerCase();
      if (href.indexOf('cal.eu/hilldigital') !== -1) jpTrack('jp_booking_caleu');
      else if (href.indexOf('calendly.com/jakub') !== -1) jpTrack('jp_booking_calendly');
      else if (href.indexOf('ars.at/seminar') !== -1) jpTrack('jp_register_ars');
      else if (href.indexOf('tectrain') !== -1) jpTrack('jp_register_tectrain');
      else if (href.indexOf('hill-digital.at/firmen-buchung') !== -1) jpTrack('jp_register_hd_firmen');
      else if (href.indexOf('mailto:jakub@popluhar.at') !== -1) jpTrack('jp_contact_mail');
      else if (href.indexOf('tel:') === 0) jpTrack('jp_contact_phone');
      else if (href.indexOf('linkedin.com') !== -1) jpTrack('jp_social_linkedin');
      // weiche "Session buchen" (scrollt zum Formular) = Intent, nicht Buchung
      else if (href.indexOf('#contact') !== -1 || /session buchen|book a session/i.test(a.textContent || '')) jpTrack('jp_cta_session_soft');
    }, true);
  } catch (e) {}
})();
