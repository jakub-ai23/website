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
    i.src = 'https://stats.jakubpopluhar.com/px?site=jakubpopluhar&path=' +
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
    var LANG = (document.documentElement.lang || '').toLowerCase();
    var EN = LANG.indexOf('en') === 0 || location.pathname.indexOf('/en/') === 0;
    var SK = LANG.indexOf('sk') === 0 || location.pathname.indexOf('/sk/') === 0;
    var T = SK ? {
      msg: 'Používame voliteľné analytické nástroje (Microsoft Clarity), aby sme rozumeli, ako sa stránka používa. Len s Vaším súhlasom.',
      ok: 'Súhlasím', no: 'Odmietnuť', more: 'Ochrana osobných údajov', moreHref: '/datenschutz.html'
    } : EN ? {
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

/* ===== Schicht 4: KI-Check-Popup, site-weit =====
   Eckkarte nach 20 Sekunden, einmal pro Besucher (30 Tage Ruhe), oeffnet den
   Check in einem neuen Tab. Zwei Ruecksichten:
   1. Nicht auf Seiten, wo der Besucher schon in einer Aufgabe steckt (der Check
      selbst, E-Learning- und Kursunterlagen, passwortgeschuetzte Angebotsseiten).
   2. Nicht solange der Consent-Hinweis noch steht, sonst stapeln sich zwei
      Kaesten uebereinander. Erst wenn der Besucher dort entschieden hat.
   Test-Schalter: ?kicheck=now zeigt es sofort. */
(function () {
  try {
    var path = location.pathname;
    if (/(ki-check|weiter|community|ars[0-9]|hw[0-9]|sportunion|viennaup|techtrain|pmi|ewi|bfi-|-onepager|training\/)/i.test(path)) return;

    var en = (document.documentElement.lang || 'de').toLowerCase().indexOf('en') === 0;
    var T = en
      ? { eb: 'Free &middot; 2 minutes', h: 'How fit are you really with AI?',
          p: '12 questions, every one with the answer. You learn something either way.',
          go: 'Start the check', later: 'Later, thanks', close: 'Close', url: '/en/ki-check/' }
      : { eb: 'Kostenlos &middot; 2 Minuten', h: 'Wie fit sind Sie wirklich mit KI?',
          p: '12 Fragen, jede mit Auflösung. Sie lernen so oder so etwas.',
          go: 'Check starten', later: 'Später, danke', close: 'Schließen', url: '/ki-check/' };

    var force = /[?&]kicheck=now/.test(location.search);
    var KEY = 'jp_kicheck_seen';
    var seen = 0;
    try { seen = +localStorage.getItem(KEY) || 0; } catch (e) {}
    if (!force && seen && (Date.now() - seen) < 30 * 864e5) return;
    function markSeen() { try { localStorage.setItem(KEY, Date.now()); } catch (e) {} }

    function build() {
      var css =
        '.jp-kcp{position:fixed;right:22px;bottom:22px;width:330px;max-width:calc(100vw - 32px);' +
        'background:#141414;border:1px solid rgba(212,160,23,0.35);border-top:3px solid #d4a017;border-radius:12px;' +
        'box-shadow:0 18px 50px rgba(0,0,0,.55);padding:18px 20px 16px;z-index:9998;' +
        'transform:translateY(24px);opacity:0;pointer-events:none;transition:transform .35s ease,opacity .35s ease;' +
        'font-family:Inter,Arial,sans-serif;color:#f2f0eb}' +
        '.jp-kcp.show{transform:translateY(0);opacity:1;pointer-events:auto}' +
        '.jp-kcp-x{position:absolute;top:6px;right:9px;background:none;border:none;font-size:1.3rem;line-height:1;color:#9a978e;cursor:pointer;padding:4px}' +
        '.jp-kcp-x:hover{color:#fff}' +
        '.jp-kcp .eb{color:#d4a017;text-transform:uppercase;letter-spacing:.12em;font-size:.66rem;font-weight:700;font-family:Montserrat,Arial,sans-serif}' +
        '.jp-kcp h3{font-family:Montserrat,Arial,sans-serif;font-size:1.12rem;font-weight:700;margin:5px 0 6px;line-height:1.2;color:#f2f0eb}' +
        '.jp-kcp p{color:#9a978e;font-size:.88rem;margin:0 0 13px;line-height:1.45}' +
        '.jp-kcp-btn{display:inline-block;background:#d4a017;color:#141414;font-family:Montserrat,Arial,sans-serif;font-weight:600;' +
        'font-size:.9rem;text-decoration:none;padding:9px 17px;border-radius:999px}' +
        '.jp-kcp-btn:hover{background:#e8b84a}' +
        '.jp-kcp-later{display:block;margin-top:9px;background:none;border:none;color:#9a978e;font-size:.8rem;' +
        'text-decoration:underline;cursor:pointer;font-family:inherit;padding:2px}' +
        '.jp-kcp-later:hover{color:#fff}' +
        '@media(max-width:480px){.jp-kcp{right:12px;left:12px;bottom:12px;width:auto}}';
      var style = document.createElement('style'); style.textContent = css; document.head.appendChild(style);
      var box = document.createElement('div');
      box.className = 'jp-kcp';
      box.setAttribute('role', 'dialog');
      box.setAttribute('aria-label', T.h);
      box.innerHTML =
        '<button class="jp-kcp-x" aria-label="' + T.close + '">&times;</button>' +
        '<div class="eb">' + T.eb + '</div>' +
        '<h3>' + T.h + '</h3>' +
        '<p>' + T.p + '</p>' +
        '<a class="jp-kcp-btn" href="' + T.url + '" target="_blank" rel="noopener">' + T.go + ' &rarr;</a>' +
        '<button class="jp-kcp-later">' + T.later + '</button>';
      document.body.appendChild(box);
      var close = function () { box.classList.remove('show'); markSeen(); };
      box.querySelector('.jp-kcp-x').addEventListener('click', close);
      box.querySelector('.jp-kcp-later').addEventListener('click', close);
      box.querySelector('.jp-kcp-btn').addEventListener('click', markSeen);
      requestAnimationFrame(function () { box.classList.add('show'); });
    }

    // Erst wenn der Consent-Hinweis weg ist. Hoechstens 60 s warten, dann aufgeben.
    // Die Wartezeit beginnt bewusst mit einer kurzen Gnadenfrist: sonst prueft der
    // Testschalter (?kicheck=now, 300 ms) BEVOR der Hinweis ueberhaupt gerendert ist,
    // sieht nichts und baut das Popup daneben. Gefunden beim Test am 2026-08-04.
    function whenFree(fn) {
      var waited = 0;
      function decided() {
        try { return !!localStorage.getItem(JP_CONSENT_KEY); } catch (e) { return false; }
      }
      setTimeout(function tick() {
        if (decided() || !document.getElementById('jp-consent')) return fn();
        if ((waited += 1000) > 60000) return;
        setTimeout(tick, 1000);
      }, 900);
    }
    setTimeout(function () { whenFree(build); }, force ? 300 : 20000);
  } catch (e) {}
})();

/* --- Abgelaufene Termine ausblenden (2026-08-21) ---------------------------
   Jede Terminzeile traegt data-date (Beginn) und bei mehrtaegigen Terminen
   zusaetzlich data-end. Ein Termin gilt bis zum Ende seines letzten Tages als
   aktuell und verschwindet erst danach.

   Das ist die Sofortwirkung im Browser: ohne sie stuende am 1. September noch
   der 31. August auf der Seite. Endgueltig aus dem HTML raeumt sie
   tools/sync-termine-vorschau.py --prune; erst dieser Lauf fuellt die
   Startseiten-Vorschau auch wieder auf fuenf Zeilen auf.

   Faellt JS aus, bleibt die Liste vollstaendig sichtbar. Das ist der
   gewuenschte Ausfall: lieber ein Termin zu viel als eine leere Seite. */
(function () {
  try {
    var rows = document.querySelectorAll('.ag[data-date]');
    if (!rows.length) return;
    var now = new Date();
    var today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    var gone = 0;
    for (var i = 0; i < rows.length; i++) {
      var r = rows[i];
      var last = r.getAttribute('data-end') || r.getAttribute('data-date');
      var p = last.split('-');
      if (p.length !== 3) continue;
      var end = new Date(+p[0], +p[1] - 1, +p[2]);
      if (end < today) { r.hidden = true; gone++; }
    }
    if (gone) {
      /* Die Trennlinie sitzt auf .ag + .ag. Ist die erste sichtbare Zeile nicht
         mehr die erste im DOM, traegt sie eine Linie ueber sich, die dort nicht
         hingehoert. */
      var first = document.querySelector('.ag[data-date]:not([hidden])');
      if (first) first.style.borderTop = 'none';
    }
  } catch (e) {}
})();
