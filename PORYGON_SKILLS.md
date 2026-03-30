# PORYGON SKILLS — Vanilla Web Development Training Manual

> **Who this is for:** Porygon (the website agent) reads this before any website task.
> **What it covers:** Modern CSS, vanilla JS patterns, design systems, reference sites, GitHub resources, performance and SEO.
> **How to use it:** Scan the section headers. Read the sections relevant to your current task. Copy-paste the code patterns directly.

---

## TABLE OF CONTENTS

1. [Modern CSS Techniques](#1-modern-css-techniques)
   - 1.1 Grid + Flexbox Advanced Patterns
   - 1.2 CSS Custom Properties (Design Tokens)
   - 1.3 Fluid Typography (clamp, no media queries)
   - 1.4 CSS Nesting (native)
   - 1.5 Container Queries
   - 1.6 Scroll-Driven Animations
   - 1.7 View Transitions API
   - 1.8 Performant CSS Animations
2. [Vanilla JS Patterns](#2-vanilla-js-patterns)
   - 2.1 Intersection Observer
   - 2.2 Performance: requestAnimationFrame, Debounce, Throttle
   - 2.3 Accessible JS Patterns
   - 2.4 Progressive Enhancement
3. [Design System in Vanilla CSS](#3-design-system-in-vanilla-css)
   - 3.1 Token Architecture for jakubpopluhar.com
   - 3.2 Spacing System
   - 3.3 Color System with Dark Mode
   - 3.4 Component Patterns
4. [Reference Sites — Speakers & Trainers](#4-reference-sites)
5. [GitHub Resources](#5-github-resources)
6. [Performance & SEO](#6-performance--seo)
   - 6.1 Core Web Vitals
   - 6.2 Image Optimization
   - 6.3 Semantic HTML
   - 6.4 JSON-LD Structured Data
7. [jakubpopluhar.com Gap Analysis](#7-jakubpopluharcom-gap-analysis)

---

## 1. MODERN CSS TECHNIQUES

### 1.1 Grid + Flexbox Advanced Patterns

**Rule:** Use Flexbox for 1D layouts (nav bars, button groups, card internals). Use Grid for 2D layouts (page structure, galleries, feature grids).

#### Advanced Flexbox: Equal-height cards with pinned footers
```css
.card-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.card {
  display: flex;
  flex-direction: column;
  flex: 1 1 300px; /* grow, shrink, min-width */
}

.card-body {
  flex: 1; /* pushes footer to bottom */
}

.card-footer {
  margin-top: auto;
}
```

#### CSS Grid: Auto-fill responsive grid (no media queries)
```css
.service-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 2rem;
}
```

#### CSS Subgrid: Align content across nested cards
```css
/* Browser support: 97%+ in 2025 */
.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}

.card {
  display: grid;
  grid-row: span 3; /* each card spans 3 rows */
  grid-template-rows: subgrid; /* inherit parent grid tracks */
}

/* Now heading, body, and CTA align perfectly across all cards */
```

#### Named Grid Areas: Page layout
```css
.page-layout {
  display: grid;
  grid-template-areas:
    "header"
    "main"
    "sidebar"
    "footer";
  grid-template-rows: auto 1fr auto auto;
}

@media (min-width: 900px) {
  .page-layout {
    grid-template-areas:
      "header  header"
      "main    sidebar"
      "footer  footer";
    grid-template-columns: 2fr 1fr;
  }
}

.site-header  { grid-area: header; }
.site-main    { grid-area: main; }
.site-sidebar { grid-area: sidebar; }
.site-footer  { grid-area: footer; }
```

---

### 1.2 CSS Custom Properties (Design Tokens)

**Architecture:** Two layers — primitive tokens (raw values) and semantic tokens (meaningful names). Always use semantic tokens in components. Changing a primitive propagates everywhere.

#### Full token system for jakubpopluhar.com
```css
:root {
  /* ─── PRIMITIVE TOKENS (raw values, never use directly in components) ─── */
  --amber-300: #fbbf24;
  --amber-400: #d4a017;  /* current --gold */
  --amber-500: #b8890f;  /* current --gold-dark */
  --amber-600: #92680a;
  --gray-900: #141414;   /* current --charcoal */
  --gray-850: #1a1a1a;
  --gray-800: #222222;
  --gray-100: #f5f5f5;
  --gray-400: #b0b0b0;

  /* ─── SEMANTIC COLOR TOKENS ─── */
  --color-brand:        var(--amber-400);
  --color-brand-hover:  var(--amber-300);
  --color-brand-dark:   var(--amber-500);
  --color-bg:           var(--gray-900);
  --color-surface:      var(--gray-850);
  --color-surface-alt:  var(--gray-800);
  --color-text:         var(--gray-100);
  --color-text-muted:   var(--gray-400);
  --color-border:       rgba(212, 160, 23, 0.2);

  /* ─── TYPOGRAPHY TOKENS ─── */
  --font-display:  'Great Vibes', cursive;
  --font-heading:  'Montserrat', sans-serif;
  --font-body:     'Inter', sans-serif;

  /* ─── FLUID TYPE SCALE (Perfect Fourth ratio 1.333, no media queries) ─── */
  --text-xs:   clamp(0.75rem,  calc(0.68rem + 0.35vw),  0.875rem);
  --text-sm:   clamp(0.875rem, calc(0.80rem + 0.38vw),  1rem);
  --text-base: clamp(1rem,     calc(0.91rem + 0.45vw),  1.25rem);
  --text-lg:   clamp(1.25rem,  calc(1.13rem + 0.60vw),  1.5rem);
  --text-xl:   clamp(1.5rem,   calc(1.36rem + 0.68vw),  1.875rem);
  --text-2xl:  clamp(1.875rem, calc(1.70rem + 0.88vw),  2.5rem);
  --text-3xl:  clamp(2.5rem,   calc(2.27rem + 1.14vw),  3.5rem);
  --text-4xl:  clamp(3.5rem,   calc(3.18rem + 1.59vw),  5rem);

  /* ─── SPACING TOKENS (8px base grid) ─── */
  --space-1:  0.5rem;   /* 8px */
  --space-2:  1rem;     /* 16px */
  --space-3:  1.5rem;   /* 24px */
  --space-4:  2rem;     /* 32px */
  --space-6:  3rem;     /* 48px */
  --space-8:  4rem;     /* 64px */
  --space-12: 6rem;     /* 96px */
  --space-16: 8rem;     /* 128px */

  /* Fluid spacing (grows with viewport) */
  --space-section: clamp(4rem, 8vw, 8rem);
  --space-component: clamp(2rem, 4vw, 4rem);

  /* ─── BORDER RADIUS ─── */
  --radius-sm:   4px;
  --radius-md:   8px;
  --radius-lg:   16px;
  --radius-full: 9999px;

  /* ─── SHADOWS ─── */
  --shadow-sm:  0 1px 3px rgba(0,0,0,0.4);
  --shadow-md:  0 4px 16px rgba(0,0,0,0.5);
  --shadow-lg:  0 8px 32px rgba(0,0,0,0.6);
  --shadow-gold: 0 0 20px rgba(212, 160, 23, 0.15);

  /* ─── TRANSITIONS ─── */
  --transition-fast:   150ms ease;
  --transition-base:   250ms ease;
  --transition-slow:   400ms ease;
  --transition-spring: 300ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

**Update tokens via JS** (for dynamic theming):
```javascript
document.documentElement.style.setProperty('--color-brand', '#new-color');
```

---

### 1.3 Fluid Typography (clamp, no media queries)

**Formula:** `clamp(MIN, PREFERRED, MAX)` where PREFERRED = `calc(BASE_REM + SLOPE * 1vw)`

**Tools:** Use [utopia.fyi](https://utopia.fyi) or [clampgenerator.com](https://clampgenerator.com) to generate values.

**Modular scale ratios** — choose one and stick to it:
| Ratio | Multiplier | Best for |
|-------|-----------|---------|
| Minor Third | 1.200 | Dense content, small screens |
| Major Third | 1.250 | Balanced, most sites |
| Perfect Fourth | 1.333 | Strong hierarchy, landing pages |
| Golden Ratio | 1.618 | Drama, hero-heavy sites |

**Ready-to-use scale** (Perfect Fourth, 320px → 1280px viewport):
```css
:root {
  --text-sm:   clamp(0.875rem, calc(0.80rem + 0.38vw), 1rem);
  --text-base: clamp(1rem,     calc(0.91rem + 0.45vw), 1.25rem);
  --text-lg:   clamp(1.25rem,  calc(1.13rem + 0.60vw), 1.5rem);
  --text-xl:   clamp(1.5rem,   calc(1.36rem + 0.68vw), 1.875rem);
  --text-2xl:  clamp(1.875rem, calc(1.70rem + 0.88vw), 2.5rem);
  --text-3xl:  clamp(2.5rem,   calc(2.27rem + 1.14vw), 3.5rem);
  --text-4xl:  clamp(3.5rem,   calc(3.18rem + 1.59vw), 5rem);
}

h1 { font-size: var(--text-4xl); }
h2 { font-size: var(--text-3xl); }
h3 { font-size: var(--text-2xl); }
h4 { font-size: var(--text-xl); }
p  { font-size: var(--text-base); }
```

**Line height system:**
```css
:root {
  --leading-tight:   1.1;  /* headings */
  --leading-snug:    1.3;  /* subheadings */
  --leading-normal:  1.6;  /* body copy */
  --leading-relaxed: 1.8;  /* long-form reading */
}
```

---

### 1.4 CSS Nesting (Native)

**Browser support:** Chrome 112+, Firefox 117+, Safari 16.5+ — 95%+ global coverage. Safe to use in production now.

**Key rule:** Always use `&` when building compound selectors or pseudo-classes.

```css
/* Button with states — clean and self-contained */
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: 0.75rem 1.5rem;
  background: var(--color-brand);
  color: var(--color-bg);
  font-family: var(--font-heading);
  font-weight: 600;
  border: 2px solid var(--color-brand);
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all var(--transition-base);

  &:hover {
    background: transparent;
    color: var(--color-brand);
  }

  &:focus-visible {
    outline: 2px solid var(--color-brand);
    outline-offset: 3px;
  }

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  /* Variant: ghost button */
  &.btn--ghost {
    background: transparent;
    color: var(--color-brand);

    &:hover {
      background: var(--color-brand);
      color: var(--color-bg);
    }
  }
}

/* Card with all states nested */
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: var(--space-4);
  transition: transform var(--transition-base), box-shadow var(--transition-base);

  &:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-gold);
  }

  & .card__title {
    font-size: var(--text-xl);
    color: var(--color-brand);
    margin-bottom: var(--space-2);
  }

  & .card__body {
    color: var(--color-text-muted);
    line-height: var(--leading-normal);
  }

  /* Max 3 levels deep — don't nest further */
}
```

---

### 1.5 Container Queries

**When to use:** Any component that appears in different layout contexts (sidebar vs. main, narrow vs. wide). Container queries respond to the component's parent size, not the viewport.

**Browser support:** 90%+ — production ready.

```css
/* Step 1: Declare the container */
.testimonial-wrapper {
  container-type: inline-size;
  container-name: testimonial;
}

/* Step 2: Style the component at container breakpoints */
.testimonial {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

/* When the wrapper is wide enough, go horizontal */
@container testimonial (min-width: 500px) {
  .testimonial {
    flex-direction: row;
    align-items: flex-start;
  }

  .testimonial__avatar {
    flex-shrink: 0;
    width: 80px;
    height: 80px;
  }
}

/* Font scale using container units (cqw) */
.card-heading {
  font-size: clamp(1rem, 4cqw, 1.5rem);
}
```

**Progressive enhancement pattern:**
```css
/* Works without container queries */
.card { padding: 1rem; }

/* Enhanced when supported */
@supports (container-type: inline-size) {
  .card-container { container-type: inline-size; }
  @container (min-width: 400px) {
    .card { padding: 2rem; }
  }
}
```

---

### 1.6 Scroll-Driven Animations

**Browser support (as of 2025):** Chrome/Edge 115+ (stable). Firefox and Safari support is partial — always add the `@supports` fallback. For critical animations, keep the JS Intersection Observer version as fallback.

**Performance rule:** Only animate `transform` and `opacity`. Never animate `height`, `width`, `top`, `left`, or `margin` — these trigger layout recalculations.

#### Fade-in on scroll (element enters viewport)
```css
.reveal {
  opacity: 0;
  transform: translateY(20px);

  /* Fallback: regular animation for non-supporting browsers */
  animation: fade-in 0.6s ease-out forwards;
  animation-play-state: paused; /* pause by default, JS handles it */
}

/* When scroll-driven is supported */
@supports (animation-timeline: view()) {
  .reveal {
    animation-play-state: running; /* CSS handles it, no JS needed */
    animation-timeline: view();
    animation-range: entry 0% entry 60%;
  }
}

@keyframes fade-in {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

#### Reading progress bar (tied to scroll position)
```css
.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 3px;
  background: var(--color-brand);
  transform-origin: left;
  z-index: 999;
}

@supports (animation-timeline: scroll()) {
  .progress-bar {
    animation: grow-bar linear;
    animation-timeline: scroll(root block);
  }

  @keyframes grow-bar {
    from { transform: scaleX(0); }
    to   { transform: scaleX(1); }
  }
}
```

#### Sticky header shrink on scroll
```css
.site-header {
  position: sticky;
  top: 0;
  padding: 1.5rem 2rem;
  transition: padding var(--transition-base), box-shadow var(--transition-base);
}

@supports (animation-timeline: scroll()) {
  .site-header {
    animation: shrink-header linear both;
    animation-timeline: scroll(root);
    animation-range: 0px 100px;
  }

  @keyframes shrink-header {
    to {
      padding: 0.75rem 2rem;
      box-shadow: 0 2px 20px rgba(0,0,0,0.5);
    }
  }
}
```

#### Staggered card reveals
```css
.card { animation-timeline: view(); animation-range: entry; }
.card:nth-child(1) { animation-delay: 0ms; }
.card:nth-child(2) { animation-delay: 100ms; }
.card:nth-child(3) { animation-delay: 200ms; }
```

---

### 1.7 View Transitions API

**What it does:** Animates DOM state changes — navigation between pages, tab switching, content updates. Makes a static site feel like an SPA.

**Browser support:** Chrome/Edge 111+. Use as progressive enhancement only.

```javascript
// Wrap any DOM update in startViewTransition
document.startViewTransition(() => {
  // whatever causes the DOM change
  document.querySelector('#content').innerHTML = newContent;
});
```

```css
/* Customize the transition */
::view-transition-old(root) {
  animation: fade-out 0.3s ease-in;
}
::view-transition-new(root) {
  animation: fade-in 0.3s ease-out;
}

/* Named transition for specific element (e.g., hero image) */
.hero-image {
  view-transition-name: hero;
}
::view-transition-old(hero) {
  animation: slide-out-left 0.4s ease-in;
}
::view-transition-new(hero) {
  animation: slide-in-right 0.4s ease-out;
}

@keyframes fade-out { to { opacity: 0; } }
@keyframes fade-in  { from { opacity: 0; } }
```

---

### 1.8 Performant CSS Animations

**Golden rules:**
1. Only animate `transform` and `opacity` — these run on the GPU compositor thread
2. Use `will-change: transform` sparingly (only right before animation, remove after)
3. Respect `prefers-reduced-motion`
4. Use `cubic-bezier` easing for personality

```css
/* Always include this globally */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

/* Easing presets with personality */
:root {
  --ease-out-expo:   cubic-bezier(0.16, 1, 0.3, 1);
  --ease-spring:     cubic-bezier(0.34, 1.56, 0.64, 1); /* slight bounce */
  --ease-in-out-quart: cubic-bezier(0.76, 0, 0.24, 1);
}

/* Entrance animation pattern */
.animate-in {
  animation: slide-up var(--transition-slow) var(--ease-out-expo) both;
}

@keyframes slide-up {
  from {
    opacity: 0;
    transform: translateY(24px);
  }
}

/* Hover micro-interaction: scale on image */
.card-image {
  overflow: hidden; /* clip the scaled image */
}
.card-image img {
  transition: transform 0.4s var(--ease-out-expo);
}
.card-image:hover img {
  transform: scale(1.05);
}
```

---

## 2. VANILLA JS PATTERNS

### 2.1 Intersection Observer

**Use instead of scroll events.** IntersectionObserver runs asynchronously — one observer watching hundreds of elements is cheaper than any scroll listener.

#### Lazy-reveal animation (replaces AOS library)
```javascript
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
      revealObserver.unobserve(entry.target); // stop watching once revealed
    }
  });
}, {
  threshold: 0.1,      // 10% of element visible triggers callback
  rootMargin: '0px 0px -50px 0px' // trigger 50px before element hits viewport
});

// Observe all elements with data-reveal attribute
document.querySelectorAll('[data-reveal]').forEach(el => {
  revealObserver.observe(el);
});
```

```css
[data-reveal] {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s var(--ease-out-expo), transform 0.6s var(--ease-out-expo);
}
[data-reveal].is-visible {
  opacity: 1;
  transform: translateY(0);
}
/* Staggered children */
[data-reveal].is-visible [data-reveal-delay="1"] { transition-delay: 100ms; }
[data-reveal].is-visible [data-reveal-delay="2"] { transition-delay: 200ms; }
[data-reveal].is-visible [data-reveal-delay="3"] { transition-delay: 300ms; }
```

#### Lazy loading images (with IntersectionObserver fallback)
```html
<img data-src="photo.webp" src="placeholder.svg" loading="lazy" alt="...">
```

```javascript
// Use native loading="lazy" — it's supported everywhere now.
// Only use IO as enhancement for preloading next batch:
const lazyObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      if (img.dataset.src) {
        img.src = img.dataset.src;
        img.removeAttribute('data-src');
        lazyObserver.unobserve(img);
      }
    }
  });
}, { rootMargin: '200px' }); // preload 200px before entering viewport
```

#### Active nav highlight (which section is in view)
```javascript
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('nav a[href^="#"]');

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(link => {
        link.classList.toggle(
          'is-active',
          link.getAttribute('href') === `#${entry.target.id}`
        );
      });
    }
  });
}, { threshold: 0.5 });

