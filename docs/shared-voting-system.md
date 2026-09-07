# Shared manager-authenticated voting system

The Top 100 ecosystem should use one voting foundation for **All-Manager Polls, Manager Awards and future authenticated votes**, rather than maintaining separate identity and anti-duplicate logic in each app.

The existing Supabase manager identity from Tournament Manager / Publishing Desk is the authoritative account layer. The current Awards app can then be refactored away from free-text manager names and Google Sheets voting storage while preserving its public Awards presentation and historical records.

## Goals

1. One verified Top 100 manager account = one eligible voter identity.
2. Eligibility is explicit and auditable.
3. A manager can vote once per voting event, but may edit their ballot until the deadline unless an event is deliberately configured otherwise.
4. Ballot choices can be private while turnout and eligibility remain auditable.
5. The same engine supports a simple yes/no poll and a multi-category Manager Awards ballot.
6. Results can be hidden until close, published automatically, or released manually by admins.
7. Historical voting events remain queryable after the season ends.
8. The public UI should never need to expose email addresses or Supabase auth IDs.

## Existing identity layer to reuse

Tournament Manager already has:

- Supabase Auth;
- `managers` records;
- `manager_portal_accounts` linking a verified `auth_user_id` to a canonical manager;
- game-world membership;
- active/inactive account state;
- admin checks and row-level security patterns.

Voting should **consume that identity**, not create another login system.

An authenticated voting request should resolve server-side to:

- manager ID;
- display name;
- game world;
- current club where relevant;
- active account status.

The browser must not be trusted to submit a manager name as proof of identity.

## Core concept: voting event

Use a general `voting_event` rather than treating every vote as a single poll.

A voting event contains one or more questions.

Examples:

### All-Manager Poll

Event: `S28 rule proposal — squad cap`

Question: `Should the proposed squad-cap change be adopted?`

Options: `Yes`, `No`, optionally `Abstain`.

### Manager Awards

Event: `Season 28 Manager Awards`

Questions:

- Overall Manager of the Season;
- Division 1 Manager of the Season;
- Cup Manager of the Season;
- Division 2 Manager of the Season;
- etc.

Each question has its own nominee/options list and may have its own eligibility/restriction rules.

This means Awards becomes a specialist UI over the same voting engine rather than a separate voting implementation.

## Proposed data model

Names are illustrative; final SQL can use the project's existing naming conventions.

### `voting_events`

- `id`
- `slug`
- `title`
- `description`
- `game_world_id`
- `event_type` — `poll`, `awards`, `governance`, `tournament`, `other`
- `status` — `draft`, `scheduled`, `open`, `closed`, `published`, `archived`
- `opens_at`
- `closes_at`
- `results_mode` — `hidden_until_close`, `live`, `manual_release`
- `ballot_visibility` — `private`, `public`
- `allow_ballot_edits` — normally true until close
- `created_by`
- `created_at`
- `closed_at`
- `published_at`

### `voting_questions`

- `id`
- `event_id`
- `title`
- `description`
- `position`
- `method` — initially `single_choice`, `yes_no`, `multiple_choice`; leave room for `ranked_choice`
- `min_selections`
- `max_selections`
- `abstain_allowed`
- optional restrictions such as self-voting policy

### `voting_options`

- `id`
- `question_id`
- `label`
- `position`
- optional `manager_id` when the option is a manager nominee
- optional metadata such as club/division/nomination note
- `active`

### `voting_electorate`

This is a **snapshot**, created when the event is opened.

- `event_id`
- `manager_id`
- `manager_account_id` where available
- `game_world_id`
- manager display-name snapshot
- club/division snapshot where useful
- `eligible`
- `eligibility_reason`
- `created_at`

A snapshot matters because a manager can change clubs, divisions or account state after voting opens. The electorate for a decision should not silently rewrite itself mid-vote.

### `voting_ballots`

- `id`
- `event_id`
- `manager_id`
- `submitted_at`
- `updated_at`
- `revision`
- `status` — `submitted`, `withdrawn`

Unique constraint: `(event_id, manager_id)`.

This enforces one ballot per eligible manager while still allowing an upsert/edit before the deadline.

### `voting_responses`

- `ballot_id`
- `question_id`
- `option_id`
- optional `rank`
- `created_at`

Constraints validate that the option belongs to the question and the number of selections meets that question's rules.

### `voting_audit_log`

Record meaningful administrative actions without publishing ballot contents:

- event created/opened/closed/reopened;
- electorate snapshot generated or explicitly amended;
- option/nominee changes;
- deadline changes;
- ballot submitted/updated/withdrawn;
- result release;
- admin override with reason.

Fields should include actor, timestamp, action, object, before/after metadata where appropriate and an optional reason.

## Privacy model

The default should be **private ballot, auditable participation**.

Public/admin-facing views may show:

- who was eligible;
- who has voted, if we decide turnout should be visible;
- total turnout;
- aggregate results after the configured release point.

They should not expose an individual manager's choices for a private ballot.

Important terminology: this is a **private ballot**, not a cryptographically anonymous election. Database owners/service-role processes can technically access stored records. If Top 100 ever genuinely needs unlinkable anonymous ballots, that should be a separate design with identity/ballot separation.

For ordinary game-world governance and awards, private-by-policy plus strong RLS and a clear audit trail is proportionate.

## Eligibility

Supported electorate builders should include:

- all active managers in a game world;
- managers in specified divisions;
- tournament entrants;
- a named/custom manager set;
- future specialist groups if needed.

