# Micro.blog shell build

This document now describes the live Top 100 navigation and page architecture after cutover.

## 1. Global public navigation

The global header should answer the public-facing questions first and avoid presenting every specialist app as a peer destination.

Use:

`Top 100 · Top 100 Regen · About · Explore`

with **Manager sign-in / Manager portal** as the separate account action.

Destinations:

- **Top 100** → `https://smtop100.blog/`
- **Top 100 Regen** → `https://smtop100.blog/regen/`
- **About** → `https://smtop100.blog/about/`
- **Explore** → `https://smtop100.blog/explore/`
- **Manager portal** → `https://manager.smtop100.blog/`

Use these absolute URLs in shared/specialist shells. Root-relative paths are only safe inside the main `smtop100.blog` site itself and will resolve against the wrong host on specialist subdomains.

The same global family links should appear across specialist apps. Specialist products then add their own local navigation beneath or alongside the global shell.

Examples:

- **Tournaments** → `Youth Cup · World Club Cup · Tournament centre`
- **Community Polls** → `Results · Vote`
- **Manager Awards** → `Awards home · Vote in the Awards · Hall of Fame & history`
- **Stats & History** → its existing section tabs for search, tables, managers, honours, analytics and related records
- **Publishing Desk** → `Write · Media · My drafts` after manager sign-in

Do not put public specialist resources behind authentication merely because they are primarily useful to managers.

## 2. Explore as the public discovery hub

`https://smtop100.blog/explore/` is the home for deeper public material that does not need to occupy the global header.

It groups:

### Competitions

- Youth Cup
- World Club Cup
- Tournament centre

### History, awards and democracy

- Stats & History
- Manager Awards
- Community Polls

### Stories and discovery

- Search
- Categories
- Write for Top 100

### Never miss a thing

- Subscribe
- Support
- Manager Portal

The intention is that outsiders can understand Top 100 quickly, while managers and long-time followers can still reach the full public ecosystem without signing in.

## 3. Homepage hierarchy

The homepage should make Top 100 understandable in a few seconds and then surface what managers actually look for.

### Hero

**Top 100**

A long-running 100-club Soccer Manager world with five divisions, its own competitions, rules, records and manager-written history.

### Prominent competition routes

Use **Youth Cup** and **World Club Cup** by name rather than relying only on the generic Tournaments label.

### Participation

Keep **Write for Top 100** visible as an invitation to contribute, even though the Publishing Desk itself requires an authenticated manager account.

### Discovery

Use Explore for Stats & History, Manager Awards, Community Polls, Search, Categories, Subscribe, Support and other deeper routes.

## 4. Main pages

Core main-site pages:

- `/about/`
- `/rules/`
- `/support/`
- `/contact/` — presented as **Contact / Join**
- `/archive/` — chronological Posts Archive
- `/search/`
- `/categories/`
- `/subscribe/`
- `/explore/`

The canonical Markdown for About, Contact / Join, Rules and Support lives in the `smtop100-blog` repository and is published to Micro.blog through the managed page-sync workflow.

Top 100 Regen is a first-class section of the same Micro.blog site:

- `/regen/` — Top 100 Regen landing page
- `/regen/rules/` — Regen-specific rule differences
- `/regen/archive/` — Regen editorial/history discovery
- `/regen/join/` — joining information

`top100regen.website` now redirects to the integrated section. Do not describe the standalone Regen site as the current destination.

## 5. Naming rules

Use these labels consistently:

- **Posts Archive** = chronological Micro.blog posts (`/archive/`)
- **Stats & History** = structured records/statistics app (`archive.smtop100.blog`)
- **Community Polls** = ordinary manager democracy / governance polls (`vote.smtop100.blog`)
- **Manager Awards** = end-of-season Manager of the Season voting and Hall of Fame (`awards.smtop100.blog`)
- **Rules** = canonical current Top 100 rules (`/rules/` plus detailed rulebook while transition completes)
- **Top 100 Regen rules** = world-specific differences (`/regen/rules/`)
- **Top 100 Regen** = the full public name; avoid bare **Regen** in global navigation
- **Manager Portal** = account identity and manager-only actions plus a public resources hub

Community Polls and Manager Awards share an authentication/voting foundation internally, but should remain distinct products in public wording and navigation.

## 6. Design direction

The main Micro.blog site is the reference implementation for the wider visual system. Specialist apps should share:

- Top 100 wordmark and pitch-line treatment
- navy / emerald family shell
- the simplified global navigation
- a separate local navigation for the product itself
- Support and Subscribe in the footer
- consistent Manager Portal/account wording
- matching mobile behaviour, focus states and contrast

Top 100 Regen keeps its own lime/green accent and distinct-world cues while remaining visibly part of the Top 100 family.

## 7. Current build order

Completed:

1. Main domain cutover to Micro.blog.
2. Top 100 Regen integration under `/regen/`.
3. `top100regen.website` redirect.
4. About, Contact / Join, Rules and Support refresh plus automatic page publishing.
5. Explore hub and simplified main-site navigation.
6. Tournaments, Community Polls, Manager Portal and Manager Awards specialist-shell cleanup.
7. Top 100 Youth Cup reminder layer: opt-in Manager Portal preferences plus new-fixture, day-before and fixture-day emails.

Current:

8. Apply the same shell to Stats & History and Publishing Desk.
9. Run a final desktop/mobile family-wide navigation and contrast check.
10. Clean stale migration/cutover documentation.
11. Extend the **Never miss a thing** reminder foundation later to World Club Cup, polls, Awards and tournament deadlines.

## 8. Not part of this immediate pass

Do not block the public/navigation cleanup on Transfer Bans automation, automated rule adjudication, manager appointments workflow or full Rules History tooling.

Those remain valuable follow-on work. The shared manager identity and voting service are already the foundation for them.
