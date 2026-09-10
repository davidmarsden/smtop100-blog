# Target architecture

The long-term Top 100 ecosystem should behave like one platform with a clear editorial home, a small number of specialist tools, and a distinct sister game world.

## Core destinations

### 1. Top 100 — `smtop100.blog`

Role: **front door, editorial layer, current rules and historical blog archive**.

Primary content:

- current news and announcements;
- season stories, previews and reviews;
- opinion and community writing;
- active club records and manager-written team news;
- selected historical features;
- current Rules;
- About, Contact and Support;
- access to the Micro.blog chronological post archive at `/archive/`;
- Top 100 Regen editorial/reference pages under `/regen/`;
- clear navigation into specialist apps.

The main site should not duplicate structured functionality already provided elsewhere.

### 2. Top 100 Stats & History — `archive.smtop100.blog`

Role: **structured history and statistical record**.

Primary content/functions:

- seasons and league history;
- clubs and honours;
- manager careers and profiles;
- historical tables, records and comparisons;
- Roll of Honour and other structured historical data.

This destination should be labelled **Top 100 Stats & History** or **Top 100 History** in the UI, not simply “Archive”, so it is clearly distinct from Micro.blog's `/archive/` chronological post archive.

Manager material from `managers.smtop100.blog` should migrate here where practical.

### 3. Tournaments — `tournaments.smtop100.blog`

Role: **competition management and tournament history**.

This replaces the narrower `youth-cup.smtop100.blog` identity and should support Youth Cup, World Club Cup, Top 100 Regen competitions and future tournaments without each competition needing its own operational site.

### 4. Voting — `vote.smtop100.blog`

Role: **shared manager-authenticated voting front door for the Top 100 ecosystem**.

Primary content/functions:

- All-Manager Polls;
- governance and rule-change ballots;
- Awards ballots where the Awards app delegates voting to the shared service;
- tournament/community votes where appropriate;
- secure sign-in using the common manager-account identity;
- one-manager-one-vote electorate enforcement;
- deadlines, result visibility, manual result release and audit history.

Voting is shared ecosystem infrastructure, not part of the Tournaments product identity and not a generic administrator console. Specialist apps may keep their own presentation while using the same Supabase voting backend.

The voting backend must be explicitly game-world scoped before Regen uses it. Top 100 and Regen electorates, ballots and results must remain separate even where a manager belongs to both worlds.

### 5. Awards — `awards.smtop100.blog`

Role: **recognition, voting presentation and award history**.

Primary content/functions:

- current Top 100 Manager Awards voting experience;
- Hall of Fame;
- manager award cabinets;
- historical award records.

Awards voting should authenticate against the same manager-account identity and Shared Voting backend used elsewhere in the Top 100 ecosystem. Regen Awards should reuse that foundation only after world scoping is implemented, with separate nominees, electorate and results.

### 6. Regen — `smtop100.blog/regen/`

Role: **distinct sister game world presented as a first-class section of the main Top 100 site**.

Current transitional site: `top100regen.website`.

The canonical target is the integrated main-site section, not a separate `regen.smtop100.blog` site. The initial page set is:

- `/regen/` — Regen home;
- `/regen/rules/` — Regen-specific rule differences;
- `/regen/archive/` — Regen editorial/history discovery;
- `/regen/join/` — joining information.

Regen remains its own game world with its own managers, seasons and rule variations. Sharing the Micro.blog site does **not** merge the two worlds operationally. Accounts, voting, Awards and tournament data must remain explicitly scoped by game world.

Once the integrated section and retained content are verified, `top100regen.website` should redirect into `/regen/` and the separate Regen Micro.blog site can be retired to free the site slot.

Top 120 is the historical precedent: its archive should be preserved, but Regen should avoid becoming a disconnected sibling site.

## Rules and governance

### Current Rules — `smtop100.blog/rules/`

The canonical human-readable current Top 100 rules should live as a page on the main site, not as a standalone rules website.

The existing `rules.smtop100.blog` should be rewritten and reformatted, then retired or redirected to `/rules/` once the new page is complete.

Regen-specific differences live at `/regen/rules/` as an exceptions layer over the canonical Top 100 rulebook.

Detailed old rules are primarily **legacy/history material**. They should be preserved in a dated or versioned form so old decisions can be checked when someone argues that a rule “didn't used to be like this”.

### Governance tooling

Several difficult administrative jobs should become one coherent governance/admin system rather than a collection of unrelated pages:

- **Transfer bans** — structured ban records, reasons, dates, expiry calculation, current/history views and automatic reminders/expiry handling.
- **Rule adjudication** — versioned rules plus an assisted decision workflow that identifies the applicable rule and produces a reasoned proposed ruling. Human administrator confirmation remains required for contentious decisions.
- **Manager appointments** — vacancies, applications, eligibility checks, agreed criteria, transparent scoring/assessment, recorded decisions and an audit trail.
- **All-manager polls** — proposals, eligible voters, deadlines, one vote per eligible manager, published results and links to rule changes where relevant, delivered through the shared Voting service.

The purpose is not to automate judgement out of existence, but to make repetitive administration consistent, auditable and much less painful.

## Shared manager identity

A common manager-account identity should increasingly power authenticated functions across the ecosystem.

The Publishing Desk and Shared Voting already reuse Tournament Manager's Supabase manager accounts. The same identity model should power Awards voting, all-manager polls, tournament administration, manager applications/appointments, authenticated governance/admin functions and future manager-specific tools.

Membership and eligibility must remain game-world scoped so one identity can safely represent a manager in Top 100, Regen or both without crossing electorates or permissions.

## Shared navigation concept

A consistent ecosystem-level navigation should be used where technically practical. The target conceptual set is:

`Top 100 · Stats & History · Tournaments · Voting · Awards · Regen`

Rules, About, Contact, Support, the chronological Posts Archive and Regen editorial pages are part of the main Top 100 site rather than separate platform destinations.

Each specialist destination can then have its own local navigation beneath or alongside this shared layer.

## Support

`/support/` remains part of the target main-site page set. Its current WordPress-era copy needs rewriting around the actual ongoing costs and current payment method.

## Design consistency across the ecosystem

The main Micro.blog site is the reference implementation for the wider family design. Review areas include shared navigation, logo/wordmark treatment, typography, spacing, buttons, cards, forms, tables, mobile behaviour, accessibility, footer language, social cards and canonical links.

Regen should retain its lime/green identity within that family system rather than becoming visually indistinguishable from the original world.

## Retire/absorb candidates

### `top100regen.website`

Redirect to `smtop100.blog/regen/` after the integrated pages and retained standalone content are verified. Then retire the separate Regen Micro.blog site.

### `rules.smtop100.blog`

Retire after the current rules have been rewritten at `smtop100.blog/rules/`. Preserve detailed historical rule material separately and redirect useful old entry points.

### `legends.smtop100.blog`

Retain the concept, not necessarily the site. Strong historical/editorial pieces can live as features on the main site, while structured historical profiles/facts belong in Stats & History.

### `managers.smtop100.blog`

Retire once Stats & History manager pages cover the useful material. Redirect old entry points to relevant manager destinations where possible.

## Design principle

Users should not need to understand the technical history of the project. They should simply understand that Top 100 has one editorial home, a small number of specialist tools, and a sister game world, all visibly part of the same ecosystem.
