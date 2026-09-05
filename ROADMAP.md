# SM Top 100 website roadmap

This roadmap now treats Micro.blog as the active migration target rather than spending time redesigning WordPress first.

The live WordPress site remains untouched while the replacement is built and tested at `https://smtop100.micro.blog/`.

## Phase 1 — Audit and preserve the WordPress site

**Status: substantially complete**

- [x] Export all WordPress content.
- [x] Export the WordPress media/attachment archive manifest and preserve a local backup.
- [x] Establish this repository as the migration control room.
- [x] Inventory posts, pages, categories, tags and post types.
- [x] Triage all 86 categories.
- [x] Triage all 105 pages.
- [x] Map the current Top 100 subdomain ecosystem.
- [x] Decide the broad ownership of overlapping blog/app functions.
- [ ] Audit media references and identify essential vs disposable media.
- [ ] Produce an initial redirect/retirement register for important old URLs and obsolete subdomains.

**Working principle:** preservation does not require keeping every historical item prominent or even as a live navigation destination.

## Phase 2 — Target information architecture

**Status: in progress**

- [x] Define the main site's permanent job: front door, editorial layer, community news and historical blog archive.
- [x] Separate current activity from historical archive material.
- [x] Classify active, app-related, archive, metadata and dormant club taxonomy.
- [x] Define how old pages should be treated: keep only a small live set; archive the rest.
- [x] Bring Top 100 Regen under the wider Top 100 umbrella conceptually, with `regen.smtop100.blog` as the preferred future home.
- [ ] Finalise the main-site navigation and homepage content model.
- [ ] Define the minimal live editorial taxonomy to recreate in Micro.blog.
- [ ] Define URL-preservation and redirect rules.

**Working ecosystem navigation:** `Top 100 · Archive · Tournaments · Awards · Rules · Regen`.

## Phase 3 — Build the Micro.blog prototype

**Status: active**

Prototype site: `https://smtop100.micro.blog/`

- [x] Create the Micro.blog prototype site.
- [ ] Import a representative WordPress content sample.
- [ ] Test Blogger-era, WordPress-era and recent posts.
- [ ] Test image-heavy and embedded-media posts.
- [ ] Test historical pages and determine which should become pages, redirects or archive-only material.
- [ ] Build the target navigation directly in Micro.blog.
- [ ] Build the new homepage around current activity and the wider ecosystem.
- [ ] Implement the minimal live taxonomy rather than reproducing WordPress category/tag sprawl.
- [ ] Create active/dormant club-record presentation.
- [ ] Confirm how Archive, Tournaments, Awards, Rules and Regen are surfaced across the site.
- [ ] Test mobile presentation, accessibility, social cards and feeds.

**Goal:** prove the replacement architecture on Micro.blog before touching the live WordPress domain.

## Phase 4 — Media audit and migration

The WordPress export contains roughly 7,000 attachment records, many of which are likely obsolete, duplicated or unused. Do not bulk-migrate them blindly.

- [ ] Cross-reference attachment records against published post/page content.
- [ ] Mark media as referenced by active/live content, referenced only by archive content, apparently unreferenced, duplicate/variant, branding, or recent active media.
- [ ] Prioritise current branding and media required by live/editorial content.
- [ ] Preserve media needed to render important historical posts.
- [ ] Avoid deliberately carrying forward disposable media-library dross.
- [ ] Verify that essential migrated content does not depend permanently on WordPress-hosted media.

## Phase 5 — Migration rehearsal

- [ ] Run a broader/full WordPress import into the Micro.blog prototype.
- [ ] Compare permalink behaviour with the WordPress URL inventory.
- [ ] Generate a redirect map for important changed URLs.
- [ ] Verify high-value historical posts and active club records.
- [ ] Verify category/archive behaviour.
- [ ] Verify essential media.
- [ ] Check links from Archive, Tournaments, Awards, Rules and Regen back to the main site.
- [ ] Identify anything that genuinely blocks migration.

## Phase 6 — Cutover to `smtop100.blog`

Proceed when the Micro.blog prototype is clearly better and the migration rehearsal is satisfactory; there is no requirement to wait for the WordPress.com subscription to expire.

- [ ] Take final WordPress content and media backups.
- [ ] Freeze or carefully control publishing during final migration.
- [ ] Run the final import/sync.
- [ ] Apply the proven Micro.blog theme and navigation.
- [ ] Point `smtop100.blog` to Micro.blog.
- [ ] Implement and verify redirects.
- [ ] Check feeds, social metadata, search indexing and key inbound links.
- [ ] Keep the old WordPress account/site available long enough to resolve migration problems safely.
- [ ] Retire or redirect obsolete destinations only after replacements are proven.

## Non-goals

- Redesigning WordPress as an intermediate destination.
- Rebuilding structured apps inside the blog.
- Preserving every historical category/tag merely because it exists.
- Migrating the current WordPress structure unchanged.
- Migrating all 7,000+ media attachments blindly.
- Deleting historical material simply because it is no longer part of the live navigation.
