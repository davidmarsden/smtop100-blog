# Micro.blog page rebuild plan

The curated WordPress import successfully migrated posts and media, but WordPress pages are not imported as Micro.blog Pages. The nine WordPress pages marked `KEEP` should therefore be handled deliberately rather than copied wholesale.

## Guiding rule

Keep the useful function, not necessarily the old page. Where a dedicated Top 100 app now does the job better, the Micro.blog page should become a short gateway or redirect rather than duplicate structured information.

| WordPress page | Old path | Treatment on Micro.blog | Notes |
| --- | --- | --- | --- |
| About Top 100 | `/about/` | **REWRITE / KEEP LIVE** | Main explanation of Top 100, history, league structure and relationship with Top 100 Regen. Also introduce Archive, Tournaments, Awards and Rules. |
| Archives | `/archives/` | **REPLACE WITH ARCHIVE GATEWAY** | Short page pointing to `archive.smtop100.blog` for structured history and retaining access to the blog archive/search. |
| Contact | `/contact/` | **REWRITE / KEEP LIVE** | Replace WordPress form cruft with simple contact details. |
| Game World Rules | `/top100-the-rules-policing/` | **CONSOLIDATE / REDIRECT** | Superseded by one concise local Rules gateway and the canonical Rules app. |
| Roll of Honour | `/about/history/` | **REPLACE WITH ARCHIVE APP** | Historical content is valuable but the structured Roll of Honour belongs in `archive.smtop100.blog`. Preserve old URL with redirect/gateway. |
| Support Our Website with a £1 Contribution | `/support-our-website-with-a-1-contribution/` | **REWRITE IF STILL WANTED** | Existing copy is tied to obsolete WordPress costs. Keep only if community contributions are still useful; update costs/payment method before publishing. |
| Top 100 Ask Me Anything | `/top-100-ask-me-anything/` | **MERGE INTO CONTACT / HELP** | Original page was effectively a WordPress form/shortcode shell. Redirect or replace with a short 'Ask the admin' gateway. |
| Top 100 Rules | `/top-100-rules/` | **KEEP AS SHORT RULES GATEWAY** | Concise prospective-manager summary plus links to the canonical Rules app and any Top 100 Regen differences. |
| Transfer Bans | `/top100-the-rules-policing/transfer-bans/` | **REWRITE / KEEP LIVE TEMPORARILY** | Keep sanctions explanation but remove stale 2019 ban list. Treat as temporary until transfer-ban administration becomes structured tooling. |

## Proposed live page set

The nine WordPress pages collapse into six useful Micro.blog Pages:

1. **About** — `/about/`
2. **Archive** — `/archives/`
3. **Contact** — `/contact/`
4. **Rules** — `/top-100-rules/` (or a cleaner `/rules/` if redirects are added)
5. **Support** — only if still wanted
6. **Transfer Bans** — temporary operational page until replaced by tooling

The old Game World Rules, Roll of Honour and Ask Me Anything paths should not become separate maintained content destinations.

## Old URL handling at cutover

When `smtop100.blog` moves to Micro.blog, verify or add mappings for:

- `/top100-the-rules-policing/` → Rules gateway / `rules.smtop100.blog`
- `/about/history/` → Archive / Roll of Honour destination
- `/top-100-ask-me-anything/` → Contact / Ask Admin
- `/top100-the-rules-policing/transfer-bans/` → Transfer Bans page

## Draft content

Drafts for the new live pages are stored under `migration/pages/`. They are intentionally short and designed for the new architecture rather than reproducing WordPress-era page sprawl.