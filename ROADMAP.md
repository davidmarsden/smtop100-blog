# SM Top 100 website roadmap

This roadmap now treats Micro.blog as the active migration target rather than spending time redesigning WordPress first.

The live WordPress site remains untouched while the replacement is built and tested at `https://smtop100.micro.blog/`.

## Phase 1 — Audit and preserve the WordPress site

**Status: complete enough to proceed**

- [x] Export all WordPress content.
- [x] Export the WordPress media/attachment archive manifest and preserve a local backup.
- [x] Establish this repository as the migration control room.
- [x] Inventory posts, pages, categories, tags and post types.
- [x] Triage all 86 categories.
- [x] Triage all 105 pages.
- [x] Map the current Top 100 subdomain ecosystem.
- [x] Decide the broad ownership of overlapping blog/app functions.
- [x] Audit media references and identify essential vs disposable media.
- [ ] Produce an initial redirect/retirement register for important old URLs and obsolete subdomains.

**Working principle:** preservation does not require keeping every historical item prominent or even as a live navigation destination.

## Phase 2 — Target information architecture

**Status: substantially complete**

- [x] Define the main site's permanent job: front door, editorial layer, community news and historical blog archive.
- [x] Separate current activity from historical archive material.
- [x] Classify active, app-related, archive, metadata and dormant club taxonomy.
- [x] Define how old pages should be treated: keep only a small live set; archive the rest.
- [x] Bring Top 100 Regen under the wider Top 100 umbrella conceptually, with `regen.smtop100.blog` as the preferred future home.
- [x] Define the main-site homepage hierarchy.
- [ ] Finalise the minimal live editorial taxonomy to recreate in Micro.blog.
- [ ] Define URL-preservation and redirect rules in operational form.

**Working ecosystem navigation:** `Top 100 · Archive · Tournaments · Awards · Rules · Regen`.

## Phase 3 — Build the Micro.blog prototype

**Status: prototype import proven**

Prototype site: `https://smtop100.micro.blog/`

- [x] Create the Micro.blog prototype site.
- [x] Import a representative WordPress content sample.
- [x] Test Blogger-era, WordPress-era and recent posts.
- [x] Test image-heavy and embedded-media posts.
- [x] Confirm Micro.blog copies referenced media into its own media library.
- [x] Confirm extensionless permalink mode and retain it as the target setting.
- [ ] Run the full WordPress import rehearsal.
- [ ] Build the target navigation directly in Micro.blog.
- [ ] Build the new homepage around current activity and the wider ecosystem.
- [ ] Implement the minimal live taxonomy rather than reproducing WordPress category/tag sprawl.
- [ ] Create active/dormant club-record presentation.
- [ ] Confirm how Archive, Tournaments, Awards, Rules and Regen are surfaced across the site.
- [ ] Test mobile presentation, accessibility, social cards and feeds.

**Goal:** prove the replacement architecture on Micro.blog before touching the live WordPress domain.

## Phase 4 — Media strategy

**Status: settled**

The WordPress export contains 7,009 attachment records. The automatic audit now gives us a migration policy rather than a manual review task.

- [x] Cross-reference attachment records against post/page content.
- [x] Identify media used by live content.
- [x] Identify media used by archive content.
- [x] Identify live-parent media that should be kept despite no direct body reference.
- [x] Identify old draft-only media that can be skipped.
- [x] Identify apparently unreferenced skip candidates.
- [x] Confirm Micro.blog copies referenced media during import.

**Media policy:**

- Keep/migrate 1,054 items used by live content.
- Keep/migrate 2,630 items used by archive content.
- Keep/migrate 201 items attached to live-parent content.
- Skip 151 old draft/pending-only items dated before 1 August 2026.
- Treat 2,874 unreferenced items as skip candidates.
- Treat 99 archive-parent-only items with no direct body reference as low priority / skip unless later shown to be needed.

## Phase 5 — Full migration rehearsal

**Status: next**

See `docs/full-migration-launch-plan.md` for the operational sequence.

- [ ] Run the full WordPress import into `smtop100.micro.blog`.
- [ ] Compare post volume with the WordPress export.
- [ ] Verify representative recent, Blogger-era, club, tournament and season-analysis posts.
- [ ] Verify keeper pages.
- [ ] Verify essential media is served independently of WordPress.
- [ ] Record representative old/new URL pairs.
- [ ] Finalise homepage, navigation and minimal live taxonomy on top of the imported corpus.
- [ ] Check links from Archive, Tournaments, Awards, Rules and Regen back to the main site.
- [ ] Identify anything that genuinely blocks migration.

## Phase 6 — Cutover to `smtop100.blog`

Proceed when the Micro.blog prototype is clearly better and the full rehearsal is satisfactory; there is no requirement to wait for the WordPress.com subscription to expire.

- [ ] Take final WordPress content and media backups.
- [ ] Record the exact WordPress.com fallback address and the existing Blogger fallback.
- [ ] Freeze or carefully control publishing during final migration.
- [ ] Run the final import/sync for anything published since rehearsal.
- [ ] Apply the proven Micro.blog theme and navigation.
- [ ] Point `smtop100.blog` to Micro.blog.
- [ ] Verify original WordPress URLs redirect correctly after cutover.
- [ ] Add explicit redirects/workarounds for important failures.
- [ ] Check feeds, social metadata, search indexing and key inbound links.
- [ ] Keep the old WordPress account/site available as a safety net while the migration beds in.
- [ ] Retire or redirect obsolete destinations only after replacements are proven.

## Non-goals

- Redesigning WordPress as an intermediate destination.
- Rebuilding structured apps inside the blog.
- Preserving every historical category/tag merely because it exists.
- Migrating the current WordPress structure unchanged.
- Migrating all 7,000+ media attachments blindly.
- Deleting historical material simply because it is no longer part of the live navigation.
