# Current architecture

## Main site

`https://smtop100.blog/`

- Platform: Micro.blog.
- History: originally a Blogger site, later imported into WordPress, then migrated to Micro.blog in September 2026.
- Function today: editorial/news site plus the historical blog archive and front door to the wider Top 100 ecosystem.
- Strategic direction: refine the live site, improve discovery and retire legacy plumbing carefully rather than continuing migration-era duplication.

## Current subdomain apps

### Archive

`https://archive.smtop100.blog/`

Structured season and manager history/statistics. This is the natural home for data-heavy historical material that is awkward to represent as blog categories or pages.

### Tournaments

`https://tournaments.smtop100.blog/`

Tournament management for the Youth Cup, World Club Cup and future competitions, with support for multiple live competitions and delegated organisers.

### Manager

`https://manager.smtop100.blog/`

The canonical Top 100 Manager Portal and manager-account identity entry point. It uses the same underlying shared manager identity as Voting and Awards. The former `tournaments.smtop100.blog/manager` route remains only for backwards compatibility.

### Rules

`https://rules.smtop100.blog/`

Still-live transitional standalone rules/governance site. The canonical long-term destination is `https://smtop100.blog/rules/`, but the subdomain must remain available until the replacement page has been rewritten, published and verified, with useful legacy entry points redirected afterwards.

### Voting

`https://vote.smtop100.blog/`

Public Voting Results at the root, with authenticated manager voting at `/vote` using the shared Manager Portal identity.

### Awards

`https://awards.smtop100.blog/`

Manager Awards voting, Hall of Fame, manager cabinets and award records. Authenticated voting reuses the same canonical manager identity.

### Legends

`https://legends.smtop100.blog/`

An editorial/history experiment. The underlying idea remains useful, but the standalone destination has not established a clear enough role. Candidate for absorption into the main site and/or Archive.

### Managers

`https://managers.smtop100.blog/`

An earlier manager-profile/community experiment that did not attract sustained use. The newer Archive manager/career tools now cover much of the useful concept more effectively. Candidate for retirement and redirect into Archive manager pages. This plural hostname is unrelated to the live singular `manager.smtop100.blog` account portal.

## Architectural direction

The ecosystem grew organically, but the main services now share a coherent navigation and identity model. The remaining work is consolidation rather than reinvention:

1. keep the main site as the clear front door;
2. keep specialist tools on purpose-specific subdomains;
3. use `manager.smtop100.blog` as the single public entry point for manager identity;
4. keep Voting and Awards on the same shared manager account system; and
5. retire or redirect older duplicate destinations only after the replacement paths have been proven in production.
