#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Startseiten-Vorschau aus /termine/ erzeugen.

Die Terminliste unter /termine/ ist die Quelle. Die Vorschau auf der Startseite
wird daraus gebaut: die ersten N Zeilen, strikt in der Reihenfolge, in der sie
dort stehen. Keine Sonderregeln, keine Auswahl von Hand, damit kein Termin
uebersprungen wird.

  python3 tools/sync-termine-vorschau.py           # DE und EN, 5 Zeilen
  python3 tools/sync-termine-vorschau.py --count 8

Nach dem Lauf: /termine/ bleibt unberuehrt, nur index.html und en/index.html
werden neu geschrieben.
"""
import io, os, re, sys, argparse, shutil, datetime
import html as _html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Lange Kurstitel, die in der schmalen Vorschauzeile umbrechen wuerden.
SHORT = {
    "Lehrgang K&uuml;nstliche Intelligenz f&uuml;r den B&uuml;roalltag": "Lehrgang KI f&uuml;r den B&uuml;roalltag",
    "K&uuml;nstliche Intelligenz f&uuml;r den B&uuml;roalltag": "KI f&uuml;r den B&uuml;roalltag",
    "KI-Grundlagen &amp; praxisnahe Anwendungen mit ChatGPT": "KI-Grundlagen mit ChatGPT",
    "Konsumentenpsychologie im Zeitalter der K&uuml;nstlichen Intelligenz": "Konsumentenpsychologie und KI",
    "Claude datenschutzkonform im Arbeitsalltag nutzen": "Claude datenschutzkonform nutzen",
    "AI za pracovn&yacute;m stolom, modul 1: z&aacute;klad, ktor&yacute; vydr&#382;&iacute; aj zmenu n&aacute;stroja": "AI za pracovn&yacute;m stolom, modul 1",
    "AI za pracovn&yacute;m stolom, modul 2: od n&aacute;stroja k vlastn&eacute;mu asistentovi": "AI za pracovn&yacute;m stolom, modul 2",
    "AI v HR praxi: od inzer&aacute;tu po hodnotenie": "AI v HR praxi",
    "AI for the everyday office (programme)": "AI for the everyday office",
    "Programme: Artificial intelligence for the everyday office": "Programme: AI for the everyday office",
    "Artificial intelligence for the everyday office": "AI for the everyday office",
    "AI fundamentals and practical applications with ChatGPT": "AI fundamentals with ChatGPT",
    "Consumer psychology in the age of artificial intelligence": "Consumer psychology and AI",
    "Using Claude in a data-compliant way at work": "Using Claude in a data-compliant way",
}
# Kurze Zusatzhinweise wandern in die Vorschau, lange Beschreibungen nicht.
NOTE_MAX = 40

LINK = {"de": "Alle Termine ansehen", "en": "See all dates"}
LANG = "de"
TODAY = datetime.date.today().isoformat()

def parse(path):
    h = io.open(path, encoding="utf-8").read()
    rows = []
    for m in re.finditer(
        r'<div class="ag"(?: data-date="([\d-]+)")?(?: data-end="([\d-]+)")?>\n'
        r'\s*<div class="ag-date"><div class="ag-day[^"]*">([^<]+)</div>'
        r'<div class="ag-mon">([^<]+)</div>.*?</div>\n'
        r'\s*<div class="ag-body">\n\s*<div class="txt">\n'
        r'\s*<h2>(.*?)</h2>\n'
        r'\s*<p>(.*?)</p>\n'
        r'(?:\s*<span class="ag-note">(.*?)</span>\n)?'
        r'\s*</div>\n\s*</div>\n'
        r'\s*<div class="ag-prov"><img src="([^"]+)" alt="([^"]+)"[^>]*></div>\n'
        r'\s*<a href="([^"]+)" class="btn-training"[^>]*>([^<]*?)\s*&rarr;</a>', h, re.S):
        date, end, day, mon, title, meta, note, logo, alt, url, cta = m.groups()
        rows.append(dict(date=date or "", end=end or date or "",
                         day=day.strip(), mon=mon.strip(), title=title.strip(),
                         meta=meta.strip(), note=(note or "").strip(),
                         logo=logo, alt=alt, url=url, cta=cta.strip(),
                         raw=m.group(0)))
    return rows


def is_past(row, today):
    """Ein Termin ist erst nach dem Ende seines letzten Tages vorbei.
       Zeilen ohne data-date bleiben immer stehen: lieber einer zu viel
       als einer zu wenig weggeworfen."""
    return bool(row["end"]) and row["end"] < today


def prune(path, today):
    """Abgelaufene Zeilen endgueltig aus der Terminliste entfernen."""
    h = io.open(path, encoding="utf-8").read()
    dropped = []
    def rep(m):
        blk = m.group(0)
        d = re.search(r'<div class="ag"(?: data-date="([\d-]+)")?(?: data-end="([\d-]+)")?>', blk)
        if not d or not d.group(1):
            return blk
        last = d.group(2) or d.group(1)
        if last < today:
            t = re.search(r'<h2>(.*?)</h2>', blk, re.S)
            dropped.append("%s  %s" % (last, _html.unescape(re.sub(r'<[^>]+>', '', t.group(1))).strip()[:44] if t else ""))
            return ""
        return blk
    h2 = re.sub(r' {6}<div class="ag".*?\n {6}</div>\n\n?', rep, h, flags=re.S)
    if dropped:
        shutil.copy2(path, path + ".bak-prune")
        io.open(path, "w", encoding="utf-8").write(h2)
    return dropped

def render(rows, logo_prefix):
    out = []
    for r in rows:
        # Der Titel traegt die Sprachfahne als <span> davor. Fahne und Text
        # werden getrennt, damit die Kuerzungstabelle nur den Text vergleicht.
        # Titel stehen teils mit HTML-Entities, teils mit echten Umlauten.
        fm = re.match(r'\s*(<span class="ag-lang".*?</span>\s*)(.*)$', r["title"], re.S)
        flag, text = (fm.group(1), fm.group(2)) if fm else ("", r["title"])
        plain = _html.unescape(text).strip()
        for long, short in SHORT.items():
            if _html.unescape(long).strip() == plain:
                text = short
                break
        title = flag + text
        meta = r["meta"]
        note = re.sub(r'<[^>]+>', '', r["note"])
        if note and len(note) <= NOTE_MAX:
            meta += " &middot; " + r["note"]
        logo = logo_prefix + r["logo"].lstrip("/")
        out.append(
'          <div class="ag">\n'
'            <div class="ag-date"><div class="ag-day%s">%s</div><div class="ag-mon">%s</div></div>\n'
'            <div class="ag-body">\n'
'              <div class="txt"><h3>%s</h3><p>%s</p></div>\n'
'            </div>\n'
'            <div class="ag-prov"><img src="%s" alt="%s" loading="lazy" decoding="async"></div>\n'
'            <a href="%s" class="btn-training" target="_blank" rel="noopener">%s &rarr;</a>\n'
'          </div>\n'
            % (" range" if len(r["day"]) > 2 else "", r["day"], r["mon"],
               title, meta, logo, r["alt"], r["url"], r["cta"]))
    return "".join(out)

def link_label(total):
    # Ohne Gesamtzahl: die nackte Zahl wirkt nach aussen wie Angeberei.
    return LINK[LANG]


def sync(src, dst, logo_prefix, count):
    rows = parse(os.path.join(ROOT, src))
    if not rows:
        sys.exit("Keine Termine in %s gelesen." % src)
    rows = [r for r in rows if not is_past(r, TODAY)]
    h = io.open(os.path.join(ROOT, dst), encoding="utf-8").read()
    m = re.search(r'(<div class="agenda">\n)(.*?)(\n?        </div>\n\n        <div class="agenda-more">)', h, re.S)
    if not m:
        sys.exit("Vorschau-Block in %s nicht gefunden." % dst)
    h = h[:m.start(2)] + render(rows[:count], logo_prefix).rstrip("\n") + h[m.end(2):]
    # Der Link unter der Vorschau wird bei jedem Lauf neu gesetzt.
    h = re.sub(r'(<div class="agenda-more">\s*\n\s*<a href="[^"]*">)[^<]*(&rarr;</a>)',
               lambda mm: mm.group(1) + link_label(len(rows)) + " " + mm.group(2), h, count=1)
    io.open(os.path.join(ROOT, dst), "w", encoding="utf-8").write(h)
    print("%-14s <- %-22s %d von %d Terminen: %s" % (
        dst, src, min(count, len(rows)), len(rows),
        ", ".join("%s %s" % (r["day"], r["mon"]) for r in rows[:count])))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=5)
    ap.add_argument("--prune", action="store_true",
                    help="abgelaufene Termine auch aus /termine/ entfernen (legt .bak-prune an)")
    ap.add_argument("--today", default=datetime.date.today().isoformat(),
                    help="Stichtag YYYY-MM-DD, zum Testen")
    a = ap.parse_args()
    globals()["TODAY"] = a.today
    if a.prune:
        for src in ("termine/index.html", "en/termine/index.html"):
            gone = prune(os.path.join(ROOT, src), a.today)
            for g in gone:
                print("  abgelaufen, entfernt aus %s: %s" % (src, g))
    globals()["LANG"] = "de"
    sync("termine/index.html",    "index.html",    "",     a.count)
    globals()["LANG"] = "en"
    sync("en/termine/index.html", "en/index.html", "../",  a.count)
