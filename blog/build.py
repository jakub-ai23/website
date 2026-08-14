#!/usr/bin/env python3
"""
build.py - Static blog generator for jakubpopluhar.com

Reads Markdown posts (frontmatter + body) from posts/de and posts/en, renders
one HTML page per post plus a blog index, in both languages. GEO-first: every
page ships raw HTML (no JS for content), JSON-LD entities, canonical + OG tags.
Also emits robots.txt, sitemap.xml, llms.txt at the site root.

  DE posts:  blog/posts/de/<slug>.md   ->  /blog/<slug>/index.html   + /blog/index.html
  EN posts:  blog/posts/en/<slug>.md   ->  /en/blog/<slug>/index.html + /en/blog/index.html

Conventions:
  - Files whose name starts with "_" (e.g. _styleguide.md) are UNLISTED: always
    built + reachable by URL, never listed, never in the sitemap.
  - `draft: true` posts are built only with --drafts and never listed.

No third-party dependencies. Run:  python3 blog/build.py [--drafts]

Created: 2026-07-05
Typography contract + GEO + sharing: see blog/CLAUDE.md
"""

import os
import re
import sys
import json
import html
import struct
from datetime import date
from urllib.parse import quote

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # site root
POSTS_DIR = os.path.join(ROOT, "blog", "posts")
SITE = "https://jakubpopluhar.com"
AUTHOR_IMG = "/images/profile/headshot.png"        # tight headshot (from profile/9.png)
DEFAULT_OG = SITE + "/images/profile/headshot.png"  # fallback share image
# Entity anchors (GEO Gate 1). Must stay identical to the site-wide sameAs used on
# every non-blog page, otherwise a rebuild silently splits the entity again.
# Set 2026-08-07 (commander decision: GitHub out, Linktree not included).
# ars.at without "www", because their own canonical says so.
SAMEAS = [
    "https://www.linkedin.com/in/jakubpopluhar/",
    "https://mindworx.net/team/jakub-popluhar/",
    "https://ars.at/referenten/jakub-popluhar/",
]

# Person entity — reused in JSON-LD everywhere (GEO Gate 1: entity consistency)
PERSON = {
    "@type": "Person",
    "name": "Jakub Popluhar",
    "jobTitle": "Business Lead bei Hill Digital & KI-Trainer",
    "worksFor": {"@type": "Organization", "name": "Hill Digital", "url": "https://hill-digital.at"},
    "url": SITE + "/",
    "image": DEFAULT_OG,
    "sameAs": SAMEAS,
}

WARNINGS = []  # collected lint warnings, printed at end (non-fatal)

# Kategorien (1 pro Post). Reihenfolge = Reihenfolge der Cluster im Index.
# `color` = Akzentfarbe pro Kategorie (Tag, Cluster-Titel, Teaser), damit man sie unterscheidet.
CATEGORIES = [
    {"slug": "meine-agenten", "slug_en": "my-agents", "de": "Meine Agenten", "en": "My Agents", "color": "#a98be0",
     "desc_de": "Meine KI-Agenten, die Roboter: wie ich sie baue, was sie tun, was schiefgeht, und was ich daraus über Automatisierung gelernt habe.",
     "desc_en": "My AI agents, the robots: how I build them, what they do, what breaks, and what each failure taught me about automating real work."},
    {"slug": "aus-der-praxis", "slug_en": "from-practice", "de": "Aus der Praxis", "en": "From Practice", "color": "#d4a017",
     "desc_de": "Was ich selbst baue: eigene Builds, Experimente und Systeme, mitsamt den Fehlern, die dabei passiert sind, und was sie gekostet haben.",
     "desc_en": "What I build myself: my own builds, experiments and systems, including the mistakes I made along the way and what they actually cost."},
    {"slug": "ki-wissen", "slug_en": "ai-knowledge", "de": "KI-Wissen", "en": "AI Knowledge", "color": "#5aa9d6",
     "desc_de": "Erklärendes und Grundlagen für normale Nutzer: was ein LLM ist, wie Hersteller, App, Modell und Abo-Stufe zusammenhängen, ohne Fachjargon.",
     "desc_en": "Explainers and fundamentals for normal users: what an LLM is, how maker, app, model and subscription tier fit together, without the jargon."},
    {"slug": "meine-reise", "slug_en": "my-journey", "de": "Meine Reise", "en": "My Journey", "color": "#e08a4b",
     "desc_de": "Meine eigene Reise: Gesundheit, Experimente am eigenen Leben, gemessene Ergebnisse statt Meinungen, und was davon wirklich etwas gebracht hat.",
     "desc_en": "My own journey: health, self-experiments, measured results instead of opinions, and the handful of things that actually made a difference."},
    {"slug": "jakub-trainings", "slug_en": "jakub-trainings", "de": "Jakub Trainings", "en": "Jakub Trainings", "color": "#6bbf8a",
     "desc_de": "Praxisbeispiele aus Trainings mit Klienten und Firmen: welche Fragen wirklich kommen, was Teams blockiert und was im Raum tatsächlich funktioniert.",
     "desc_en": "Practical examples from trainings with clients and companies: the questions people really ask, what blocks teams, and what works in the room."},
]
CAT_BY_SLUG = {c["slug"]: c for c in CATEGORIES}

# Slug pairing DE <-> EN, filled in main() from the post filenames.
#   PAIRS[stem][lang] = slug in that language
PAIRS = {}
# Old EN URL -> new EN URL, written as redirect stubs.
#
# Until 2026-08-14 the English mirror reused the German slug, so English readers got
# URLs like /en/blog/agenten-ohne-gedaechtnis/. Those URLs were live, indexed and
# shared, so they must keep resolving. This list is explicit rather than derived: it
# is the record of what was once live, and a new article must never land in it.
LEGACY_EN_PATHS = {
    # articles
    "agenten-ohne-gedaechtnis": "ai-agents-without-memory",
    "diktieren-ist-orchestrieren": "dictating-is-orchestrating",
    "ki-landkarte": "ai-map-providers-models",
    "prompt-ist-ein-lasso": "a-prompt-is-a-lasso",
    "prozess-der-sich-selbst-repariert": "process-that-repairs-itself",
    "regel-gebrochen": "ai-broke-my-rule",
    "zehn-mitarbeiter-eine-frage": "ten-employees-one-question",
    # categories
    "aus-der-praxis": "from-practice",
    "ki-wissen": "ai-knowledge",
    "meine-agenten": "my-agents",
}
REDIRECTS = [(f"/en/blog/{old}/", f"/en/blog/{new}/")
             for old, new in sorted(LEGACY_EN_PATHS.items())]


