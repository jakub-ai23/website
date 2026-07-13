#!/usr/bin/env python3
"""
Echter Mobil-Emulations-Check fuer den Blog (und beliebige Seiten).

Nutzt Playwright mit echtem iPhone-Profil (Viewport, devicePixelRatio, Touch,
Mobile-User-Agent) statt eines simplen Fenster-Resizes, der clippt statt zu
emulieren. Meldet horizontalen Overflow (die haeufigste Mobil-Suende) UND
listet die konkreten Elemente auf, die ueber den Viewport hinausragen, damit
der Fix zielgerichtet ist. Schreibt Screenshots.

Voraussetzung: Playwright-venv (channel="chrome", kein Browser-Download).
  python3 -m venv <venv> && <venv>/bin/pip install playwright

Aufruf:
  <venv>/bin/python blog/mobile-check.py --base http://localhost:8910 \
      --out <screenshot-dir> [--device "iPhone 13"] [PATH ...]

Exit-Code 0 = alle Seiten sauber, 1 = mindestens eine Seite mit Overflow.
"""
import argparse
import sys
from playwright.sync_api import sync_playwright

DEFAULT_PATHS = [
    "/blog/",
    "/blog/prompt-ist-ein-lasso/",
    "/blog/aus-der-praxis/",
    "/en/blog/",
]

# Findet Elemente, deren rechter Rand ueber den Viewport hinausragt (der echte
# Overflow-Verursacher), plus die Gesamt-Overflow-Breite.
OVERFLOW_JS = """
() => {
  const vw = document.documentElement.clientWidth;
  const docW = document.documentElement.scrollWidth;
  const offenders = [];
  for (const el of document.querySelectorAll('*')) {
    const r = el.getBoundingClientRect();
    if (r.right > vw + 1 && r.width > 0) {
      offenders.push({
        tag: el.tagName.toLowerCase(),
        cls: (el.className && el.className.toString().slice(0, 60)) || '',
        right: Math.round(r.right),
        width: Math.round(r.width),
      });
    }
  }
  // nur die aussersten paar, nach Ueberstand sortiert
  offenders.sort((a, b) => b.right - a.right);
  return { vw, docW, overflow: Math.max(0, docW - vw), offenders: offenders.slice(0, 8) };
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="http://localhost:8910")
    ap.add_argument("--out", default="/tmp/mobile-check")
    ap.add_argument("--device", default="iPhone 13")
    ap.add_argument("paths", nargs="*", default=None)
    args = ap.parse_args()

    import os
    os.makedirs(args.out, exist_ok=True)
    paths = args.paths or DEFAULT_PATHS

    failures = 0
    with sync_playwright() as p:
        device = p.devices.get(args.device) or p.devices["iPhone 13"]
        browser = p.chromium.launch(channel="chrome", headless=True)
        ctx = browser.new_context(**device)
        page = ctx.new_page()
        print(f"Geraet: {args.device}  Viewport: {device['viewport']}  DPR: {device['device_scale_factor']}")
        print("=" * 72)
        for path in paths:
            url = args.base.rstrip("/") + path
            try:
                page.goto(url, wait_until="networkidle", timeout=20000)
            except Exception as e:
                print(f"FEHLER Laden {path}: {str(e)[:80]}")
                failures += 1
                continue
            res = page.evaluate(OVERFLOW_JS)
            slug = path.strip("/").replace("/", "_") or "index"
            shot = os.path.join(args.out, f"{slug}.png")
            page.screenshot(path=shot, full_page=True)
            status = "OK " if res["overflow"] == 0 else "OVERFLOW"
            if res["overflow"] > 0:
                failures += 1
            print(f"[{status}] {path}  vw={res['vw']} doc={res['docW']} overflow={res['overflow']}px")
            for o in res["offenders"]:
                print(f"         -> <{o['tag']} class=\"{o['cls']}\"> right={o['right']} w={o['width']}")
            print(f"         screenshot: {shot}")
        browser.close()
    print("=" * 72)
    print("ERGEBNIS:", "ALLE SAUBER" if failures == 0 else f"{failures} Seite(n) mit Problem")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
