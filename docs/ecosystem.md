# Top 100 ecosystem map

This document records the role and intended future of each known Top 100 destination.

| Destination | Current role | Future | Notes |
| --- | --- | --- | --- |
| `smtop100.blog` | Main Micro.blog editorial/news site and historical blog archive | **Keep as main home** | Front door, editorial layer, current Rules, About, Contact, Support, chronological post archive and the integrated Regen section at `/regen/`. |
| `archive.smtop100.blog` | Season, manager and historical statistics | **Keep / expand** | Canonical structured-history destination. Present in the UI as **Top 100 Stats & History** or **Top 100 History**, not simply Archive. |
| `tournaments.smtop100.blog` | Tournament tooling and competition history | **Keep / expand** | Supports Youth Cup, World Club Cup, Regen competitions and future tournaments. |
| `manager.smtop100.blog` | Canonical Manager Portal and manager-account identity entry point | **Keep / expand** | Public home for manager sign-in, account identity and manager-only entry points. Shared identity is reused by Voting, Awards and other authenticated tools. |
| `rules.smtop100.blog` | Standalone rules/governance site | **Retire after rewrite** | Canonical current Top 100 Rules belong at `smtop100.blog/rules/`; preserve historical rule versions separately. |
| `vote.smtop100.blog` | Top 100 Voting Results and authenticated voting | **Keep / extend by game world** | Current service is Top-100-only; Regen should use the same backend only after explicit game-world scoping. |
| `awards.smtop100.blog` | Top 100 Manager Awards voting and history | **Keep / extend by game world** | Current Awards are Top-100-only. Regen Awards should reuse the same identity/voting foundation with separate world-scoped events and results. |
| `smtop100.blog/regen/` | Planned integrated Regen editorial/reference section | **Publish and verify** | Regen remains a distinct game world but no longer needs its own Micro.blog site. |
| `top100regen.website` | Current standalone Regen site | **Redirect / retire** | Keep until `/regen/` and retained content are verified, then redirect into the integrated section and free the Micro.blog site slot. |
| `legends.smtop100.blog` | Standalone historical/editorial concept | **Likely retire/absorb** | Preserve good material; move editorial stories to main site and structured facts to Stats & History. |
| `managers.smtop100.blog` | Standalone manager/community concept | **Likely retire/absorb** | Stats & History now provides a better long-term home for manager profiles/careers. This plural hostname is separate from the canonical singular `manager.smtop100.blog` account portal. |

## Main-site pages

The main Micro.blog site should own ordinary editorial/reference pages rather than splitting them into unnecessary subdomains:

- `/about/`
- `/rules/`
- `/contact/`
- `/support/`
- `/archive/` — Micro.blog's chronological **Posts Archive**
- `/regen/`
- `/regen/rules/`
- `/regen/archive/`
- `/regen/join/`

This `/archive/` must remain clearly distinct from `archive.smtop100.blog`, which is the structured **Top 100 Stats & History** application.

## Desired user mental model

The permanent ecosystem should feel like one Top 100 family with a small number of clear destinations:

1. **Top 100** — what is happening, what managers are writing, and the current rules/reference pages.
2. **Stats & History** — what happened, who did it and the statistical record.
3. **Tournaments** — competitions happening now and their histories.
4. **Voting** — manager-authenticated ballots and public results, explicitly scoped by game world.
5. **Awards** — recognition and award history, likewise scoped by game world.
6. **Regen** — a distinct sister Top 100 game world whose editorial/reference pages live under `/regen/`.
7. **Manager** — the canonical account and identity entry point for authenticated manager services.

A concise ecosystem nav can therefore be:

`Top 100 · Stats & History · Tournaments · Voting · Awards · Regen · Manager`

Rules belongs within Top 100 itself.

## Shared manager accounts

The ecosystem uses one manager identity rather than separate logins per app. `manager.smtop100.blog` is the canonical public entry point for that identity. Membership, account access and voting eligibility must remain explicitly scoped by game world so the same person can belong to Top 100, Regen or both without crossing electorates or permissions.

## Governance/admin tooling opportunity

The current structure exposes several jobs that deserve proper tooling:

- **Transfer bans** — structured records, automatic dates/expiry, public current/history views and less manual upkeep.
- **Rule adjudication** — versioned current/historical rules plus assisted rule application, with human confirmation and a recorded rationale.
- **Manager appointments** — vacancy publishing, applications, eligibility, agreed criteria, scoring/assessment, decisions and audit trail.
- **All-manager polling** — authenticated electorate, deadlines, one vote per manager, published outcomes and links to resulting rule changes.

These can share the manager identity layer while remaining world-scoped.

## Top 120 precedent

`Top 120` is a useful historical precedent. It was Top 100's legacy sister game world and its material should remain in the archive. Top 100 Regen should avoid repeating the old pattern of becoming a disconnected sibling site; integrating its editorial home at `/regen/` makes the relationship explicit while preserving its separate-world identity.

## Cross-site design review

All surviving apps and sections should share a family resemblance: common global navigation, logo/wordmark treatment, typography and spacing, predictable forms/cards/tables/buttons, mobile and accessibility behaviour, consistent footer language and social-card treatment.

Regen should retain its own lime/green cues within that shared family design.
