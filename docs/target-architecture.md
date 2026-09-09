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
- clear navigation into specialist apps and the sister Regen world.

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

The existing `/vote` route in the Tournaments application should remain as a compatibility entry point during the transition.

### 5. Awards — `awards.smtop100.blog`

Role: **recognition, voting presentation and award history**.

Primary content/functions:

- current Manager Awards voting experience;
- Hall of Fame;
- manager award cabinets;
- historical award records.

Awards voting should authenticate against the same manager-account identity and Shared Voting backend used elsewhere in the Top 100 ecosystem. Awards should keep its purpose-specific presentation and historical features rather than becoming a skin for a generic poll page.

### 6. Regen — proposed `regen.smtop100.blog`

Role: **separate sister game-world website within the Top 100 family**.

Current site: `top100regen.website`.

Top 100 Regen is not an app for the main Top 100 world. It is its own website and game world. The preferred long-term direction is to move it beneath the `smtop100.blog` umbrella at `regen.smtop100.blog`, while retaining its own identity, content and current-world information.

Shared branding, navigation and account concepts may connect it to the original Top 100, but the two worlds must remain clearly distinguishable.

Top 120 is the historical precedent: its archive should be preserved, but Regen should avoid becoming a disconnected sibling site.

## Rules and governance

### Current Rules — `smtop100.blog/rules/`

The canonical human-readable current rules should live as a page on the main site, not as a standalone rules website.

The existing `rules.smtop100.blog` should be rewritten and reformatted, then retired or redirected to `/rules/` once the new page is complete.

The current Rules page should be concise and operational, with layers such as:

1. short version / essentials;
2. Top 100 and Top 100 Regen relationship and differences;
3. current squad, transfer and conduct rules;
4. competition rules;
5. administration and dispute procedures;
6. links to historical rule versions where needed.

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

The Publishing Desk and Shared Voting already reuse Tournament Manager's Supabase manager accounts. The same identity model should power:

- Awards voting;
- all-manager polls;
- tournament administration;
- manager applications/appointments;
- authenticated governance/admin functions;
- future manager-specific tools.

This should give the ecosystem a single answer to “who is this manager?” without forcing each app to invent another login system.

## Shared navigation concept

A consistent ecosystem-level navigation should be used where technically practical. The target conceptual set is:

`Top 100 · Stats & History · Tournaments · Voting · Awards · Regen`

Rules, About, Contact, Support and the chronological Posts Archive are part of the main Top 100 site rather than separate platform destinations.

Each specialist destination can then have its own local navigation beneath or alongside this shared layer.

## Support

`/support/` remains part of the target main-site page set. Its current WordPress-era copy needs rewriting around the actual ongoing costs and current payment method before launch.

## Design consistency across the ecosystem

All existing apps and sites should be reviewed before cutover so the ecosystem has a clear family resemblance.

Review areas:

- shared global navigation;
- logo/wordmark treatment;
- typography;
- spacing and layout conventions;
- buttons, cards, forms and tables;
- mobile behaviour;
- accessibility;
- footer/ownership language;
- social-card treatment;
- canonical links back to `smtop100.blog`;
- clear cues when moving from the editorial site into an app or into Regen.

The aim is a consistent Top 100 design system, not pixel-identical interfaces.

## Retire/absorb candidates

### `rules.smtop100.blog`

Retire after the current rules have been rewritten at `smtop100.blog/rules/`. Preserve detailed historical rule material separately and redirect useful old entry points.

### `legends.smtop100.blog`

Retain the concept, not necessarily the site. Strong historical/editorial pieces can live as features on the main site, while structured historical profiles/facts belong in Stats & History.

### `managers.smtop100.blog`

Retire once Stats & History manager pages cover the useful material. Redirect old entry points to relevant manager destinations where possible.

## Main-site homepage hierarchy

The homepage should answer three questions quickly:

1. **What is happening now?**
2. **Where do I go to do something?**
3. **Where do I find the history?**

A first-pass hierarchy:

1. **Top 100 identity / current-world status** — concise introduction and any genuinely important Admin notice.
2. **Latest editorial** — newest meaningful posts, not a raw dump of every historical category.
3. **Quick access to the platform** — prominent links/cards for Stats & History, Tournaments, Voting and Awards, with Regen visibly presented as the sister world.
4. **Current competitions** — surfaced from or linked directly into Tournaments rather than requiring duplicate organiser posts.
5. **Club records / Team News** — active club diaries such as Espanyol and Hamburger, with dormant club records discoverable but not cluttering the homepage.
6. **Season analysis** — current prediction/review editorial where it adds interpretation; structured history points into Stats & History.
7. **From the blog archive** — selective resurfacing of older editorial material.
8. **Community / governance** — concise links to About, Rules, Contact, Support and active manager votes.

## Design principle

Users should not need to understand the technical history of the project. They should simply understand that Top 100 has one editorial home, a small number of specialist tools, and a sister game world, all visibly part of the same ecosystem.