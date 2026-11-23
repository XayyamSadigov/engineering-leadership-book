# Chapter 40 solutions — The Director's Job: Leading 50 to 150 Engineers

Worked solutions for the [chapter 40 exercises](../parts/09-engineering-directorship/40-the-directors-job.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — "My managers tell me everything"

**What the confidence can tell the director:** that the managers are communicative and that nothing
alarming has reached the director. **What it cannot tell them:** what has not reached them. That is
the whole problem. Milliken, Morrison, and Hewlin found that most of the 40 employees they
interviewed had stayed silent with a supervisor about a concern, most often for fear of being labeled
negatively (an exploratory, qualitative study read at abstract level). A director of 120 has two such
hops, and the second carries the manager's own reputation. Williamson's model makes the same point in
structural terms: each layer distorts. The director's belief is untestable from inside the channel it
is about.

**A low-cost test:** one quarter of skip-level groups of three (about 30 hours across the quarter for
120 engineers, 40 groups at 45 minutes), plus reading the raw records of two incidents a month.
Compare what comes up with what the managers had raised. If the managers really do raise everything,
the cost buys confirmation and relationships; if not, it finds the filters.

**Weak answer:** "trust your managers" or "managers can't be trusted". The point is calibration, not
trust or distrust.

## F2 — Classifying signal sources

| Item | Source | Main distortion |
|---|---|---|
| Billing's on-call pages for two weekends | Direct data | Read without context: pages that needed no action look like noise but show the alerting problem (61 of 180 at baseline needed no action) |
| A group with three Orders engineers | Skip-level | Group effects and fear of labeling; one person's view may be suppressed or amplified |
| A renewal customer's quarterly review | Customer contact | The loudest or largest customer stands in for all; sales framing |
| Review of a payments-gateway Sev2 | Incident review | The director's presence changes the room; people perform blamelessness |
| A manager's slide on team health | None of the four: it is the main channel | The manager's selection and framing |

A good answer notices the trap in the last item: a manager's report on health is the primary source
the others exist to test, however well made. It also says that each firsthand source has its own
distortion, so none is "the truth"; the value is in disagreement between sources. The weak answer
treats raw data as undistorted. Measurement gaps are distortions too: at Northstar the four shell-script
services logged nothing, and severity was rated without definitions before week 3.

## F3 — Coverage arithmetic for 85 engineers

**Groups of four:** 85 ÷ 4 = 21.25, rounded up to 22 groups. At 45 minutes each, 22 × 0.75 = 16.5
hours a quarter, or 16.5 ÷ 13 = about 1.3 hours a week. **Latency:** a concern raised just after an
engineer's slot waits up to 13 weeks for the next one.

**Groups of two:** 85 ÷ 2 = 42.5, rounded up to 43 groups; 43 × 0.75 = 32.25 hours a quarter, about
2.5 hours a week. Latency is unchanged, because coverage is still once a quarter.

**What changes besides cost.** Smaller groups make individual topics easier to raise and reduce the
chance that one confident voice sets the agenda; a pair is close to an individual meeting at three quarters of
the cost per person. Larger groups surface shared problems and cost less, but a group of four with mixed
seniority may stay at safe topics. A good answer chooses size by what the director most needs to hear
(shared friction or individual risk) and handles latency with the other sources (weekly incident
reviews and raw data), not by holding skip-levels more often. The weak answer only computes hours.

## A1 — The skip-level rule, and Daniel

**A workable rule, announced at the first leadership team meeting of quarter 3 (or the managers' meeting if that redesign is not adopted), before the first group:**

- *Purpose:* to hear how work feels from the teams, and to calibrate what the director knows, not to
  evaluate managers or run teams.
- *What passes on:* patterns, to the relevant manager, within a week, without names unless the person
  agrees. Anything about safety, harassment, or legal risk goes to the right channel immediately.
- *What stays confidential:* individual career or personal topics, unless the person asks the director
  to raise them.
- *What the director never does in a skip-level:* assign work, change priorities, promise anything the
  manager has not agreed, or criticize a manager.
- *How managers hear back:* a monthly summary of patterns to all six managers, and what the director
  is changing because of them.

**Daniel and Mateo.** Mateo agreed in week 17 that the director could raise what he said, so Daniel
should hear it before the first Customer Experience group, from the director, in a one-on-one, framed
as information about a structure (one board, a lead's job without a title) rather than a complaint.
Otherwise Daniel learns that his team is being interviewed after a conversation he was not told about,
which is exactly the back-channel pattern the rule is meant to prevent. A good answer also schedules
Customer Experience in its normal place in the rotation (Bogotá first, as planned for all 16 Bogotá
engineers), not as a special session. The weak answer keeps Mateo's conversation from Daniel "to
protect Mateo", when Mateo has already consented.

## A2 — Ledger escalation "in progress"

**Pattern or one case?** Two engineers in one group is more than an anecdote but less than a pattern.
Before acting, check other sources: the paging tool for the last month (who handled after-hours ledger
pages), and whether the stay interviews in weeks 14 and 15 named the same issue (two of the three ledger
experts named after-hours escalation as a reason they might leave, and Tomasz Wierzbicki's offer is
still open). Those make it a pattern with retention risk attached.

**Ask the manager first.** In the next one-on-one with Marcus Oyelaran, share the pattern without names
and ask what "in progress" means: what has changed, by when, what is blocking. Then follow the diagram.
If Marcus knew and did not raise the lack of progress, fix what reaches the director: ask for the
escalation path's status in his weekly update with a date and an owner. If the block is systemic (no
second ledger-capable responder ready; Tamsin Achterberg can respond alone only on credit notes), the
director owns it: capacity for the ledger knowledge plan, or a temporary change to the rotation.

**What not to do:** tell the Billing engineers that the director will fix it, change the rotation
directly, or criticize Marcus in front of anyone. A good answer separates the information problem (the
update said "in progress") from the substance (the path has not changed) and acts on both within two
weeks. The weak answer treats the skip-level as a verdict on Marcus.

## A3 — Groups or individual skip-levels in quarter 3

**What each format found.** The individual conversations from week 16 produced the quarter's most
consequential signal: Mateo Arango Ríos, one to one in week 17, describing a lead's job done for over
a year without recognition. Northstar has never run group skip-levels, so their value there is a
prediction: groups tend to surface shared friction (a team's after-hours ledger pages, a recurring
dependency on Orders) that one person might present as a personal complaint. Groups are better at shared
friction; individual conversations at personal risk and at what someone will not say in front of
peers (the fear of labeling in Milliken and colleagues' interviews).

**Coverage.** Four individual conversations a week reach 52 people a quarter (44 had been held by
week 26), so 25 of 77 would go unheard each quarter; two groups of three reach 78 places, enough for everyone.

**A defensible answer:** run the proposal (groups for coverage, one individual slot a week), but
reserve the individual slots for the list of eight plus anyone who asks after a group, and keep
Bogotá groups to engineers from one team, so mobile engineers are not outnumbered. **What would show
the choice was wrong:** groups that produce only themes the managers already reported by week 33, or an
individual concern (a resignation, a conflict) that surfaces later and that a group member says they
had not wanted to raise in the group. Another defensible answer keeps individual conversations and
accepts partial coverage, prioritizing teams with the weakest signals.

The weak answer picks a format on cost alone, or assumes that full attendance at groups means
everything has been heard.

## X1 — "Five and a half hours of listening is a luxury"

**The response.** The 5.5 hours (two of them skip-levels already in Chapter 37's forum plan) are not
instead of next year's organization; they are how the director knows whether it rests on reality. In two
quarters, the surprises that mattered reached the director firsthand or late: the week 7 severity
drift was found by reading incidents, mobile's four red areas by a facilitated health check, Mateo's
lead role by a direct conversation, while the slipped migration check surfaced only through a Sev1.
Next year's organization may decide whether to split Customer Experience and promote Mateo; it should not
rest on Daniel Cho's status updates alone. And the hours come mainly from escalations and
administration, not from the two protected strategy half-days, which stay at 11 hours.

**If Victor insists**, cut in this order: the monthly customer call (Sofia Alvarez's escalation review
covers much of it), the individual skip-level slot, then the incident-review half-hour. Keep the raw-data
hour and the incident review, the cheapest early warning on quality, which is the mandate.

**Evidence at the end of quarter 3:** a list of issues first learned through firsthand sources, with
how much earlier they arrived than through the main channel; decisions changed because of them; and
the managers' view of whether skip-levels helped or undermined them. Commit in advance to cut the
hours if the list is empty. A good answer offers a falsifiable test. The weak answer argues that
listening is a leadership virtue.

## X2 — The Bogotá travel budget

**Options.** Escalating over Rajiv Menon to Victor Lindqvist for a few thousand dollars spends
credibility on a small item. Finding the money elsewhere (inside the $250,000 discretionary tooling
budget, which is meant for tooling) is a misuse that will look worse when found. Redesigning coverage
by video is free and partly works.

**A defensible answer:** redesign first, and make a case to the person who decides. Schedule all 16
Bogotá engineers in the first five weeks of the rotation as planned, with mobile's groups held by video
with each engineer on their own screen, and hold individual meetings with Mateo
monthly. Then take the case to Victor (who owns the engineering budget conversation with Rajiv), not
around Rajiv: Mobile has the worst health check in the organization; two of Customer Experience's four
baseline Sev2s were on the mobile side; the open Customer Experience structure question could produce Northstar's
first Bogotá-based manager, whose success depends on the director knowing the site; and one trip costs little against the
cost of losing a mobile engineer (median 15 weeks to backfill at baseline). Ask for a small standing
travel line rather than one trip, since Northstar has never had travel as a budget line.

A good answer respects flat operating expense, uses evidence rather than fairness alone, and has a
plan that works if the answer is still no. The weak answer quietly moves money between budget lines.