sections.forEach(section => sectionObserver.observe(section));
```

---

### 2.2 Performance: requestAnimationFrame, Debounce, Throttle

**Rule of thumb:**
- `requestAnimationFrame` — for anything that animates or repaints (scroll parallax, progress bars)
- `debounce` — for events that fire rapidly but you only care about the last one (resize, search input)
- `throttle` — for events where you want periodic updates (scroll position reading)

#### requestAnimationFrame scroll handler
```javascript
let ticking = false;

window.addEventListener('scroll', () => {
  if (!ticking) {
    requestAnimationFrame(() => {
      // do scroll-based work here
      updateScrollProgress();
      ticking = false;
    });
    ticking = true;
  }
});

function updateScrollProgress() {
  const scrolled = window.scrollY;
  const total = document.body.scrollHeight - window.innerHeight;
  const progress = scrolled / total;
  document.querySelector('.progress-bar').style.transform = `scaleX(${progress})`;
}
```

#### Debounce (wait for user to stop)
```javascript
function debounce(fn, delay = 250) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

// Usage: resize handler
window.addEventListener('resize', debounce(() => {
  recalculateLayout();
}, 300));
```

#### Throttle (limit to once per interval)
```javascript
function throttle(fn, interval = 100) {
  let lastCall = 0;
  return (...args) => {
    const now = Date.now();
    if (now - lastCall >= interval) {
      lastCall = now;
      fn(...args);
    }
  };
}

