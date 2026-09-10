# Micro.blog shell build

This is the implementation plan for the live Top 100 Micro.blog site and its post-cutover refinements.

## 1. Main navigation

Use a two-level mental model.

### Ecosystem navigation

Primary family links:

`Top 100 · Stats & History · Tournaments · Voting · Awards · Regen`

Destinations:

- **Top 100** → `/`
- **Stats & History** → `https://archive.smtop100.blog/`
- **Tournaments** → `https://tournaments.smtop100.blog/`
- **Voting** → `https://vote.smtop100.blog/`
- **Awards** → `https://awards.smtop100.blog/`
- **Regen** → `/regen/`

Current Voting and Awards are for the original Top 100 world only. Regen-facing equivalents should reuse the same shared identity/voting foundation after game-world scoping is complete.

### Main-site utility navigation

Keep the editorial/site pages local to `smtop100.blog`:

`About · Rules · Support · Contact · Posts Archive · Search · Subscribe · Write`

`Write` points to the manager-authenticated Publishing Desk.

Avoid labelling `archive.smtop100.blog` merely as “Archive”; use **Stats & History** consistently so it cannot be confused with Micro.blog's chronological `/archive/`.

## 2. Homepage hierarchy

The homepage should make Top 100 understandable in a few seconds and then surface what is happening now.

### Hero

**Top 100**

A long-running 100-club Soccer Manager world with five divisions, its own competitions, rules, records and manager-written history.

### Explore Top 100

Clear cards/links for:

- **Stats & History** — seasons, tables, managers, honours and records
- **Tournaments** — Youth Cup, World Club Cup and fixtures
- **Awards** — Top 100 Manager Awards and history
- **Top 100 Regen** — sister game world at `/regen/`

### Community / governance

A quieter section can surface Rules, current All-Manager Polls, Support and Write / Publishing Desk.

## 3. Main pages

Core main-site pages:

- `/about/`
- `/rules/`
- `/support/`
- `/contact/`
- `/archive/` — chronological Posts Archive
- `/search/`
- `/subscribe/`

Regen lives in the same Micro.blog site as a first-class section:

- `/regen/` — Regen landing page
- `/regen/rules/` — Regen-specific rule differences
- `/regen/archive/` — Regen editorial/history discovery
- `/regen/join/` — joining information

The standalone Regen Micro.blog site remains only during the migration. After these routes and retained Regen content are verified, redirect `top100regen.website` into `/regen/` and retire the separate site.

## 4. Naming rules

Use these labels consistently:

- **Posts Archive** = chronological Micro.blog posts (`/archive/`)
- **Stats & History** = structured archive app (`archive.smtop100.blog`)
- **Rules** = canonical current Top 100 rules (`/rules/`)
- **Regen Rules** = world-specific differences (`/regen/rules/`)
- **Regen** = distinct sister game world presented within the main site, not another app or another Micro.blog site

## 5. Design direction

The main Micro.blog site is the reference implementation for the wider visual system. Regen should inherit the Top 100 family shell while keeping its lime/green accent and distinct-world cues.

Minimum design system: wordmark/logo treatment, type scale, spacing rhythm, buttons/links, cards, page widths, tables, forms, mobile navigation, footer, focus/hover states and contrast.

## 6. Current build order

1. Publish and verify `/regen/`, `/regen/rules/`, `/regen/archive/` and `/regen/join/`.
2. Migrate standalone Regen posts worth retaining into the main Micro.blog site.
3. Verify navigation, links, archive discovery, feeds/social metadata and mobile behaviour.
4. Redirect `top100regen.website` to the appropriate `/regen/` destinations.
5. Retire the standalone Regen Micro.blog site and free its site slot.
6. Continue About/Rules/Support/Contact and taxonomy/theme cleanup.
7. Extend Voting/Awards with explicit Regen game-world scoping before exposing those services to Regen managers.

## 7. Not part of this immediate pass

Do not block the Regen editorial integration on Transfer Bans automation, automated rule adjudication, manager appointments workflow or full Rules History tooling.

Those remain valuable follow-on work. The shared manager identity and voting service are already the foundation for them.
