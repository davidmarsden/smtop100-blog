# SM Top 100 Blog

Planning, audit and redesign repository for [smtop100.blog](https://smtop100.blog/) and the wider Top 100 web ecosystem.

The main site is now live on Micro.blog after more than a decade split across Blogger and WordPress. This repository documents the migration, current architecture, taxonomy decisions, redirects, page drafts and the continuing cleanup of the connected Top 100 services.

## Core ecosystem

The live platform is built around complementary destinations:

- **smtop100.blog** — editorial/community hub: news, season stories, announcements, opinion and the historical post archive.
- **archive.smtop100.blog** — structured history and statistics: seasons, clubs, managers, careers, honours and records.
- **tournaments.smtop100.blog** — competition management and tournament history.
- **manager.smtop100.blog** — canonical Top 100 Manager Portal and manager-account identity entry point.
- **vote.smtop100.blog** — public Voting Results and authenticated manager voting.
- **awards.smtop100.blog** — Manager Awards voting, Hall of Fame, cabinets and records.

Two earlier experiments remain candidates for retirement rather than continued standalone development:

- `legends.smtop100.blog` — absorb useful editorial/history material into the main site and/or Archive.
- `managers.smtop100.blog` — absorb manager profiles/history into the Archive and redirect where practical. This is distinct from the singular `manager.smtop100.blog`, which is the live authenticated Manager Portal.

## Current phase

**Post-cutover cleanup and consolidation.**

The WordPress export taken on 5 September 2026 remains the migration source/backup dataset. The live focus is now on page and theme refinement, manager onboarding, redirect cleanup, archive/taxonomy discoverability and carefully retiring legacy plumbing once the replacement paths have survived real-world use.

See [ROADMAP.md](ROADMAP.md) and the documents under [`docs/`](docs/).

## Principles

1. Preserve the history without preserving every accident of the old structure.
2. Keep structured data and interactive tools in the apps that already do those jobs better.
3. Make the main site the front door, editorial layer and historical blog archive.
4. Keep one canonical manager identity across services rather than creating separate logins.
5. Preserve useful existing URLs where practical and document redirects for anything retired or moved.
6. Retire legacy systems cautiously, after their replacements have been proven in production.

## Repository scope

This repository holds planning documents, audit outputs, taxonomy and URL inventories, design prototypes, reusable branding assets, migration notes and current architecture documentation. It should not become a duplicate dump of the full raw WordPress export or media library.
