# Taxonomy decisions

This document records the editorial and archival decisions for the Top 100 WordPress taxonomy as part of the redesign and eventual migration to Micro.blog.

## Core principle

A large amount of the existing WordPress content is historical archive material. It should be preserved as a matter of principle, but preservation does **not** mean every item needs to remain prominent on the live main site.

The redesign should distinguish between:

- **Live editorial content** — current news, previews, reviews, announcements and actively maintained club records.
- **Structured app content** — material better handled by Tournaments, Awards, Archive or Rules.
- **Historical archive content** — preserved and retrievable, but not necessarily surfaced as part of the main site's everyday navigation.

The main site should increasingly act as the editorial/community front door, while structured and repetitive functions move into the dedicated apps where those apps can do the job better.

## Current decisions

| Taxonomy / series | Decision | Notes |
| --- | --- | --- |
| Uncategorized | MOSTLY ARCHIVE / REVIEW | Largely a legacy of managers not understanding or remembering to add categories. Likely to contain mixed states, but probably mostly archival. Do not treat `Uncategorized` as a meaningful editorial category. Reclassify automatically where confidence is high; otherwise preserve without forcing a new category. |
| Season Predictions and Reviews | LIVE + ARCHIVE + APP-RELATED | Still active and goes back many seasons. It contains both previews and reviews and that distinction must be preserved. Malcolm's twice-seasonly prediction/review updates are now partly duplicated by data in `archive.smtop100.blog`; over time the Archive app may become the primary structured destination while editorial posts remain available where they add commentary/context. |
| Team of the Week | ARCHIVE | Historically important but not maintained for years. Preserve the material, but it does not need to be treated as an active editorial series. |
| Back Pages | ARCHIVE | Historically important but not maintained for years. Preserve as archive material rather than an active section of the live site. |
| Top 100 Media | ARCHIVE | Historical media/promotion material. Preserve and make discoverable through archive/search rather than primary navigation. |
| Future Transfers | ARCHIVE | Historical series; preserve but do not treat as active navigation. |
| World Club Shield | ARCHIVE | Historical competition material. Preserve; current/future structured competition activity belongs in Tournaments. |
| Top 120 | ARCHIVE | Legacy sister game world. Preserve as part of Top 100 history, but do not present as a current destination. |
| Player Awards | ARCHIVE | Historical awards material. Preserve; active recognition workflows now live elsewhere. |
| Match Preview | ARCHIVE | Historical editorial series. Preserve, but do not treat as an active section of the current site. |
| Team of the Season | ARCHIVE | Historical editorial/awards series. Preserve, but do not treat as an active current section. |
| Youth Cup | LIVE + TOURNAMENTS | Active and historically deep. Includes organiser updates and match reports. Structured fixtures, registration, results, tables and progression should increasingly live in `tournaments.smtop100.blog`; editorial match reports and genuinely useful organiser commentary can remain on the main site. |
| World Club Cup | LIVE + TOURNAMENTS | Same model as Youth Cup: active and historically deep, with organiser updates and match reports. The Tournament app should become the primary operational destination, while editorial coverage remains optional rather than mandatory duplication. |
| Team News | LIVE PARENT CATEGORY | Parent category for club-specific posts such as Espanyol and Hamburger. It should remain conceptually available as the umbrella for manager-written club records, even if the presentation changes in a future migration. |
| Managers | LIVE PARENT CATEGORY / REVIEW PRESENTATION | Parent category for manager-related material. Keep the organising concept, but review whether it needs visible navigation now that manager profiles and career history increasingly belong in Archive. |
| Stats | LIVE PARENT CATEGORY / APP-RELATED | Parent category for statistical material. Keep the organising concept, but structured stats should increasingly point to Archive rather than duplicating app functionality in posts. |
| Admin | LIVE / OCCASIONAL | Used by the game-world administrator for important news affecting everyone. Keep available and clearly identifiable, but it does not need to dominate navigation. |
| Manager Awards | LIVE POINTER + AWARDS APP | Current WordPress posts are now mainly organiser updates and signposts directing managers to `awards.smtop100.blog` to vote or view results. The Awards app is the primary functional destination; the main site only needs announcements when they add value. Historical Awards posts remain preserved. |
| Espanyol | KEEP — ACTIVE CLUB RECORD | Live and regularly updated, with a history spanning different managers. This demonstrates that club records belong to the club/community history, not solely to one author. Must remain meaningfully accessible. |
| Hamburger | KEEP — ACTIVE CLUB RECORD | David's ongoing club record across seasons. Must remain meaningfully accessible. |
| D1 / D2 / D3 / D4 / D5 tags | PRESERVE AS STRUCTURED METADATA | Useful historical and analytical dimensions; should survive migration even if the presentation changes. |
| S1 / S2 / ... season tags | PRESERVE AS STRUCTURED METADATA | Essential for historical organisation and migration into season-aware archive views. |

## Important distinction: club records

Club-specific categories are not disposable just because they are currently dormant.

A club category may be inactive because the manager who maintained it stopped writing, changed club, or left the game. A future manager could revive that same club record. We should therefore preserve club categories as reusable community infrastructure, not treat inactivity as a reason to delete them.

Club records can also span multiple managers over time. Espanyol is a confirmed example: the value is the continuing history of the club within Top 100, not merely one manager's authorship.

For each club category we should determine:

1. Is it currently being updated?
2. Is it written as an ongoing club diary / record?
3. Does it span more than one manager?
4. Is it dormant but potentially reusable by a future manager?
5. Does it deserve a permanent landing page or archive view?
6. Should it remain on the main site, move into Archive, or be represented in both places?

This suggests three useful club states rather than simply live/dead:

- **ACTIVE CLUB RECORD** — currently maintained and visibly accessible.
- **DORMANT CLUB RECORD** — preserved, not prominent, but explicitly available for revival by a future manager.
- **HISTORICAL CLUB ARCHIVE** — historical material that should remain retrievable even if the club no longer has a continuing editorial record.

Dormant club categories should remain recoverable and capable of becoming active again without creating a parallel duplicate category.

## App substitution principle

Where a dedicated app now performs a repetitive or structured function better than WordPress posts, the app should become the primary destination.

This applies especially to:

- **Tournaments** — registration, fixtures, results, tables, progression and organiser workflow can reduce or eliminate the need for routine tournament update posts.
- **Archive** — structured season, manager, club and historical data can reduce duplication in recurring prediction/review posts where the post is primarily reporting data already available in the app.
- **Awards** — voting and results already belong in the Awards app; main-site posts are mainly useful as announcements or pointers.

This should not mean banning editorial posts. Match reports, analysis, opinion, previews and commentary still belong on the main site when they add something human that the app does not.

A key redesign goal should therefore be to make the apps prominent enough that managers naturally use them directly, instead of requiring a WordPress post every time an organiser needs to tell people where to look.

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
- **APP** — current structured function belongs primarily in one of the subdomain apps;
- **LIVE + APP** — active editorial material remains valuable, but structured/repetitive functionality should be handled by an app;
- **ARCHIVE** — preserve but remove from active navigation;
- **METADATA** — retain as a useful historical dimension rather than a main editorial category;
- **REVIEW** — unclear and requires human judgement.

Club-specific categories should be reviewed individually and additionally marked as **ACTIVE CLUB RECORD**, **DORMANT CLUB RECORD**, or **HISTORICAL CLUB ARCHIVE** rather than bulk-retired.