// Usage: scroll tracking
window.addEventListener('scroll', throttle(() => {
  updateActiveNavItem();
}, 100));
```

---

### 2.3 Accessible JS Patterns

**Core principle:** Native HTML elements (button, a, input) are keyboard-friendly by default. Use them. Only add JS when you need custom behavior.

#### Focus trap for modals
```javascript
function trapFocus(element) {
  const focusableSelectors = [
    'a[href]', 'button:not([disabled])', 'input:not([disabled])',
    'select:not([disabled])', 'textarea:not([disabled])',
    '[tabindex]:not([tabindex="-1"])'
  ].join(', ');

  const focusableElements = element.querySelectorAll(focusableSelectors);
  const firstEl = focusableElements[0];
  const lastEl = focusableElements[focusableElements.length - 1];

  element.addEventListener('keydown', (e) => {
    if (e.key !== 'Tab') return;

    if (e.shiftKey) {
      if (document.activeElement === firstEl) {
        e.preventDefault();
        lastEl.focus();
      }
    } else {
      if (document.activeElement === lastEl) {
        e.preventDefault();
        firstEl.focus();
      }
    }
  });
}
```

#### Accessible modal
```javascript
class Modal {
  constructor(trigger, dialog) {
    this.trigger = trigger;
    this.dialog = dialog;
    this.previousFocus = null;

    trigger.addEventListener('click', () => this.open());
    dialog.querySelector('[data-close]').addEventListener('click', () => this.close());
    dialog.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') this.close();
    });
  }

  open() {
    this.previousFocus = document.activeElement;
    this.dialog.showModal(); // native <dialog> handles ARIA automatically
    this.dialog.querySelector('[data-autofocus]')?.focus();
    trapFocus(this.dialog);
  }

  close() {
    this.dialog.close();
    this.previousFocus?.focus(); // return focus to trigger
  }
}
```

```html
<!-- Use native <dialog> — gets ARIA for free -->
<dialog id="contact-modal" aria-labelledby="modal-title">
  <h2 id="modal-title">Kontakt aufnehmen</h2>
  <button data-close aria-label="Schließen">×</button>
  <form>...</form>
