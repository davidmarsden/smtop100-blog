# Does the weighting change the result?

Every applicant for a vacant club gets an appointment score out of 100 ([rule 3.2](https://smtop100.blog/rules/#32-club-vacancies-and-manager-appointments)). It's built from six parts:

| Part | Points | What it measures |
|---|---|---|
| This season | 20 | Where you finished, and how that compared with the prediction |
| Recent seasons | 15 | The last two completed seasons |
| Honours | 15 | Titles and promotions |
| Level | 10 | Your record at the vacancy's division or higher |
| Stability | 20 | Time at your current club, bottom-three finishes, and conduct |
| Activity | 20 | Competitions, trading with other Top 100 managers, squad building, helping run Top 100, community, and focus |

Those weights aren't arbitrary, but they are a judgement. Why 20 for this season and only 10 for level? Why does activity count as much as this season's results? A fair question is whether a different set of weights would have picked different managers.

So we tested it.

## The test

We took this round's applicants and their actual score breakdowns, and re-weighted the parts six ways. Each total was rescaled to 100, and the allocation was re-run every time, using the same method as the real one: each round, every applicant points at their most-preferred open club, and the highest score is appointed.

| Weighting | 1st | 2nd | 3rd | Dortmund | Hellas | Juventus | Atlético |
|---|---|---|---|---|---|---|---|
| **The rules as they are** | Mister TRX | Neil Frankland | Sir Stephen Beddows | Frankland | Beddows | TRX | Simon Thomas |
| Results first: this season and recent seasons ×1.5 | Mister TRX | Neil Frankland | Sir Stephen Beddows | Frankland | Beddows | TRX | Simon Thomas |
| Long record first: honours and level ×1.5 | Mister TRX | Neil Frankland | Sir Stephen Beddows | Frankland | Beddows | TRX | Simon Thomas |
| Loyalty first: stability ×1.5 | Mister TRX | Neil Frankland | Sir Stephen Beddows | Frankland | Beddows | TRX | Simon Thomas |
| Activity first: activity ×1.5 | Mister TRX | Neil Frankland | Sir Stephen Beddows | Frankland | Beddows | TRX | Simon Thomas |
| Every part equal | Mister TRX | Sir Stephen Beddows | Neil Frankland | Frankland | Beddows | TRX | Simon Thomas |
| **Plus a new squad-health part** (10 points) | Sir Stephen Beddows | Mister TRX | Neil Frankland | Frankland | Beddows | TRX | Simon Thomas |

## What it shows

**1. This season, the weights hardly matter.** Whichever parts are given more weight, the same three managers come out on top, and every club goes to the same manager. When the strongest candidates are this far ahead, no reasonable weighting overturns them.

**2. Managers' own choices matter more than the weights.** You can only be appointed to a club you applied for, in the order you put them. Some of the strongest managers applied for just one or two clubs, so for some vacancies the real decision was made by who applied, not by the score.

**3. We also tested a squad-health part.** Several managers have argued, on the newsfeed and elsewhere, that the score should reward leaving a squad in good shape: younger players, real market value, not just high ratings bought with older players. So we tried adding a 10-point part for it. It was the only change that altered the order, swapping the top two. But it still didn't change a single appointment.

## Why we're keeping the rules as they are

Top 100 is a football management game, and the aim is to win matches and titles. Managers play it in different ways:
- some love scouting, trading and long squad-building projects;
- some just want to win matches;
- the best do both.

Winning is the natural measure for a better job. It's also what most applicants are offering: the managers who apply most often tend to be the ones winning promotions and titles. The squad builders often don't apply at all, or apply for jobs a step beyond what their results so far support.

So winning stays at the heart of the score. Squad health is still useful **context**: the admin team looks at the squad a manager would leave behind, and at what each vacant club needs. It just isn't a separate part of the score.

## What each vacant club needed

This round we also wrote down, for every vacancy, what kind of manager we thought the club needed. You can see it on the [vacancies list](https://tournaments.smtop100.blog/appointments):

- **Dortmund:** a winner, to turn one of the two strongest squads in Top 100 into title challengers.
- **Hellas Verona:** a winner who brings stability, to get the champions of Seasons 20 to 25 winning again before a gradual rebuild.
- **Juventus:** a proven promotion winner, to go straight back up and then challenge for the title.
- **Atlético Madrid:** a winner. The young squad has been built, and the job is to win promotions with it.

The score tells us who has the strongest record. What the club needs helps the admin team decide between close candidates.

The full rules are in [section 3.2](https://smtop100.blog/rules/#32-club-vacancies-and-manager-appointments), and every score and decision is published at [tournaments.smtop100.blog/appointments](https://tournaments.smtop100.blog/appointments).

<!--
NOTES FOR DAVID (delete before publishing):
- Publish only after the vacancy decisions are published: the post names the leading candidates and the allocation's suggested appointments. If the admin team's final appointments differ from the allocation (for example TRX to Dortmund, or Chris East to Atlético), update the table and add a line saying the team departed from the allocation and why.
- Method: each applicant's rule 3.2 breakdown from the scoring, with each part multiplied by its weight and the total rescaled to 100. The squad-health part = 5 + (squad value rank − squad strength rank, among the 100 clubs) ÷ 6, capped at 0–10, with the other parts scaled to 90. Community assessments were still blank (half marks for everyone).
- Scores aren't shown, only the order, to keep the focus on the method. Add them if you prefer: TRX 77.9, Frankland 71.9, Beddows 68.8 under the current rules.
- No individual squad's age or value is named.
-->
