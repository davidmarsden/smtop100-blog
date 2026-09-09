# Shared voting audit — September 2026

## Executive summary

The shared voting foundation already exists and is good enough to become the canonical voting backend for the Top 100 ecosystem. The work should now move from architecture to adoption.

The key conclusion from this audit is:

> **Do not build another voting service. Reuse the existing Supabase voting foundation in `top100-tournaments`, and migrate Awards onto it as the first production consumer.**

The existing implementation already provides authenticated manager identity, electorate snapshots, one ballot per manager, edit-until-close behaviour, private ballots, aggregate results and audit logging. The Awards app is the main remaining outlier: it still relies on free-text manager identity, a local fallback manager list and Google Sheets-backed Netlify functions.

## Repositories audited

### `davidmarsden/top100-tournaments`

This is currently the home of the shared manager identity and the first voting implementation.

Relevant assets:

- `docs/shared-voting-v1.md`
- `supabase/migrations/20260907_shared_voting_v1.sql`
- existing Supabase Auth
- `manager_portal_accounts`
- canonical `managers` records
- `/vote` test UI

### `davidmarsden/smtop100-blog`

This is the architecture/planning source of truth.

Relevant asset:

- `docs/shared-voting-system.md`

This document is still directionally correct and should remain the long-form design reference.

### `davidmarsden/top100-mots`

This is the Awards application at `awards.smtop100.blog`.

Relevant assets include:

- `src/VotingApp.jsx`
- `netlify/functions/submit-vote.js`
- `netlify/functions/results.js`
- `netlify/functions/managers.js`
- `netlify/functions/deadline.js`
- `netlify/functions/reset-votes.js`
- `netlify/functions/archive-results.js`
- `netlify/functions/_google.js`

## What already works in the shared foundation

The V1 Supabase implementation already provides the most important integrity guarantees.

### Identity

Voting consumes the existing Top 100 manager identity rather than trusting a typed manager name.

The authenticated user is resolved through `manager_portal_accounts`, which links Supabase Auth to the canonical manager record.

### Electorate snapshot

Opening an event snapshots active manager accounts into `voting_electorate`.

This is the right model because eligibility should not silently change halfway through a vote when a manager changes club, division or account state.

### One manager, one ballot

`voting_ballots` has a unique `(event_id, manager_id)` constraint.

Submitting again before the deadline updates the same ballot rather than creating another vote.

### Server-enforced deadline

`submit_voting_ballot()` checks event status and `closes_at` server-side. A stale browser cannot submit after voting has closed.

### Private ballot / aggregate results

Managers can read only their own ballot and responses. Aggregate results are exposed through `get_voting_results()` according to the event's result visibility setting.

### Audit trail

Opening, closing and ballot submission create entries in `voting_audit_log`.

This is already a major improvement over the current Awards workflow.

## Gaps in V1 before Awards can use it

These are extensions, not reasons to redesign the engine.

### 1. Awards event support needs richer metadata

Current V1 question types are:

- `yes_no`
- `single_choice`

That is enough for the current Awards voting method because each category is a single-choice question.

However, Awards needs nominee metadata so the UI can render manager, club, achievement, description and category cleanly without hard-coding all nominees in React.

Recommended addition:

- `voting_options.manager_id` nullable
- `voting_options.metadata jsonb` for club, achievement, description, division and presentation details

### 2. Event lifecycle should grow slightly

V1 currently uses `draft`, `open`, `closed`, `cancelled`.

For Awards and governance history, add either:

- `published` as a status; or
- a separate `published_at` / result-release state.

Do not make publication equivalent to closing: admins may want to close voting, inspect results, then reveal them later.

### 3. Results visibility should support manual release

Current modes:

- `hidden`
- `after_close`
- `live`

Add:

- `manual_release`

This maps directly to the existing Awards Show/Hide Results workflow.

### 4. Ballot read RPC

Add a clean function such as:

`get_my_voting_ballot(event_id)`

It should return:

- eligibility
- event state
- current selections
- submitted/updated timestamps

This keeps Awards UI code simple and avoids direct table knowledge.

### 5. Admin event builder