</dialog>
```

#### Keyboard navigation for custom components
```javascript
// Roving tabindex pattern for tab panels / accordion
function initRovingTabindex(container) {
  const items = container.querySelectorAll('[role="tab"]');

  items.forEach((item, index) => {
    item.setAttribute('tabindex', index === 0 ? '0' : '-1');

    item.addEventListener('keydown', (e) => {
      let newIndex;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
        newIndex = (index + 1) % items.length;
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        newIndex = (index - 1 + items.length) % items.length;
      } else if (e.key === 'Home') {
        newIndex = 0;
      } else if (e.key === 'End') {
        newIndex = items.length - 1;
      }
      if (newIndex !== undefined) {
        items.forEach(i => i.setAttribute('tabindex', '-1'));
        items[newIndex].setAttribute('tabindex', '0');
        items[newIndex].focus();
      }
    });
  });
}
```

---

### 2.4 Progressive Enhancement

**Principle:** Build the core HTML first. It works without CSS or JS. Layer CSS for presentation. Layer JS for enhancement. Never gate core content behind JS.

```html
<!-- Progressive disclosure without JS -->
<details>
  <summary>Häufige Fragen: Wie läuft ein Training ab?</summary>
  <p>Wir starten mit einer Bedarfsanalyse...</p>
</details>