def cat_label(cat, lang):
    return cat[lang]


def cat_slug(cat, lang):
    """Category slug in the page language. `slug` stays the canonical DE key used in
    frontmatter and in CAT_BY_SLUG; `slug_en` is the URL the English site uses."""
    return cat.get("slug_en", cat["slug"]) if lang == "en" else cat["slug"]


def slug_for(stem, lang):
    """The slug of this article in `lang`, or None if that translation is missing."""
    return PAIRS.get(stem, {}).get(lang)


def cat_color(cat):
    return cat.get("color", "#d4a017")

STRINGS = {
    "de": {
        "lang": "de",
        "blog_base": "/blog",
        "home": "/",
        "other_lang_label": "EN",
        "other_lang_href_index": "/en/blog/",
        "index_title": "Blog: KI in der Praxis - Jakub Popluhar",
        "index_h1": "Blog",
        "index_intro": "Meine Erfahrungen aus der Praxis.",
        "index_desc": ("Erfahrungen aus der Arbeit mit KI-Agenten und KI-Assistenten: was ich selbst baue, was dabei schiefgeht und was ich in Trainings daraus mitnehme."),
        "home_link": "Startseite",
        "read_more": "Lesen →",
        "min_read": "Min. Lesezeit",
        "empty": "Der erste Artikel ist gerade in Arbeit. Bald mehr.",
        "back_all": "← Alle Artikel",
        "latest": "Neueste Beiträge",
        "view_all": "Alle ansehen →",
        "more_card": "Weiterlesen →",
        "more_all": "Weitere Artikel →",
        "share_label": "Teilen:",
        "share_email": "E-Mail",
        "share_copy": "Link kopieren",
        "share_copied": "Kopiert ✓",
        "author_name": "Jakub Popluhar",
        "author_bio": 'Business Lead bei Hill Digital und KI-Trainer. <a href="/#about">Mehr über mich</a>',
        "impressum": ("Impressum", "/impressum.html"),
        "datenschutz": ("Datenschutz", "/datenschutz.html"),
    },
    "en": {
        "lang": "en",
        "blog_base": "/en/blog",
        "home": "/en/",
        "other_lang_label": "DE",
        "other_lang_href_index": "/blog/",
        "index_title": "Blog: AI in Practice - Jakub Popluhar",
        "index_h1": "Blog",
        "index_intro": "Lessons from my practice.",
        "index_desc": ("Field notes on working with AI agents and assistants: what I build myself, what breaks along the way, and what I take from it into corporate training."),
        "home_link": "Home",
        "read_more": "Read →",
        "min_read": "min read",
        "empty": "The first article is being written right now. More soon.",
        "back_all": "← All articles",
        "latest": "Latest",
        "view_all": "View all →",
        "more_card": "Read more →",
        "more_all": "More articles →",
        "share_label": "Share:",
        "share_email": "Email",
        "share_copy": "Copy link",
        "share_copied": "Copied ✓",
        "author_name": "Jakub Popluhar",
        "author_bio": 'Business Lead at Hill Digital and AI trainer. <a href="/en/#about">More about me</a>',
        "impressum": ("Imprint", "/impressum.html"),
        "datenschutz": ("Privacy", "/datenschutz.html"),
    },
}

# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------
def parse_post(path):
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    meta, body = {}, raw
    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            block = raw[3:end].strip()
            body = raw[end + 4:].lstrip("\n")
            for line in block.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"').strip("'")
    base = os.path.splitext(os.path.basename(path))[0]
    # The filename stem is identical for a DE post and its EN translation. It, not the
    # slug, is what pairs the two languages, so each language is free to carry a slug
    # in its own language (an English reader should not get a German URL).
    meta["_stem"] = base
    meta.setdefault("slug", base)
    meta.setdefault("title", meta["slug"])
    # title_seo: optional. The <title> shown in search results, when the headline on
    # the page is longer than a result line. The H1 is never touched by it.
    for key in ("date", "description", "lede", "hero", "caption", "category",
                "title_seo", "hero_alt"):
        meta.setdefault(key, "")
    meta["draft"] = str(meta.get("draft", "false")).lower() == "true"
    meta["_unlisted"] = os.path.basename(path).startswith("_")
    meta["_body"] = body
    meta["_reading"] = max(1, round(len(re.findall(r"\w+", body)) / 200))
    return meta


# ---------------------------------------------------------------------------
# Lints (non-fatal; collected in WARNINGS)
# ---------------------------------------------------------------------------
def lint_post(p, lang):
    tag = f"[{lang}] {p['slug']}"
    if not p["_unlisted"] and not p["description"]:
        WARNINGS.append(f"{tag}: missing `description` (GEO: needed for meta description)")
    if not p["_unlisted"] and p["category"] and p["category"] not in CAT_BY_SLUG:
        WARNINGS.append(f"{tag}: unknown category '{p['category']}' (only in Neueste, no cluster)")
    # em/en dash house rule
    if re.search(r"[–—]", p["_body"]):
        WARNINGS.append(f"{tag}: em/en dash in body — replace with ', ' or restructure")
    # heading order: no skipped levels (## -> #### is a jump)
    prev = 1
    for m in re.finditer(r"^(#{2,4})\s", p["_body"], re.M):
        lvl = len(m.group(1))
        if lvl > prev + 1:
            WARNINGS.append(f"{tag}: heading jumps from H{prev} to H{lvl} (keep hierarchy tight)")
        prev = lvl


