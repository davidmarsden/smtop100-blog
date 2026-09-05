# Migration to Micro.blog

The active plan is now to build and test the replacement directly in Micro.blog at `https://smtop100.micro.blog/`, rather than redesigning WordPress first.

WordPress remains the live production site until the replacement is proven. It is now a source system and safety net, not the target architecture.

## Strategy

Use the Micro.blog prototype to implement the future site directly:

- editorial/community front door on `smtop100.blog`;
- structured history in Archive;
- competitions in Tournaments;
- voting/recognition in Awards;
- governance in Rules;
- sister-world identity for Top 100 Regen, preferably at `regen.smtop100.blog`.

The working ecosystem navigation is:

`Top 100 · Archive · Tournaments · Awards · Rules · Regen`

The migration should be selective and deliberate. Preserve history, but do not recreate WordPress's accumulated taxonomy, page and media clutter unless it still serves a purpose.

## What has already been decided

- The WordPress WXR content export is preserved.
- A separate WordPress media/attachment export manifest is preserved.
- All 86 categories have been triaged.
- All 105 pages have been triaged; only a small set needs to survive in a live/redirected/merged form.
- Dormant club categories remain reusable club records rather than disposable taxonomy.
- The main blog should stop duplicating repetitive structured information when a dedicated app handles it better.
- The Micro.blog prototype site has been created.

## Prototype import plan

Do not begin by trying to make the whole eleven-year archive perfect.

Start with a representative sample containing:

1. a recent normal editorial post;
2. an active club-record post;
3. a current tournament post;
4. a Season Predictions and Reviews post;
5. a Blogger-era historical post;
6. an image-heavy post;
7. a post with embeds or unusual HTML;
8. one or two pages that we intend to keep.

For each sample, verify:

- title and body formatting;
- author/date preservation;
- categories/tags;
- images and media URLs;
- internal links;
- resulting permalink;
- feed output and social metadata where relevant.

Once the representative sample behaves well, test a much larger/full import.

## Permalinks and redirects

The migration should preserve existing post URLs where Micro.blog permits it. Where paths cannot be reproduced exactly, record explicit redirects.

Special attention should be paid to:

- old Blogger-derived slugs;
- WordPress date-based URLs and other historical path patterns;
- pages linked externally;
- active club archives;
- high-value historical posts;
- links from Archive, Awards, Tournaments, Rules and Regen back into the main site;
- attachment/media URLs that matter to migrated content.

We do not need to preserve every category/tag archive URL if the taxonomy itself is being intentionally retired, but important inbound URLs should be redirected sensibly rather than simply abandoned.

## Media

The WordPress media export contains roughly 7,000 attachment records. Treat it as an inventory, not a mandate to migrate every file.

The media audit should identify:

- media referenced by live/current content;
- media referenced only by archive content;
- apparently unreferenced media;
- duplicate or derivative files;
- current branding/logos;
- recent active-content media.

The preferred launch state is not dependent on the WordPress account for essential media, but low-value unused media-library material should not be moved merely for completeness.

## Taxonomy

Recreate only the taxonomy needed by the future site.

Key principles:

- active club records remain visible and dormant club records remain revivable;
- season and division can survive as useful metadata without becoming navigation clutter;
- live editorial categories should be few and meaningful;
- structured tournament, awards and archive data belongs primarily in the relevant apps;
- `Uncategorized` is not a meaningful destination and should not be reproduced as a first-class category.

## Pages

Only pages explicitly marked to keep need a live future treatment. The current keep set is small and should be consolidated where sensible.

Likely future functions include:

- About;
- Contact;
- Archive gateway;
- Rules gateway/summary;
- Support;
- Ask Me Anything/help;
- Transfer Bans/admin tooling until superseded by something better.

Everything else can remain preserved as archive material without rebuilding 100+ WordPress pages.

## Theme and navigation

Build the Micro.blog theme for the target architecture, not as an imitation of WordPress.

The homepage should prioritise:

- current Top 100 identity and important admin notices;
- latest meaningful editorial;
- obvious access to Archive, Tournaments, Awards, Rules and Regen;
- current competitions;
- active club records;
- current season analysis;
- selectively resurfaced history.

## Cutover principle

There is no longer any strategic need to wait until the WordPress.com subscription is nearly finished.

Cut over when:

- the Micro.blog prototype is stable;
- important historical URLs are mapped;
- essential media works independently of WordPress;
- the target navigation/theme is clearly better;
- publishing and feeds work reliably;
- a final backup and migration rehearsal have succeeded.

Until then, leave the live WordPress site alone and use it as the authoritative production copy.

## Success criteria

The migration is successful when:

- readers can find current Top 100 activity quickly;
- important historical posts remain available at their old or redirected URLs;
- essential media is under the new site's control;
- Archive, Tournaments, Awards, Rules and Regen feel like one ecosystem;
- the blog no longer carries structured functions better handled by those apps;
- dormant club records remain available for future revival;
- publishing on Micro.blog is simpler than maintaining the old WordPress structure.