<!-- With JS enhancement: smooth animation -->
```

```javascript
// Enhance <details> with animation if JS available
document.querySelectorAll('details').forEach(details => {
  const content = details.querySelector('summary + *');
  details.addEventListener('toggle', () => {
    content.style.height = details.open ? `${content.scrollHeight}px` : '0';
  });
});
```

---

## 3. DESIGN SYSTEM IN VANILLA CSS

### 3.1 Token Architecture for jakubpopluhar.com

The site already uses CSS variables but lacks the two-layer system. Upgrade path:

**Current state:**
```css
/* One flat layer — fragile */
--gold: #d4a017;
--charcoal: #141414;
```

**Target state (two layers):** See full token system in Section 1.2 above.

**Naming convention for all new tokens:** `--[category]-[variant]-[state]`

Examples:
- `--color-brand` (semantic)
- `--color-brand-hover` (semantic + state)
- `--space-section` (semantic spacing)
- `--amber-400` (primitive, never used directly in components)

---

### 3.2 Spacing System

**Base:** 8px grid. All spacing values are multiples of 8.

```css
/* The complete spacing scale */
--space-1:  0.5rem;   /* 8px  — icon gaps, tight padding */
--space-2:  1rem;     /* 16px — base padding */
--space-3:  1.5rem;   /* 24px — card padding */
--space-4:  2rem;     /* 32px — section internal padding */
--space-6:  3rem;     /* 48px — large component separation */
--space-8:  4rem;     /* 64px — between sections */
--space-12: 6rem;     /* 96px — major section gaps */
--space-16: 8rem;     /* 128px — hero breathing room */

/* Fluid section spacing — the most useful addition */
--space-section:    clamp(4rem, 8vw, 8rem);
--space-component:  clamp(2rem, 4vw, 4rem);
```

**Usage rule:** Use `--space-section` for padding between full-width sections. Use `--space-component` for internal component padding. Use fixed values (1-4) for micro-spacing within components.

---

### 3.3 Color System with Light/Dark Mode

The current site is dark-only. When a light mode becomes relevant:

```css
:root {
  /* Dark mode (default — matches current site) */
  --color-bg:         #141414;
  --color-surface:    #1a1a1a;
  --color-text:       #f5f5f5;
  --color-text-muted: #b0b0b0;
  --color-brand:      #d4a017;
}

/* Light mode — activated by user preference OR data-theme attribute */
@media (prefers-color-scheme: light) {
  :root:not([data-theme="dark"]) {
    --color-bg:         #f8f5f0;
    --color-surface:    #ffffff;
    --color-text:       #1a1a1a;
    --color-text-muted: #6b6b6b;
    --color-brand:      #b8890f; /* slightly darker gold on light bg */
  }
}

/* Manual override (toggle button) */
[data-theme="light"] {
  --color-bg:         #f8f5f0;
  --color-surface:    #ffffff;
  --color-text:       #1a1a1a;
  --color-text-muted: #6b6b6b;
  --color-brand:      #b8890f;
}
```

```javascript
// Theme toggle
const toggle = document.querySelector('[data-theme-toggle]');
toggle.addEventListener('click', () => {
  const current = document.documentElement.getAttribute('data-theme');
  document.documentElement.setAttribute('data-theme', current === 'light' ? 'dark' : 'light');
  localStorage.setItem('theme', current === 'light' ? 'dark' : 'light');
});

// Restore saved preference
const saved = localStorage.getItem('theme');
if (saved) document.documentElement.setAttribute('data-theme', saved);
```

---

### 3.4 Component Patterns

#### Testimonial card (production-ready)
```html
<div class="testimonial-grid">
  <article class="testimonial" itemscope itemtype="https://schema.org/Review">
    <blockquote itemprop="reviewBody">
      "Jakub hat unser Team in 2 Stunden zu echten KI-Nutzern gemacht."
    </blockquote>
    <footer class="testimonial__author">
      <img src="photo.webp" alt="Katarzyna Pichler" width="48" height="48" loading="lazy">
      <div>
        <cite itemprop="author">Katarzyna Pichler</cite>
        <span>Innovatic Group</span>
      </div>
    </footer>
  </article>
</div>
```

```css
.testimonial-grid {
  container-type: inline-size;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: var(--space-4);
}

.testimonial {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-left: 3px solid var(--color-brand);
  border-radius: var(--radius-md);
  padding: var(--space-4);

  & blockquote {
    font-size: var(--text-lg);
    line-height: var(--leading-normal);
    color: var(--color-text);
    margin: 0 0 var(--space-3);
    font-style: italic;

    &::before { content: '"'; color: var(--color-brand); font-size: 2em; }
  }

  & .testimonial__author {
    display: flex;
    align-items: center;
    gap: var(--space-2);

    & img {
      width: 48px;
      height: 48px;
      border-radius: var(--radius-full);
      object-fit: cover;
      border: 2px solid var(--color-brand);
    }

    & cite { font-style: normal; font-weight: 600; }
    & span { font-size: var(--text-sm); color: var(--color-text-muted); }
  }
}
```

#### Gold accent divider
```css
.section-divider {
  width: 60px;
  height: 3px;
  background: var(--color-brand);
  margin: var(--space-3) auto;
  border: none;
}
```

#### Trust logo marquee (improvement over current implementation)
```css
.trust-bar {
  --marquee-duration: 30s;
  overflow: hidden;
  mask-image: linear-gradient(to right, transparent 0%, black 10%, black 90%, transparent 100%);
}

