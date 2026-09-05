# Taxonomy plan

The current WordPress taxonomy reflects eleven years of changing workflows, Blogger import history and multiple attempts to organise Top 100 content. It should be audited before any destructive cleanup.

## Working principles

1. **Editorial taxonomy belongs on the blog.** Categories should help readers discover writing, not replicate database dimensions.
2. **Structured entities belong in structured apps.** Clubs, managers, seasons, honours and records are better handled by Archive where possible.
3. **Competitions belong primarily in Tournaments.** The blog may still use an editorial competition category when useful, but it should not become the authoritative fixture/result database.
4. **Keep the number of permanent categories deliberately small.** A category should describe a recurring editorial type or subject that a reader could reasonably browse.
5. **Use tags sparingly.** Do not recreate hundreds of historical tags simply because they exist in the export.
6. **Preserve old URLs even when taxonomy changes.** Removal from navigation does not imply that historical category/tag URLs can safely disappear without redirects or review.

## Likely editorial families to investigate

These are hypotheses for the audit, not final categories:

- News / Announcements
- Season Reviews & Predictions
- The Pink Final / editorial features
- Cups & Tournaments
- Manager Awards
- History / From the Archive
- Community / Managers

Some of these may ultimately become sections, series or landing pages rather than WordPress/Micro.blog categories.

## Audit workflow

For every existing category and important tag, capture:

- name and slug;
- post count;
- date range;
- representative posts;
- whether it describes editorial content, a structured entity, a season/competition, or an obsolete workflow;
- proposed disposition: **keep, merge, convert, move, hide, retire**;
- redirect/canonical destination if applicable.

## Do not do yet

- bulk-delete categories or tags;
- move hundreds of posts by hand;
- rename slugs on the live site;
- assume "Uncategorized" posts lack useful metadata or historical value;
- mirror the current taxonomy in Micro.blog before the audit is finished.
