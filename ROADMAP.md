# SM Top 100 website roadmap

The main `smtop100.blog` domain has moved from WordPress.com to Micro.blog. The cutover is complete, Top 100 Regen is integrated at `/regen/`, the old Regen domain redirects into the main site, and the specialist apps now share a consistent family shell. The current phase is post-launch refinement and new manager-facing features rather than migration.

## Completed foundation

- [x] Export and preserve the WordPress content/media history.
- [x] Audit and curate posts, pages, categories, tags and media.
- [x] Import the historical corpus to Micro.blog.
- [x] Restore original contributor bylines for migrated posts.
- [x] Build and deploy the custom Top 100 theme/navigation.
- [x] Move `smtop100.blog` to Micro.blog.
- [x] Keep WordPress and Blogger as safety-net archives during the bedding-in period.
- [x] Establish the specialist ecosystem: Stats & History, Tournaments, Community Polls, Manager Awards and Manager Portal.
- [x] Build the Publishing Desk around authenticated Top 100 manager identity.
- [x] Build shared manager-authenticated Community Polls for All-Manager Polls.
- [x] Move Manager Awards voting onto the shared voting foundation while preserving the historical Awards archive.
- [x] Add canonical Top 100 manager lifecycle controls for active/inactive managers.
- [x] Scope manager membership by game world so Regen/test identities do not enter Top 100 electorates.
- [x] Keep already-open voting electorates frozen while future votes use the current active Top 100 roster.
- [x] Absorb Top 100 Regen into the main Micro.blog site at `/regen/`.
- [x] Redirect `top100regen.website` to the integrated Top 100 Regen section.
- [x] Refresh and automate publication of the main About, Contact / Join, Rules and Support pages.
- [x] Simplify the public family navigation to Top 100, Top 100 Regen, About and Explore, with manager/account actions separate.
- [x] Give Tournaments, Community Polls and Manager Awards their own local specialist navigation.
- [x] Turn Manager Portal into the public resources hub plus authenticated manager account area.
- [x] Add authenticated Youth Cup fixture reminders to Manager Portal accounts, including new-fixture, day-before and fixture-day emails, delivery logging and manager-facing reminder status.

## Current priority — finish family-shell consistency and discovery

- [x] Integrated Regen section live at `smtop100.blog/regen/` with Rules, Archive and Join child pages.
- [x] Redirect old Regen public domain to the integrated section.
- [x] Finish/review the main Micro.blog Pages: About, Rules, Contact / Join and Support.
- [x] Add an Explore hub for competitions, history, awards, democracy, search, categories, writing, Subscribe and Support.
- [x] Surface Youth Cup and World Club Cup explicitly rather than relying only on the generic Tournaments label.
- [x] Simplify navigation across Tournaments, Community Polls, Manager Portal and Manager Awards.
- [ ] Merge and verify the same simplified family shell on Stats & History and Publishing Desk.
- [ ] Review the chronological Posts Archive and distinguish it clearly from Stats & History.
- [ ] Finalise the minimal live editorial taxonomy; keep historical metadata without recreating WordPress clutter.
- [ ] Improve active/dormant club-record browsing under Team News.
- [ ] Audit navigation on desktop/mobile across the live blog and every specialist app after the final shell changes merge.
- [ ] Check typography, spacing, forms, cards, tables and dark-mode contrast across the family.
- [ ] Finish social-card consistency across the Top 100 family.
- [ ] Check feeds, search, archive discovery and key legacy inbound URLs.
- [ ] Maintain an explicit redirect register for important WordPress/Blogger/Regen URLs that do not map automatically.

## Manager identity, Community Polls and Awards

**Status: Top 100 production architecture complete; real-world use and broader Regen scoping remain the next acceptance gates.**

- [x] Shared Supabase manager identity reused by Manager Portal, Publishing Desk, Community Polls and Awards.
- [x] One-manager-one-vote, deadlines, electorate snapshots, ballot editing, audit trail and result visibility controls.
- [x] Public Community Poll Results at `vote.smtop100.blog/`.
- [x] Authenticated Community Poll voting at `vote.smtop100.blog/vote`.
- [x] Manager Awards at `awards.smtop100.blog`, with current voting and historical Hall of Fame/history separated cleanly.
- [x] Manager lifecycle admin can add managers, mark them inactive and reactivate returning managers without deleting history.
- [x] Deactivation disables linked Top 100 Manager Portal access and delegated Top 100 tournament organiser/assistant access.
- [x] Internal rollback-only database tests completed for manager create/deactivate/reactivate behaviour and electorate snapshot logic.
- [ ] Add explicit world scoping to voting events so Top 100 and Regen can run separate polls using the same identity/voting foundation.
- [ ] Add Regen-specific Awards and Regen-only public/authenticated voting views without mixing electorates or results with Top 100.
- [ ] Before the next genuine production poll/Awards round, reconcile the active Top 100 manager roster against linked/approved Manager Portal accounts and resolve every unexplained omission.
- [ ] Onboard current managers who should be eligible but do not yet have a linked/approved account before opening the production event.
- [ ] Exercise the new Awards system with the next genuine Awards round.
- [ ] After successful real-world Awards use, remove the executable legacy typed-name Awards voting backend while retaining historical data/reference material.
- [ ] Reuse the shared voting service for other community/tournament votes where useful.

## Never miss a thing

Youth Cup reminders are now live as an authenticated Manager Portal benefit. They are tied to the manager's verified Top 100 identity and use the manager account email, rather than the general blog Subscribe list.

Current and planned reminder types:

- [x] Youth Cup fixture reminders: new fixture / next-round assignment, day-before reminder, fixture-day reminder if the result is still outstanding.
- [ ] World Club Cup fixture/registration reminders.
- [ ] Community Poll opening and closing reminders.
- [ ] Manager Awards opening and closing reminders.
- [ ] Tournament registration deadlines.

Keep reminders opt-in, clearly scoped and easy to switch off. Public Subscribe remains the front door for blog/newsletter delivery; targeted manager reminders belong to the authenticated Manager Portal preference layer.

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
- [ ] Retire or redirect obsolete standalone subdomains only after their replacement destinations are proven.
- [ ] Decide whether trusted regular contributors need native Micro.blog Family/team-author access in addition to the Publishing Desk.

## Non-goals

- Rebuilding structured specialist apps inside the blog.
- Recreating WordPress category/tag sprawl.
- Deleting historical material merely because it is no longer in live navigation.
- Treating Top 100 Regen as merely another Top 100 app; it remains a distinct game world even though its editorial pages live inside the main site.
- Allowing automated governance tooling to make unreviewed contentious decisions.