.trust-bar__track {
  display: flex;
  gap: var(--space-8);
  width: max-content;
  animation: marquee var(--marquee-duration) linear infinite;
}

/* Pause on hover — better UX */
.trust-bar:hover .trust-bar__track {
  animation-play-state: paused;
}

@keyframes marquee {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}
```

---

## 4. REFERENCE SITES

Analyzed for design lessons applicable to jakubpopluhar.com. All sites are for AI/tech speakers and trainers positioning at the premium end.

### Zack Kass — zackkass.com
**Positioning:** Former OpenAI Head of GTM, AI keynote speaker, author

**Design:**
- Color: Deep navy (#001A2A), orange-red CTA (#FF4411)
- Scroll-reveal hero that collapses to a 64px sticky header on scroll
- Client logos (Coca-Cola, Microsoft, Morgan Stanley) in the first viewport
- Auto-rotating testimonial carousel (4-second interval)
- Book jacket as visual credibility anchor

**Lessons for jakubpopluhar.com:**
1. Lead with logos — client brand recognition builds trust faster than copy
2. The "USA Bestseller" badge equivalent is any external validation (TU Wien, ARS Akademie logos)
3. Collapsing hero to sticky header is a pattern worth implementing (scroll-driven animation)
4. Dark + one vivid accent (their red, our gold) = premium signal

---

### Steven Bartlett — stevenbartlett.com
**Positioning:** Entrepreneur, author, Dragon's Den, Diary of a CEO host

**Design:**
- Neon yellow-green (#CDFF57) against black — extreme contrast, Gen Z energy
- Magazine-style layout: asymmetric grid, large pull quotes, full-bleed images
- Video-first: Diary of a CEO clips dominate above the fold
- Podcast as primary CTA — content fuels the funnel

**Lessons for jakubpopluhar.com:**
1. One vivid accent on black = strong brand recognition (their neon green, our gold — already doing this)
2. Asymmetric grid breaks the "AI consultant template" feel — consider for Services section
3. Video content (even speaking clips) dramatically increases time-on-page and trust

---

### Simon Sinek — simonsinek.com
**Positioning:** Author of "Start with Why," leadership speaker

**Design:**
- Orange + purple against generous white space — bold but academic
- Hand-drawn icons and playful layout signal approachability
- "Start Here" page — explicit onboarding for new visitors
- Newsletter as primary email capture (not "book a call" first)

**Lessons for jakubpopluhar.com:**
1. A "Start Here" page beats a generic About page — guides new visitors to the right offer
2. Newsletter as first step lowers friction vs. "book a call" (better for cold traffic)
3. Playful visual elements (icons, illustrations) humanize a serious expert brand

---

### Gary Vaynerchuk — garyvee.com
**Design:**
- Black, white, primary colors — intentionally "loud" and energetic
- Social media feed integration as hero content — constant freshness
- Content volume signals — "I publish every day" = authority
- Multiple CTAs for different audience segments (entrepreneurs vs. corporations)

**Lessons for jakubpopluhar.com:**
1. Content volume on the landing page signals active expertise — a "recent LinkedIn post" section would work
2. Segment CTAs by audience — "Für Unternehmen" vs. "Für Einzelpersonen"

---

### Design Patterns Across All Top Sites

| Pattern | Why it works | How to implement |
|---------|-------------|-----------------|
| Client logos in first viewport | Borrowed authority — instant trust | Marquee above the fold, actual partner logos |
| Video/speaking clip | Proves speaking ability — words on page can't | Embedded YouTube clip or autoplay muted video |
| Social proof at every scroll stop | Prevents bounce at each decision point | Weave testimonials between service sections |
| Single vivid accent color on dark | Memorable, premium, focused | Already done — maintain gold consistently |
| Mobile-first snap scroll | Mirrors native app experience | Already done — maintain |
| "Book a call" as final CTA | Clear single next step | Needs Calendly integration |
| Collapsing header on scroll | Shows technical sophistication | Implement with scroll-driven animation |

---

## 5. GITHUB RESOURCES

### CSS Libraries (no-JS, production ready)

**[Vanilla CSS Design System](https://github.com/pattespatte/vanilla-css-design-system)**
Pure vanilla CSS. No SCSS, no JavaScript. Includes design tokens, CSS variables, component patterns. Bidirectional token conversion (CSS ↔ JSON). Good reference for token architecture patterns.

**[Vanilla Framework](https://vanillaframework.io/) (by Canonical)**
CSS grid, base element styles, utility classes. LGPL licensed. Not a copy-paste library but good reference for component pattern names and organization.

**[Accessible Components](https://github.com/scottaohara/accessible_components)** — use for accessible patterns
12 patterns including modals, accordions, tabs, tooltips, switches. Each includes proper ARIA markup. The accordion and modal patterns are directly applicable to jakubpopluhar.com's FAQ and contact sections.

**[Awesome CSS Frameworks](https://github.com/troxler/awesome-css-frameworks)**
Curated list. Use to find alternatives when a specific component type is needed.

### JS Animation Libraries (lightweight, no jQuery)

**[Anime.js](https://animejs.com/)** — 4.3kb gzipped
Most popular lightweight GSAP alternative. Works with HTML elements, CSS properties, SVG, and JS objects. Syntax: `anime({ targets: '.card', opacity: [0, 1], translateY: [20, 0], delay: anime.stagger(100) })`. Good for staggered entrance animations.

**[Motion (formerly Framer Motion for vanilla JS)](https://motion.dev/)**
Built on Web Animations API (WAAPI). 16M+ downloads/month. Works with vanilla JS (not just React). More performant than Anime.js because it runs on WAAPI directly. Growing faster than any alternative.

**[Vivus.js](https://maxwellito.github.io/vivus/)** — SVG path drawing animations. Zero dependencies. Good for logo animations or decorative SVG elements.

**Recommendation for jakubpopluhar.com:** Use CSS animations + Intersection Observer as primary approach (no extra dependency). If complex timeline animations are needed (e.g., a multi-step product demo), reach for Motion (vanilla JS version) — better performance than Anime.js, growing ecosystem.

### Claude Code Skills for Web Quality

**[web-quality-skills](https://github.com/addyosmani/web-quality-skills)** by Addy Osmani (Google Chrome team)
Installs 6 Claude Code skills: `web-quality-audit`, `performance`, `core-web-vitals`, `accessibility`, `seo`, `best-practices`. Covers 50+ performance patterns, 40+ accessibility rules, WCAG 2.2. Run before any significant website push.

Install: `npx add-skill addyosmani/web-quality-skills`

---

## 6. PERFORMANCE & SEO

### 6.1 Core Web Vitals (2025 targets)

Google's ranking signals. These matter for jakubpopluhar.com on GitHub Pages.

| Metric | Target | What it is |
|--------|--------|-----------|
| LCP (Largest Contentful Paint) | ≤ 2.5s | How fast the main content loads |
| INP (Interaction to Next Paint) | ≤ 200ms | How fast the page responds to clicks |
| CLS (Cumulative Layout Shift) | ≤ 0.1 | How stable the layout is while loading |

**LCP quick wins for GitHub Pages:**
```html
<!-- Preload the hero image — biggest LCP impact -->
<link rel="preload" as="image" href="/images/hero.avif" fetchpriority="high">

