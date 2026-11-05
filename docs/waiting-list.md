# Waiting list for Top 100 and Top 100 Regen

Status: phase 1 in progress (November 2026). The rules are in [rules section 3.3](../migration/pages/rules.md).

## Decisions

- **One list per game world.** An applicant can join either list or both. New managers are encouraged to start in Regen.
- **Identity.** The applicant gives their Soccer Manager manager name. Their email comes from Manager Account sign-up. There's no separate ownership check.
- **Asked on joining:** manager name, game world(s), how they found Top 100, and the rules agreement. The agreement covers later changes by vote or by the administrators, so it isn't re-accepted when the rules change.
- **Order:** returning Top 100 managers first, then by waiting-list score, then by date joined.
- **Score (out of 100):**
  - Top 100 record 40 (half the public-record appointment score, which is out of 80, from Stats & History);
  - Regen record 20 (5 a season, Top 100 list only);
  - Gold 15;
  - focus 10 (three or fewer game worlds, less 1 for each further one);
  - recommendations 15 (5 each).
  - Each concern takes 10 off.
- **Recommendations and concerns.** Only current managers with Manager Accounts can give them, one per applicant. Concerns need no evidence, are confidential to the administrators, and have no right of reply.
- **Staying on the list.** Applicants re-confirm each season or their place lapses. They can withdraw at any time.
- **Linked to vacancies.** The list feeds the appointment rounds: newcomers in the review balance, and applicants for clubs still vacant after current managers.
- **Offers** come with a deadline. When the applicant takes the club in Soccer Manager, the records check links their Manager Account and closes their entry.
- **Privacy.** Public pages show nothing beyond the rules. Scores, concerns, Gold and the number of game worlds are visible to the administrators only. The applicant sees their own status and approximate position.
- **Not now:** buddy managers, and a re-agreement on rule changes.

## Phases

1. **List** (tournaments + Supabase):
   - tables `waiting_list_entries` and `waiting_list_endorsements`;
   - functions to join, confirm, withdraw, give or remove a recommendation or concern, and the admin list and updates;
   - Manager Portal join card, for people with or without a club;
   - a card for current managers to recommend or raise concerns;
   - an admin Waiting list tab, with history from Stats & History and Regen stints, Gold and game worlds (from records checks, or entered by an administrator), recommendations, concerns, the score and the order.
2. **Automation:**
   - records checks look up applicants' Gold and game worlds;
   - an applicant who takes a club is detected and linked;
   - offers with deadlines and notifications;
   - a public "Join Top 100" page on smtop100.blog linking to the Manager Portal.
