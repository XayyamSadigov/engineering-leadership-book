# Chapter 7 solutions — Hiring and Structured Interviews

Worked solutions for the [chapter 7 exercises](../parts/02-people-management/07-hiring-and-structured-interviews.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — How structured is "the same four interviewers"?

**Content.** The loop is partly structured in what it asks: every candidate meets the same people
and gets the same algorithm question. But nothing ties the question or the sessions to a written
scorecard, so it is not clear what attribute the algorithm question measures or whether anything the
job needs is measured at all.

**Evaluation.** Here the loop is unstructured. Free-text summaries with no rubric let each
interviewer decide on overall impression, and a hire or no-hire vote in a meeting combines those
impressions with whatever anchoring the meeting produces. The research distinguishes structure in
content from structure in evaluation, and this loop has only a little of the first.

**The two changes that add the most.** First, a rubric: named attributes, each rated on a scale with
anchored descriptions of poor, borderline, solid, and outstanding answers, so interviewers rate the
same thing in the same way. Second, independent ratings submitted before the debrief and revealed
together, so the meeting combines readings instead of producing one. A third, writing the scorecard
first, is arguably more fundamental; a strong answer may rank it first and explain that the rubric
depends on it.

**Weak answer.** "It is structured because the questions are the same." Same questions with
impression-based scoring is the most common false sense of structure.

## F2 — Replying to the cognitive-ability proposal

**A good reply.** The 1998 summary by Schmidt and Hunter did report the highest validity for general
mental ability combined with a work sample, an integrity test, or a structured interview. Sackett and
colleagues' 2022 revision argued that the corrections behind those figures overcorrected, and that
most estimates should fall by roughly .10 to .20. Their 2023 open-access article states a revised
cognitive ability estimate of .31, about .20 lower than before, and says it is no longer the stand-out
predictor; structured interviews rank first at .42. The case for adding a cognitive test to every
engineering loop rested on the old figures. If the aim is better prediction, improving the structure
of the interviews we already run is better supported than adding a general test.

**What not to claim.** That cognitive ability does not matter (.31 is not zero); that the revised
numbers are final (the authors say considerable uncertainty remains); or that any of these figures
describe software engineering specifically (the criterion is mostly supervisor ratings across many
occupations). A strong answer may also note that the 2022 paper pairs validity with subgroup
differences, a fairness consideration this chapter did not examine in detail.

**Weak answer.** Citing the .63 combination as current, or dismissing the revision as "one paper".

## F3 — What a validity of .42 means

**Correction.** .42 is a correlation between interview scores and later performance, not a hit rate.
It does not mean the interview is right 42 percent of the time.

**A translation.** Under textbook assumptions (both normally distributed, the top half of candidates
hired), a correlation of .42 means about 64 percent of hires turn out above-median performers,
against 50 percent for hiring at random. That is a real improvement, and it still leaves about one
hire in three below the median. (Method: for two normal variables with correlation r, the chance that
both exceed their medians is 1/4 + arcsin(r)/2π; dividing by 1/2 gives the share among hires. For
r = .42 that is about .32, or 64 percent of hires.)

**The credibility interval, for a non-specialist.** The .42 is an average across many studies in
many organizations. In some settings the structured interview predicted much better, in others much
worse; 80 percent of settings are estimated to fall between .18 and .66. So the average tells you
what structured interviews can achieve when done in the conditions studied, not what yours achieves.

**About your own loop.** The figure says that structure is worth having. It does not tell you your
loop's validity, which depends on the scorecard, the questions, the interviewers, and the debrief, and
which you cannot compute from a few hires a year. A good answer ends with that limit; a weak answer
quotes a single number as if it were a property of the method rather than of a well-run instance.

## A1 — Scorecard and loop for the next ledger backfill

**First-year outcomes** (one worked version): on the Billing on-call rotation by month 4; ships a
ledger schema change with a rehearsed migration by month 6; can diagnose a ledger incident to the
point of a safe mitigation without escalation by month 9; is the second person on one area that
today only one ledger engineer knows by month 12.

**Attributes and sessions.**

| Attribute | Must-have? | Measured in |
|---|---|---|
| Correctness of money movement (idempotency, rounding, double-entry) | Yes | Work sample; structured technical questions |
| Safe schema change on a live database | Yes | Work sample; debugging session |
| Diagnosing a production failure | No | Debugging session on recorded logs |
| Working across team boundaries | No | Behavioral interview |
| Code quality in a large Java codebase | No | Work sample |

**Work sample.** 90 minutes reviewing and then extending a real (sanitized) ledger change that
contains a migration which locks a table and a rounding defect. A strong candidate finds both and
proposes a safe rollout.

**Decision rule.** Both must-haves at "meets" or above; the rest averaging "meets".

**How it surfaces the earlier gap.** Live-migration experience would have been a must-have measured
twice, so the ledger engineer's observation would have been a recorded rating below "meets" rather
than a remark absorbed in discussion. Either the rule rejects, or the team hires knowingly with a
written ramp plan and time allocated for pairing. A strong answer notes that the second outcome may be
right: the scorecard makes the trade explicit. A weak answer copies the chapter's list without
explaining how the rule would have changed the decision.

## A2 — The hiring manager speaks first

**In the next five minutes.** Interrupt politely and name the protocol: "Before we hear views, let's
reveal the ratings; you were going to go last." Reveal all ratings. Two interviewers rated a
must-have below "meets", so the discussion starts with that attribute: each of them describes what
the candidate said or did, then others add evidence for or against. The hiring manager speaks last.
Apply the decision rule as written. If the evidence supports raising a rating, it can be raised, but
the original stays in the record.

**What to record.** Original and final ratings, the evidence cited on the must-have, the decision,
and that the hiring manager offered a view before the reveal.

**Afterward.** Make the reveal mechanical (ratings locked in the tool before the meeting can start),
brief hiring managers on why they speak last, and have facilitators open every debrief by stating the
order. Look at whether this hiring manager's debriefs show ratings moving toward their view.

**Weak answers.** Letting it pass because the hiring manager is senior, which makes the protocol
optional; or reprimanding them in front of the panel, which teaches interviewers that debriefs are
about status. A strong answer treats it as a process gap, not a character flaw.

## A3 — Six hires and a "proven" work sample

**What you can conclude.** Very little statistically. Six hires is far too few to estimate validity,
and you see only people the loop accepted, so the range is restricted. Four matches out of six could
happen with a weakly predictive work sample.

**What the two misses can tell you.** Look at each as a case. For the hire much weaker than
predicted on the work-sample attribute, read the interview notes and the rubric: did the work sample
measure what the job turned out to need, did the candidate get unusual help, or did onboarding fail
(no pairing time, wrong first assignments)? For the hire much stronger than predicted, check whether
the work sample penalized an unfamiliar tool or whether the person learned fast. Each answer points
to a different fix: the task, the rubric, or the team.

**What to change.** Keep the work sample, because job-specific samples are among the better-supported
methods, but review the specific task against the miss, add a second rater to six-month checks, and
keep collecting. Tell the hiring manager the honest version: the work sample is a reasonable
method that has not failed badly, not a proven one.

**Weak answer.** Accepting "proven" or, in the other direction, dropping the work sample because of
one miss.

## X1 — Deciding on the pilot

**Decision.** Run it, for the next two backfills, with explicit costs and measures.

**Marcus: the work sample will scare off candidates.** Replace the 60-minute algorithm exercise
with the 90-minute work sample rather than adding it, so the loop grows by about half an hour. Tell
candidates in advance what it is and why. Measure: offer acceptance and withdrawals after the work
sample is announced. Gaming: recruiters may stop telling candidates, or soften the task; review the
task with Marcus and keep it fixed for the pilot.

**Tom: infrastructure engineers pulled into panels.** Build a trained pool, cap interview hours per
person per month, and use only people whose skills the role needs. Measure interview hours by
person. Gaming: hours logged as something else; take them from the calendar invites.

**Victor: how will we know?** Within a year you will know process measures (time to accepted offer,
acceptance, panel hours, whether the protocol was followed) and the six-month checks for at most two
hires. You will not know whether the structured loop selects better; that needs years and more hires.

**What not to promise.** A measurable improvement in hiring quality within a year, or any effect on
incidents. Promise a recorded process, its cost, and a review at twelve months. A weak answer promises
quality gains to win the argument.

## X2 — Delaying backfills and adding rounds

**The arithmetic** (Northstar figures and this chapter's assumptions; fictional). Eight backfills a
year delayed by eight weeks adds 64 seat-weeks of vacancy, about 1.2 engineer-years. At $185,000 fully
loaded, that saves about $228,000 of personnel expense ($185,000 / 52 × 64). It costs the capacity of
those seats, on top of the 120 seat-weeks the 15-week median already leaves empty, and it lengthens
the period in which single-person areas like the ledger have no second person.

**The two extra rounds.** Rigor comes from the design of the loop, not from its length. Extra rounds
add interviewer time (roughly 2 to 3 engineer-hours per loop each, with write-up and debrief), more
chances for anchoring, and more weeks in which candidates accept other offers. Nothing in the
selection research says more interviews raise validity; job-specific content and structured
evaluation do. "Using" a delay for more rounds couples an expense decision to a quality claim it does
not support.

**Recommendation.** Separate the two. If expense must be held, decide explicitly which backfills
to delay, excluding roles that cover single points of knowledge or the on-call rotation, and state the
capacity cost to Victor and Rajiv. Improve the loop by structuring it, which costs about 1.2
engineer-weeks per hire, not by lengthening it. A strong answer presents the expense saving honestly
rather than dismissing the CFO's goal; a weak answer either accepts the package or rejects it without
numbers.