<!-- Never lazy-load above-the-fold images -->
<img src="hero.avif" loading="eager" fetchpriority="high" alt="Jakub Popluhar">
```

**CLS prevention:**
```css
/* Always set explicit dimensions on images */
img {
  width: 100%;
  height: auto;
  aspect-ratio: 16/9; /* prevents layout shift while loading */
}

/* Reserve space for fonts to prevent FOUT/FOUT */
@font-face {
  font-family: 'Montserrat';
  font-display: swap; /* show fallback immediately, swap when loaded */
}
```

**INP improvement:**
- Move all non-critical JS to `defer` or `type="module"`
- Break up long tasks with `setTimeout(fn, 0)` to yield to the browser
- Don't block interactions with heavy scroll handlers (use requestAnimationFrame)

---

### 6.2 Image Optimization

**Format priority:** AVIF first (smallest), WebP fallback, JPEG/PNG last.
**Tool:** Use `cwebp` (WebP) or `avifenc` (AVIF) for conversion. Or Squoosh.app for manual.

#### The complete pattern
```html
<!-- Hero image: AVIF + WebP + JPEG fallback, preloaded, eager, no lazy -->
<link rel="preload" as="image" href="/images/hero.avif" fetchpriority="high">
<picture>
  <source srcset="/images/hero.avif" type="image/avif">
  <source srcset="/images/hero.webp" type="image/webp">
  <img src="/images/hero.jpg"
       alt="Jakub Popluhar — KI-Trainer & Konsumentenpsychologe"
       width="1200" height="800"
       loading="eager"
       fetchpriority="high">
</picture>

<!-- Below-fold images: lazy loaded -->
<picture>
  <source srcset="/images/photo-400.avif 400w, /images/photo-800.avif 800w" type="image/avif">
  <source srcset="/images/photo-400.webp 400w, /images/photo-800.webp 800w" type="image/webp">
  <img src="/images/photo-800.jpg"
       srcset="/images/photo-400.jpg 400w, /images/photo-800.jpg 800w"
       sizes="(max-width: 600px) 100vw, 50vw"
       alt="Description"
       width="800" height="600"
       loading="lazy">
</picture>
```

**Quality settings:**
- AVIF: 50-60% quality (lossy) — still looks excellent
- WebP: 70-85% quality
- JPEG: 80-85% quality for photos, 90% for text-heavy images

**CSS aspect-ratio trick (prevent CLS):**
```css
.image-wrapper {
  aspect-ratio: 4/3;
  overflow: hidden;
}
.image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

---

### 6.3 Semantic HTML

Semantic HTML improves SEO, accessibility, and Core Web Vitals (by reducing JS needed to patch non-semantic elements).

```html
<!-- Page structure -->
<header role="banner">
  <nav aria-label="Hauptnavigation">
    <ul>
      <li><a href="#ueber-mich">Über mich</a></li>
      <li><a href="#angebote">Angebote</a></li>
      <li><a href="#kontakt">Kontakt</a></li>
    </ul>
  </nav>
</header>

<main id="main-content">
  <section aria-labelledby="hero-heading">
    <h1 id="hero-heading">KI-Trainer & Konsumentenpsychologe</h1>
  </section>

  <section aria-labelledby="about-heading">
    <h2 id="about-heading">Über mich</h2>
  </section>

  <section aria-labelledby="services-heading">
    <h2 id="services-heading">Angebote</h2>
    <ul>
      <li>
        <article>
          <h3>KI-Training für Teams</h3>
          <p>...</p>
        </article>
      </li>
    </ul>
  </section>
</main>

<footer role="contentinfo">
  <address>
    <a href="mailto:jakub@popluhar.at">jakub@popluhar.at</a>
  </address>
</footer>
```

**Skip link (required for keyboard accessibility):**
```html
<a href="#main-content" class="skip-link">Zum Hauptinhalt springen</a>
```

