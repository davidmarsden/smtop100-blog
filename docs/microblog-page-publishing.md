# Micro.blog page publishing

The canonical Markdown sources for the main Top 100 standalone pages live in `migration/pages/`.

Managed pages:

| Source | Live page | Publishing state |
| --- | --- | --- |
| `migration/pages/about.md` | `https://smtop100.blog/about/` | approved for automatic publishing |
| `migration/pages/contact.md` | `https://smtop100.blog/contact/` | approved for automatic publishing |
| `migration/pages/rules.md` | `https://smtop100.blog/rules/` | validation only until the full rules source is approved |
| `migration/pages/support.md` | `https://smtop100.blog/support/` | validation only until its source is explicitly approved |

## Publishing flow

`.github/workflows/sync-microblog-pages.yml` validates all managed page sources on pull requests. After an approved managed page change is merged to `main`, the workflow runs `scripts/sync_microblog_pages.py` and updates the existing Micro.blog standalone page through the Micropub API.

Publishing is intentionally gated. Only page entries marked `ready: True` in the synchroniser can be sent to production. Validation still covers every managed page, including pages that are not yet authoritative enough to publish automatically.

Changes to the page-sync workflow or synchroniser also trigger a production sync when merged to `main`. This is intentional: it means fixes to the publishing machinery can be exercised immediately against the approved page set. The safety boundary is the per-page `ready: True` gate, so automation changes may republish approved pages but cannot publish Rules or Support until those pages are explicitly promoted. Manual workflow runs are restricted to the `main` branch, and the publish job explicitly checks out `main`.

The first Markdown H1 is stripped during publishing because Micro.blog already renders the page title. This avoids duplicate headings while keeping the source files readable in GitHub. A managed source is rejected if its body is empty after heading removal.

The synchroniser only updates known existing page URLs; it does not create pages or change Micro.blog navigation. This is deliberate protection against accidental duplicate pages.

## Required secret

Add a repository Actions secret named:

`MICROBLOG_TOKEN`

Use a Micro.blog app token with permission to update the `smtop100.blog` blog. The token is sent only as the Micropub Bearer token and must never be committed to the repository.

## Manual run

The workflow supports `workflow_dispatch` from `main`. It republishes only pages currently marked production-ready.

For local validation of all managed sources without publishing:

```bash
python scripts/sync_microblog_pages.py --all --dry-run
```

To publish selected approved pages locally when `MICROBLOG_TOKEN` is present:

```bash
python scripts/sync_microblog_pages.py about contact
```

Pages not marked production-ready will refuse a live publish even when named explicitly.
