# Micro.blog page publishing

The canonical Markdown sources for the main Top 100 standalone pages live in `migration/pages/`.

Managed pages:

| Source | Live page | Publishing state |
| --- | --- | --- |
| `migration/pages/about.md` | `https://smtop100.blog/about/` | approved for automatic publishing |
| `migration/pages/contact.md` | `https://smtop100.blog/contact/` | approved for automatic publishing |
| `migration/pages/rules.md` | `https://smtop100.blog/rules/` | approved for automatic publishing |
| `migration/pages/support.md` | `https://smtop100.blog/support/` | approved for automatic publishing |

## Publishing flow

`.github/workflows/sync-microblog-pages.yml` validates all managed page sources on pull requests. After an approved managed page change is merged to `main`, the workflow runs `scripts/sync_microblog_pages.py` and updates the existing Micro.blog standalone page through the Micropub API.

Publishing remains explicitly gated by the per-page `ready: True` setting in the synchroniser. All four currently managed standalone pages are now approved for production publishing.

Changes to the page-sync workflow or synchroniser also trigger a production sync when merged to `main`. This is intentional: fixes to the publishing machinery can be exercised immediately against the approved page set. Manual workflow runs are restricted to the `main` branch, and the publish job explicitly checks out `main`.

The first Markdown H1 is stripped during publishing because Micro.blog already renders the page title. This avoids duplicate headings while keeping the source files readable in GitHub. A managed source is rejected if its body is empty after heading removal.

The synchroniser only updates known existing page URLs; it does not create pages or change Micro.blog navigation. This is deliberate protection against accidental duplicate pages.

## Rules

`https://smtop100.blog/rules/` is the canonical current Top 100 rulebook. The former standalone rules site at `https://rules.smtop100.blog/` is retained only as a compatibility redirect to the main page after the September 2026 consolidation.

Competition-specific rules remain with the relevant current competition tooling, and Regen-specific exceptions remain on the Regen rules page. The precedence order is documented in the canonical rulebook itself.

Historical rulebook snapshots may be retained in source control for reference, but must not be presented as current authority.

## Required secret

Add a repository Actions secret named:

`MICROBLOG_TOKEN`

Use a Micro.blog app token with permission to update the `smtop100.blog` blog. The token is sent only as the Micropub Bearer token and must never be committed to the repository.

## Manual run

The workflow supports `workflow_dispatch` from `main`. It republishes pages currently marked production-ready.

For local validation of all managed sources without publishing:

```bash
python scripts/sync_microblog_pages.py --all --dry-run
```

To publish selected approved pages locally when `MICROBLOG_TOKEN` is present:

```bash
python scripts/sync_microblog_pages.py rules support
```
