# Migration to Micro.blog

The intended long-term direction is to move `smtop100.blog` from WordPress.com to Micro.blog once the remaining WordPress subscription period is close to ending and the replacement has been tested properly.

This is not a reason to leave the WordPress site untouched for the next 16 months. The redesign period should make the eventual migration easier.

## Strategy

Use WordPress as the live publishing platform for now, while treating Micro.blog as the target architecture.

That means:

- simplify rather than deepen WordPress-specific structure;
- avoid new plugin/block dependencies that cannot migrate cleanly;
- keep structured functions in the specialist subdomain apps;
- clean taxonomy deliberately;
- preserve URL knowledge;
- maintain independent backups of content and media;
- build and test a parallel Micro.blog prototype before cutover.

## What needs testing

### Content import

Test representative samples from:

- original Blogger-era posts;
- early WordPress posts;
- recent block-editor posts;
- image-heavy posts;
- posts with embedded media;
- longform editorial pieces;
- routine announcements/results;
- pages.

### Permalinks and redirects

The migration should aim to preserve existing post URLs where Micro.blog permits it. Where paths cannot be reproduced exactly, record explicit redirects.

Special attention should be paid to:

- old Blogger-derived slugs;
- WordPress date-based URLs, if present;
- pages linked externally;
- category/tag archives;
- attachment/media URLs;
- links from Archive, Awards, Tournaments and Rules back into the main site.

### Media

Confirm whether imported posts reference WordPress-hosted media or copy it into the new Micro.blog media library. The preferred launch state is not dependent on an expiring WordPress account for essential images.

### Taxonomy

Only the cleaned editorial taxonomy should be reproduced. Do not migrate hundreds of legacy tags solely for completeness if they provide no reader value.

### Theme and navigation

The Micro.blog prototype should implement the target ecosystem model directly:

`Top 100 · Archive · Tournaments · Awards · Rules`

It should be designed as the editorial front door rather than an imitation of the current WordPress theme.

## Suggested timeline

### Now

Audit, redesign the WordPress information architecture, reduce clutter and map URLs.

### During the remaining subscription period

Build a private/test Micro.blog version and repeatedly test representative imports and theme/navigation work.

### Near subscription end

Run a full migration rehearsal, verify redirects and media, then schedule final cutover only when the test site is proven.

## Success criteria

The migration is successful when:

- readers can find current Top 100 activity quickly;
- important historical posts remain available at their old or redirected URLs;
- essential media is under the new site's control;
- Archive/Tournaments/Awards/Rules are clearly integrated as one ecosystem;
- the blog no longer carries structured functions better handled by those apps;
- publishing on Micro.blog is simpler than maintaining the old WordPress structure.
