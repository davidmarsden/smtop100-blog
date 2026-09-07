# Top 100 ecosystem map

This document records the role and intended future of each known Top 100 destination.

| Destination | Current role | Future | Notes |
| --- | --- | --- | --- |
| `smtop100.blog` | WordPress editorial/news site and historical blog archive | **Migrate to Micro.blog and keep as main home** | Front door, editorial layer, current Rules, About, Contact, Support and chronological post archive. |
| `archive.smtop100.blog` | Season, manager and historical statistics | **Keep / expand** | Canonical structured-history destination. Present in the UI as **Top 100 Stats & History** or **Top 100 History**, not simply Archive. |
| `youth-cup.smtop100.blog` | Youth Cup and tournament tooling | **Rename/evolve to `tournaments.smtop100.blog`** | Broaden beyond one competition; support multiple organisers and live tournaments. |
| `rules.smtop100.blog` | Standalone rules/governance site | **Retire after rewrite** | Canonical current Rules should become `smtop100.blog/rules/`; preserve historical rule versions separately and redirect old entry points. |
| `awards.smtop100.blog` | Manager Awards voting and history | **Keep / review** | Voting, Hall of Fame, cabinets and records. Move toward shared manager-account authentication. |
| `top100regen.website` | Separate sister game-world website | **Move under Top 100 umbrella; proposed `regen.smtop100.blog`** | Regen is not an app. It remains a distinct game-world website with shared family branding/navigation. |
| `legends.smtop100.blog` | Standalone historical/editorial concept | **Likely retire/absorb** | Preserve good material; move editorial stories to main site and structured facts to Stats & History. |
| `managers.smtop100.blog` | Standalone manager/community concept | **Likely retire/absorb** | Stats & History now provides a better long-term home for manager profiles/careers. |

## Main-site pages

The Micro.blog main site should own ordinary editorial/reference pages rather than splitting them into unnecessary subdomains:

- `/about/`
- `/rules/`
- `/contact/`
- `/support/`
- `/archive/` — Micro.blog's chronological **Posts Archive**

This `/archive/` must remain clearly distinct from `archive.smtop100.blog`, which is the structured **Top 100 Stats & History** application.

## Desired user mental model

The permanent ecosystem should feel like one Top 100 family with a small number of clear destinations:

1. **Top 100** — what is happening, what managers are writing, and the current rules/reference pages.
2. **Stats & History** — what happened, who did it and the statistical record.
3. **Tournaments** — competitions happening now and their histories.
4. **Awards** — recognition, manager-authenticated voting and award history.
5. **Regen** — a separate sister Top 100 game world, visibly part of the same family but not an app within the original world.

A concise ecosystem nav can therefore be:

`Top 100 · Stats & History · Tournaments · Awards · Regen`

Rules belongs within Top 100 itself.

## Shared manager accounts

The ecosystem should move toward one manager identity rather than separate logins per app.

The Publishing Desk already reuses Tournament Manager's Supabase manager accounts. Review whether the same account layer can also power:

- Awards voting;
- all-manager polls;
- tournament administration;
- manager applications and appointment workflows;
- authenticated admin/governance tools;
- future manager-specific features.

This is especially important for voting: eligibility, one-manager-one-vote, auditability and manager attribution should come from the manager account rather than from a free-form name field.

## Governance/admin tooling opportunity

The current site structure exposes several jobs that deserve proper tooling:

- **Transfer bans** — structured records, automatic dates/expiry, public current/history views and less manual upkeep.
- **Rule adjudication** — versioned current/historical rules plus assisted rule application, with human confirmation and a recorded rationale.
- **Manager appointments** — vacancy publishing, applications, eligibility, agreed criteria, scoring/assessment, decisions and audit trail.
- **All-manager polling** — authenticated electorate, deadlines, one vote per manager, published outcomes and links to resulting rule changes.

These can share the manager identity layer even if the public-facing pieces ultimately live in different apps/pages.

## Top 120 precedent

`Top 120` is a useful historical precedent. It was Top 100's legacy sister game world and its material should remain in the archive. Top 100 Regen should avoid repeating the old pattern of becoming a disconnected sibling site. Moving it to `regen.smtop100.blog` would make the relationship explicit while preserving its separate-world identity.

## Cross-site design review

All surviving apps/sites should be reviewed as part of the migration rather than treated as finished islands.

Review:

- shared global navigation;
- common logo/wordmark treatment;
- typography and spacing;
- form, card, table and button conventions;
- mobile layout;
- accessibility;
- consistent footer links and ownership language;
- shared social-card family;
- canonical links back to `smtop100.blog`;
- clear indication when a user is entering a specialist app or the separate Regen website;
- authentication UX wherever manager accounts are used.

The goal is family resemblance and predictable interaction patterns, not forcing every app or sister-world page into an identical UI.