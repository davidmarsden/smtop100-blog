# Page triage results

Completed human triage of the 105 WordPress pages from the September 2026 export.

## Principle

The default decision is **ARCHIVE** unless a page was explicitly marked KEEP. This reflects the fact that many pages are legacy navigation, old campaigns, outdated competition/admin pages, or material now better served by the specialist apps.

## Summary

- **Total pages:** 105
- **Keep in some form:** 9
- **Archive by default:** 96

## Pages to keep in some form

| Page | Current URL | Initial future treatment |
| --- | --- | --- |
| About Top 100 | `https://smtop100.blog/about/` | KEEP. Rewrite as the main concise introduction to Top 100, including the relationship with Top 100 Regen and clear links into the wider ecosystem. |
| Archives | `https://smtop100.blog/archives/` | KEEP CONCEPT / REDESIGN. The old WordPress archive page may be replaced by a cleaner browse/search/archive gateway, with structured history increasingly delegated to `archive.smtop100.blog`. |
| Contact | `https://smtop100.blog/contact/` | KEEP. Simplify and retain as the main contact route. |
| Game World Rules | `https://smtop100.blog/top100-the-rules-policing/` | KEEP AS REDIRECT / SUMMARY. Canonical detailed rules should live at `rules.smtop100.blog`; this URL should survive as a useful summary or redirect. |
| Roll of Honour | `https://smtop100.blog/about/history/` | KEEP CONCEPT / ARCHIVE APP. Structured honours belong naturally in `archive.smtop100.blog`; preserve this historical entry point and redirect or rework it accordingly. |
| Support Our Website with a £1 Contribution | `https://smtop100.blog/support-our-website-with-a-1-contribution/` | KEEP. Review wording/payment mechanism during redesign, but preserve the ability for managers to support the site. |
| Top 100 Ask Me Anything | `https://smtop100.blog/top-100-ask-me-anything/` | KEEP. Retain as a community/help entry point, subject to redesign and checking that the interaction method still works. |
| Top 100 Rules | `https://smtop100.blog/top-100-rules/` | KEEP AS REDIRECT / SUMMARY. Avoid maintaining two competing canonical rules pages; point clearly to `rules.smtop100.blog`. |
| Transfer Bans | `https://smtop100.blog/top100-the-rules-policing/transfer-bans/` | KEEP FUNCTION / REPLACE PAGE MODEL. Transfer bans remain a live admin need, but the current page/post approach should be replaced by structured admin tooling if practical. Preserve the URL as a useful public entry point. |

## Archive default

The remaining 96 pages should be preserved in the WordPress export/history but are **not required as first-class live pages** in the redesigned site.

Before any destructive action or migration, retain a URL inventory so historically linked pages can be redirected where a clear successor exists. Otherwise they can be preserved in an archive copy or historical content store without appearing in navigation.

## Architecture implications

The nine retained pages collapse into a much smaller set of actual live functions:

1. **About / Welcome** — one strong current introduction rather than multiple overlapping welcome/history pages.
2. **Contact** — one simple contact destination.
3. **Archive gateway** — browse/search editorial history, with structured records handed off to Archive.
4. **Rules** — one canonical Rules app, with old WordPress rule URLs redirected or converted into short summaries.
5. **Support** — retain contribution/support option.
6. **Ask Me Anything / Help** — retain community-facing question/help route if still useful.
7. **Transfer Bans** — retain the public function, but redesign the admin workflow rather than preserving the old page model.
8. **Roll of Honour** — treat as Archive data rather than a separately maintained WordPress history page.

This confirms that the future main site can be dramatically simpler than the current WordPress page tree while preserving the underlying historical material.
