---
title: jakubpopluhar.com Homepage Redesign — Luxury Refined
created: 2026-04-12
status: ready to execute
execute_with: "Read ~/Projects/websites/personal/HOMEPAGE-REDESIGN-PLAN.md and execute the full redesign. Use the /frontend-design skill. Read the project CLAUDE.md first."
---

# Homepage Redesign — Luxury Refined

## Context

The jakubpopluhar.com homepage is the personal brand for Jakub's AI training business. It currently works well (dark charcoal + gold, Montserrat + Inter, 9 snap-scroll slides, premium feel) but uses some generic elements — Inter font, standard grid layouts, no depth effects, no cinematic hero. Tuesday's ARS training is an opportunity to show the site. The goal: evolve the current DNA into something that feels like "Apple meets private banking" without losing the existing content or breaking what works.

## Aesthetic Direction: Luxury Refined

- **Colors:** Keep dark charcoal (#141414) + gold (#d4a017) palette but add depth — subtle gradient meshes, noise textures on dark backgrounds, gold used more sparingly and precisely
- **Typography:** Replace Inter (body) with **Outfit** (modern geometric sans with more character). Replace Montserrat (headings) with **Cormorant Garamond** (elegant serif for headings — creates the "private banking" feel). Keep Great Vibes for the accent badge.
- **Hero:** Cinematic — either a Seedance loop video background (if available by then) or a parallax image with depth layers. Larger, more dramatic entrance.
- **Animations:** Staggered fade-in reveals on scroll (IntersectionObserver, already exists — enhance timing). Parallax depth on hero. Gold line animations on section dividers. Subtle hover lifts on cards.
- **Layout:** Keep snap-scroll structure (it works) but add asymmetry — offset stat cards, overlapping elements, diagonal gold accent lines. Break the rigid grid without breaking readability.
- **Stat cards:** Glass-morphic with subtle gold borders, micro-animation on scroll-in (counter ticks up).

## Files to Modify

- **`~/Projects/websites/personal/index.html`** — the entire homepage (all inline CSS + JS + HTML in one 2,431-line file)
- **`~/Projects/websites/personal/fonts/`** — add Cormorant Garamond + Outfit WOFF2 files (self-hosted, GDPR-compliant, no Google Fonts)

## What Changes

### Typography
- Download + self-host: Cormorant Garamond (400, 500, 600, 700) + Outfit (300, 400, 500, 600)
- CSS variables: `--font-heading: 'Cormorant Garamond', serif` / `--font-body: 'Outfit', sans-serif`
- Great Vibes stays for the accent badge
- Increase heading sizes — Cormorant Garamond shines large

### Hero Section
- Full-viewport cinematic background (dark gradient mesh or video-ready container)
- Larger, serif h1 with elegant letter-spacing
- Typewriter effect stays but with refined timing
- Trust bar logos: subtle opacity animation instead of marquee scroll (classier)
- Parallax depth: hero image/content shifts on scroll

### Section Transitions
- Gold horizontal line dividers between sections (animated width on scroll-in)
- Staggered content reveals: heading → subhead → body → cards, 100ms delays
- Subtle parallax on background elements

### Stat Cards / Proof Section
- Glassmorphic: `backdrop-filter: blur(12px)`, semi-transparent dark bg, thin gold border
- Counter animation: numbers tick up from 0 when scrolled into view
- Asymmetric layout: cards slightly offset, not a perfect 3-column grid

### Services / Training Cards
- Subtle hover: lift + gold glow shadow
- Card corners: rounded but with one sharp corner (asymmetric detail)

### Navigation
- Slim down: J·P monogram instead of full logo (feels more luxury)
- Nav dots: refined — smaller, gold outline only, filled on active
- Frosted glass nav bar stays (it works)

### Footer / CTA
- Full-width gold gradient line above
- CTA button: gold fill with dark text, refined border-radius, subtle pulse
- Footer: minimal, editorial — links in a single row, no visual weight

## What Does NOT Change

- Content/copy — all existing German text stays
- Section order — 9 slides, same sequence
- Formspree integration
- Legal pages (impressum, datenschutz)
- Sub-pages (training, weiter, ars140426, community) — untouched
- CNAME / GitHub Pages deploy
- OpenGraph / JSON-LD / SEO meta tags

## Verification

1. Open `index.html` locally in browser — check all 9 slides render correctly
2. Test snap-scroll navigation + dot indicators
3. Test mobile responsive (hamburger nav, grid collapse)
4. Test form submission (Formspree)
5. Verify fonts load (no FOUT/FOIT — use `font-display: swap`)
6. Check `prefers-reduced-motion` still works (animations disabled)
7. Lighthouse performance check (current is fast due to inline CSS — keep it that way)
8. Push to GitHub Pages → verify live at jakubpopluhar.com

## Font Files Needed

Download from Google Fonts (WOFF2 only, self-host):
- Cormorant Garamond: Regular 400, Medium 500, SemiBold 600, Bold 700
- Outfit: Light 300, Regular 400, Medium 500, SemiBold 600

Save to `~/Projects/websites/personal/fonts/` alongside existing Montserrat + Inter + Great Vibes.

## Design References

- Apple.com product pages (cinematic hero, clean transitions)
- Private banking / wealth management sites (Cormorant Garamond + dark bg = trust)
- Current site DNA: the gold accent, the dark mode, the snap-scroll — these are the identity. Don't lose them, elevate them.

## Symmetry Rule

All visual output must be symmetric. Same font sizes, same line counts, same padding across rows/grids. "Das menschliche Gehirn sehnt sich nach Symmetrie." — Commander's standing order.
