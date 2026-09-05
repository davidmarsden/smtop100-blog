# Micro.blog prototype migration test

Prototype destination: `https://smtop100.micro.blog/`

This is the first controlled WordPress → Micro.blog migration rehearsal. The goal is to test a deliberately small but awkward sample before attempting a large import.

## Test package

A compact WordPress WXR import file has been generated containing:

- **10 selected posts/pages** covering current, historical and legacy content patterns;
- **50 attachment records** associated with those selected items;
- relevant authors and taxonomy definitions required by the sample.

The test file is intentionally not the full WordPress export.

## Selected content

1. **Big Bertha Sign's The Good Doctor** — 12 Aug 2015 — Blogger-era legacy post.
2. **Game World Rules** — 29 Jun 2017 — keeper page / future Rules redirect candidate.
3. **About Top 100** — 19 Aug 2019 — keeper page.
4. **Hamburger U20 Development Squad** — 9 Apr 2021 — legacy/embed/media stress test.
5. **Youth Cup Carnage** — 26 Oct 2025 — tournament/editorial content.
6. **Espanyol Season Review: Against All Odds – A Youth Revolution in Full Flow!** — 11 Jun 2026 — active club record spanning managers.
7. **The Entertainers** — 19 Jun 2026 — recent Hamburger club record.
8. **Season 28 Division 1 Stats and Facts** — 26 Jun 2026 — current season prediction/review/statistics material.
9. **WORLD CLUB CUP S28** — 1 Jul 2026 — current World Club Cup organiser/update post.
10. **Introducing the Youth Cup Tournament App** — 23 Jul 2026 — recent image-heavy app/tournament post.

## What to inspect after import

For every item, record whether the following survived correctly:

- title and publication date;
- body formatting;
- images/media;
- embeds and unusual HTML;
- categories/tags;
- resulting Micro.blog URL;
- internal links;
- any obvious WordPress/Blogger artefacts.

## Media test

The WXR contains attachment records and WordPress media URLs, not local media binaries. One purpose of this rehearsal is therefore to establish whether Micro.blog copies/fetches these assets into its own media library or leaves imported posts dependent on WordPress-hosted files.

Do not assume migration is complete merely because an image renders immediately after import: inspect the resulting image URL.

## Pass criteria

The first rehearsal is successful if:

- all ten selected posts/pages import;
- recent and legacy HTML remain readable;
- important media is copied or can be migrated predictably;
- dates and authorship are sensible;
- category behaviour is understandable;
- permalink differences are small enough to map with redirects;
- no failure suggests that a full selective migration is impractical.

## Next step after the rehearsal

Use the completed checklist to classify each problem as:

- **IMPORT OK** — no intervention needed;
- **THEME FIX** — content imported correctly but presentation needs Hugo/theme work;
- **CONTENT TRANSFORM** — source content needs an automated cleanup during migration;
- **MEDIA MIGRATION** — asset needs copying/remapping;
- **REDIRECT** — URL needs an explicit redirect;
- **MANUAL REVIEW** — exceptional content that should not dictate the bulk workflow.

If this sample behaves well, expand to a second rehearsal covering a much larger representative slice before any domain cutover.
