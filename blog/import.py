#!/usr/bin/env python3
"""
import.py - turn a finished content-pipeline Markdown into a blog-ready stub.

Reads a file from ~/Projects/content/{articles,posts,drafts}/... , strips the
internal scaffolding that must never be published, and emits a blog post stub
with clean frontmatter for human review. NEVER auto-publishes: the stub is
`draft: true` and lede/description/category are left as placeholders to fill.

Usage:
    python3 blog/import.py <path-to-content.md> [--lang de|en] [--slug SLUG] [--write]

Without --write it prints the stub to stdout (dry run). With --write it saves to
blog/posts/<lang>/<date>-<slug>.md (draft: true).

Stripped: leading "# Title" (-> frontmatter), italic *Created:/Status:/Voice:* line,
[ABOVE THIS LINE ...] hook sentinel, trailing META:/SURF block, "P.S." CTA
paragraph, hashtag-only lines. Flags [INTERN-*] / sensitivity so nothing leaks.

Created: 2026-07-05  ·  see blog/CLAUDE.md (Säule 2)
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def slugify(text):
    text = text.lower()
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        text = text.replace(a, b)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text


def split_frontmatter(raw):
    meta = {}
    body = raw
    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            for line in raw[3:end].strip().splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"').strip("'")
            body = raw[end + 4:].lstrip("\n")
    return meta, body


def clean_body(body):
    notes = []
    lines = body.split("\n")
    out = []
    title = ""
    for line in lines:
        st = line.strip()
        # trailing internal blocks -> stop importing from here
        if re.match(r"^(META:|#{0,3}\s*META\b)", st) or st.startswith("- **Framework:"):
            notes.append("stripped trailing META block")
            break
        if re.match(r"^P\.?S\.?[\s:.]", st):
            notes.append("stripped P.S. CTA")
            break
        # leading H1 -> title
        if not title and st.startswith("# "):
            title = st[2:].strip()
            continue
        # italic metadata / status / voice line
        if re.match(r"^\*.*(Created:|Status:|Voice:|Owner:|Channel:).*\*$", st):
            notes.append("stripped metadata line")
            continue
        # hook sentinel
        if "ABOVE THIS LINE" in st:
            notes.append("stripped hook sentinel")
            continue
        # hashtag-only line
        if st and re.match(r"^(#\w+\s*)+$", st):
            notes.append("stripped hashtags")
            continue
        out.append(line)
    # collapse leading/trailing blank lines
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"
    return title, text, notes


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    opts = [a for a in sys.argv[1:] if a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(1)
    src = args[0]
    lang = "de"
    slug = ""
    for o in opts:
        if o.startswith("--lang"):
            lang = o.split("=")[-1] if "=" in o else "de"
    if "--lang" in opts and opts.index("--lang") + 1 < len(sys.argv):
        pass
    # simple flag parsing for `--lang de` and `--slug x`
    for i, a in enumerate(sys.argv):
        if a == "--lang" and i + 1 < len(sys.argv):
            lang = sys.argv[i + 1]
        if a == "--slug" and i + 1 < len(sys.argv):
            slug = sys.argv[i + 1]
    write = "--write" in sys.argv

    with open(src, encoding="utf-8") as f:
        raw = f.read()

    # sensitivity gate
    sensitive = bool(re.search(r"\[INTERN-|Sensitivity-Reason|NEEDS APPROVAL", raw))

    fm, body = split_frontmatter(raw)
    title, cleaned, notes = clean_body(body)

    base = os.path.splitext(os.path.basename(src))[0]
    m = re.match(r"(\d{4}-\d{2}-\d{2})[-_](.*)", base)
    date = fm.get("date_published") or (m.group(1) if m else "")
    if not slug:
        slug = slugify(title) if title else (m.group(2) if m else base)
    title = title or fm.get("title", slug)

    em_dash = "  ⚠ contains em/en dash, fix before publish" if re.search(r"[–—]", cleaned) else ""

    stub = (
        "---\n"
        f'title: "{title}"\n'
        f"slug: {slug}\n"
        f"date: {date}\n"
        "category:            # aus-der-praxis | jakub-trainings | ki-wissen\n"
        "draft: true\n"
        "description:         # 1-2 sentences, answer-first (GEO)\n"
        "lede:                # standfirst hook\n"
        "hero:\n"
        "caption:\n"
        "---\n\n"
        f"{cleaned}"
    )

    print(f"# source: {src}")
    print(f"# stripped: {', '.join(notes) or 'nothing'}")
    if em_dash:
        print(f"#{em_dash}")
    if sensitive:
        print("# ⚠ SENSITIVITY FLAG found ([INTERN-*]/NEEDS APPROVAL). Do NOT publish "
              "until cleared. Stub kept as draft.")
    print("# TODO fill: category, description, lede, hero(+caption)\n")

    if write:
        out_dir = os.path.join(ROOT, "blog", "posts", lang)
        os.makedirs(out_dir, exist_ok=True)
        fname = f"{date}-{slug}.md" if date else f"{slug}.md"
        out_path = os.path.join(out_dir, fname)
        if os.path.exists(out_path):
            print(f"# refused: {out_path} already exists (review/rename manually)")
            sys.exit(2)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(stub)
        print(f"# wrote {os.path.relpath(out_path, ROOT)} (draft: true)")
    else:
        print(stub)


if __name__ == "__main__":
    main()