# ---------------------------------------------------------------------------
# Minimal Markdown -> HTML
# Supported: H2-H4, paragraphs, bold/italic/code, links, images(+caption),
# blockquote (>), pull-quote (>>), ul/ol, tables, code fences, hr.
# ---------------------------------------------------------------------------
IMG_INLINE = re.compile(r'!\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
IMG_BLOCK = re.compile(r'^!\[([^\]]*)\]\(([^)\s]+)(?:\s+"([^"]*)")?\)\s*$')
IMG_NARROW_SUFFIX = "|narrow"


def _inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = IMG_INLINE.sub(
        lambda m: f'<img src="{m.group(2)}" alt="{m.group(1)}"{img_attrs(m.group(2))}>', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def _cells(row):
    row = row.strip().strip("|")
    return [c.strip() for c in row.split("|")]


def md_to_html(md):
    lines = md.split("\n")
    out, i, n = [], 0, len(md.split("\n"))
    while i < len(lines):
        line = lines[i]
        # code fence
        if line.strip().startswith("```"):
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(html.escape(lines[i], quote=False))
                i += 1
            i += 1
            out.append("<pre><code>" + "\n".join(buf) + "</code></pre>")
            continue
        # blank
        if not line.strip():
            i += 1
            continue
        # hr
        if re.match(r"^\s*(---|\*\*\*|___)\s*$", line):
            out.append("<hr>")
            i += 1
            continue
        # table: header row + |---| separator
        if line.lstrip().startswith("|") and i + 1 < len(lines) and \
           re.match(r"^\s*\|?[\s:|-]+\|?\s*$", lines[i + 1]) and "-" in lines[i + 1]:
            header = _cells(lines[i])
            i += 2
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(_cells(lines[i]))
                i += 1
            thead = "".join(f"<th>{_inline(c)}</th>" for c in header)
            tbody = "".join(
                "<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in r) + "</tr>" for r in rows
            )
            out.append(f'<div class="table-wrap"><table><thead><tr>{thead}</tr></thead>'
                       f"<tbody>{tbody}</tbody></table></div>")
            continue
        # heading
        m = re.match(r"^(#{2,4})\s+(.*)$", line)
        if m:
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{_inline(m.group(2).strip())}</h{lvl}>")
            i += 1
            continue
        # pull-quote (>>)  — check before blockquote
        if line.lstrip().startswith(">>"):
            buf = []
            while i < len(lines) and lines[i].lstrip().startswith(">>"):
                buf.append(lines[i].lstrip()[2:].lstrip())
                i += 1
            out.append('<blockquote class="pullquote">' + _inline(" ".join(buf)) + "</blockquote>")
            continue
        # blockquote (>)
        if line.lstrip().startswith(">"):
            buf = []
            while i < len(lines) and lines[i].lstrip().startswith(">") \
                    and not lines[i].lstrip().startswith(">>"):
                buf.append(lines[i].lstrip()[1:].lstrip())
                i += 1
            out.append("<blockquote>" + _inline(" ".join(buf)) + "</blockquote>")
            continue
        # unordered list
        if re.match(r"^\s*[-*]\s+", line):
            buf = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                buf.append("<li>" + _inline(re.sub(r"^\s*[-*]\s+", "", lines[i])) + "</li>")
                i += 1
            out.append("<ul>" + "".join(buf) + "</ul>")
            continue
        # ordered list
        if re.match(r"^\s*\d+\.\s+", line):
            buf = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                buf.append("<li>" + _inline(re.sub(r"^\s*\d+\.\s+", "", lines[i])) + "</li>")
                i += 1
            out.append("<ol>" + "".join(buf) + "</ol>")
            continue
        # standalone image (optional caption via title)
        m = IMG_BLOCK.match(line)
        if m:
            alt, src, cap = m.group(1), m.group(2), m.group(3)
            if cap:
                fig_class = "body-fig"
                if cap.endswith(IMG_NARROW_SUFFIX):
                    cap = cap[:-len(IMG_NARROW_SUFFIX)]
                    fig_class = "body-fig body-fig-narrow"
                out.append(f'<figure class="{fig_class}">'
                           f'<img src="{src}" alt="{html.escape(alt)}"{img_attrs(src)}>'
                           f'<figcaption>{html.escape(cap)}</figcaption></figure>')
            else:
                out.append(f'<img src="{src}" alt="{html.escape(alt)}"{img_attrs(src)}>')
            i += 1
            continue
        # paragraph
        buf = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(
            r"^\s*(#{2,4}\s|[-*]\s|\d+\.\s|>|```|---|\|)", lines[i]
        ):
            buf.append(lines[i])
            i += 1
        out.append("<p>" + _inline(" ".join(b.strip() for b in buf)) + "</p>")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------
def fmt_date(d, lang):
    try:
        y, m, day = (int(x) for x in d.split("-"))
        months = {
            "de": ["Jan.", "Feb.", "März", "Apr.", "Mai", "Juni", "Juli",
                   "Aug.", "Sep.", "Okt.", "Nov.", "Dez."],
            "en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
                   "Aug", "Sep", "Oct", "Nov", "Dec"],
        }[lang]
        return f"{day}. {months[m-1]} {y}" if lang == "de" else f"{months[m-1]} {day}, {y}"
    except Exception:
        return d


def abs_url(path):
    return path if path.startswith("http") else SITE + path


# ---------------------------------------------------------------------------
# Image attributes: width/height stop the layout jumping while the image loads
# (CLS), loading=lazy keeps below-the-fold images off the critical path.
# Dimensions are read straight from the file header, stdlib only.
# ---------------------------------------------------------------------------
_DIM_CACHE = {}


def _read_dims(path):
    """(width, height) from a PNG/JPEG/GIF/WebP header, or None."""
    try:
        with open(path, "rb") as f:
            head = f.read(32)
            if head[:8] == b"\x89PNG\r\n\x1a\n":
                w, h = struct.unpack(">II", head[16:24])
                return int(w), int(h)
            if head[:3] == b"GIF":
                w, h = struct.unpack("<HH", head[6:10])
                return int(w), int(h)
            if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
                if head[12:16] == b"VP8X":
                    w = int.from_bytes(head[24:27], "little") + 1
                    h = int.from_bytes(head[27:30], "little") + 1
                    return w, h
                f.seek(0)
                buf = f.read(64)
                if buf[12:16] == b"VP8 ":
                    w = int.from_bytes(buf[26:28], "little") & 0x3FFF
                    h = int.from_bytes(buf[28:30], "little") & 0x3FFF
                    return w, h
                if buf[12:16] == b"VP8L":
                    b = int.from_bytes(buf[21:25], "little")
                    return (b & 0x3FFF) + 1, ((b >> 14) & 0x3FFF) + 1
                return None
            if head[:2] == b"\xff\xd8":  # JPEG: walk the marker chain to an SOF
                f.seek(2)
                while True:
                    b = f.read(1)
                    if not b:
                        return None
                    if b != b"\xff":
                        continue
                    marker = f.read(1)
                    while marker == b"\xff":
                        marker = f.read(1)
                    if not marker:
                        return None
                    m = marker[0]
                    if m in (0xD8, 0xD9) or 0xD0 <= m <= 0xD7:
                        continue
                    seg = f.read(2)
                    if len(seg) < 2:
                        return None
                    length = struct.unpack(">H", seg)[0]
                    if m in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                             0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                        data = f.read(5)
                        h, w = struct.unpack(">HH", data[1:5])
                        return int(w), int(h)
                    f.seek(length - 2, 1)
    except Exception:
        return None
    return None


def img_dims(src):
    """(width, height) for a site-absolute image path like /images/blog/x.png."""
    if not src or src.startswith("http") or src not in _DIM_CACHE:
        if not src or src.startswith("http"):
            return None
        _DIM_CACHE[src] = _read_dims(os.path.join(ROOT, src.lstrip("/")))
    return _DIM_CACHE[src]


def social_image(hero):
    """The image a share preview should use, not the on-page hero.

    Two reasons they differ. The hero is a WebP sized for the page; LinkedIn's
    scraper is unreliable with WebP. And the raw hero can be far larger than the
    caps social scrapers enforce (Facebook rejects over 8 MB outright), which is
    how a share silently ends up with no picture at all. So every hero gets a
    1200x630 JPEG twin under images/blog/social/, and that is what og:image points
    at. Falls back to the hero, then the headshot, if no twin exists."""
    if not hero:
        return DEFAULT_OG
    base = os.path.splitext(os.path.basename(hero))[0]
    candidate = f"/images/blog/social/{base}.jpg"
    if os.path.exists(os.path.join(ROOT, candidate.lstrip("/"))):
        return abs_url(candidate)
    return abs_url(hero)


def img_attrs(src, lazy=True):
    """width/height + loading/decoding attributes for an <img>, as a string."""
    parts = []
    dims = img_dims(src)
    if dims:
        parts.append(f'width="{dims[0]}" height="{dims[1]}"')
    parts.append('loading="lazy" decoding="async"' if lazy else 'decoding="async"')
    return " " + " ".join(parts)


LOGO_SVG = ('<svg class="logo-svg-nav" viewBox="0 0 380 125" height="46" aria-label="Jakub Popluhar">'
            '<defs><linearGradient id="goldGradient" x1="0%" y1="0%" x2="100%" y2="0%">'
            '<stop offset="0%" stop-color="#bf953f"/><stop offset="18%" stop-color="#fcf6ba"/>'
            '<stop offset="40%" stop-color="#b38728"/><stop offset="65%" stop-color="#fbf5b7"/>'
            '<stop offset="85%" stop-color="#daa520"/><stop offset="100%" stop-color="#aa771c"/>'
            '</linearGradient><filter id="goldGlow"><feDropShadow dx="0" dy="1" stdDeviation="1.5"'
            ' flood-color="#d4a017" flood-opacity="0.35"/></filter></defs>'
            '<text x="15" y="70" text-anchor="start" font-family="\'Great Vibes\', cursive"'
            ' font-size="74" fill="url(#goldGradient)" filter="url(#goldGlow)">Jakub</text>'
            '<text x="85" y="112" text-anchor="start" font-family="\'Montserrat\', sans-serif"'
            ' font-size="19" font-weight="400" fill="#ffffff" style="letter-spacing: 8px;">POPLUHAR</text></svg>')

NAV_LABELS = {
    "de": ("Über mich", "Angebote", "Ergebnisse", "Blog", "Session buchen"),
    "en": ("About", "Services", "Results", "Blog", "Book a session"),
}


def nav_html(s, other_href):
    home, lang = s["home"], s["lang"]
    about, services, results, blog, cta = NAV_LABELS[lang]
    de_active = "active" if lang == "de" else ""
    en_active = "active" if lang == "en" else ""
    de_href = s["blog_base"] + "/" if lang == "de" else other_href
    en_href = other_href if lang == "de" else s["blog_base"] + "/"
    return f"""<nav class="nav">
    <div class="container">
      <a href="{home}" class="nav-logo">{LOGO_SVG}</a>
      <div class="nav-right">
        <ul class="nav-links" id="blogNavLinks">
          <li><a href="{home}#about">{about}</a></li>
          <li><a href="{home}#services">{services}</a></li>
          <li><a href="{home}#proof">{results}</a></li>
          <li><a href="{s['blog_base']}/" class="active">{blog}</a></li>
          <li><a href="{home}#contact" class="nav-cta">{cta}</a></li>
        </ul>
        <div class="nav-lang" aria-label="Sprache">
          <a href="{de_href}" class="{de_active}">DE</a>
          <span class="nav-lang-sep">/</span>
          <a href="{en_href}" class="{en_active}">EN</a>
        </div>
        <button class="nav-toggle" id="blogNavToggle" aria-label="Menu" aria-expanded="false" aria-controls="blogNavLinks">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </nav>
  <script>
  (function(){{
    var t=document.getElementById('blogNavToggle'),l=document.getElementById('blogNavLinks');
    if(!t||!l)return;
    t.addEventListener('click',function(){{
      var open=l.classList.toggle('open');
      t.setAttribute('aria-expanded',open?'true':'false');
    }});
    l.querySelectorAll('a').forEach(function(a){{
      a.addEventListener('click',function(){{l.classList.remove('open');t.setAttribute('aria-expanded','false');}});
    }});
  }})();
  </script>"""


def share_html(s, url, title):
    enc, tenc = quote(url, safe=""), quote(title, safe="")
    li = f"https://www.linkedin.com/sharing/share-offsite/?url={enc}"
    tw = f"https://twitter.com/intent/tweet?url={enc}&text={tenc}"
    fb = f"https://www.facebook.com/sharer/sharer.php?u={enc}"
    mail = f"mailto:?subject={tenc}&body={quote(title + ' ' + url, safe='')}"
    return f"""<div class="share-row">
      <span class="share-label">{s['share_label']}</span>
      <a class="share-btn" href="{li}" target="_blank" rel="noopener" aria-label="LinkedIn">LinkedIn</a>
      <a class="share-btn" href="{mail}" aria-label="{s['share_email']}">{s['share_email']}</a>
      <a class="share-btn" href="{tw}" target="_blank" rel="noopener" aria-label="X">X</a>
      <a class="share-btn" href="{fb}" target="_blank" rel="noopener" aria-label="Facebook">Facebook</a>
      <button class="share-btn copy" data-url="{html.escape(url)}" data-done="{s['share_copied']}">{s['share_copy']}</button>
    </div>"""


COPY_JS = """<script>
document.querySelectorAll('.share-btn.copy').forEach(function(b){
  b.addEventListener('click',function(){
    navigator.clipboard.writeText(b.dataset.url).then(function(){
      var t=b.textContent;b.textContent=b.dataset.done;setTimeout(function(){b.textContent=t;},1500);
    });
  });
});
</script>"""


def footer_html(s):
    imp, dat = s["impressum"], s["datenschutz"]
    return f"""<footer class="blog-footer">
    <div class="wrap">
      <div class="links">
        <a href="{imp[1]}">{imp[0]}</a>
        <a href="{dat[1]}">{dat[0]}</a>
      </div>
      <div>&copy; {date.today().year} Jakub Popluhar</div>
    </div>
  </footer>"""


TITLE_MAX = 65   # Google truncates a result title around here
BRAND = " - Jakub Popluhar"


def page_title(title):
    """Append the brand only while it still fits. A headline that already fills the
    result line does not need the name glued on to be cut off mid-word."""
    title = title.strip()
    return title + BRAND if len(title) + len(BRAND) <= TITLE_MAX else title


def clamp_description(text, lang, what=""):
    """Meta descriptions live in a 70-165 character window: shorter wastes the slot,
    longer gets cut. This only reports out-of-range values, it never invents text."""
    text = (text or "").strip()
    n = len(text)
    if what and (n < 70 or n > 165):
        WARNINGS.append(f"[{lang}] {what}: description {n} chars (target 70-165)")
    return text


def jsonld(obj):
    data = {"@context": "https://schema.org", **obj}
    return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=2) + "\n</script>"


