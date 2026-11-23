# Project 6 solution: assessing and developing Northstar's managers

This is one worked answer to [Project 6](../p6-manager-development-and-succession.md). It treats the
director's week-24 draft in [Chapter 41](../../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md)
as a submission to be tested. The conclusion is that the draft's method is right and most of its
evidence is strong, but that it never states how the week-22 expectation page counts, three of
its Not yet ratings rest on evidence from before the window, one manager's Not yet ratings share the
same few items, and one development plan contains no delegated decision. The ratings below are this
solution's judgments, one defensible set among several; Chapter 41's are defensible under a different
treatment of that page, which this solution states. All Northstar facts are fictional.

People named, with roles (see the [cast](../../case-studies/northstar/cast.md)): Victor Lindqvist (CTO);
the engineering managers Priya Raman (Orders), Marcus Oyelaran (Billing), Elena Sokolova (Payments and
Integrations), Daniel Cho (Customer Experience), Farah Haddad (Data and Analytics), and Tom Becker
(Platform Operations); the staff engineers Ines Carvalho, Kwame Mensah, and Li Na Zhou; and the
engineers Aisha Bello and Rafael Duarte (Orders), Teodora Vasquez-Lund and Tomasz Wierzbicki (Billing
ledger engineers), Hannah Lindgren and Mateo Arango Ríos (Customer Experience's informal web and mobile
leads), Sunil Varghese (Data and Analytics), and Bram Verhoeven (senior infrastructure engineer).
Incidents named: INC-421 (bulk order upload dropped lines beyond row 500, a repeat of an earlier
failure), INC-423 (a warehouse maintenance window overlapped scheduled customer exports), and INC-426
(offline sync corrupted mobile drafts; the fix waited for app store review).

## 1. The window and the week-22 page

Window: weeks 1 to 26. Baseline-quarter facts are context.

| Expectation | When the manager learned it | Who |
|---|---|---|
| One-line job description; annual review on roadmap delivery | Before the window | All six |
| Hands-on work capped at 8 hours a week | Week 2 | Priya Raman |
| Prevention allocation by team | Week 4 | All six |
| Incident commander training | Weeks 4 and 5 | All six |
| Tier 1 operational minimums on owned components | Week 5 (DL-04) | All six |
| Every kept corrective action has a manager owner | Quarter 1 | All six |
| The six dimensions, one page | Week 22 | All six |
| Leading across sites | Never stated | Daniel Cho |
| Which of two roles comes first | Never stated | Farah Haddad |

**The rule.** The rubric and Chapter 41 say the same thing: rate Not yet only against an expectation
the manager knew before the behavior rated; facts from before the window are context. So Priya Raman's
cap (week 2) supports a Not yet on her weeks 16 to 24, and a baseline-quarter fact supports nothing.

**The open question is the week-22 page.** Chapter 41's draft in effect treats it as known by the
week-25 conversations. This solution counts an expectation from the week it was stated: the week-22
page leaves four weeks of behavior, too few to rate on, so a gap that only the week-22 page names is
rated **Not yet (unset)**. It informs development, and it is not used for pay this cycle. That is how
Chapter 41 already treats two cells; this solution applies it to all six managers.

## 2. Evidence and ratings

One dated window item per cell, with the strongest contrary item. Sources are the case pages and the
chapters indexed in [`p6-manager-evidence.csv`](../data/p6-manager-evidence.csv).

