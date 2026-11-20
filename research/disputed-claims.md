# Disputed claims

Topics on which informed people disagree. Each entry records the positions, what evidence exists for
each, and the position this book takes, so that every chapter treats the dispute the same way. Write
the entry before a chapter takes a side. Bibliography ids refer to `research/bibliography.yaml`.

## D1. Can individual developer productivity be measured usefully?

**Positions.**

- *Yes, with the right system.* A 2023 McKinsey article proposes measuring software developer
  productivity with a combination of DORA and SPACE measures plus new measures of its own
  (`mckinsey2023productivity`, read from an archived copy of the original page; the exhibits are images
  and were not read, so the book does not state how many new measures it proposes).
- *Not at the individual level in a way that helps.* Gergely Orosz and Kent Beck's published response
  argues that measuring effort and output for individuals distorts behavior, and that outcomes and
  impact are what matter (`orosz2023measuring`, verified).
- *Measure across dimensions, at team or system level.* The SPACE paper argues that productivity
  cannot be captured by a single metric (`forsgren2021space`, abstract). DORA's guide warns against
  using its metrics as goals or to compare teams (`dora-metrics-guide`, full text).

**Book's position.** Measure delivery and developer experience at team and system level, across
several dimensions, for improvement rather than ranking. Do not score individuals with delivery
metrics. Individual performance is assessed through evidence of impact and behavior (Chapter 9).
**Owner:** Chapter 18, which takes this position with five reasons.

## D2. Do speed and stability trade off?

**Positions.**

- *They trade off:* moving faster means more failures; quality requires slowing down. Common in
  organizations with large-batch release processes.
- *They do not, in general:* DORA's guide states that its research has repeatedly found speed and
  stability not to be trade-offs and that its metrics are correlated for most teams
  (`dora-metrics-guide`, full text).

**Evidence quality.** DORA's evidence is survey-based and correlational. Observational studies of
open-source projects associate continuous integration with releasing more often (`hilton2016usage`,
abstract) and with integrating more contributions without an observable loss of quality
(`vasilescu2015quality`, abstract); both are observational and in open-source settings.

**Book's position.** The trade-off is not a law, and the mechanism (smaller batches are easier to
test, diagnose, and roll back) is plausible. A specific transformation may still cost speed for a
period, and the book says so with numbers (Chapter 27). **Owner:** Chapters 18 and 23.

## D3. Microservices or a modular monolith?

**Positions.** The case for microservices as independently deployable services organized around
business capabilities, with decentralized data and team ownership (`lewis2014microservices`); the
case for starting with a monolith and extracting services when boundaries are understood
(`fowler2015monolithfirst`, expert opinion with stated caveats); and accounts of teams folding
distributed components back into one process, of which the best known is Prime Video's
audio/video monitoring service (`kolny2023primevideo`, now **verified** from a Wayback Machine
capture of the original post: one service, serverless components replaced by a single process,
self-reported infrastructure cost reduction of over 90 percent, and an explicit "case by case"
conclusion; it is not evidence that Amazon or Prime Video abandoned microservices).

**Evidence.** No controlled comparison of the two styles across organizations was found. Studies of
migrations are qualitative or survey-based and sample organizations that chose to migrate:
maintainability and scalability are the main motives and the service cut the main challenge
(`fritzsch2019migration`, `taibi2017processes`); one case shows technical debt growing more slowly
after extraction (`lenarduzzi2020migrating`); mature teams credit shared infrastructure built early
(`wang2021promises`). Change history carries real coupling signal for drawing boundaries
(`gall1998logical`, `zimmermann2005mining`). The mirroring hypothesis is covered in Chapter 33.

**Book's position (taken in Chapter 31).** The decision follows from change patterns, team
ownership, runtime needs, and operational capability, not from fashion. Separate the module,
deployment, data, and ownership boundaries and choose the weakest one that solves the problem.
Where the platform cannot yet give every service a pipeline, monitoring, and on-call, an
organization under about 100 engineers is usually better served by a well-modularized monolith
with a few services extracted for clear reasons. This is this book's recommendation, not a
research finding.

## D4. Centralized QA, embedded QA, or no separate QA role?

