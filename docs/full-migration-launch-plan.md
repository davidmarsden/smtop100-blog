# Full migration and launch plan

This is the operational plan for moving `smtop100.blog` from WordPress.com to Micro.blog, using `https://smtop100.micro.blog/` as the proven migration target.

The working assumption is now that the Micro.blog import path is sound: representative Blogger-era, WordPress-era, current, image-heavy and embedded content imported successfully, and Micro.blog copied referenced media into its own media library.

## 1. Migration policy

### Content

- Import the historical WordPress post corpus rather than manually recreating it.
- Preserve archive material, but do not reproduce the old site's navigation/taxonomy clutter.
- Recreate only the minimal live editorial taxonomy agreed in the category audit.
- Keep active club records visible; preserve dormant club records so a future manager can revive them.
- Keep only the small set of pages identified in `docs/page-triage-results.md`; everything else is archive material.

### Media

Treat the media audit as settled:

- **KEEP / MIGRATE:** 1,054 items used by live content.
- **KEEP / MIGRATE:** 2,630 items directly used by archive content.
- **KEEP / MIGRATE:** 201 items attached to live-parent content even where no direct body reference was detected.
- **SKIP:** 151 items associated only with old draft/pending material before 1 August 2026.
- **SKIP CANDIDATES:** 2,874 unreferenced attachment records.
- **LOW PRIORITY / SKIP UNLESS NEEDED:** 99 archive-parent-only attachments with no direct body reference.

Micro.blog has already demonstrated that referenced media is copied during WordPress import. The migration should therefore rely primarily on content references rather than a separate bulk upload of the full WordPress media library.

### URLs

- Keep Micro.blog's extensionless permalink setting enabled.
- Do not attempt to force every Micro.blog slug to match the original WordPress slug before migration.
- Record representative old/new URL pairs before cutover.
- After `smtop100.blog` points to Micro.blog, immediately verify that original WordPress URLs redirect correctly to their imported Micro.blog equivalents.
- Preserve a redirect register for any important URLs that do not map automatically.

## 2. Pre-full-import preparation

Before running the full import into the prototype:

- [ ] Confirm `.html` extensions remain disabled in Micro.blog.
- [ ] Remove or ignore duplicate test-import content only if it would materially confuse the full rehearsal; otherwise treat the prototype as disposable and reset/recreate if easier.
- [ ] Finalise the minimal live taxonomy to recreate after import.
- [ ] Finalise the keeper-page list and intended destinations.
- [ ] Record a representative URL test set covering recent, Blogger-era, club, tournament, predictions/reviews and keeper-page content.
- [ ] Record the current WordPress fallback URL (`*.wordpress.com`) once confirmed.
- [ ] Record `smtop100.blogspot.co.uk` as the older Blogger-era fallback/archive source.

## 3. Full migration rehearsal on `smtop100.micro.blog`

Run a full WordPress import into the prototype while the live site remains on WordPress.

After import, verify:

- [ ] Total post volume is broadly consistent with the WordPress export.
- [ ] Dates and authorship survived where meaningful.
- [ ] Recent posts render correctly.
- [ ] Blogger-era posts render correctly.
- [ ] Active club records render correctly.
- [ ] Youth Cup / World Club Cup historical and current posts render correctly.
- [ ] Season Predictions and Reviews render correctly.
- [ ] Keeper pages render or can be rebuilt cleanly.
- [ ] Referenced images are now served from Micro.blog rather than depending on WordPress.
- [ ] Embedded media and awkward legacy HTML remain usable.
- [ ] Categories/tags imported without blocking publication, even if most are later hidden or rationalised.
- [ ] Feeds build successfully.

Do not spend time manually repairing archive-only cosmetic oddities unless they materially affect readability or navigation.

## 4. Build the replacement site on top of the imported corpus

Once the full rehearsal is stable, build the real information architecture on the prototype.

### Global ecosystem navigation

`Top 100 · Archive · Tournaments · Awards · Rules · Regen`

### Main homepage priorities

1. Current Top 100 identity and important Admin notices.
2. Latest meaningful editorial/community posts.
3. Strong entry points to Archive, Tournaments, Awards, Rules and Regen.
4. Current tournament activity via Tournaments rather than repetitive organiser posts where possible.
5. Active club records / Team News.
6. Current season previews/reviews and analysis.
7. Selected historical features, not the full archive firehose.
8. Concise About / Contact / Support / Help links.

### Pages/functions to retain in some form

- About Top 100
- Archives (as a gateway rather than a giant manual index)
- Contact
- Rules (one canonical route to the Rules app)
- Roll of Honour (primarily Archive)
- Support Our Website
- Top 100 Ask Me Anything / help
- Transfer Bans (until a better structured workflow replaces it)

## 5. Pre-cutover checklist

Before moving the domain:

- [ ] Take a fresh final WordPress export.
- [ ] Preserve the media/attachment export manifest.
- [ ] Record the exact WordPress.com fallback address.
- [ ] Record the Blogger fallback address.
- [ ] Freeze or tightly control publishing on WordPress during the final sync window.
- [ ] Import any posts published after the rehearsal export.
- [ ] Confirm the Micro.blog theme/navigation is final enough for launch.
- [ ] Confirm `archive.smtop100.blog`, `tournaments.smtop100.blog`, `awards.smtop100.blog`, `rules.smtop100.blog` and planned `regen.smtop100.blog` entry points are correct.
- [ ] Prepare a short redirect test list of important original WordPress URLs.
- [ ] Check social-card metadata, feeds and mobile presentation on the prototype.

## 6. Domain cutover

When ready:

1. Point `smtop100.blog` to Micro.blog using Micro.blog's current custom-domain instructions.
2. Allow DNS/certificate changes to settle.
3. Confirm homepage and representative posts load on the custom domain.
4. Test original WordPress URLs from the redirect test set.
5. Record any failed mappings and add explicit redirects/workarounds where needed.
6. Test images on old and recent posts.
7. Test feeds and feed discovery.
8. Test social previews.
9. Test links from all specialist apps back to the main site.
10. Keep the WordPress site/account untouched as a safety net while the migration beds in.

## 7. Post-launch cleanup

Only after the Micro.blog version has proved stable:

- [ ] Remove redundant navigation/categories from the visible site.
- [ ] Hide/archive obsolete pages rather than rebuilding them.
- [ ] Rationalise taxonomy presentation without destroying historical metadata unnecessarily.
- [ ] Add/confirm active and dormant club-record browse views.
- [ ] Improve homepage modules as real publishing resumes.
- [ ] Build a better solution for All-Manager Polls.
- [ ] Build a better solution for Transfer Bans.
- [ ] Complete migration of Top 100 Regen to `regen.smtop100.blog` when ready.
- [ ] Retire/redirect `legends.smtop100.blog` and `managers.smtop100.blog` only after replacement destinations are proven.

## 8. Safety-net principle

The migration is not destructive.

For the transition period we retain multiple fallback layers:

- the live/legacy WordPress.com site;
- the older Blogger site at `smtop100.blogspot.co.uk`;
- local WordPress WXR exports;
- the WordPress attachment/media manifest;
- the GitHub audit and migration documentation.

This allows the Micro.blog site to be selective and clean without pretending that historical material has ceased to exist.