PAGE = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{ogtitle}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="{ogtype}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ogimage}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/blog/blog.css">
{head_extra}
</head>
<body>
{nav}
<main>
{content}
</main>
{footer}
{scripts}
<!-- Analytics: zentraler cookieless Beacon (+ Consent-gated Clarity). NICHT entfernen,
     sonst ist der Artikel ungetrackt. Siehe assets/js/site.js. -->
<script src="/assets/js/site.js" defer></script>
</body>
</html>
"""


def post_card(s, p, lang, featured=False, small=False):
    cls = "post-card"
    if featured:
        cls += " featured"
    if small:
        cls += " small"
    thumb = (f'<img class="thumb" src="{p["hero"]}" alt=""{img_attrs(p["hero"])}>'
             if featured and p["hero"] else "")
    excerpt = "" if small else f'<p>{html.escape(p["description"] or p["lede"])}</p>'
    more = "" if small else f'<span class="more">{s["read_more"]}</span>'
    return f"""<a class="{cls}" href="{s['blog_base']}/{p['slug']}/">
        {thumb}
        <div class="meta">{fmt_date(p['date'], lang)} &middot; {p['_reading']} {s['min_read']}</div>
        <h2>{html.escape(p['title'])}</h2>
        {excerpt}{more}
      </a>"""


def mag_featured(s, p, lang):
    """Magazine hero: newest post, big image (or category-colour tile) + text."""
    cat = CAT_BY_SLUG.get(p["category"])
    color = cat_color(cat) if cat else "#d4a017"
    label = cat_label(cat, lang) if cat else ""
    if p["hero"]:
        media = (f'<div class="mag-feat-img"><img src="{p["hero"]}" alt=""'
                 f'{img_attrs(p["hero"], lazy=False)} fetchpriority="high"></div>')
    else:
        media = (f'<div class="mag-feat-img tile" '
                 f'style="background:linear-gradient(135deg,{color},{color}55)">'
                 f'<span>{html.escape(label)}</span></div>')
    eyebrow = f'<span class="mag-eyebrow" style="color:{color}">{html.escape(label)}</span>' if label else ""
    return f"""<a class="mag-feat" href="{s['blog_base']}/{p['slug']}/">
      {media}
      <div class="mag-feat-body">
        <div class="mag-meta">{eyebrow}<span class="mag-date">{fmt_date(p['date'], lang)}</span></div>
        <h2>{html.escape(p['title'])}</h2>
        <p>{html.escape(p['description'] or p['lede'])}</p>
        <span class="more">{s['read_more']}</span>
      </div>
    </a>"""


def mag_grid_card(s, p, lang):
    """Image grid card: hero (or category-colour tile) + hover-zoom, date + category, title."""
    cat = CAT_BY_SLUG.get(p["category"])
    color = cat_color(cat) if cat else "#d4a017"
    label = cat_label(cat, lang) if cat else ""
    tail = f" &middot; {html.escape(label)}" if label else ""
    if p["hero"]:
        media = (f'<div class="mag-card-img"><img src="{p["hero"]}" alt=""'
                 f'{img_attrs(p["hero"])}></div>')
    else:
        media = (f'<div class="mag-card-img tile" '
                 f'style="background:linear-gradient(135deg,{color},{color}55)">'
                 f'<span>{html.escape(label)}</span></div>')
    desc = html.escape(p['description'] or p['lede'] or "")
    return f"""<a class="mag-card" href="{s['blog_base']}/{p['slug']}/" style="--cat:{color}">
      {media}
      <span class="mag-card-date">{fmt_date(p['date'], lang)}{tail}</span>
      <h3>{html.escape(p['title'])}</h3>
      <p class="mag-card-desc">{desc}</p>
      <span class="mag-card-more">{s['more_card']}</span>
    </a>"""


def hreflang_links(de_tail, en_tail=None):
    """Bilingual alternate links. The tails are the blog-relative paths after the
    language base ("" for the index, "<slug>/" for an article or category) and they
    now differ per language, because each language carries its own slug. A tail of
    None means that translation does not exist, and then no alternate is claimed for
    it: pointing hreflang at a 404 is worse than omitting it.
    DE is the site default (x-default), mirroring the homepage."""
    out = []
    if de_tail is not None:
        de = abs_url(f"/blog/{de_tail}")
        out.append(f'<link rel="alternate" hreflang="de" href="{de}">')
    if en_tail is not None:
        en = abs_url(f"/en/blog/{en_tail}")
        out.append(f'<link rel="alternate" hreflang="en" href="{en}">')
    if de_tail is not None:
        out.append(f'<link rel="alternate" hreflang="x-default" href="{abs_url(f"/blog/{de_tail}")}">')
    elif en_tail is not None:
        out.append(f'<link rel="alternate" hreflang="x-default" href="{abs_url(f"/en/blog/{en_tail}")}">')
    return "\n".join(out)


def render_index(lang, posts):
    """Hybrid index: newest posts on top, then a cluster per category."""
    s = STRINGS[lang]
    if not posts:
        body = f'<p class="empty-note">{s["empty"]}</p>'
    else:
        # 1) Neueste - Magazine-Layout: Featured (Hauptartikel) + genau 3 Karten
        latest = posts
        parts = [f'<h2 class="section-h">{s["latest"]}</h2>',
                 mag_featured(s, latest[0], lang)]
        if len(latest) > 1:
            grid = "\n".join(mag_grid_card(s, p, lang) for p in latest[1:4])
            parts.append(f'<div class="mag-grid">{grid}</div>')
        # 2) Rest hinter "Weitere Artikel" (CSS :target, kein JS, Inhalt bleibt im DOM = GEO-sicher)
        clusters = []
        for cat in CATEGORIES:
            in_cat = [p for p in posts if p["category"] == cat["slug"]]
            if not in_cat:
                continue
            c = cat_color(cat)
            chead = (f'<div class="cluster-head"><h2 style="color:{c}">{cat_label(cat, lang)}</h2>'
                     f'<a href="{s["blog_base"]}/{cat_slug(cat, lang)}/" style="color:{c}">{s["view_all"]}</a></div>')
            ccards = "\n".join(post_card(s, p, lang, small=True) for p in in_cat[:3])
            clusters.append(f'<section class="cluster">{chead}'
                            f'<div class="post-list small-list">{ccards}</div></section>')
        if clusters:
            parts.append(f'<div id="more" class="more-content">{"".join(clusters)}</div>')
            parts.append(f'<div class="more-cta"><a href="#more" class="more-btn">{s["more_all"]}</a></div>')
        body = "\n".join(parts)

    content = f"""<header class="blog-head">
    <div class="wrap-wide">
      <h1>{s['index_h1']}</h1>
      <p>{s['index_intro']}</p>
    </div>
  </header>
  <section class="wrap-wide">
    {body}
  </section>"""

    canonical = abs_url(f"{s['blog_base']}/")
    return PAGE.format(
        lang=lang, title=s["index_title"],
        description=clamp_description(s["index_desc"], lang, "blog index"),
        ogtitle=s["index_h1"], ogtype="website", canonical=canonical, ogimage=DEFAULT_OG,
        head_extra=hreflang_links("", "") + "\n" + jsonld(PERSON),
        nav=nav_html(s, s["other_lang_href_index"]),
        content=content, footer=footer_html(s), scripts="",
    )


def render_category(lang, cat, posts):
    """One archive page per category: all its posts, newest first."""
    s = STRINGS[lang]
    cards = "\n".join(post_card(s, p, lang) for p in posts)
    label = cat_label(cat, lang)
    content = f"""<header class="blog-head">
    <div class="wrap">
      <div class="cat-eyebrow"><a href="{s['blog_base']}/">Blog</a> / <span style="color:{cat_color(cat)}">{label}</span></div>
      <h1 style="color:{cat_color(cat)}">{label}</h1>
      <p>{cat['desc_'+lang]}</p>
    </div>
  </header>
  <section class="wrap">
    <div class="post-list">{cards}</div>
  </section>"""
    canonical = abs_url(f"{s['blog_base']}/{cat_slug(cat, lang)}/")
    breadcrumb = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Blog", "item": abs_url(f"{s['blog_base']}/")},
            {"@type": "ListItem", "position": 2, "name": label, "item": canonical},
        ],
    }
    return PAGE.format(
        lang=lang, title=page_title(f"{label} - Blog"), description=cat['desc_'+lang],
        ogtitle=label, ogtype="website", canonical=canonical, ogimage=DEFAULT_OG,
        head_extra=(hreflang_links(f"{cat['slug']}/", f"{cat_slug(cat, 'en')}/")
                    + "\n" + jsonld(PERSON) + "\n" + jsonld(breadcrumb)),
        nav=nav_html(s, other_lang_category(lang, cat)),
        content=content, footer=footer_html(s), scripts="",
    )


def other_lang_category(lang, cat):
    other = "en" if lang == "de" else "de"
    return f"{STRINGS[other]['blog_base']}/{cat_slug(cat, other)}/"


def render_article(lang, p):
    s = STRINGS[lang]
    canonical = abs_url(f"{s['blog_base']}/{p['slug']}/")
    ogimage = social_image(p["hero"])          # share preview: 1200x630 JPEG
    jsonld_image = abs_url(p["hero"]) if p["hero"] else DEFAULT_OG   # schema: the real image
    if p["hero"]:
        cap = (f'<figcaption class="article-hero-caption">{html.escape(p["caption"])}</figcaption>'
               if p["caption"] else "")
        # Hero is the LCP element: never lazy, and it needs a real alt. Falls back to
        # the caption, then the title, so it is never an empty alt="" on a content image.
        hero_alt = html.escape(p.get("hero_alt") or p["caption"] or p["title"])
        hero = (f'<figure class="article-hero-fig">'
                f'<img class="article-hero" src="{p["hero"]}" alt="{hero_alt}"'
                f'{img_attrs(p["hero"], lazy=False)} fetchpriority="high">{cap}</figure>')
    else:
        hero = ""
    lede = f'<p class="lede">{html.escape(p["lede"])}</p>' if p["lede"] else ""
    share = share_html(s, canonical, p["title"])
    # split off a trailing "Quellen"/"Sources"/"Hinweis" section -> render ultra small
    parts = re.split(r"(?m)^(?=##\s+(?:Quellen|Sources|Hinweis)\b)", p["_body"], maxsplit=1)
    body_html = md_to_html(parts[0])
    if len(parts) > 1:
        body_html += '\n<div class="article-sources">\n' + md_to_html(parts[1]) + "\n</div>"
    cat = CAT_BY_SLUG.get(p["category"])
    # Kategorie als Eyebrow ueber dem Titel (HD-Struktur)
    eyebrow = (f'<div class="cat-eyebrow"><a href="{s["blog_base"]}/{cat_slug(cat, lang)}/"'
               f' style="color:{cat_color(cat)}">{cat_label(cat, lang)}</a></div>'
               if cat else "")
    # Byline unter dem Titel: Foto + Name + Datum . Lesezeit (HD-Struktur)
    byline = (f'<div class="byline">'
              f'<img class="byline-img" src="{AUTHOR_IMG}" alt="{s["author_name"]}"'
              # sits above the fold next to the headline: eager, not lazy
              f'{img_attrs(AUTHOR_IMG, lazy=False)}>'
              f'<div class="byline-text">'
              f'<span class="byline-name">{s["author_name"]}</span>'
              f'<span class="byline-meta">{fmt_date(p["date"], lang)} &middot; {p["_reading"]} {s["min_read"]}</span>'
              f'</div></div>')
    content = f"""<article>
    <header class="article-head">
      <div class="wrap">
        {eyebrow}
        <h1>{html.escape(p['title'])}</h1>
        {lede}
        {byline}
        {share}
      </div>
    </header>
    <div class="wrap">
      {hero}
      <div class="article-body">
{body_html}
      </div>
      {share}
      <div class="author-box">
        <img src="{AUTHOR_IMG}" alt="{s['author_name']}"{img_attrs(AUTHOR_IMG)}>
        <div>
          <div class="name">{s['author_name']}</div>
          <div class="bio">{s['author_bio']}</div>
        </div>
      </div>
      <div class="article-foot"><a href="{s['blog_base']}/">{s['back_all']}</a></div>
    </div>
  </article>"""

    posting = {
        "@type": "BlogPosting",
        "headline": p["title"],
        "description": p["description"] or p["lede"],
        "datePublished": p["date"],
        "dateModified": p["date"],
        "image": jsonld_image,
        "author": PERSON,
        "publisher": {"@type": "Organization", "name": "Hill Digital", "url": "https://hill-digital.at"},
        "mainEntityOfPage": canonical,
        "inLanguage": lang,
    }
    de_slug, en_slug = slug_for(p["_stem"], "de"), slug_for(p["_stem"], "en")
    head = hreflang_links(f"{de_slug}/" if de_slug else None,
                          f"{en_slug}/" if en_slug else None) + "\n" + jsonld(posting)
    if cat:
        crumbs = [
            {"@type": "ListItem", "position": 1, "name": "Blog", "item": abs_url(f"{s['blog_base']}/")},
            {"@type": "ListItem", "position": 2, "name": cat_label(cat, lang),
             "item": abs_url(f"{s['blog_base']}/{cat_slug(cat, lang)}/")},
            {"@type": "ListItem", "position": 3, "name": p["title"], "item": canonical},
        ]
        head += "\n" + jsonld({"@type": "BreadcrumbList", "itemListElement": crumbs})
    return PAGE.format(
        lang=lang, title=html.escape(page_title(p.get("title_seo") or p["title"])),
        description=clamp_description(p["description"] or p["lede"], lang, p["slug"]),
        ogtitle=html.escape(p["title"]),
        ogtype="article", canonical=canonical, ogimage=ogimage,
        head_extra=head, nav=nav_html(s, other_lang_article(lang, p)),
        content=content, footer=footer_html(s), scripts=COPY_JS,
    )


def other_lang_article(lang, p):
    """Link to the same article in the other language. If that translation does not
    exist, fall back to the other language's blog index rather than a dead URL."""
    other = "en" if lang == "de" else "de"
    slug = slug_for(p["_stem"], other)
    base = STRINGS[other]["blog_base"]
    return f"{base}/{slug}/" if slug else f"{base}/"


