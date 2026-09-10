# Post-cutover status — 10 September 2026

`smtop100.blog` is now live on Micro.blog. The migration phase is complete enough that the project focus has shifted from proving the move to refining the live site and retiring legacy plumbing carefully.

## Live architecture

- `smtop100.blog` — main editorial/community site on Micro.blog.
- `archive.smtop100.blog` — Stats & History.
- `tournaments.smtop100.blog` — Youth Cup / World Club Cup tournament manager and Manager Portal.
- `vote.smtop100.blog/` — public Voting Results.
- `vote.smtop100.blog/vote` — authenticated Manager Voting.
- `awards.smtop100.blog` — Manager Awards voting plus Hall of Fame/history.
- `top100regen.website` — current Top 100 Regen sister-world site.
- `regen.smtop100.blog` — planned future hostname for Top 100 Regen once that separate move is complete.

The shared ecosystem navigation is now centred on: **Top 100 · Stats & History · Tournaments · Voting Results · Vote · Awards · Regen**.

## Shared manager identity

The canonical Top 100 manager lifecycle now feeds Manager Portal access, Voting and Awards. Managers are preserved historically rather than deleted. Administrators can add a manager, mark somebody inactive when they leave, and reactivate a returning manager.

Top 100 membership is explicitly scoped by game world. Regen-only and seeded-test identities therefore do not count as current Top 100 managers or enter future Top 100 voting electorates.

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

## Awards transition

Current Awards voting now uses the shared authenticated manager identity/voting system. The historical Hall of Fame, cabinets, records and previous-season data remain intact.

The old typed-name voting implementation should remain only until the new system has survived a genuine Awards round. After that, remove the executable legacy voting path while preserving any historical data/reference material required by the archive.

## Immediate next work

The main work is now on the live Micro.blog site itself: finish and polish About, Rules, Contact and Support; improve archive/taxonomy/club-record discovery; check redirects and inbound legacy URLs; and continue theme/navigation/mobile/accessibility cleanup.

In parallel, complete the electorate reconciliation/onboarding gate before any genuine production vote, and move Top 100 Regen from `top100regen.website` to `regen.smtop100.blog` only when that separate site migration is ready.
