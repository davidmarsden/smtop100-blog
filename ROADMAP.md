# SM Top 100 website roadmap

This roadmap covers the redesign of `smtop100.blog` during the remaining WordPress.com period and the eventual move to Micro.blog.

## Phase 1 — Understand what we have

**Status: in progress**

- [x] Export all WordPress content.
- [ ] Export/download the media library separately and preserve a local backup.
- [x] Establish this repository as the redesign control room.
- [ ] Inventory posts, pages, categories, tags, post types, menus and important URL patterns.
- [ ] Identify Blogger-import artefacts and WordPress-era cruft.
- [ ] Identify high-value evergreen/history content that should remain prominent.
- [x] Map the current Top 100 subdomain ecosystem.
- [ ] Decide canonical ownership of overlapping content/functions between the blog and apps.
- [ ] Produce an initial redirect/retirement register for `legends` and `managers`.

**Exit condition:** we can describe the current site and ecosystem clearly enough to redesign it without guessing.

## Phase 2 — Information architecture

- [ ] Define the main site's permanent job: front door, editorial layer, community news and historical blog archive.
- [ ] Define top-level navigation shared conceptually across the ecosystem.
- [ ] Separate current activity from historical archive material.
- [ ] Design a simpler taxonomy for editorial content.
- [ ] Decide how season, competition, club and manager metadata should be represented without recreating the existing category/tag sprawl.
- [ ] Define where legacy WordPress pages belong: keep, merge, move, redirect or retire.
- [ ] Create URL-preservation rules for the eventual migration.

**Working ecosystem navigation:** `Top 100 · Archive · Tournaments · Awards · Rules`.

## Phase 3 — WordPress redesign

- [ ] Choose the best WordPress.com-compatible theme/layout approach available on the Personal plan.
- [ ] Prototype the homepage around current activity and the five-part ecosystem.
- [ ] Simplify navigation and remove dead-end/duplicated destinations.
- [ ] Improve article, archive and category presentation.
- [ ] Create consistent Top 100 branding and cross-site visual language where practical.
- [ ] Improve mobile presentation and accessibility.
- [ ] Avoid adding dependencies that make a later Micro.blog move harder.
- [ ] Test changes before applying them to the live site.

**Goal:** make the current WordPress site substantially better without treating WordPress as the permanent architecture.

## Phase 4 — Clean the historical archive

This is deliberately separate from the visual redesign because the archive is large and valuable.

- [ ] Triage uncategorised and poorly categorised posts.
- [ ] Consolidate redundant categories/tags.
- [ ] Preserve useful season/competition metadata.
- [ ] Move structured historical facts to `archive.smtop100.blog` where that provides a better experience than old blog taxonomy.
- [ ] Surface selected historical writing/editorial features on the main site.
- [ ] Record redirects for content that moves.

## Phase 5 — Parallel Micro.blog prototype

This can begin before the WordPress subscription ends.

- [ ] Create a private/test Micro.blog site.
- [ ] Prototype the target navigation and theme independently of WordPress.
- [ ] Test import of a representative sample of Blogger-era, WordPress-era and recent posts.
- [ ] Test image/media handling.
- [ ] Compare permalink behaviour and identify required redirects.
- [ ] Test categories and any custom metadata needed for the cleaned editorial taxonomy.
- [ ] Confirm how cross-site navigation to Archive, Tournaments, Awards and Rules will work.

## Phase 6 — Migration and launch

Target timing: toward the end of the current WordPress.com plan, once the Micro.blog prototype is proven.

- [ ] Take final WordPress content and media backups.
- [ ] Freeze or carefully control publishing during final migration.
- [ ] Import cleaned content into Micro.blog.
- [ ] Apply target theme and navigation.
- [ ] Configure custom domain.
- [ ] Implement and verify redirects.
- [ ] Check high-value historical URLs and media.
- [ ] Verify feeds, social metadata, search indexing and cross-site links.
- [ ] Retire/redirect obsolete subdomains once replacement destinations are proven.

## Non-goals

- Rebuilding every structured app inside the blog.
- Preserving every historical category/tag merely because it exists.
- Migrating the current WordPress structure unchanged to Micro.blog.
- Undertaking destructive taxonomy cleanup before the export/audit is complete.