# ---------------------------------------------------------------------------
# Homepage teaser: inject latest posts into a marked region of index.html
# ---------------------------------------------------------------------------
def home_teaser_cards(lang, posts):
    s = STRINGS[lang]
    out = []
    for p in posts[:3]:
        cat = CAT_BY_SLUG.get(p["category"])
        meta = fmt_date(p["date"], lang)
        color = "#d4a017"
        if cat:
            meta += f" &middot; {cat_label(cat, lang)}"
            color = cat_color(cat)
        out.append(
            f'<a class="blog-card" href="{s["blog_base"]}/{p["slug"]}/">'
            f'<span class="blog-card-meta" style="color:{color}">{meta}</span>'
            f'<span class="blog-card-title">{html.escape(p["title"])}</span></a>'
        )
    return "\n        ".join(out)


def inject_home_teaser(lang, posts):
    path = os.path.join(ROOT, "index.html") if lang == "de" else os.path.join(ROOT, "en", "index.html")
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        doc = f.read()
    start, end = "<!-- BLOG-TEASER:START -->", "<!-- BLOG-TEASER:END -->"
    if start not in doc or end not in doc:
        return  # no teaser region in this file (e.g. EN not wired yet)
    cards = home_teaser_cards(lang, posts)
    new = re.sub(re.escape(start) + r".*?" + re.escape(end),
                 start + "\n        " + cards + "\n        " + end, doc, flags=re.S)
    if new != doc:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
        print("  injected home teaser ->", os.path.relpath(path, ROOT))


