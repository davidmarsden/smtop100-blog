# Micro.blog page rebuild plan

The curated WordPress import successfully migrated posts and media, but WordPress pages are not imported as Micro.blog Pages. The nine WordPress pages marked `KEEP` should therefore be handled deliberately rather than copied wholesale.

## Guiding rule

Keep the useful function, not necessarily the old page. Ordinary editorial/reference material should live on the main Micro.blog site; structured functions belong in the specialist apps.

| WordPress page | Old path | Treatment on Micro.blog | Notes |
| --- | --- | --- | --- |
| About Top 100 | `/about/` | **REWRITE / KEEP LIVE** | Main explanation of Top 100, history, league structure, apps and relationship with Top 100 Regen. |
| Archives | `/archives/` | **REPLACE / REDIRECT TO POSTS ARCHIVE** | The main site should expose Micro.blog's chronological post archive at `/archive/`. Do not confuse this with `archive.smtop100.blog`, which is **Top 100 Stats & History**. |
| Contact | `/contact/` | **REWRITE / KEEP LIVE** | Replace WordPress form cruft with a simple current contact/help route. |
| Game World Rules | `/top100-the-rules-policing/` | **CONSOLIDATE / REDIRECT** | Current canonical rules move to `smtop100.blog/rules/`. Detailed old rules are retained only as versioned legacy/history material. |
| Roll of Honour | `/about/history/` | **REPLACE WITH STATS & HISTORY** | Structured Roll of Honour belongs in `archive.smtop100.blog`. Preserve old URL with redirect/gateway. |
| Support Our Website with a £1 Contribution | `/support-our-website-with-a-1-contribution/` | **REWRITE / KEEP AS `/support/`** | Support remains part of the target site. Rewrite around current costs and payment method rather than WordPress-era wording. |
| Top 100 Ask Me Anything | `/top-100-ask-me-anything/` | **MERGE INTO CONTACT / HELP** | Original page was effectively a form shell. Redirect to Contact/help. |
| Top 100 Rules | `/top-100-rules/` | **REWRITE AS `/rules/`** | Concise current human-readable rules. Retire the standalone rules subdomain after the rewrite is proven. |
| Transfer Bans | `/top100-the-rules-policing/transfer-bans/` | **TEMPORARY GATEWAY, THEN TOOLING** | Avoid a stale manually maintained list. Target a manager/admin-backed transfer-ban system with structured records and automatic expiry handling. |

## Proposed live page set

The nine WordPress pages collapse into five core maintained Micro.blog Pages plus the built-in posts archive:

1. **About** — `/about/`
2. **Rules** — `/rules/`
3. **Contact** — `/contact/`
4. **Support** — `/support/`
5. **Transfer Bans** — temporary gateway only until replaced by structured tooling
6. **Posts Archive** — `/archive/` (Micro.blog chronological archive, not the stats app)

The old Game World Rules, Roll of Honour and Ask Me Anything paths should not become separate maintained content destinations.

## Rules architecture

`/rules/` becomes the canonical current rules destination.

The old `rules.smtop100.blog` content should be reviewed, rewritten and reformatted rather than copied verbatim. Once the new page is complete, the subdomain should redirect to `/rules/`.

The current page should stay concise. Detailed historical rules should be preserved separately as dated/versioned legacy records, useful when resolving questions about how a rule worked in an earlier season.

Rule application itself is a candidate for structured admin tooling: identify the applicable current/versioned rule, propose an adjudication and rationale, and require human confirmation for contentious decisions.

## Archive naming

There are two distinct archive concepts:

- `smtop100.blog/archive/` — **Posts Archive**, chronological Micro.blog posts.
- `archive.smtop100.blog` — **Top 100 Stats & History**, structured seasons/managers/clubs/honours data.

Navigation and copy must never label both simply “Archive”.

## Support

`/support/` is part of the target live page set. Before publication, replace the old £1/WordPress-cost framing with the actual current purpose, costs and payment route.

## Old URL handling at cutover

When `smtop100.blog` moves to Micro.blog, verify or add mappings for:

- `/archives/` → `/archive/`
- `/top100-the-rules-policing/` → `/rules/`
- `/top-100-rules/` → `/rules/`
- `rules.smtop100.blog` → `/rules/` after the rewrite is ready
- `/about/history/` → relevant Top 100 Stats & History / Roll of Honour destination
- `/top-100-ask-me-anything/` → `/contact/`
- `/support-our-website-with-a-1-contribution/` → `/support/`
- `/top100-the-rules-policing/transfer-bans/` → temporary bans gateway / eventual bans tool

## Draft content

Drafts under `migration/pages/` are starting points only. Rules, Support and Transfer Bans in particular now need rewriting around this revised architecture rather than reproducing the old WordPress pages.