```css
.skip-link {
  position: absolute;
  top: -100%;
  left: 1rem;
  padding: 0.5rem 1rem;
  background: var(--color-brand);
  color: var(--color-bg);
  z-index: 9999;
  border-radius: var(--radius-sm);
}
.skip-link:focus { top: 1rem; }
```

---

### 6.4 JSON-LD Structured Data

Add to `<head>` of index.html. This feeds Google's Knowledge Panel and improves search appearance.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Jakub Popluhar",
  "honorificPrefix": "M.Ed.",
  "url": "https://jakubpopluhar.com",
  "image": "https://jakubpopluhar.com/images/jakub-popluhar.jpg",
  "jobTitle": "KI-Trainer & Konsumentenpsychologe",
  "description": "M.Ed. Jakub Popluhar ist KI-Trainer und Konsumentenpsychologe. Er hilft Führungskräften und Teams im DACH-Raum, KI praktisch und nachhaltig einzusetzen.",
  "email": "jakub@popluhar.at",
  "url": "https://jakubpopluhar.com",
  "sameAs": [
    "https://www.linkedin.com/in/jakub-popluhar/",
    "https://www.instagram.com/jakub.popluhar/"
  ],
  "worksFor": {
    "@type": "Organization",
    "name": "became ai",
    "url": "https://became.ai"
  },
  "knowsAbout": [
    "Künstliche Intelligenz",
    "KI-Adoption",
    "Konsumentenpsychologie",
    "KI-Training",
    "Generative AI",
    "Change Management"
  ],
  "knowsLanguage": ["de", "sk", "en"],
  "address": {
    "@type": "PostalAddress",
    "addressCountry": "AT",
    "addressLocality": "Wien"
  },
  "alumniOf": {
    "@type": "EducationalOrganization",
    "name": "Universität Wien"
  },
  "offers": {
    "@type": "Service",
    "name": "KI-Training & Workshops",
    "provider": {
      "@type": "Person",
      "name": "Jakub Popluhar"
    },
    "areaServed": {
      "@type": "GeoCircle",
      "description": "DACH-Region (Deutschland, Österreich, Schweiz)"
    }
  }
}
</script>
```

**Validate at:** [Google Rich Results Test](https://search.google.com/test/rich-results)

---

## 7. JAKUBPOPLUHAR.COM GAP ANALYSIS

Current state vs. what the top speaker/trainer sites do. Prioritized by impact.

### HIGH IMPACT GAPS

| Gap | Current state | Target state | Effort |
|-----|--------------|--------------|--------|
| Booking integration | All CTAs link to `#` | Calendly or Cal.com embedded | Medium |
| Hero image preload | Not preloaded | `<link rel="preload">` + `fetchpriority="high"` | Low |
| Fluid typography | Static px/rem values | CSS clamp() on all type | Low |
| JSON-LD structured data | None | Person schema in `<head>` | Low |
| Skip link | None | `<a href="#main-content">` | Low |

### MEDIUM IMPACT GAPS

| Gap | Current state | Target state | Effort |
|-----|--------------|--------------|--------|
| Scroll-driven header shrink | Static header | Collapses to 64px on scroll | Medium |
| Design token architecture | Flat CSS variables | Two-layer primitive + semantic | Medium |
| Image formats | Unknown (check current images) | AVIF + WebP + fallback | Medium |
| `font-display: swap` | Unknown | Set on all `@font-face` | Low |
| Container queries on cards | None | Testimonial cards adapt to container | Medium |

### LOW IMPACT / FUTURE GAPS

| Gap | Current state | Target state | Effort |
|-----|--------------|--------------|--------|
| Video / speaking clip | None | Embedded speaking reel | High (content needed) |
| Light/dark mode toggle | Dark-only | Optional light mode | High |
| View transitions | None | Between page states | Medium |
| Progress bar | None | Reading progress indicator | Low |
| Web Components | None | Testimonial card as custom element | High |

### QUICK WINS (do these in any single session)

1. Add `<link rel="preload">` for the hero image — 5 minute fix, big LCP improvement
2. Add JSON-LD Person schema to `<head>` — 10 minute fix, SEO benefit
3. Add skip link for keyboard accessibility — 10 minute fix
4. Add `font-display: swap` to Google Fonts — 2 minute fix, prevents FOUT
5. Set explicit `width` and `height` on all `<img>` tags — prevents CLS

---

## APPENDIX: TOOL REFERENCE

| Task | Tool | Notes |
|------|------|-------|
| Generate fluid type scale | [utopia.fyi](https://utopia.fyi) | Enter min/max viewport + font sizes |
| Generate clamp() values | [clampgenerator.com](https://clampgenerator.com) | Simpler than Utopia for single values |
| Convert images to WebP | `cwebp input.jpg -q 80 -o output.webp` | Install via Homebrew |
| Convert images to AVIF | [Squoosh.app](https://squoosh.app) | Browser-based, no install |
| Validate JSON-LD | [Rich Results Test](https://search.google.com/test/rich-results) | Google's official tool |
| Check browser support | [caniuse.com](https://caniuse.com) | Before using any new CSS feature |
| Lighthouse audit | Chrome DevTools → Lighthouse | Run before every push |
| CSS easing visualizer | [cubic-bezier.com](https://cubic-bezier.com) | Preview custom easing curves |
| Modular scale calculator | [type-scale.com](https://type-scale.com) | Pick ratio, get all step values |
| Web quality Claude skill | `npx add-skill addyosmani/web-quality-skills` | 6 audit skills for Porygon |

---

*Last updated: 2026-03-22. Research conducted by the researcher agent. Next update when: CSS scroll-driven animations reach >80% browser support including Firefox, or when major design system changes are made to index.html.*