# ---------------------------------------------------------------------------
# Site-level files (GEO)
# ---------------------------------------------------------------------------
def write_robots():
    bots = ["GPTBot", "OAI-SearchBot", "PerplexityBot", "ClaudeBot", "Google-Extended", "Bingbot"]
    lines = ["User-agent: *", "Allow: /", ""]
    for b in bots:
        lines += [f"User-agent: {b}", "Allow: /", ""]
    lines.append(f"Sitemap: {SITE}/sitemap.xml")
    write(os.path.join(ROOT, "robots.txt"), "\n".join(lines) + "\n")


def write_sitemap(entries):
    """entries: list of (url, lastmod|None, [(hreflang, url), ...]).
    lastmod tells crawlers what actually changed; the xhtml:link alternates state the
    DE/EN pairing in the sitemap itself, which is what Google reads for hreflang."""
    rows = []
    for u, lastmod, alts in sorted(set(entries), key=lambda e: e[0]):
        row = [f"  <url>", f"    <loc>{SITE}{u}</loc>"]
        if lastmod:
            row.append(f"    <lastmod>{lastmod}</lastmod>")
        for hl, href in alts:
            row.append(f'    <xhtml:link rel="alternate" hreflang="{hl}" href="{SITE}{href}"/>')
        row.append("  </url>")
        rows.append("\n".join(row))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    write(os.path.join(ROOT, "sitemap.xml"), xml)


