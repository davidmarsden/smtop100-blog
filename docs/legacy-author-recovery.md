# Legacy author recovery

The Micro.blog WordPress importer preserved the content of the historical Top 100 archive but did not preserve WordPress authorship in the rendered posts. The original WXR export still contains the author information, so historical credit can be restored at theme level without editing 2,262 imported posts individually.

## What we recovered

- **2,262 published posts** in the curated migration corpus.
- **77 distinct WordPress creators** attached to those posts.
- **91 WordPress author records** exist in the raw export, including accounts that did not author a published post in the migrated corpus.
- One date/title combination occurs twice (`Brilliant Beddows masters revivial`, 9 March 2019), but both copies have the same author, so the lookup is unambiguous for byline purposes.

The repository intentionally does **not** store WordPress author email addresses.

## Data files

- `data/legacy-authors.json` — lookup used by the Hugo/Micro.blog theme. It is nested by publication date and title.
- `audit/legacy-contributors.csv` — contributor/account summary with published-post counts. Many older WordPress display names are still usernames; these can be progressively replaced with proper names where known.

Example structure:

```json
{
  "2026-06-19": {
    "The Entertainers": {
      "author_login": "davidmarsden1",
      "author_name": "David Marsden",
      "author_display_name": "David Marsden",
      "wordpress_url": "https://smtop100.blog/2026/06/19/the-entertainers/"
    }
  }
}
```

## Theme strategy

For imported historical posts, look up the post by `.Date.Format "2006-01-02"` and `.Title`. If a matching legacy author exists, display a byline using the recovered `author_name`.

A prototype partial lives at `prototypes/theme/layouts/partials/legacy-author.html`.

Suggested display order for the final theme:

1. Native Micro.blog/team author when available for a new post.
2. Recovered legacy WordPress author for imported historical posts.
3. Site/default author only as a final fallback.

This prevents all historical posts from appearing to have been written by David while allowing future native Micro.blog authorship to take precedence.

## Contributor-name cleanup

The WXR records contain a mixture of real names and usernames. For example, `Stephen Beddows`, `Norman Little`, `Alexander McLean`, `Rahul Warrier`, `Mark Deadman`, `Heath Brown`, and others can already be recovered as names, while accounts such as `mistertrex`, `princenathan88`, and `fhirst` currently resolve only to their old WordPress display/login names.

The lookup should therefore be treated as historically correct at the account level now, with friendly-name cleanup as a separate editorial task. Updating the name in the JSON lookup later will update every matching historical byline at once.

## Future contributors

Historical author recovery is separate from future contribution workflow.

The preferred long-term model is hybrid:

- native Micro.blog team authors for a small number of trusted regular contributors, if useful;
- a submission/review/publishing workflow for occasional manager contributions;
- explicit contributor bylines on submitted posts so credit does not depend on every writer having a Micro.blog account.

Do not use categories as a substitute for authorship. Categories should describe the subject/series/club rather than the person who wrote the post.
