# SM Top 100 website roadmap

This roadmap treats Micro.blog as the active migration target rather than spending time redesigning WordPress first.

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

- [x] Define the main site's permanent job: front door, editorial layer, community news, current Rules and historical blog archive.
- [x] Separate the Micro.blog chronological Posts Archive from the structured Top 100 Stats & History app.
- [x] Separate current activity from historical archive material.
- [x] Classify active, app-related, archive, metadata and dormant club taxonomy.
- [x] Define how old pages should be treated: keep only a small live set; archive the rest.
- [x] Keep `/support/` as a first-class main-site page, with rewritten current-purpose copy.
- [x] Decide that current Rules belong at `smtop100.blog/rules/`, not on a permanent standalone rules subdomain.
- [x] Treat detailed old rules as versioned legacy/history material rather than the main current rulebook.
- [x] Bring Top 100 Regen under the wider Top 100 umbrella conceptually, with `regen.smtop100.blog` as the preferred future home while remaining a separate website/game world.
- [x] Define the main-site homepage hierarchy.
- [x] Define the preferred ecosystem mental model: Top 100, Stats & History, Tournaments, Voting, Awards and Regen.
- [x] Separate shared voting from the Tournaments identity and give it a first-class destination at `vote.smtop100.blog`.
- [ ] Finalise the minimal live editorial taxonomy to recreate in Micro.blog.
- [ ] Define URL-preservation and redirect rules in operational form.

**Working ecosystem navigation:** `Top 100 · Stats & History · Tournaments · Voting · Awards · Regen`.

Rules, About, Contact, Support and Posts Archive belong within the Top 100 site itself.

## Phase 3 — Build the Micro.blog prototype

**Status: full curated import complete**

Prototype site: `https://smtop100.micro.blog/`

- [x] Create the Micro.blog prototype site.
- [x] Import a representative WordPress content sample.
- [x] Test Blogger-era, WordPress-era and recent posts.
- [x] Test image-heavy and embedded-media posts.
- [x] Confirm Micro.blog copies referenced media into its own media library.
- [x] Confirm extensionless permalink mode and retain it as the target setting.
- [x] Run the curated full WordPress import rehearsal.
- [x] Confirm WordPress Pages do not become Micro.blog Pages and switch to a deliberate page rebuild plan.
- [ ] Create the rebuilt Micro.blog Pages: About, Rules, Contact and Support, plus any temporary operational gateways.
- [ ] Build the target navigation directly in Micro.blog.
- [ ] Build the new homepage around current activity and the wider ecosystem.
- [ ] Implement the minimal live taxonomy rather than reproducing WordPress category/tag sprawl.
- [ ] Create active/dormant club-record presentation.
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
- Keep/migrate 201 records attached to live-parent content.
- Skip 151 old draft/pending-only items dated before 1 August 2026.
- Treat 2,874 unreferenced items as skip candidates.
- Treat 99 archive-parent-only items with no direct body reference as low priority / skip unless later shown to be needed.

The three keep buckets contain 3,885 audit records representing 3,884 unique attachment IDs.

## Phase 5 — Curated full migration rehearsal

**Status: complete enough to design on top of**

See `docs/full-migration-launch-plan.md` for the operational sequence.

A curated WXR rehearsal package was generated from the original WordPress export. It preserves the published history without carrying across discarded drafts, obsolete pages, plugin/custom-post-type debris, tag sprawl or low-value media-library cruft.

**Curated rehearsal package:**

- 2,262 published posts.
- 9 keeper-page records in the WXR (handled separately because Micro.blog does not import them as Pages).
- 3,884 unique selected media attachment records.
- 83 explicitly approved categories.
- 0 legacy WordPress tags.
- Draft/pending posts excluded.
- 96 non-keeper pages excluded.
- `Uncategorized` excluded.
- Metadata-only/review-only category parents excluded.
- Obsolete WordPress/plugin/custom post types excluded.
- Old-draft, unreferenced and low-priority archive-parent-only media excluded.

- [x] Generate the curated rehearsal WXR from the completed content, page, category and media decisions.
- [x] Import the curated WXR into `smtop100.micro.blog`.
- [x] Confirm imported posts and media render correctly across old and recent material.
- [x] Confirm essential media is copied to and served independently by Micro.blog.
- [ ] Record representative old/new URL pairs.
- [ ] Finalise homepage, navigation and minimal live taxonomy on top of the imported corpus.
- [ ] Check links from Stats & History, Tournaments, Voting, Awards and Regen back to the main site.
- [ ] Identify anything that genuinely blocks migration.

## Phase 5A — Restore authorship and manager publishing

**Status: working end-to-end; manager-authenticated Publishing Desk implemented**

Micro.blog imported historical WordPress content under the site owner account, so the migration also restores the original contributor layer rather than flattening Top 100 history into one author.