**Positions.** Central QA as an independent check; embedded quality engineers in product teams;
developers owning all testing with no separate role. Practitioner literature leans toward team
ownership with specialist support; no research found yet compares the models directly.

**Evidence.** Indirect only: in three product companies, testing was done by many roles, testing by
people with customer contact and domain expertise mattered, and developer-found defects had the
highest fix rates (`mantyla2012who`, abstract); Firefox's move to rapid releases narrowed system
testing to the highest-risk areas (`mantyla2013rapid`, abstract).

**Book's position (taken in Chapter 19).** Team ownership of quality outcomes, with specialist quality
engineers embedded where risk or domain complexity justifies them; central QA only for specialized or
mandated testing (performance, accessibility, compliance). Labeled as this book's recommendation.
Chapter 27 applies it to Northstar. **Owner:** Chapter 19. **Gap:** `research-gaps.md` G4.

## D5. Remote, hybrid, or colocated teams?

**Positions.** Strong practitioner advocates on both sides. The largest verified study in the
bibliography found that firm-wide remote work at a large technology company was associated with
more siloed collaboration networks and more asynchronous communication (`yang2022remote`; confirm
exact wording from the abstract before writing Chapter 14).

**Book's position (taken in Chapter 14).** No study shows that one working arrangement is best for
software teams. Hybrid with anchor days is a low-risk default; fully remote work needs deliberate
compensations (bridges between groups, structured feedback); newer engineers gain most from time
together. Labeled as this book's recommendation. **Owner:** Chapter 14.

## D6. Are blameless reviews effective?

**Positions.** Strong practitioner consensus in operations engineering for blameless review
(`google2017postmortem`; `allspaw2012blameless`, verified 2026-11-19). Critics argue that
"blameless" can become "accountability-free".

**Evidence.** No peer-reviewed study measuring the effect of blameless reviews on outcomes was found.
Psychological safety research (`edmondson1999psychological`) and healthcare just-culture reviews
(`murray2023just`, `vanmarum2022barriers`) support the mechanism: fear of blame suppresses reporting.
Murray et al. describe the outcome evidence for just culture as scant.

**Book's position (taken in Chapter 25).** Blameless toward individuals; strict about truthfulness,
follow-through, and system ownership (also Chapter 27, "Accountability without blame"). State the
evidence gap plainly. **Owner:** Chapter 25.

## D7. Who decides architecture: managers or technical leaders?

**Positions.** Managers own decisions because they own outcomes and staffing; staff-plus engineers own
technical direction; teams decide within guardrails. Practitioner sources differ by company shape.

**Book's position (Chapter 28).** Split the right by what the decision is mainly about, and give each
decision one named decider. Teams decide design inside their own components. Cross-team interfaces and
data contracts are decided by a technical leader with a written mandate for the domain (or the
providing team's technical lead), after written consultation of consumers; affected managers hold an
agreement right limited to capacity and dates. Organization-wide direction is decided by a small forum
of technical leaders with one named signer, the director or CTO agreeing on cost and risk. Trade-offs
of date, money, or risk appetite go to the director or CTO. Conditions: a technical leader holds the
right only with a written mandate, time to do the work, and accountability for consequences (review
trigger, involvement when the decision fails); otherwise the manager decides by default and says so; in
small organizations one person may wear both hats; disagreements between technical leaders escalate to
the owner of the trade-off; executive overrules are recorded as superseding decisions. **Evidence:**
the formal/real authority model of Aghion and Tirole (`aghion1997formal`, abstract level) and
practitioner sources (`larson-staffeng-actually-do`, `larson-staff-archetypes`,
`larson-staffeng-reporting`); no empirical study comparing these arrangements in software
organizations was found. **Owner:** Chapter 28.

## D8. How much do structured interviews and cognitive tests predict job performance?

**Positions.** The long-cited estimates of Schmidt and Hunter (`schmidt1998validity`) placed general
cognitive ability at the top of selection methods. Sackett et al. (`sackett2022revisiting`,
`sackett2023revisiting`) argue those estimates were inflated by range-restriction corrections and
revise several of them downward, leaving structured interviews among the most valid methods.

**Book's position (Chapter 7).** Use the revised estimates, state them with their uncertainty, and
prefer structured interviews and job-related work samples; do not present any single number as settled.
Gap G10 records what was not read.