**Priya Raman (Orders, 16).** Outcomes: No evidence at week 24; bulk ordering is due at the end of week
26 (branch: if it ships with acceptance complete, the cell is rated at week 27 from the release
record). Operational ownership: Solid; week 2, Rafael Duarte takes the open bulk-upload test action
that the INC-421 recurrence showed was never done (contrary: Orders has no near-miss log). People
growth: Solid; week 2, Aisha Bello leads bulk-ordering implementation and Rafael and Aisha own
order-capture reviews, and the delegation held (contrary: Rafael's career question is open). Team
health: No evidence; nobody has asked how candid Orders is with Priya. Leverage: Solid; Orders tagged
every core/customer change for a quarter (Chapter 21), and at the start of quarter 2 Priya asks to
adopt Payments' operations review. Running the role: **Not yet**; cap stated in week 2, hands-on time
8, 10, and 12 hours at the week 16, 20, and 24 checks.

**Marcus Oyelaran (Billing, 15).** Outcomes: Solid; quarter 2, Billing reserves its first three weeks
for the ledger export the accounting integration needed, live in week 19 (context: seven of eight
baseline Billing incidents came through Core releases or migrations). Operational ownership:
**Not yet**; incident commander training stated weeks 4 and 5 and he asked to skip it; "no capacity"
was Billing's first answer on testing, flaky tests, and runbooks in quarter 1 (Chapters 19, 20, 22).
People growth: No evidence; the ledger knowledge map exists (quarter 2), but nothing yet shows a new
person able to respond alone. Team health: **Not yet (unset)**; weeks 14 and 15, the stay interviews
name after-hours load, and in week 20 Tomasz Wierzbicki reports an outside offer; no expectation on
spreading load was stated before week 22. Leverage: Solid; Billing reviewed contract expectations for
meaning (Chapter 22). Running the role: Solid; he raised the tax-svc risk himself (Chapter 30), which
is escalating early with options (contrary: asked to skip commander training).

**Elena Sokolova (Payments and Integrations, 13).** As the template's worked example: outcomes Strong
(week 19), operational ownership Strong (week 8 contract test; contrary, the configuration blind spot),
people growth Solid (rotating facilitator; the acting tech lead has no title), team health Strong (the
engineer coming off on-call presents, Elena speaks last), leverage Strong (week 16 health check for
Customer Experience; Priya's request to adopt her practice), running the role Solid (WIP limits
lowered; whether she escalated Victor Lindqvist's "read the tables now" is not recorded).

**Daniel Cho (Customer Experience, 17).** Outcomes: Solid; delivery measures healthy (Chapter 14).
Operational ownership: **No evidence** in the window; the mobile Sev2 incidents and INC-426's 1,310
minutes are baseline-quarter context. Action: read the quarter 1 and 2 records for mobile-app and
mobile-bff by week 28. People growth: **Not yet (unset)**; weeks 14 to 19, 55 of 84 one-on-ones
mainly status; week 17, Mateo Arango Ríos says he has done a lead's job for over a year. Team health:
**Not yet (unset)**; week 16, mobile rates 4 of 10 indicators red. Leverage: No evidence. Running the
role: Solid; he drafted the one-on-one changes himself.

**Farah Haddad (Data and Analytics, 11).** Outcomes: Solid. Operational ownership: Solid; quarter 2,
the team charter answers INC-423 with a maintenance notice. People growth: **Not yet (unset)**; the team
holds Senior to a staff standard (Chapter 8); one promotion to Senior in two years is context. Team
health: No evidence. Leverage: Solid; the charter gives other teams one queue (Chapter 12). Running the
role: **Not yet (unset)**; 45 percent technical time, and nobody told her which role comes first.

**Tom Becker (Platform Operations, 5).** Outcomes: Solid; week 18, environment waits from about 6 days
to 2 and other teams' requests from 20 to 14 points. Operational ownership: Solid; the two-person
interrupt rotation with a single intake (quarter 2). People growth: **No evidence**; the evidence
Chapter 41 cites (31 of Bram Verhoeven's 74 tickets moved silently, "meets expectations") is from the
baseline quarter; the window holds Tom's own expectations plan for Bram, a strong response with its
decision open. Team health: **No evidence**; knowledge concentration in Bram and the shell-script
expert was measured at baseline, not since. Leverage: Solid; the platform roadmap drafted with Kwame
Mensah (Chapter 32). Running the role: Solid.

| Manager | Outcomes | Operational | People growth | Team health | Leverage | Running the role |
|---|---|---|---|---|---|---|
| Priya Raman | No evidence | Solid | Solid | No evidence | Solid | Not yet |
| Marcus Oyelaran | Solid | Not yet | No evidence | Not yet (unset) | Solid | Solid |
| Elena Sokolova | Strong | Strong | Solid | Strong | Strong | Solid |
| Daniel Cho | Solid | No evidence | Not yet (unset) | Not yet (unset) | No evidence | Solid |
| Farah Haddad | Solid | Solid | Not yet (unset) | No evidence | Solid | Not yet (unset) |
| Tom Becker | Solid | Solid | No evidence | No evidence | Solid | Solid |

**Counted by rating:** Strong 4; Solid 3 + 3 + 2 + 2 + 3 + 4 = 17; Not yet 2 (Priya, Marcus); Not yet
(unset) 1 + 2 + 2 = 5; No evidence 2 + 1 + 2 + 1 + 2 = 8. Total 4 + 17 + 2 + 5 + 8 = 36.
**Counted by manager:** each row has six cells; 6 × 6 = 36.

**Against Chapter 41's draft** (16 Solid, 11 Not yet, 5 No evidence, 4 Strong), seven cells change:
Marcus's running the role (Not yet to Solid), Marcus's team health (to unset), Daniel's operational
ownership (to No evidence), Daniel's people growth (to unset), Farah's people growth (to unset), and
Tom's people growth and team health (to No evidence). Check: Solid 16 + 1 = 17; No evidence 5 + 3 = 8;
Not yet 11 − 4 = 7, of which 5 are unset. Four of the seven changes come from the window rule and the
evidence rule, not from a different opinion of the managers.

**Halo, both ways.** Elena's four Strong cells cite four different items, so they pass. Marcus's draft
cells in Chapter 41 rested three ratings on the same few items (the stipend, "no capacity", the skipped
training); his running-the-role cell, rated from its own evidence, comes out Solid. A halo can also
point down.

**Eight No evidence cells** are a finding about the director's information: no group skip-levels, no
reading of Daniel's or Tom's window records. Each has an action: Priya's team health and Daniel's and
Tom's people cells from the first quarter 3 skip-level groups; Daniel's operational ownership from
incident records by week 28; Marcus's people growth from the week-38 knowledge map recount; Daniel's
leverage from his peers by week 30.

## 3. The Not yet flow

| Cell | Expectation stated? | Mainly the system? | Skill or fit? | Response |
|---|---|---|---|---|
| Priya, running the role | Yes, week 2 | Partly: a renewal date in week 26 and a span of 16 | Skill: time budget under pressure | Plan; recheck after the date passes |
| Marcus, operational | Yes, weeks 4 and 5 | Partly: the Core release train triggered most incidents, but the response (training, runbooks) is his | Skill | Plan with a delegated decision |
| Marcus, team health (unset) | No | Partly: three ledger experts, one backfill | Not yet known | State the expectation now; develop |
| Daniel, people growth (unset) | No | Partly: 17 reports across two sites | Not yet known | State it; plan |
| Daniel, team health (unset) | No | Yes: one board and sprint for two products | Director's problem first | Fix the system question; rate his response |
| Farah, people growth (unset) | No | No | Not yet known | State it; plan |
| Farah, running the role (unset) | No | Yes: two roles nobody separated | Director's problem first | Decide which role comes first by week 27 |

No cell reaches "possible role fit": that needs Not yet on several dimensions for two quarters despite a
plan, and no plan existed before week 27.

## 4. Six plans for quarter 3

This solution adopts Chapter 41's plans for four managers, amends two, and adds what each plan does under
the open decisions.

| Manager | Focus | Delegated decision and level | Bench action | Check |
|---|---|---|---|---|
| Priya | Running the role | Aisha Bello runs Orders' quarter 3 planning, level 3 | Aisha named interim cover; her order-capture review share moves to Rafael Duarte and one other senior, so she does not hold three roles | Hands-on hours at or below 8 in weeks 32 and 38 |
| Marcus | Operational ownership | Teodora Vasquez-Lund leads the TR-07 pairing plan, level 3; Marcus joins ledger incidents only as commander | A named senior engineer runs Billing's monthly quality review preparation (management work, not ledger work) | Knowledge map recount, week 38: one more person able to respond alone on credit notes or period close |
| Elena | Organization-wide leverage | Chairs a monthly artifact-review slot on operational readiness, level 3 | Informal tech lead represents the team in cross-team planning; their scope written down | Peer managers asked, week 38 |
| Daniel | People growth | A career conversation with every engineer, and a sponsorship action each for Hannah Lindgren and Mateo Arango Ríos | Hannah and Mateo as half-team covers | One-on-one recode, weeks 32 to 37 |
| Farah | Running the role | Sunil Varghese leads one warehouse design decision, level 3 | Sunil on the architecture half | Technical share in the week-38 calendar |
| Tom | People growth | **Amended:** Tom decides the order of the quarter 3 platform roadmap items within the 4.5 FTE line, level 3, with Kwame Mensah consulted | **Amended:** one infrastructure engineer (not the person whose plan is open) runs the weekly intake review of the interrupt rotation | Quarter 3 skip-level group: is work moved silently? Pages and tickets per person on the rotation |

Chapter 41's plan for Tom ("raises any performance gap with the person within two weeks") is an
expectation, not a delegated decision, and its bench action was "none yet". Both are amended. The
roadmap order is a real decision; the CI consolidation target is not offered, because it is an open log
entry (DL-10) with no decider.

**Under the open decisions.** Rafael chooses the staff track: Aisha remains Orders' only development
candidate, so a second is sought (Orders' other seniors are not named in the case; ask Priya). Tomasz
leaves: Marcus's check moves from "one more person" to "no fewer people" able to respond alone, and the
pairing plan reprioritizes posting rules. Customer Experience splits later: Hannah and Mateo each cover
a whole team, not a half. Bram's plan is decided either way: Tom's bench action does not depend on him.

## 5. Succession at week 26

Chapter 36's readiness scale and coverage rule, applied to the ten critical roles with week-26
knowledge.

| Critical role | Ready now or interim | In development | Gap |
|---|---|---|---|
| Orders (Priya Raman) | Aisha Bello, interim | Aisha Bello; Rafael Duarte if he chooses management | Nobody ready now |
| Billing (Marcus Oyelaran) | None | None | Teodora Vasquez-Lund's ledger knowledge is not management |
| Payments (Elena Sokolova) | Informal tech lead, interim | Same person | One person in both columns |
| Customer Experience (Daniel Cho) | Hannah Lindgren, interim | Mateo Arango Ríos | Each covers half the team |
| Data and Analytics (Farah Haddad) | None | Sunil Varghese, architecture half only | Farah holds two roles |
| Platform Operations (Tom Becker) | Kwame Mensah, interim | None | Kwame holds a critical role |
| Staff, core domain (Ines Carvalho) | None | Aisha Bello, Rafael Duarte (order capture); Teodora Vasquez-Lund (ledger) | Nobody covers the whole domain |
| Staff, infrastructure (Kwame Mensah) | Bram Verhoeven, Core Jenkins only | None | His expectations plan is open |
| Staff, data and integration (Li Na Zhou) | None | Sunil Varghese (warehouse); Payments' informal tech lead (integration) | Split cover |
| Director | Elena Sokolova, interim | Elena Sokolova | If Elena acts, Payments falls to its informal tech lead |

**Counted by row:** ready now 0; interim cover in 6 rows (Orders, Payments, Customer Experience,
Platform, infrastructure staff, director); no interim cover in 4 (Billing, Data and Analytics, core
domain, data and integration). **Counted by column:** interim names Aisha, the tech lead, Hannah, Kwame,
Bram, Elena: 6. 6 + 4 = 10.

**Coverage rule.** Adequate cover needs interim or ready-now cover and someone in development, with a
cover who neither holds another critical role nor is primary cover for one. Platform fails (Kwame holds
a critical role), the director's role fails (Elena does), infrastructure staff fails (nobody in
development). Orders, Payments, and Customer Experience pass: 3 of 10, and Orders and Payments each by one
person in both columns.

**People named more than once:** Aisha Bello 3 (Orders interim and development, core-domain
development); Payments' informal tech lead 3 (Payments interim and development, integration
development); Sunil Varghese 2; Rafael Duarte 2 (both conditional on his choice); Elena Sokolova 2 while
holding a critical role; Kwame Mensah 1 while holding one. Four people carry 10 of the table's
entries. The week-44 table in Chapter 36 reaches the same count; at week 26 the method alone produces
it, which is the argument for doing it now rather than when a reorganization forces the question.

**Bench actions** (this solution's estimates: a trial assignment at about 10 percent of a person's time
for 13 weeks costs about 1.3 engineer-weeks):

| Gap | Action in quarter 3 | Sponsor | Cost |
|---|---|---|---|
| Billing | Ask Teodora Vasquez-Lund, without commitment, whether she wants management work; if yes, she runs one quarter planning session | Director | 1.3 |
| Data and Analytics | Sunil co-owns warehouse architecture (the plan above) | Farah | 1.3 |
| Payments | Write the tech lead's scope; bring a promotion case to calibration if it holds | Elena | 1.3 |
| Platform | The intake-review engineer (Tom's plan) | Tom | 1.3 |
| Customer Experience | Mateo and Hannah each run their half's planning | Daniel | 2.6 |
| Core domain | Ines Carvalho pairs Aisha or Rafael on one Core design review a fortnight | Director | 1.3 |

Total about 9.1 engineer-weeks, under 1 percent of the quarter's 1,040, against a median 15 weeks to
replace a leaver.

## 6. Conversations, HR, and the director's time

**Weeks 25 and 26.** Self-assessments due two working days before each 90-minute conversation. The
manager speaks first, then the director shares the evidence items, never who said what in a skip-level.
They agree one focus, and the written plan follows within three days. Priya's conversation is held at
the end of week 26 or in week 27, so that the outcomes cell can be rated on the bulk-ordering record
rather than a forecast. No manager's ratings are discussed with another.

**HR record.** Final ratings with evidence items; "Not yet (unset)" marked as development only;
No evidence never converted. No composite.

**Director's hours per quarter.** One-on-ones 6 × 0.75 × 13 = 58.5; skip-levels (two groups of three at 45
minutes plus one individual slot at 30, 2.0 hours a week) 2.0 × 13 = 26; assessment 6 × 4 hours every
two quarters = 12 a quarter. Total 96.5, about 7.4 hours a week (4.5 + 2.0 + 0.9), which exactly fills
the 4.5 hours of one-on-ones and 2 of skip-levels the constraint names, plus under an hour of
writing. One-off: six 90-minute conversations (9 hours) and about 6 hours on the
succession table in weeks 25 and 26.

**The hypothetical test.** To Victor's ranking: decline, because ratings are per dimension and teams sit
in different parts of the system; offer each manager's ratings with evidence and the calibrated cycle as
the route to pay. To "who runs Payments if Elena is promoted": nobody is ready now; the informal tech
lead could hold it for weeks, not quarters; and promoting Elena also removes the director's only interim
cover. That answer is the succession table's purpose.

## 7. Evaluation of Chapter 41's draft

**Strengths.** Dated evidence for most cells; No evidence used openly (5 cells); outcomes read in
context for Marcus; two cells marked unset; no composite; plans with real delegated decisions for five
managers; the director's own line (written expectations by week 27).

**Weaknesses, honestly.**

1. **How the week-22 page counts is not stated,** and it is applied unevenly: two cells are marked unset,
   while people growth for Daniel and Farah, rated against no earlier expectation, are plain Not yet.
2. **Three Not yet cells rest on baseline-quarter evidence:** Daniel's operational ownership, and Tom's
   people growth and team health. The rubric treats them as context; the chapter itself notes that
   the three must be re-sourced before week 27, and the draft has not yet done it.
3. **One manager's cells share evidence:** Marcus's three Not yet ratings lean on the same items.
4. **Tom's plan has no delegated decision and no bench action.**
5. **No succession table at week 26.** The chapter defers to Chapter 36, which builds it at week 44,
   after the reorganization question has already been raised.

**Scored against the rubric:** expectations 6 of 10; evidence 15 of 20; rating judgment 11 of 15; plans
16 of 20; succession 6 of 20 (a bench column per manager, no table); process 10 of 15 (conversations
and finalization dated, director's hours computed, the hypothetical not addressed). Total 64:
adequate, and it fails acceptance criteria 2 and 5.

**Other defensible answers.** Keeping Chapter 41's ratings, counting the week-22 page as known by the
conversations, scores as well, if that treatment is stated and applied to all six and the three
baseline-evidence cells are re-sourced. Rating Tom's people growth Solid on the strength of his plan for
Bram is defensible if the plan's execution is the quarter 3 check. Naming Rafael rather than Aisha as
Orders' interim cover is defensible if Aisha's load is the deciding factor, but only after Rafael's
choice, which is open.

## What a weak submission looks like

> "Elena is our strongest manager and should be considered for promotion. Marcus is defensive about
> capacity and needs coaching. Daniel cares about his people but is too nice. Farah is too technical.
> Priya is learning. Tom is fine. Overall ranking: Elena, Priya, Tom, Daniel, Farah, Marcus. All
> managers will attend a leadership course in quarter 3. Successors: each manager's senior engineer."

Against the rubric: no expectations or window (weak); adjectives instead of dated evidence (weak); a
ranking, which the rubric forbids, and no system context for Marcus or Daniel (weak); a course instead
of a delegated decision, no checks (weak); "each manager's senior engineer" names nobody, counts nothing,
and ignores that Kwame and Elena hold critical roles (weak); no conversations, no self-assessment, no
director hours (weak). It fails acceptance criteria 1 to 5 and 8.

**An adequate submission** reproduces Chapter 41's matrix and plans with correct counts and builds a
succession table, but does not state how the week-22 page counts, keeps the baseline-quarter evidence, and
counts the table once. It scores in the 60s. **What separates excellent from adequate** is applying the
rubric's rules to the director's own evidence (the window, the week-22 page, the halo in both
directions), and counting the succession table until the four people carrying ten entries become
visible.
