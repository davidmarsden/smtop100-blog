# SM Top 100 website roadmap

The main `smtop100.blog` domain has now moved from WordPress.com to Micro.blog. The migration is no longer a prototype project: the live site is on the new platform, the specialist apps are connected, and the remaining work is post-launch cleanup, page/theme refinement and gradual retirement of legacy infrastructure.

## Completed foundation

- [x] Export and preserve the WordPress content/media history.
- [x] Audit and curate posts, pages, categories, tags and media.
- [x] Import the historical corpus to Micro.blog.
- [x] Restore original contributor bylines for migrated posts.
- [x] Build and deploy the custom Top 100 theme/navigation.
- [x] Move `smtop100.blog` to Micro.blog.
- [x] Keep WordPress and Blogger as safety-net archives during the bedding-in period.
- [x] Establish the ecosystem: Top 100, Stats & History, Tournaments, Voting Results, Vote and Awards, with Top 100 Regen remaining a separate sister-world site pending its own hostname move.
- [x] Build the Publishing Desk around authenticated Top 100 manager identity.
- [x] Build shared manager-authenticated Voting for All-Manager Polls.
- [x] Move Manager Awards voting onto the shared Voting foundation while preserving the historical Awards archive.
- [x] Add canonical Top 100 manager lifecycle controls for active/inactive managers.
- [x] Scope manager membership by game world so Regen/test identities do not enter Top 100 electorates.
- [x] Keep already-open voting electorates frozen while future votes use the current active Top 100 roster.

## Current priority — live site pages and theme cleanup

- [ ] Finish/review the main Micro.blog Pages: About, Rules, Contact and Support.
- [ ] Review the chronological Posts Archive and distinguish it clearly from Stats & History.
- [ ] Finalise the minimal live editorial taxonomy; keep historical metadata without recreating WordPress clutter.
- [ ] Improve active/dormant club-record browsing under Team News.
- [ ] Audit navigation on desktop/mobile across the live blog and specialist apps.
- [ ] Check typography, spacing, forms, cards, tables and dark-mode contrast on the main site.
- [ ] Finish social-card consistency across the Top 100 family.
- [ ] Check feeds, search, archive discovery and key legacy inbound URLs.
- [ ] Maintain an explicit redirect register for important WordPress/Blogger URLs that do not map automatically.

## Manager identity, Voting and Awards

**Status: production architecture complete; electorate reconciliation and real-world use remain acceptance gates.**

- [x] Shared Supabase manager identity reused by Manager Portal, Publishing Desk, Voting and Awards.
- [x] One-manager-one-vote, deadlines, electorate snapshots, ballot editing, audit trail and result visibility controls.
- [x] Public Voting Results at `vote.smtop100.blog/`.
- [x] Authenticated Manager Voting at `vote.smtop100.blog/vote`.
- [x] Manager Awards at `awards.smtop100.blog`, with current voting and historical Hall of Fame/history separated cleanly.
- [x] Manager lifecycle admin can add managers, mark them inactive and reactivate returning managers without deleting history.
- [x] Deactivation disables linked Top 100 Manager Portal access and delegated Top 100 tournament organiser/assistant access.
- [x] Internal rollback-only database tests completed for manager create/deactivate/reactivate behaviour and electorate snapshot logic.
- [ ] Before the next genuine production poll/Awards round, reconcile the active Top 100 manager roster against linked/approved Manager Portal accounts and resolve every unexplained omission.
- [ ] Onboard current managers who should be eligible but do not yet have a linked/approved account before opening the production event.
- [ ] Exercise the new Awards system with the next genuine Awards round.
- [ ] After successful real-world Awards use, remove the executable legacy typed-name Awards voting backend while retaining historical data/reference material.
- [ ] Reuse the shared voting service for other community/tournament votes where useful.

## Governance/admin tooling still to build

- [ ] Structured Transfer Bans workflow with reason, dates, automatic expiry and current/history views.
- [ ] Versioned Rules History so rulings can cite the rule version that applied at the time.
- [ ] Assisted rule adjudication with proposed reasoning but mandatory human confirmation.
- [ ] Manager appointment workflow with vacancy, applicants, criteria and recorded final decision.
- [ ] Keep contentious/admin decisions human-confirmed even where checks and recommendations are automated.

## Post-cutover cleanup

- [ ] Verify representative old WordPress URLs and add explicit redirects where necessary.
- [ ] Check feeds, social metadata, search indexing and key inbound links after the domain move.
- [ ] Keep the old WordPress site/account available as a safety net while the new site beds in.
- [ ] Retire/redirect obsolete standalone subdomains only after their replacement destinations are proven.
- [ ] Move the existing Top 100 Regen site at `top100regen.website` to the planned `regen.smtop100.blog` hostname when that separate migration is ready.
- [ ] Decide whether trusted regular contributors need native Micro.blog Family/team-author access in addition to the Publishing Desk.

## Non-goals

- Rebuilding structured specialist apps inside the blog.
- Recreating WordPress category/tag sprawl.
- Deleting historical material merely because it is no longer in live navigation.
- Treating Top 100 Regen as merely another Top 100 app.
- Allowing automated governance tooling to make unreviewed contentious decisions.