def write_redirect(old_path, new_path, lang="en"):
    """GitHub Pages serves no 30x, so a moved URL needs a stub page that is
    noindex + canonical to the new URL and bounces the reader instantly."""
    target = abs_url(new_path)
    doc = ('<!doctype html>\n'
           f'<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n'
           '<meta name="robots" content="noindex, follow">\n'
           f'<link rel="canonical" href="{target}">\n'
           f'<meta http-equiv="refresh" content="0; url={target}">\n'
           '<title>Moved</title>\n</head>\n<body>\n'
           f'<p>This page has moved to <a href="{target}">{target}</a>.</p>\n'
           f'<script>location.replace({json.dumps(target)});</script>\n'
           '</body>\n</html>\n')
    path = os.path.join(ROOT, old_path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)
    print("  redirect", old_path, "->", new_path)


def write_llms(all_posts=None):
    """llms.txt is cheap insurance, not a lever (GEO doctrine: no measured effect).
    Kept small, but it now lists the actual articles with one line each, so a model
    reading it learns what is here instead of only that a blog exists."""
    lines = [
        "# Jakub Popluhar",
        "",
        "> Business Lead at Hill Digital and AI trainer, based in Vienna, Austria.",
        "> Corporate AI training in German and English across the DACH region.",
        "> Practical, first-hand notes on working with AI agents and assistants.",
        "",
        "## Site",
        "",
        f"- [About]({SITE}/#about): who he is, what he trains, references.",
        f"- [Dates]({SITE}/termine/): confirmed open seminars (ARS Akademie, tecTrain).",
        f"- [Blog, German]({SITE}/blog/)",
        f"- [Blog, English]({SITE}/en/blog/)",
    ]
    for lang, heading in (("en", "## Articles (English)"), ("de", "## Artikel (Deutsch)")):
        posts = [p for p in (all_posts or {}).get(lang, [])
                 if not p["draft"] and not p["_unlisted"]]
        if not posts:
            continue
        lines += ["", heading, ""]
        base = STRINGS[lang]["blog_base"]
        for p in posts:
            desc = (p["description"] or p["lede"] or "").strip()
            lines.append(f"- [{p['title']}]({SITE}{base}/{p['slug']}/): {desc}")
    write(os.path.join(ROOT, "llms.txt"), "\n".join(lines) + "\n")


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
def load(lang):
    d = os.path.join(POSTS_DIR, lang)
    if not os.path.isdir(d):
        return []
    posts = [parse_post(os.path.join(d, f)) for f in os.listdir(d) if f.endswith(".md")]
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def write(path, content):
    # Analytics-Gate: jede gebaute HTML-Seite MUSS site.js laden, sonst kein Tracking.
    if path.endswith(".html") and "/assets/js/site.js" not in content:
        raise SystemExit(f"Analytics-Hook fehlt in {path}: site.js nicht im generierten HTML")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  wrote", os.path.relpath(path, ROOT))


