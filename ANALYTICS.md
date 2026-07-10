# Analytics — jakubpopluhar.com

Created: 2026-07-10
Last updated: 2026-07-10 (first-party beacon migration done)

How visitor tracking on this site works, what is verified, and the known blind spot.
All tracking logic lives in **one file**: `assets/js/site.js` (loaded by every page — homepage, all blog articles, EN mirror, training pages). Edit there, not per-page.

---

## The two layers

| Layer | Tool | Needs consent? | What you get | Where the data lives |
|---|---|---|---|---|
| 1 | Cookieless beacon | No | Pageviews: which page, referrer, count | VPS nginx log `/var/log/nginx/beacon.log` (rotated daily) |
| 2 | Microsoft Clarity | **Yes** | Heatmaps, session recordings, rage-clicks, scroll depth, conversion events | Clarity dashboard (project ID `xk7y1dwu8h`) |

### Layer 1 — cookieless beacon (FIRST-PARTY as of 2026-07-10)
On every page load `site.js` fires a 1x1 image request to
`https://stats.jakubpopluhar.com/px?site=jakubpopluhar&path=...&ref=...`.
`stats.jakubpopluhar.com` is a subdomain of the site's own domain → **first-party** (same registrable domain), so Safari ITP / Firefox / iOS do NOT treat it as third-party. Neutral path `/px` (not `t.gif`) dodges ad-blocker filename patterns. Served by nginx on the VPS as a static GIF (`return 200`), logged in the same `beacon` log format → same archive → same HD dashboard. No cookies, no consent needed. Runs BEFORE and independently of the consent banner.

**Previous (blocked) endpoint:** `https://deflifeos.popluhar.at/t.gif?...` — a DIFFERENT domain = third-party = blocked by ITP/blockers. Replaced 2026-07-10.

### Layer 2 — Microsoft Clarity (consent-gated)
Clarity sets cookies and records behaviour, so under DSGVO it needs consent. `site.js` only injects the Clarity tag (`https://www.clarity.ms/tag/xk7y1dwu8h`) **after the visitor clicks "Zustimmen"** in the consent banner. The choice is stored in `localStorage` as `jp_consent_stats` = `yes` / `no`.
- `yes` on a later visit → Clarity loads automatically, no banner.
- `no` → nothing loads, banner does not reappear.
- Layer 3 in `site.js` fires Clarity **custom conversion events** (form submits, booking-link clicks, mailto/tel) — only when Clarity is loaded, i.e. only for consenting visitors.

---

## Status — VERIFIED 2026-07-10

- Clarity snippet + ID `xk7y1dwu8h` is deployed, live (HTTP 200), and loaded on every page. **Correct and working.**
- Live browser test: fresh visit → banner shows, Clarity NOT loaded (correct gate). Click "Zustimmen" → `window.clarity` becomes a live function, real network call to `clarity.ms/tag/xk7y1dwu8h` returns 204 (Clarity's normal success). Reload as consented visitor → Clarity auto-loads. **End-to-end confirmed.**

Clarity is done. Nothing to fix there. First data can take up to ~2 hours to appear in the dashboard.

---

## KNOWN BLIND SPOT — the beacon is being blocked (important)

**"What if people don't accept Clarity?"** → The cookieless beacon is supposed to still count them. But it does NOT count everyone.

Diagnosed live on 2026-07-10:
- Real browser visits (test browsers used by Jakub, plus the automation browser) fired the beacon, but the requests **never reached the server** — they are absent from `beacon.log`. The browser saw synthetic `503` / `204` responses.
- The **same request sent server-side via curl returns 200 and logs correctly.** The beacon works fine for non-blocking clients (other sites log ~20+ hits/day).

**Root cause (fact):** the requests are intercepted between browser and server — browser tracking-protection and ad blockers. The beacon is a cross-domain pixel named `t.gif` with `?site=&path=&ref=` params — the textbook signature that Safari ITP, Firefox/Brave tracking protection, and ad blockers (uBlock etc.) block.

**Consequence:** Layer 1 only records visitors whose browser is NOT blocking (observed in logs: Windows Edge, Android Samsung Browser). Safari / iPhone / privacy-browser / ad-blocker users are missed in **both** layers. **The beacon undercounts, possibly by a lot.** Do not treat its numbers as total traffic.

Correction to an earlier claim: Layer 1 does **not** "count everyone." It counts everyone whose browser doesn't block third-party trackers.

---

## How to check your data

**Clarity (reliable, consenting visitors):** Clarity dashboard → Recordings / Heatmaps. This is the trustworthy signal. To generate a test session: open the site, click "Zustimmen", browse a bit.

**Beacon (partial, non-blocking visitors):** on the VPS —
```
ssh vps
grep "site=jakubpopluhar" /var/log/nginx/beacon.log
```
Older days: `zcat /var/log/nginx/beacon.log.N.gz | grep site=jakubpopluhar`. There is also a basic dashboard at `deflifeos.popluhar.at/analytics/` (nginx basic-auth, `/root/.stats_htpasswd`).

**Testing tips:**
- `https://jakubpopluhar.com/?consent=preview` force-shows the consent banner even after you decided.
- Reset your own choice: run `window.jpCookieSettings()` in the browser console, or clear site data.
- Do not judge the beacon by Safari/iPhone tests — those get blocked and will show nothing even when the site works perfectly.

---

## DONE — first-party beacon migration (2026-07-10)

The blind spot above is fixed for jakubpopluhar.com. What was done:
- **DNS:** `stats.jakubpopluhar.com` A → `46.224.207.147` (VPS), at GoDaddy.
- **VPS nginx:** new server block `/etc/nginx/sites-available/stats-jakubpopluhar` with `location = /px` serving the pixel, `access_log ... beacon` → same `beacon.log` → same archive pipeline → HD dashboard. TLS via certbot (`/etc/letsencrypt/live/stats.jakubpopluhar.com/`, auto-renew), HTTP→HTTPS redirect.
- **site.js:** beacon URL swapped to `https://stats.jakubpopluhar.com/px`.
- **datenschutz.html §7:** server hostname updated to the new subdomain.
- Verified: HTTPS 200, redirect 301, hits land in `beacon.log`.

**Remaining verification:** confirm a real Safari/iPhone visit now lands in the log (the old endpoint dropped these). Test after deploy.

**Not yet migrated (separate pass):** the HD sites (hill-digital.at etc.) still POST to `deflifeos.popluhar.at/t.gif` — inline beacons in `preview-2005/*` and other repos. Roll the same first-party pattern (`t.hill-digital.at` etc.) to those when ready.

## Ceiling (unchanged)
No client-side method is 100%. First-party subdomain + neutral path beats ITP and the large majority of ad-blockers; a small hardcore-privacy minority still slips. The only fully unblockable method is server-side log analysis, which GitHub Pages denies us — that is why the beacon exists at all.