- [x] Recover original WordPress creator metadata for all 2,262 published migrated posts.
- [x] Identify 77 distinct historical WordPress contributors.
- [x] Generate a date/title author lookup for Hugo/Micro.blog.
- [x] Integrate recovered bylines into the Micro.blog theme.
- [x] Add a contributor audit without storing WordPress email addresses.
- [x] Curate friendly contributor names where the old WordPress display name is only a username.
- [x] Build the Top 100 Publishing Desk as a combined Submission Desk / Markdown Hand / BUM Hand workflow.
- [x] Support private unfinished drafts and direct image uploads.
- [x] Run a light-touch automated review and publish normal submissions automatically to Micro.blog.
- [x] Divert exceptional/incomplete submissions to Micro.blog Drafts rather than dead-ending them.
- [x] Keep an explicit contributor byline independent of the Micro.blog account that technically publishes the post.
- [x] Reuse Tournament Manager's Supabase manager-account identity rather than inventing a separate login system.
- [x] Restrict writing, drafts and media uploads to approved active Top 100 manager accounts.
- [x] Prefill canonical manager name and current club server-side.
- [x] Make private drafts manager-specific and available across devices after sign-in.
- [x] Add a `Write` entry point to the custom Sumo theme navigation.
- [ ] Verify the manager magic-link redirect and full authenticated flow on the deployed Publishing Desk.
- [ ] Replace the temporary Netlify URL with the final Publishing Desk address after domain cutover (preferred: `submit.smtop100.blog`).
- [ ] Decide whether any trusted regular contributors also justify native Micro.blog Family/team-author access.

See `docs/legacy-author-recovery.md` and the private `smtop100-editorial` repository.

## Phase 5B — Shared design system and app review

**Status: substantially complete**

The surviving sites/apps should look and behave like one family without erasing their individual jobs.

- [x] Audit and refresh the current design of Stats & History, Tournaments, Awards, Publishing Desk and Regen.
- [x] Define and apply a compact Top 100 design system: wordmark/logo rules, typography, spacing, buttons, forms, cards, tables, mobile patterns and accessibility expectations.
- [x] Add consistent ecosystem navigation and footer/ownership language where practical.
- [x] Standardise the family favicon/browser theme treatment across the principal sites/apps.
- [x] Make transitions between the editorial site, specialist apps and Regen obvious but visually coherent.
- [ ] Add Voting to the shared ecosystem navigation across the remaining family sites as they next receive changes.
- [ ] Create a shared social-card family where still missing.
- [ ] Review authentication UX across manager-facing tools after Voting and Awards share the same production flow.

## Phase 5C — Manager accounts, polling and governance tooling

**Status: in progress — Shared Voting V2 deployed**

The existing Supabase manager identity used by Tournament Manager and the Publishing Desk is now the preferred common identity layer for authenticated Top 100 functions.

- [x] Design and implement a reusable manager-authenticated polling service.
- [x] Support an explicit electorate, one-manager-one-vote, deadlines, result-visibility controls and a clear audit trail.
- [x] Build **All-Manager Polls** on the shared voting service.
- [x] Add Shared Voting V2: nominee metadata, manual result release, ballot restoration, audited electorate correction, per-category Awards finalisation and archive export support.
- [x] Apply the Shared Voting V2 migrations to the production Supabase project.
- [x] Preserve the existing `/vote` route as a compatibility entry point.
- [ ] Deploy/attach the dedicated voting front door at `vote.smtop100.blog` and smoke-test it end-to-end.
- [ ] Refactor **Awards voting** to use the same manager accounts and voting primitives while preserving Hall of Fame, cabinets, records and historical Sheets data.
- [ ] Complete the post-season archive bridge so released Supabase Awards results flow into the existing historical presentation until those readers migrate.
- [ ] Reuse the service for tournament/community votes where appropriate rather than building separate voting backends.
- [ ] Complete electorate reconciliation/account-claim checks before the first production Awards cutover.
- [ ] Design a structured **Transfer Bans** workflow with reasons, start/end dates, automatic expiry and current/history views.
- [ ] Build a versioned **Rules History** so historical adjudications can cite the rule that actually applied at the time.
- [ ] Prototype **rule adjudication assistance**: enter the facts, identify applicable rules, produce a proposed ruling and rationale, then require admin confirmation.
- [ ] Design **manager appointments** workflow: vacancy, applicants, eligibility, agreed criteria, scoring/assessment, final decision and recorded rationale.
- [ ] Ensure contentious/admin decisions remain human-confirmed even when checks and recommendations are automated.

**Voting architecture:** `vote.smtop100.blog` is the manager-facing voting front door. It is shared ecosystem infrastructure, not a Tournaments feature and not a generic admin console. Awards, Tournaments and future governance surfaces can keep purpose-specific presentation while using the same manager identity and Supabase voting backend.

The goal is consistency, auditability and less repetitive admin — not opaque automatic government by software.

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
- [ ] Retire or redirect `rules.smtop100.blog`, `legends.smtop100.blog` and `managers.smtop100.blog` only after replacements are proven.
- [ ] Move or redirect `top100regen.website` to `regen.smtop100.blog` only after the Regen site migration has been tested separately.

## Non-goals

- Redesigning WordPress as an intermediate destination.
- Rebuilding structured apps inside the blog.
- Treating Top 100 Regen as merely another app.
- Preserving every historical category/tag merely because it exists.
- Migrating the current WordPress structure unchanged.
- Migrating all 7,000+ media attachments blindly.
- Deleting historical material simply because it is no longer part of the live navigation.
- Allowing automated governance tools to make unreviewed contentious decisions.