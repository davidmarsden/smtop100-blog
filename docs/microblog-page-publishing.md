# Micro.blog page publishing

The canonical Markdown sources for the main Top 100 standalone pages live in `migration/pages/`.

Managed pages:

| Source | Live page |
| --- | --- |
| `migration/pages/about.md` | `https://smtop100.blog/about/` |
| `migration/pages/contact.md` | `https://smtop100.blog/contact/` |
| `migration/pages/rules.md` | `https://smtop100.blog/rules/` |
| `migration/pages/support.md` | `https://smtop100.blog/support/` |

## Publishing flow

`.github/workflows/sync-microblog-pages.yml` validates managed page sources on pull requests. After a managed page change is merged to `main`, the workflow runs `scripts/sync_microblog_pages.py` and updates the existing Micro.blog standalone page through the Micropub API.

The first Markdown H1 is stripped during publishing because Micro.blog already renders the page title. This avoids duplicate headings while keeping the source files readable in GitHub.

The synchroniser only updates known existing page URLs; it does not create pages or change Micro.blog navigation. This is deliberate protection against accidental duplicate pages.

## Required secret

Add a repository Actions secret named:

`MICROBLOG_TOKEN`

Use a Micro.blog app token with permission to update the `smtop100.blog` blog. The token is sent only as the Micropub Bearer token and must never be committed to the repository.

## Manual run

The workflow also supports `workflow_dispatch`, which republishes all managed pages from `main`.

For local validation without publishing:

```bash
python scripts/sync_microblog_pages.py --dry-run
```

To publish selected pages locally when `MICROBLOG_TOKEN` is present:

```bash
python scripts/sync_microblog_pages.py about contact
```
