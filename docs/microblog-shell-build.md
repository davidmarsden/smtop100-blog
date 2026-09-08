# Micro.blog shell build

This is the immediate implementation plan for turning the successful curated import into the actual replacement Top 100 site.

## 1. Main navigation

Use a two-level mental model.

### Ecosystem navigation

Primary family links:

`Top 100 · Stats & History · Tournaments · Awards · Regen`

Destinations:

- **Top 100** → `/`
- **Stats & History** → `https://archive.smtop100.blog/`
- **Tournaments** → `https://tournaments.smtop100.blog/`
- **Awards** → `https://awards.smtop100.blog/`
- **Regen** → future `https://regen.smtop100.blog/`; until migration, link to the current Regen website

### Main-site utility navigation

Keep the editorial/site pages local to `smtop100.blog`:

`About · Rules · Support · Contact · Posts Archive · Write`

`Write` should point to the manager-authenticated Publishing Desk.

Avoid labelling `archive.smtop100.blog` merely as “Archive”; use **Stats & History** consistently so it cannot be confused with Micro.blog's chronological `/archive/`.

## 2. Homepage hierarchy

The homepage should make Top 100 understandable in a few seconds and then surface what is happening now.

### Hero

**Top 100**

A long-running 100-club Soccer Manager world with five divisions, its own competitions, rules, records and manager-written history.

Primary actions:

- Read the latest
- View Stats & History
- Tournaments
- Rules

Optional small link: `Manage a club? Write for Top 100 →`

### Current activity

Show the latest editorial posts prominently. Avoid turning the homepage into a giant chronological archive.

Useful content groups to test:

- Latest
- Season previews & reviews
- Team news / club records
- Tournaments
- Admin / game-world news

These should be driven only by the final minimal live taxonomy.

### Explore Top 100

Four clear cards/links:

- **Stats & History** — seasons, tables, managers, honours and records
- **Tournaments** — Youth Cup, World Club Cup and fixtures
- **Awards** — voting, results and Manager Awards history
- **Top 100 Regen** — separate sister game world

### Community / governance

A quieter section can surface:

- Rules
- current All-Manager Polls, when one is open
- Support Top 100
- Write / Publishing Desk

The shared voting service should eventually provide the live “poll open” state here rather than requiring a manual blog announcement.

## 3. Main pages

Create/rebuild these as Micro.blog Pages:

- `/about/` — use `migration/pages/about.md`
- `/rules/` — use `migration/pages/rules.md`; this becomes canonical current Top 100 rules
- `/support/` — keep first-class but do not publish obsolete WordPress costs/payment details
- `/contact/` — use rewritten contact copy

Micro.blog's normal `/archive/` should be treated as **Posts Archive**, not Top 100 Stats & History.

Legacy page treatment:

- old Game World Rules → `/rules/`
- old Roll of Honour → Stats & History
- old Ask Me Anything → `/contact/`
- `rules.smtop100.blog` → eventually redirect to `/rules/`

## 4. Homepage/site naming rules

Use these labels consistently:

- **Posts Archive** = chronological Micro.blog posts (`/archive/`)
- **Stats & History** = structured archive app (`archive.smtop100.blog`)
- **Rules** = canonical current Top 100 rules (`/rules/`)
- **Rules History** = dated/versioned historical rulebook material
- **Regen** = separate sister website/game world, not an app

## 5. Design direction

Before polishing individual pages, define enough of the shared visual system that the main site can later propagate outward to the apps.

Minimum first pass:

- Top 100 wordmark/logo treatment
- one primary type scale
- spacing rhythm
- buttons and links
- card treatment
- page-width rules
- tables
- form inputs
- mobile navigation
- footer
- focus/hover states and contrast

The main Micro.blog site should be the reference implementation. Stats & History, Tournaments, Awards, Voting, Publishing Desk and Regen can then be reviewed against it rather than each inventing another design language.

## 6. Immediate build order

1. Create About, Rules, Support and Contact in Micro.blog.
2. Confirm `/archive/` renders as a chronological Posts Archive and label links to it accordingly.
3. Replace the prototype navigation with the ecosystem + utility navigation above.
4. Build the homepage hero, latest-content area and Explore Top 100 cards.
5. Finalise the minimal live taxonomy and wire homepage content groups to it.
6. Test mobile, old posts, author bylines, media, feeds and social metadata.
7. Only then start the cross-app design-system pass.

## 7. Not part of this pass

Do not block the Micro.blog shell on:

- Transfer Bans automation
- automated rule adjudication
- manager appointments workflow
- full Rules History tooling
- Regen migration

Those remain valuable follow-on work. The shared manager identity and voting service are already the foundation for them.
