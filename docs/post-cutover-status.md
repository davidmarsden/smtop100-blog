# Post-cutover status — 10 September 2026

`smtop100.blog` is now live on Micro.blog. The migration phase is complete enough that the project focus has shifted from proving the move to refining the live site and retiring legacy plumbing carefully.

## Live architecture

- `smtop100.blog` — main editorial/community site on Micro.blog, including the integrated Top 100 Regen section at `/regen/`.
- `archive.smtop100.blog` — Stats & History.
- `tournaments.smtop100.blog` — Youth Cup / World Club Cup tournament manager and Manager Portal.
- `vote.smtop100.blog/` — public Top 100 Voting Results.
- `vote.smtop100.blog/vote` — authenticated Top 100 Manager Voting.
- `awards.smtop100.blog` — Top 100 Manager Awards voting plus Hall of Fame/history.
- `top100regen.website` — legacy Regen domain to redirect after the `/regen/` section and content migration are verified.

The shared ecosystem navigation is centred on: **Top 100 · Stats & History · Tournaments · Voting Results · Vote · Awards · Regen**.

Regen is a distinct game world, but its editorial/home pages now belong inside the main Top 100 site instead of consuming a separate Micro.blog site slot. The target paths are `/regen/`, `/regen/rules/`, `/regen/archive/` and `/regen/join/`.

## Shared manager identity

The canonical Top 100 manager lifecycle now feeds Manager Portal access, Voting and Awards. Managers are preserved historically rather than deleted. Administrators can add a manager, mark somebody inactive when they leave, and reactivate a returning manager.

Membership is explicitly scoped by game world. Regen-only and seeded-test identities therefore do not count as current Top 100 managers or enter future Top 100 voting electorates.

When a manager is deactivated:

- their Top 100 Manager Portal account is disabled;
- future Voting/Awards electorates exclude them;
- active delegated organiser/assistant roles on Top 100 tournaments are revoked;
- already-open voting electorates remain frozen and are not silently rewritten.

## Internal verification

Rollback-only production-database tests were run after the lifecycle migration. They created a temporary canonical manager, deactivated and reactivated that manager, checked lifecycle state/audit behaviour, and rolled the transaction back so no test identity remained.

A second rollback-only test created a hidden test poll, opened it, and verified that the electorate snapshot exactly matched the current eligible Top 100 account/membership count before rolling the transaction back.

At the time of the check there were **103 active Top 100 memberships** and **22 active, linked Top 100 Manager Portal accounts**, so **22 managers were currently eligible to cast an authenticated ballot**.

That result proves the electorate filter is behaving consistently, but it is **not** a sign-off that the production electorate is complete. Before the next genuine All-Manager Poll or Awards round, the active-manager roster must be reconciled against linked/approved Manager Portal accounts and every unexplained omission resolved or deliberately accounted for. Eligible current managers who have not yet claimed or had an account approved need to be onboarded before the event opens; once opened, the electorate snapshot is intentionally frozen.

## Voting and Awards scope

The current Voting and Awards services are still for the original Top 100 world only. Regen must not be sent into those electorates merely because its pages now live under `smtop100.blog`.

The next shared-voting extension should make every event explicitly belong to a game world, allowing Top 100 and Regen to run separate polls and Awards using the same authenticated manager identity without mixing electorates, ballots or results.

## Awards transition

Current Top 100 Awards voting uses the shared authenticated manager identity/voting system. The historical Hall of Fame, cabinets, records and previous-season data remain intact.

The old typed-name voting implementation should remain only until the new system has survived a genuine Awards round. After that, remove the executable legacy voting path while preserving any historical data/reference material required by the archive.

## Immediate next work

The main work is now on the live Micro.blog site itself: publish and verify the integrated `/regen/` section; migrate standalone Regen posts worth retaining; redirect the old Regen domain; free the separate Regen Micro.blog site slot; finish and polish About, Rules, Contact and Support; improve archive/taxonomy/club-record discovery; check redirects and inbound legacy URLs; and continue theme/navigation/mobile/accessibility cleanup.

In parallel, complete the Top 100 electorate reconciliation/onboarding gate before any genuine production vote and build explicit Regen-scoped Voting and Awards before exposing those services to Regen managers.
