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
SAMEAS = [
    "https://www.linkedin.com/in/jakubpopluhar/",
    "https://github.com/jakub-ai23",
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
CATEGORIES = [
    {"slug": "aus-der-praxis", "de": "Aus der Praxis", "en": "From Practice",
     "desc_de": "Was ich selbst baue: eigene Builds, Experimente, Systeme.",
     "desc_en": "What I build myself: my own builds, experiments, systems."},
    {"slug": "jakub-trainings", "de": "Jakub Trainings", "en": "Jakub Trainings",
     "desc_de": "Praxisbeispiele aus Trainings mit Klienten und Firmen.",
     "desc_en": "Practical examples from trainings with clients and companies."},
    {"slug": "ki-wissen", "de": "KI-Wissen", "en": "AI Knowledge",
     "desc_de": "Erklärendes und Grundlagen: was ist ein LLM und so weiter.",
     "desc_en": "Explainers and fundamentals: what an LLM is, and so on."},
]
CAT_BY_SLUG = {c["slug"]: c for c in CATEGORIES}


def cat_label(cat, lang):
    return cat[lang]

STRINGS = {
    "de": {
        "lang": "de",
        "blog_base": "/blog",
        "home": "/",
        "other_lang_label": "EN",
        "other_lang_href_index": "/en/blog/",
        "index_title": "Blog - Jakub Popluhar",
        "index_h1": "Blog",
        "index_intro": "Meine Erfahrungen aus der Praxis.",
        "home_link": "Startseite",
        "read_more": "Lesen →",
        "min_read": "Min. Lesezeit",
        "empty": "Der erste Artikel ist gerade in Arbeit. Bald mehr.",
        "back_all": "← Alle Artikel",
        "latest": "Neueste Beiträge",
        "view_all": "Alle ansehen →",
        "share_label": "Teilen:",
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
        "index_title": "Blog - Jakub Popluhar",
        "index_h1": "Blog",
        "index_intro": "Lessons from my practice.",
        "home_link": "Home",
        "read_more": "Read →",
        "min_read": "min read",
        "empty": "The first article is being written right now. More soon.",
        "back_all": "← All articles",
        "latest": "Latest",
        "view_all": "View all →",
        "share_label": "Share:",
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
    meta.setdefault("slug", base)
    meta.setdefault("title", meta["slug"])
    for key in ("date", "description", "lede", "hero", "caption", "category"):
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


def _inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = IMG_INLINE.sub(r'<img src="\2" alt="\1">', text)
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
                out.append(f'<figure class="body-fig"><img src="{src}" alt="{html.escape(alt)}">'
                           f'<figcaption>{html.escape(cap)}</figcaption></figure>')
            else:
                out.append(f'<img src="{src}" alt="{html.escape(alt)}">')
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


def nav_html(s, other_href):
    return f"""<nav class="blog-nav">
    <a class="logo" href="{s['home']}">Jakub<span>POPLUHAR</span></a>
    <div class="blog-nav-right">
      <a class="home-link" href="{s['home']}">{s['home_link']}</a>
      <a href="{s['blog_base']}/">Blog</a>
      <span class="blog-lang">
        <a href="{s['blog_base']}/" class="active">{'DE' if s['lang']=='de' else 'EN'}</a>
        <span class="sep">/</span>
        <a href="{other_href}">{s['other_lang_label']}</a>
      </span>
    </div>
  </nav>"""


def share_html(s, url, title):
    enc, tenc = quote(url, safe=""), quote(title, safe="")
    li = f"https://www.linkedin.com/sharing/share-offsite/?url={enc}"
    tw = f"https://twitter.com/intent/tweet?url={enc}&text={tenc}"
    fb = f"https://www.facebook.com/sharer/sharer.php?u={enc}"
    return f"""<div class="share-row">
      <span class="share-label">{s['share_label']}</span>
      <a class="share-btn" href="{li}" target="_blank" rel="noopener" aria-label="LinkedIn">LinkedIn</a>
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
</body>
</html>
"""


def post_card(s, p, lang, featured=False, small=False):
    cls = "post-card"
    if featured:
        cls += " featured"
    if small:
        cls += " small"
    thumb = (f'<img class="thumb" src="{p["hero"]}" alt="">'
             if featured and p["hero"] else "")
    excerpt = "" if small else f'<p>{html.escape(p["description"] or p["lede"])}</p>'
    more = "" if small else f'<span class="more">{s["read_more"]}</span>'
    return f"""<a class="{cls}" href="{s['blog_base']}/{p['slug']}/">
        {thumb}
        <div class="meta">{fmt_date(p['date'], lang)} &middot; {p['_reading']} {s['min_read']}</div>
        <h2>{html.escape(p['title'])}</h2>
        {excerpt}{more}
      </a>"""


def render_index(lang, posts):
    """Hybrid index: newest posts on top, then a cluster per category."""
    s = STRINGS[lang]
    if not posts:
        body = f'<p class="empty-note">{s["empty"]}</p>'
    else:
        # 1) Neueste
        latest = posts[:5]
        cards = [post_card(s, p, lang, featured=(i == 0)) for i, p in enumerate(latest)]
        parts = [f'<h2 class="section-h">{s["latest"]}</h2>',
                 '<div class="post-list">' + "\n".join(cards) + "</div>"]
        # 2) Cluster je Kategorie (nur mit Posts)
        for cat in CATEGORIES:
            in_cat = [p for p in posts if p["category"] == cat["slug"]]
            if not in_cat:
                continue
            chead = (f'<div class="cluster-head"><h2>{cat_label(cat, lang)}</h2>'
                     f'<a href="{s["blog_base"]}/{cat["slug"]}/">{s["view_all"]}</a></div>')
            ccards = "\n".join(post_card(s, p, lang, small=True) for p in in_cat[:3])
            parts.append(f'<section class="cluster">{chead}'
                         f'<div class="post-list small-list">{ccards}</div></section>')
        body = "\n".join(parts)

    content = f"""<header class="blog-head">
    <div class="wrap">
      <h1>{s['index_h1']}</h1>
      <p>{s['index_intro']}</p>
    </div>
  </header>
  <section class="wrap">
    {body}
  </section>"""

    canonical = abs_url(f"{s['blog_base']}/")
    return PAGE.format(
        lang=lang, title=s["index_title"], description=s["index_intro"],
        ogtitle=s["index_h1"], ogtype="website", canonical=canonical, ogimage=DEFAULT_OG,
        head_extra=jsonld(PERSON), nav=nav_html(s, s["other_lang_href_index"]),
        content=content, footer=footer_html(s), scripts="",
    )


def render_category(lang, cat, posts):
    """One archive page per category: all its posts, newest first."""
    s = STRINGS[lang]
    cards = "\n".join(post_card(s, p, lang) for p in posts)
    label = cat_label(cat, lang)
    content = f"""<header class="blog-head">
    <div class="wrap">
      <div class="cat-eyebrow"><a href="{s['blog_base']}/">Blog</a> / {label}</div>
      <h1>{label}</h1>
      <p>{cat['desc_'+lang]}</p>
    </div>
  </header>
  <section class="wrap">
    <div class="post-list">{cards}</div>
  </section>"""
    canonical = abs_url(f"{s['blog_base']}/{cat['slug']}/")
    breadcrumb = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Blog", "item": abs_url(f"{s['blog_base']}/")},
            {"@type": "ListItem", "position": 2, "name": label, "item": canonical},
        ],
    }
    return PAGE.format(
        lang=lang, title=f"{label} - Blog - Jakub Popluhar", description=cat['desc_'+lang],
        ogtitle=label, ogtype="website", canonical=canonical, ogimage=DEFAULT_OG,
        head_extra=jsonld(PERSON) + "\n" + jsonld(breadcrumb),
        nav=nav_html(s, s["other_lang_href_index"]),
        content=content, footer=footer_html(s), scripts="",
    )


def render_article(lang, p):
    s = STRINGS[lang]
    canonical = abs_url(f"{s['blog_base']}/{p['slug']}/")
    ogimage = abs_url(p["hero"]) if p["hero"] else DEFAULT_OG
    if p["hero"]:
        cap = (f'<figcaption class="article-hero-caption">{html.escape(p["caption"])}</figcaption>'
               if p["caption"] else "")
        hero = f'<figure class="article-hero-fig"><img class="article-hero" src="{p["hero"]}" alt="">{cap}</figure>'
    else:
        hero = ""
    lede = f'<p class="lede">{html.escape(p["lede"])}</p>' if p["lede"] else ""
    share = share_html(s, canonical, p["title"])
    cat = CAT_BY_SLUG.get(p["category"])
    cat_tag = (f' &middot; <a class="cat-tag" href="{s["blog_base"]}/{cat["slug"]}/">{cat_label(cat, lang)}</a>'
               if cat else "")
    content = f"""<article>
    <header class="article-head">
      <div class="wrap">
        <div class="meta">{fmt_date(p['date'], lang)} &middot; {p['_reading']} {s['min_read']}{cat_tag}</div>
        <h1>{html.escape(p['title'])}</h1>
        {lede}
        {share}
      </div>
    </header>
    <div class="wrap">
      {hero}
      <div class="article-body">
{md_to_html(p['_body'])}
      </div>
      {share}
      <div class="author-box">
        <img src="{AUTHOR_IMG}" alt="{s['author_name']}">
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
        "image": ogimage,
        "author": PERSON,
        "publisher": {"@type": "Organization", "name": "Hill Digital", "url": "https://hill-digital.at"},
        "mainEntityOfPage": canonical,
        "inLanguage": lang,
    }
    head = jsonld(posting)
    if cat:
        crumbs = [
            {"@type": "ListItem", "position": 1, "name": "Blog", "item": abs_url(f"{s['blog_base']}/")},
            {"@type": "ListItem", "position": 2, "name": cat_label(cat, lang),
             "item": abs_url(f"{s['blog_base']}/{cat['slug']}/")},
            {"@type": "ListItem", "position": 3, "name": p["title"], "item": canonical},
        ]
        head += "\n" + jsonld({"@type": "BreadcrumbList", "itemListElement": crumbs})
    return PAGE.format(
        lang=lang, title=f"{html.escape(p['title'])} - Jakub Popluhar",
        description=p["description"] or p["lede"], ogtitle=html.escape(p["title"]),
        ogtype="article", canonical=canonical, ogimage=ogimage,
        head_extra=head, nav=nav_html(s, other_lang_article(lang, p['slug'])),
        content=content, footer=footer_html(s), scripts=COPY_JS,
    )


def other_lang_article(lang, slug):
    return f"{STRINGS['en' if lang=='de' else 'de']['blog_base']}/{slug}/"


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


def write_sitemap(urls):
    body = "\n".join(
        f"  <url><loc>{SITE}{u}</loc></url>" for u in sorted(set(urls))
    )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{body}\n</urlset>\n")
    write(os.path.join(ROOT, "sitemap.xml"), xml)


def write_llms():
    txt = (f"# Jakub Popluhar\n\n"
           f"> Business Lead at Hill Digital & AI trainer. Practical notes on working with AI.\n\n"
           f"- [Blog (DE)]({SITE}/blog/)\n- [Blog (EN)]({SITE}/en/blog/)\n"
           f"- [About]({SITE}/#about)\n")
    write(os.path.join(ROOT, "llms.txt"), txt)


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
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  wrote", os.path.relpath(path, ROOT))


def main():
    include_drafts = "--drafts" in sys.argv
    sitemap_urls = []
    cat_slugs = {c["slug"] for c in CATEGORIES}
    for lang in ("de", "en"):
        s = STRINGS[lang]
        posts = load(lang)
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
            write(os.path.join(out_base, cat["slug"], "index.html"), render_category(lang, cat, in_cat))
            sitemap_urls.append(f"{s['blog_base']}/{cat['slug']}/")
            cats_built += 1
        print(f"[{lang}] {len(listed)} listed, {len(buildable)} built, {cats_built} categor(y/ies)")
        write(os.path.join(out_base, "index.html"), render_index(lang, listed))
        sitemap_urls.append(f"{s['blog_base']}/")
        for p in buildable:
            write(os.path.join(out_base, p["slug"], "index.html"), render_article(lang, p))
            if not p["draft"] and not p["_unlisted"]:
                sitemap_urls.append(f"{s['blog_base']}/{p['slug']}/")

    # site-level GEO files + core pages in the sitemap
    sitemap_urls += ["/", "/en/", "/impressum.html", "/datenschutz.html"]
    write_robots()
    write_sitemap(sitemap_urls)
    write_llms()

    if WARNINGS:
        print("\nLINT WARNINGS:")
        for w in WARNINGS:
            print("  -", w)
    print("\nDone.")


if __name__ == "__main__":
    main()