The V1 test event is seeded in SQL. That was fine for proving the foundation.

Next, admins need to be able to create an event and its questions/options without writing a migration.

For the first Awards migration, this can be deliberately modest: an admin import/config screen rather than a fully generic poll-builder UI.

## Awards audit

The current Awards app has excellent presentation and historical features, but the live voting mechanism is the legacy piece.

### Current identity model

`VotingApp.jsx` maintains:

- `currentManager`
- `currentClub`
- `nameInput`
- `clubInput`
- a hard-coded `ADMIN_USERS` list
- a large `FALLBACK_ACTIVE_MANAGER_NAMES` array

It calls `/api/managers` and attempts to match a manager by normalized name and optional club.

This is useful as a historical compatibility mechanism, but it should no longer be proof of voting identity.

### Current nominees

Awards categories and nominees are hard-coded inside `VotingApp.jsx`.

That means a new season currently requires a code change simply to configure the ballot.

The migration should move nominees into the shared voting event while keeping the same visual cards.

### Current storage

The Netlify function inventory confirms the Awards app still owns a parallel voting backend, including Google integration:

- `_google.js`
- `submit-vote.js`
- `results.js`
- `deadline.js`
- `reset-votes.js`
- `archive-results.js`

This backend should become legacy-only after the Supabase migration.

### What should remain untouched initially

Do **not** rewrite the parts of Awards that already work well:

- Hall of Fame
- manager cabinets
- records
- previous-season archive
- existing presentation and gold Awards identity
- category navigation
- historical Google Sheets data

The migration is about live voting identity/storage first.

## Canonical architecture

### Identity source

**Supabase Auth + `manager_portal_accounts` is authoritative.**

No other app should maintain its own manager login or treat a typed name as identity.

### Voting data owner

The shared Supabase project should own:

- voting events
- questions
- options/nominees
- electorate snapshots
- ballots
- responses
- audit log

The schema may currently live in the Tournaments repository, but conceptually it is ecosystem infrastructure, not tournament-specific data.

### Presentation owners

Each app remains responsible for presentation:

- Awards renders the Awards experience.
- Tournaments renders tournament-specific votes when needed.
- A future `vote.smtop100.blog` can render general governance polls.

They all consume the same backend.

## Recommended implementation sequence

### Phase A — harden the shared backend

In `top100-tournaments`:

1. Add nominee/option metadata support.
2. Add manual result release.
3. Add `get_my_voting_ballot()`.
4. Add admin event creation/update RPCs or a small admin configuration layer.
5. Extend audit logging to include explicit result release and admin edits.
6. Add tests for one-ballot-per-manager, edit-until-close and result visibility.
7. Add an audited electorate-correction path so admins can include a genuinely eligible manager whose account state or mapping was wrong at snapshot time, with a required reason logged.

### Phase B — migrate Awards in compatibility mode

In `top100-mots`:

1. Add the Supabase client using the same project as Tournament Manager.
2. Replace typed-name login for voting with Supabase Auth.
3. Resolve the signed-in user to the canonical manager identity.
4. Load the current Awards event/questions/options from Supabase.
5. Convert each current category into one voting question.
6. Render nominee metadata through the existing Awards card UI.
7. Save/revise the full ballot through `submit_voting_ballot()`.
8. Show a clear `Your ballot is saved` state.
9. Preserve admin result controls, but drive them from the shared event result-release state.
10. Keep legacy Hall of Fame/history endpoints unchanged.

### Phase C — run in parallel for one test event

Before S28 Awards becomes the live production vote:

1. Create a private/draft Awards-shaped test event in Supabase.
2. Invite a small group of existing authenticated managers.
3. Compare Supabase tallies with an intentionally duplicated legacy test submission.
4. Verify edit-before-close behaviour.
5. Verify late submissions are rejected server-side.
6. Verify non-electorate accounts cannot vote.
7. Verify ordinary voters cannot read another manager's ballot.
8. Verify result hiding/manual release.

Do not dual-write the real production Awards ballot unless there is a specific rollback reason. A short dedicated test is cleaner than maintaining two authoritative stores.

### Phase C2 — electorate reconciliation and account onboarding