def main():
    include_drafts = "--drafts" in sys.argv
    sitemap_urls = []
    cat_slugs = {c["slug"] for c in CATEGORIES} | {cat_slug(c, "en") for c in CATEGORIES}

    # Pass 1: read both languages and build the DE<->EN pairing before rendering
    # anything, because hreflang and the language switcher need the other language's
    # slug, and the slugs no longer match.
    all_posts = {lang: load(lang) for lang in ("de", "en")}
    for lang, posts in all_posts.items():
        for p in posts:
            PAIRS.setdefault(p["_stem"], {})[lang] = p["slug"]

    for lang in ("de", "en"):
        s = STRINGS[lang]
        posts = all_posts[lang]
        listed = [p for p in posts if not p["draft"] and not p["_unlisted"]]
        # build: listed + unlisted always; drafts only with --drafts
        buildable = [p for p in posts if p["_unlisted"] or not p["draft"] or include_drafts]
        for p in posts:
            lint_post(p, lang)
            if p["slug"] in cat_slugs:
                WARNINGS.append(f"[{lang}] {p['slug']}: post slug collides with a category slug")
        out_base = os.path.join(ROOT, "blog") if lang == "de" else os.path.join(ROOT, "en", "blog")
        # category pages: only for categories that have >=1 listed post (DE-first emerges naturally)
        cats_built = 0
        for cat in CATEGORIES:
            in_cat = [p for p in listed if p["category"] == cat["slug"]]
            if not in_cat:
                continue
            write(os.path.join(out_base, cat_slug(cat, lang), "index.html"),
                  render_category(lang, cat, in_cat))
            newest_in_cat = max((p["date"] for p in in_cat), default=None)
            sitemap_urls.append((
                f"{s['blog_base']}/{cat_slug(cat, lang)}/", newest_in_cat,
                (("de", f"/blog/{cat['slug']}/"),
                 ("en", f"/en/blog/{cat_slug(cat, 'en')}/"),
                 ("x-default", f"/blog/{cat['slug']}/")),
            ))
            cats_built += 1
        print(f"[{lang}] {len(listed)} listed, {len(buildable)} built, {cats_built} categor(y/ies)")
        inject_home_teaser(lang, listed)
        write(os.path.join(out_base, "index.html"), render_index(lang, listed))
        newest = max((p["date"] for p in listed), default=None)
        sitemap_urls.append((f"{s['blog_base']}/", newest,
                             (("de", "/blog/"), ("en", "/en/blog/"), ("x-default", "/blog/"))))
        for p in buildable:
            write(os.path.join(out_base, p["slug"], "index.html"), render_article(lang, p))
            if not p["draft"] and not p["_unlisted"]:
                de_s, en_s = slug_for(p["_stem"], "de"), slug_for(p["_stem"], "en")
                alts = []
                if de_s:
                    alts.append(("de", f"/blog/{de_s}/"))
                if en_s:
                    alts.append(("en", f"/en/blog/{en_s}/"))
                if de_s:
                    alts.append(("x-default", f"/blog/{de_s}/"))
                sitemap_urls.append((f"{s['blog_base']}/{p['slug']}/", p["date"], tuple(alts)))

    # Old English URLs carried the German slug. They are indexed and shared, so each
    # one gets a noindex + canonical stub pointing at the new English URL.
    for old_path, new_path in REDIRECTS:
        write_redirect(old_path, new_path)

    # site-level GEO files + core pages in the sitemap
    today = date.today().isoformat()
    for u in ("/", "/en/", "/termine/", "/en/termine/"):
        sitemap_urls.append((u, today, ()))
    for u in ("/impressum.html", "/datenschutz.html"):
        sitemap_urls.append((u, None, ()))
    write_robots()
    write_sitemap(sitemap_urls)
    write_llms(all_posts)

    if WARNINGS:
        print("\nLINT WARNINGS:")
        for w in WARNINGS:
            print("  -", w)
    print("\nDone.")


if __name__ == "__main__":
    main()