Default All-Manager Poll rule: snapshot all approved active original-Top-100 manager accounts when the poll opens.

If a manager is genuinely eligible but has not yet claimed their account, an admin should be able to add/correct eligibility with a recorded reason rather than asking them to vote through an insecure fallback form.

## Voting lifecycle

1. Admin drafts event/questions/options.
2. System validates dates and configuration.
3. Opening the event creates the electorate snapshot.
4. Eligible manager signs in with the existing Supabase account.
5. Server resolves their manager identity and eligibility.
6. Manager submits ballot.
7. They may revisit and edit until close if allowed.
8. At `closes_at`, submissions stop server-side even if a stale browser remains open.
9. Results are calculated from valid ballots.
10. Results are released according to event settings.
11. Event and audit record remain available as history.

Client-side countdowns are presentation only; the database/server clock is authoritative.

## Results and quorum

Each event should expose:

- electorate size;
- ballots cast;
- turnout percentage;
- abstentions where supported;
- valid vote totals per question;
- result/tie state.

Governance polls should optionally define:

- quorum requirement;
- simple majority / supermajority threshold;
- tie rule;
- whether abstentions count towards quorum but not majority.

Do **not** hard-code one governance rule into the engine. Store the configured rule with the event so the historical result remains explainable.

## Awards-specific behaviour

The Awards UI can keep its identity — cabinets, Hall of Fame, season presentation and category navigation — while replacing the voting backend.

Changes from the current implementation:

- manager identity comes from authenticated Supabase account, not a typed/submitted manager name;
- one event-level ballot replaces spreadsheet rows identified by free-text manager/category pairs;
- nominee IDs should use canonical manager IDs where practical;
- category results remain hidden until the deadline unless admins deliberately reveal them;
- the app can show `Your ballot is saved` and let a manager amend it until close;
- season results can be archived into the existing Awards history after publication.

The current Google Sheets archive should be treated as **legacy historical data**, not necessarily rewritten on day one. New seasons can use Supabase while old seasons continue to render from the existing archive until we choose to normalize them.

## Poll-specific behaviour

A lightweight All-Manager Poll UI should support:

- proposal/title;
- explanatory text and links to relevant current rule;
- clear opening/closing times;
- yes/no/abstain or a small option list;
- authentication status;
- saved-vote confirmation;
- turnout;
- result and threshold explanation after close;
- permanent historical result URL.

A poll that changes a rule should be linkable to the resulting rules-history version and effective date.

## Security / integrity requirements

Enforce server-side / database-side:

- authenticated account required;
- account must be active;
- manager must appear in the event electorate;
- event must currently be open;
- one ballot per manager/event;
- responses must belong to that event/question;
- selection limits must be respected;
- ballot edits rejected after close;
- admin overrides require an audit reason;
- public clients cannot read private ballot responses.

Do not rely on disabled buttons or browser-supplied manager identity for any of these checks.

## Suggested Supabase functions

Prefer transactional RPCs/functions for the high-value operations:

- `open_voting_event(event_id)` — validates config and snapshots electorate;
- `get_my_voting_ballot(event_id)` — returns current user's eligibility and saved selections;
- `submit_voting_ballot(event_id, responses)` — validates/upserts atomically;
- `withdraw_voting_ballot(event_id)` if permitted;
- `close_voting_event(event_id)`;
- `get_voting_results(event_id)` — respects result-release rules;
- admin functions for electorate corrections and event amendments with audit logging.

## UI / domain architecture

The voting engine is shared infrastructure, not necessarily another top-level destination in global navigation.

Possible presentation:

- **Awards:** remains `awards.smtop100.blog`, using the shared engine.
- **All-Manager Polls:** can use a small voting UI such as `vote.smtop100.blog`, or be embedded later into a broader manager/admin portal.
- **Tournaments:** may reuse the engine for genuine votes without coupling voting logic to the tournament UI.

The exact public URL for general polls can be chosen when implementation starts; the data model should not depend on it.

## Implementation sequence

### V1 — foundation

- create voting schema and RLS in the existing shared Supabase project;
- reuse `manager_portal_accounts` for identity;
- implement electorate snapshot;
- implement single-choice / yes-no voting;
- implement one-ballot-per-manager and edit-until-close;
- implement private ballot + aggregate results;
- implement audit log;
- build one small authenticated test poll.

### V2 — All-Manager Polls

- add admin poll creator;
- add quorum/threshold/tie settings;
- add permanent results pages;
- connect successful rule-change polls to Rules History.

### V3 — Awards migration

- adapt `top100-mots` / `awards.smtop100.blog` to Supabase Auth and the voting engine;
- retain existing Awards presentation and historical archive;
- run one season in parallel/test mode before removing Google Sheets as the live vote store.

### V4 — richer methods

Only when a real need appears:

- multiple choice;
- ranked-choice/STV-style methods;
- tournament-specific electorates;
- notifications/reminders to eligible non-voters;
- deeper governance reporting.

## Decisions made

- Use the existing Supabase manager identity rather than a new login.
- One reusable engine should power both All-Manager Polls and Awards.
- Snapshot electorates when voting opens.
- Default to private ballots and auditable participation.
- Allow edits until the deadline by default.
- Store governance rules/thresholds with the event.
- Keep historical Awards data intact while new voting moves to Supabase.
- Automation enforces eligibility, deadlines and counting; it does not decide what question managers should be asked or what a result politically means.
