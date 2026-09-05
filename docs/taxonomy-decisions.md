# Taxonomy decisions

This document records the editorial and archival decisions for the Top 100 WordPress taxonomy as part of the redesign and eventual migration to Micro.blog.

## Core principle

A large amount of the existing WordPress content is historical archive material. It should be preserved as a matter of principle, but preservation does **not** mean every item needs to remain prominent on the live main site.

The redesign should distinguish between:

- **Live editorial content** — current news, previews, reviews, announcements and actively maintained club records.
- **Structured app content** — material better handled by Tournaments, Awards, Archive or Rules.
- **Historical archive content** — preserved and retrievable, but not necessarily surfaced as part of the main site's everyday navigation.

## Current decisions

| Taxonomy / series | Decision | Notes |
| --- | --- | --- |
| Season Predictions and Reviews | KEEP | Must retain both previews and reviews. The current label is clunky but accurately reflects that the category contains both. A future rename should preserve that distinction rather than reducing it to only "Season Reviews". |
| Team of the Week | ARCHIVE | Historically important but not maintained for years. Preserve the material, but it does not need to be treated as an active editorial series. |
| Back Pages | ARCHIVE | Historically important but not maintained for years. Preserve as archive material rather than an active section of the live site. |
| Youth Cup | MOVE CONCEPTUALLY TO TOURNAMENTS | Current and future structured competition material belongs at `tournaments.smtop100.blog`; historical editorial material should still be preserved. |
| World Club Cup | MOVE CONCEPTUALLY TO TOURNAMENTS | Same principle as Youth Cup: tournament data and live competition workflows belong in Tournaments, while historical posts remain preserved. |
| Manager Awards | MOVE CONCEPTUALLY TO AWARDS | Voting, records and Hall of Fame material belong at `awards.smtop100.blog`; historical editorial posts remain preserved. |
| Espanyol | KEEP — ACTIVE CLUB RECORD | This is a live and regularly updated club-specific record written by one of the community's most active managers. It must remain available in a meaningful form and should not be treated as disposable taxonomy cruft. |
| Hamburger | KEEP — ACTIVE CLUB RECORD | This is David's own ongoing club record across seasons. It must remain available in a meaningful form. |
| D1 / D2 / D3 / D4 / D5 tags | PRESERVE AS STRUCTURED METADATA | Useful historical and analytical dimensions; should survive migration even if the presentation changes. |
| S1 / S2 / ... season tags | PRESERVE AS STRUCTURED METADATA | Essential for historical organisation and migration into season-aware archive views. |

## Important distinction: club records

Club-specific categories are not disposable just because they are currently dormant.

A club category may be inactive because the manager who maintained it stopped writing, changed club, or left the game. A future manager could revive that same club record. We should therefore preserve club categories as reusable community infrastructure, not treat inactivity as a reason to delete them.

For each club category we should determine:

1. Is it currently being updated?
2. Is it written as an ongoing club diary / record?
3. Does it have a consistent author or manager identity?
4. Is it dormant but potentially reusable by a future manager?
5. Does it deserve a permanent landing page or archive view?
6. Should it remain on the main site, move into Archive, or be represented in both places?

This suggests three useful club states rather than simply live/dead:

- **ACTIVE CLUB RECORD** — currently maintained and visibly accessible.
- **DORMANT CLUB RECORD** — preserved, not prominent, but explicitly available for revival by a future manager.
- **HISTORICAL CLUB ARCHIVE** — historical material that should remain retrievable even if the club no longer has a continuing editorial record.

Espanyol and Hamburger are confirmed examples of active club records that must be retained prominently in some form. Dormant club categories should remain recoverable and capable of becoming active again without creating a parallel duplicate category.

## Archive strategy

"Archive" should not mean deletion, hiding from export, or losing URLs.

The preferred model is:

- preserve the original content and historical URLs where practical;
- remove dormant series from primary navigation;
- surface them through a dedicated archive/search/browse experience;
- retain metadata such as season, division, competition and club;
- preserve dormant club records in a form that can be reactivated;
- avoid forcing every historical category to remain a first-class live-site navigation item.

This gives us a cleaner present-day site without sacrificing eleven years of community history or closing off future revival of old club records.

## Next audit step

The next taxonomy pass should classify all significant categories into these states:

- **LIVE** — actively maintained and should remain visibly accessible;
- **APP** — current structured function belongs in one of the subdomain apps;
- **ARCHIVE** — preserve but remove from active navigation;
- **METADATA** — retain as a useful historical dimension rather than a main editorial category;
- **REVIEW** — unclear and requires human judgement.

Club-specific categories should be reviewed individually and additionally marked as **ACTIVE CLUB RECORD**, **DORMANT CLUB RECORD**, or **HISTORICAL CLUB ARCHIVE** rather than bulk-retired.
