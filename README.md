# SM Top 100 Blog

Planning, audit and redesign repository for [smtop100.blog](https://smtop100.blog/) and its eventual migration from WordPress.com to Micro.blog.

The live site has more than a decade of history and was originally a Blogger site before being imported into WordPress. This repository is therefore not intended to reproduce the current site blindly. Its first job is to understand what exists, decide what belongs where across the wider Top 100 ecosystem, and design a cleaner long-term structure.

## Core ecosystem

The target platform is built around five complementary destinations:

- **smtop100.blog** — editorial/community hub: news, season stories, announcements, opinion and selected historical features.
- **archive.smtop100.blog** — structured history and statistics: seasons, clubs, managers, careers, honours and records.
- **tournaments.smtop100.blog** — competition management and tournament history. This will replace `youth-cup.smtop100.blog`.
- **awards.smtop100.blog** — Manager Awards voting, Hall of Fame, cabinets and records.
- **rules.smtop100.blog** — canonical rules and governance.

Two earlier experiments are candidates for retirement rather than continued standalone development:

- `legends.smtop100.blog` — absorb useful editorial/history material into the main site and/or Archive.
- `managers.smtop100.blog` — absorb manager profiles/history into the Archive and redirect where practical.

## Current phase

**Phase 1: Understand what we have.**

A WordPress export taken on 5 September 2026 contains 9,834 objects, including 2,447 posts across published/draft/pending states, 105 pages, 7,008 attachments, 86 categories and 342 tags. The raw export is being treated as a backup/source dataset, not as the future information architecture.

See [ROADMAP.md](ROADMAP.md) and the documents under [`docs/`](docs/).

## Principles

1. Preserve the history without preserving every accident of the old structure.
2. Keep structured data and interactive tools in the apps that already do those jobs better.
3. Make the main site the front door, editorial layer and historical blog archive.
4. Avoid new WordPress-specific lock-in during the remaining WordPress.com subscription period.
5. Design every major decision with eventual Micro.blog migration in mind.
6. Preserve useful existing URLs where practical and document redirects for anything retired or moved.

## Repository scope

This repository will hold planning documents, audit outputs, taxonomy and URL inventories, design prototypes, reusable branding assets and migration notes. It should not become a duplicate dump of the full raw WordPress export or media library.