The live cutover must not assume every eligible Awards voter has already claimed a `manager_portal_accounts` identity.

Before the first production Supabase-backed Awards event:

1. Build the expected Awards electorate from the current active-manager source of truth and compare it with active `manager_portal_accounts`.
2. Produce a reconciliation report of eligible managers who are missing an account, mapped to the wrong manager, inactive unexpectedly or otherwise unable to authenticate.
3. Run an account-claim/onboarding campaign before voting opens, with clear instructions and enough lead time for managers to verify their email/account.
4. Re-run the reconciliation immediately before the event is opened and require zero unexplained missing eligible managers.
5. For genuinely eligible edge cases that cannot be fixed before opening, use the audited electorate-correction/admin inclusion path with a recorded reason; do not fall back to typed-name voting.
6. Keep typed-name voting available only in the legacy test path until this reconciliation has passed; remove it from the production Awards path only after the electorate is complete.

The production electorate snapshot should therefore be a controlled cutover gate, not simply “all currently claimed accounts”.

### Phase D — S28 cutover

For the next live Awards season:

- Supabase becomes the authoritative live vote store.
- The reconciled/claimed account list is the basis for the electorate snapshot, with any manual eligibility corrections audited.
- Google Sheets stops receiving live ballot writes after the cutover succeeds, but remains the historical store for previous seasons during the compatibility period.
- Remove or disable the live legacy submission functions only after the first Supabase-backed Awards cycle completes successfully.

### Phase E — archive the Supabase-backed season into Awards history

Before the first Supabase-backed season is treated as historical, provide an explicit bridge so Hall of Fame, manager cabinets and archive views can see its winners.

Preferred short-term compatibility path:

1. After results are formally released, generate a canonical season-results export from the Supabase event (season, category, winning manager ID/name, club, vote totals and any tie metadata needed by Awards history).
2. Import/write that published result set into the existing historical Awards data shape consumed by `archive-results.js`, using an admin-only audited action.
3. Verify S28 appears correctly in Hall of Fame, cabinets, records and archive views before marking the Google-backed history layer read-only for that season.
4. Keep ballots themselves in Supabase only; the legacy history store receives published winners/results, not voter-level data.

Longer term, replace `archive-results.js` and the historical readers with Supabase-backed history directly. Do not make that rewrite a prerequisite for the live voting migration, but do not retire the compatibility export until those readers have moved.

## All-Manager Polls after Awards

Once Awards proves the engine at scale, build the small general poll interface.

It should support:

- proposal title and explanation
- relevant rule/source links
- Yes / No / Abstain or a short single-choice list
- electorate size and turnout
- configurable quorum / threshold / tie rule
- permanent results URL
- link from adopted rule changes to Rules History

This can live at `vote.smtop100.blog` or inside a future broader manager portal. The data model should remain URL-agnostic.

## Decisions from this audit

1. The existing Supabase implementation is the canonical voting foundation.
2. Awards should be the first major production migration.
3. Do not create a separate Awards authentication system.
4. Do not migrate historical Awards sheets as a prerequisite.
5. Do not rewrite Hall of Fame/cabinets/records during the voting migration.
6. Move future nominee configuration out of `VotingApp.jsx` and into voting event data.
7. Preserve private ballots and auditable participation.
8. Preserve edit-until-close behaviour.
9. Keep result publication separate from ballot closing.
10. Require full electorate/account reconciliation before removing typed-name production access.
11. Preserve each new Supabase-backed season in Awards history via an explicit published-results export until the historical readers themselves move to Supabase.
12. After Awards, use the same engine for All-Manager Polls and tournament votes.

## Immediate next PRs

### `top100-tournaments`

Create **Shared voting V2** with backend extensions required by Awards, including audited electorate correction support.

### `top100-mots`

After V2 schema/RPCs are stable, create **Awards shared voting adapter**.

The first Awards PR should deliberately avoid deleting the Google/legacy code. It should introduce the Supabase path behind an explicit test/event configuration so it can be exercised safely before the live cutover, and include the account-reconciliation and published-results archive bridge before production retirement of typed-name/live-Sheets paths.
