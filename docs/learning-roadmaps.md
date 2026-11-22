# Learning roadmaps

The book can be read front to back, but most readers have a specific transition or problem in front of
them. These eight paths select and order chapters for those situations: six by role, one for tech leads
and staff-plus engineers, and one for a quality transformation. Chapter numbers refer to the
[curriculum](curriculum.md).

## Choosing a path

| You are | Path | Reading | With practice |
|---|---|---|---|
| A senior engineer becoming a manager, or in your first year | [A](#path-a-new-engineering-manager) | 16 chapters | about 18 weeks |
| A manager with a year or more running a team | [B](#path-b-experienced-engineering-manager) | 14 chapters | about 19 weeks |
| Managing managers, or about to | [C](#path-c-engineering-director) | 13 chapters | about 20 weeks |
| A director becoming a VP, or a new VP | [D](#path-d-vp-of-engineering) | 10 chapters | about 16 weeks |
| A VP or senior director preparing for a CTO role | [E](#path-e-cto-aspirant) | 5 chapters, then the capstone | about 13 weeks, plus the capstone |
| A sitting CTO or VP with a specific problem | [F](#path-f-cto-reference) | read by problem | as needed |
| A tech lead or staff-plus engineer | [G](#path-g-tech-lead-and-staff-plus-engineer) | 12 chapters | about 14 weeks |
| Responsible for fixing quality or reliability | [H](#path-h-quality-transformation) | 14 chapters | about 14 weeks, plus projects |

Paths A to E form one climb: each assumes the one before it, so no chapter appears twice. If you join
the climb partway, skim the earlier path's list and read any chapter whose topic is new to you.

**How the times are calculated.** About four hours a week: one chapter (30 to 45 minutes to read), one
exercise, and one reflection question, so roughly one chapter a week. A full project adds 18 to 35
hours, or five to nine weeks at the same pace; each project also has a shorter core version (see the
[projects index](projects/index.md)).

**Before you start any path,** read the [Northstar overview](case-studies/northstar/index.md) (about
fifteen minutes) and glance at the [timeline](case-studies/northstar/timeline.md). Every chapter uses
the case, and the chapters are not in story order. The [cast](case-studies/northstar/cast.md) and the
[glossary](glossary.md) are there when you meet an unfamiliar name or term.

## Path A: New engineering manager

**For:** senior engineers and tech leads preparing for, or in the first year of, a people-management role.
**Prerequisites:** none.
**Before you start:** the Northstar overview (15 minutes).
**Focus:** the identity change, delegation, one-on-ones, feedback, hiring, performance, and team effectiveness.

| Order | Chapters | Why in this order |
|---|---|---|
| 1 | 1, 2, 3 (the job, the transition, leverage) | What the job is, before any technique |
| 2 | 5, 6 (one-on-ones, feedback) | The daily tools |
| 3 | 11, 12, 13 (trust and accountability, team agreements, decisions) | The team as the unit |
| 4 | 7, 8, 9, 10 (hiring, careers, performance, retention) | The people decisions you will make in year one |
| 5 | 15, 16, 18 (planning, flow, measurement) | Execution and measurement at team scale |
| 6 | 14 (distributed teams and diagnosing dysfunction) | Diagnosing a team that is not working, once you know what working looks like |

**Practice:** none of the eight projects is set at a first-line manager's scope, so this path ends with a
practice set on your own team instead (about 8 to 10 hours, spread over the path): run four weeks of
one-on-ones with the [one-on-one template](templates/one-on-one.md), write one
[career development plan](templates/career-development-plan.md) with an engineer, run one
[team health assessment](templates/team-health-assessment.md), and do the Applied Leadership exercises
of Chapters 5, 6, 9, and 14. Project 2 is the natural first project once you start Path B.
**Schedule:** about 16 weeks of reading, about 18 with the practice set.

## Path B: Experienced engineering manager

**For:** managers with a year or more running a team who want to run delivery and quality well, lead
senior and staff engineers, work across teams, and prepare for a larger scope.
**Prerequisites:** Path A or equivalent experience.
**Before you start:** the Northstar overview (15 minutes).
**Focus:** predictability, quality and reliability at team scale, technical leadership, and working with product and peers.

| Order | Chapters | Why in this order |
|---|---|---|
| 1 | 4 (the leadership ladder) | Where you are, and what the next level asks |
| 2 | 17 (predictability) | Commitments other teams can rely on |
| 3 | 19, 21, 22, 23 (quality, technical debt, testing, code review and CI/CD) | Quality as something your team engineers, not inspects |
| 4 | 24, 25 (reliability and SLOs, incidents) | Running a service in production |
| 5 | 28, 29 (architecture decisions, staff and principal engineers) | Sharing technical authority with your strongest engineers |
| 6 | 44, 42, 46 (working with product, cross-team dependencies and influence, stakeholders) | Getting things done through people you do not manage |
| 7 | 56 (recovering a failing organization) | Triage and the keep, coach, move, or replace decision, which the project applies |

**Project:** [Project 2](projects/p2-diagnose-a-low-performing-team.md), Diagnose a Low-Performing
Engineering Team (about 18 to 24 hours). It is set one level up: you play the new director diagnosing
Billing, a team of 13, in your first three weeks. The team is at the scale you know, and the director's
view is the rehearsal for the next role. It applies Chapter 56 and draws on Chapters 9, 16, and 25, all in
Paths A and B, and on Chapter 40's advice on gathering signal as a director (Path C).
**Schedule:** about 14 weeks of reading, about 19 with the project.

## Path C: Engineering director

**For:** experienced managers taking on managers of their own, or new directors.
**Prerequisites:** Path B or equivalent experience.
**Before you start:** the Northstar overview and the [timeline](case-studies/northstar/timeline.md) (20 minutes).
**Focus:** managing managers, the operating system, quality at organization scale, organizational design, and leading change.

| Order | Chapters | Why in this order |
|---|---|---|
| 1 | 40, 41 (the director's job, managing managers) | How the job changes when your reports are managers |
| 2 | 37, 38, 39 (cadences, scorecards and capacity, reviews and reporting) | The operating system you will run the organization through |
| 3 | 27, 20 (quality transformation, engineering standards) | Quality as an organizational property |
| 4 | 33, 34, 35, 36 (team topologies, spans and layers, organizations at four scales, reorganizations) | Organizational design |
| 5 | 43 (leading change, director failure patterns) | How directors fail, and how change sticks |
| 6 | 45 (engineering economics) | Arguing for capacity and investment in money terms |

**Projects:** choose one, by the problem in front of you (each about 20 to 35 hours; the chapters they
apply are in Paths A to C):

| If your problem is | Project |
|---|---|
| Quality is declining and you have just arrived | [Project 3](projects/p3-quality-transformation-plan.md), quality transformation plan (Chapter 26 also helps) |
| Your calendar and meetings have grown back | [Project 1](projects/p1-management-operating-system.md), management operating system |
| Your managers need development and you have no bench | [Project 6](projects/p6-manager-development-and-succession.md), manager development and succession |
| The structure no longer fits the work | [Project 4](projects/p4-redesign-an-80-engineer-organization.md), redesign an 80-engineer organization |

**Schedule:** about 13 weeks of reading, about 20 with one project. Each further project adds five to
nine weeks.

## Path D: VP of Engineering

**For:** directors becoming VPs, and new VPs managing several directors.
**Prerequisites:** Path C or equivalent experience.
**Before you start:** the timeline and the [quarter 4 briefing](case-studies/northstar/quarter-4-briefing.md)
(20 minutes); these chapters are set in Northstar's quarters 3 and 4, and at Halvard Systems.
**Focus:** the portfolio, capacity and workforce strategy, multi-year change, technology direction, and the hard situations.

| Order | Chapters | Why in this order |
|---|---|---|
| 1 | 47, 48, 49 (the VP role, capacity and workforce, multi-year transformation) | The job: directors, the portfolio, and change over years |
| 2 | 30, 51 (technical strategy, enterprise technology strategy) | Strategy at engineering scale, then the layer above it |
| 3 | 31, 32 (service boundaries, platform engineering) | The structural technology bets a VP funds |
| 4 | 57, 58, 59 (crises and disagreement, reductions and acquisitions, change under constraint) | The situations that test a VP |

**Project:** [Project 7](projects/p7-twelve-month-engineering-strategy.md), Design a 12-Month Engineering
Strategy (about 22 to 28 hours). Its prerequisite chapters (29, 30, 38, 45 to 49, and 51) are all in
Paths B to D.
**Schedule:** about 10 weeks of reading, about 16 with the project.

## Path E: CTO aspirant

**For:** VPs and senior directors preparing for a CTO role.
**Prerequisites:** Path D or equivalent experience.
**Before you start:** the quarter 4 briefing (10 minutes); every chapter here turns on decisions still open at year end.
**Focus:** the CTO job, finance, risk, data and AI, and boards. Chapter 56 (Path B), on recovering a
failing organization, is worth rereading from the CTO's seat.

| Order | Chapters | Why in this order |
|---|---|---|
| 1 | 50 (what a CTO does) | The job, before its parts |
| 2 | 52 (investment, budgeting, financial literacy) | Finance before risk and boards, because those conversations are held in money |
| 3 | 53, 54 (risk and security, data and AI) | The two areas where a CTO answers to the board directly |
| 4 | 55 (boards, due diligence, executive decisions) | Presenting and defending all of it |
| 5 | 60 (the capstone) | Transforming Northstar from the director's seat and then the CTO's |

**Projects:** [Project 8](projects/p8-cto-technology-investment-proposal.md), Build a CTO Technology
Investment Proposal (about 28 to 35 hours; its prerequisites, Chapters 30, 38, 45, 46, 48, 49, and 52,
are in Paths B to E), then the capstone. The capstone is the largest piece of work in the book: ten
stages that reuse the outputs of earlier projects. Chapter 60 sets out its stages and their order.
**Schedule:** about 5 weeks of reading and about 8 for Project 8, then the capstone.

## Path F: CTO reference

**For:** experienced CTOs and VPs who want a specific framework, not a course.
**Before you start:** the Northstar overview and the quarter 4 briefing (25 minutes), so the cases make sense out of order.

Read non-linearly. Start from the problem:

| If you need to… | Go to |
|---|---|
| Diagnose and reverse declining quality | Chapter 27, then 56 |
| Recover an organization in serious trouble | Chapter 56 |
| Build a scorecard that will not be gamed | Chapters 18 and 38, then 27 |
| Decide on a reorganization | Chapters 35 and 36 (33 and 34 for the method) |
| Decide whether you need a VP of Engineering | Chapter 47 |
| Plan capacity and the workforce for next year | Chapter 48 |
| Make the case for an investment to finance | Chapters 45 and 52 |
| Write a technology strategy | Chapters 30 and 51 |
| Set how architecture decisions are made and reviewed | Chapter 28 |
| Define what staff and principal engineers are for | Chapter 29 |
| Build your leadership bench and succession | Chapters 41 and 36 |
| Set risk, security, and compliance strategy | Chapters 53 and 26 |
| Decide what to do about data and AI | Chapter 54 |
| Prepare for a board or due diligence | Chapter 55 |
| Handle a crisis or a disagreement among executives | Chapter 57 |
| Plan a reduction or integrate an acquisition | Chapter 58 |
| Fix a management system that has grown bureaucratic | Chapters 37 and 59 |

The [template library](templates/index.md) is designed for this path.

## Path G: Tech lead and staff-plus engineer

**For:** tech leads, staff, and principal engineers who lead through technical authority rather than
management, and senior engineers deciding between the two tracks.
**Prerequisites:** none beyond engineering experience.
**Before you start:** the Northstar overview (15 minutes).
**Focus:** leverage, decisions, architecture governance, technical strategy, and influence without authority.

| Order | Chapters | Why in this order |
|---|---|---|
| 1 | 1, 3, 4 (the job, leverage, the leadership ladder) | What leadership asks of you, on either track |
| 2 | 13, 28 (team decisions, architecture decisions) | How technical decisions get made and recorded |
| 3 | 29 (staff and principal engineers) | The role itself: archetypes, mandates, and how it fails |
| 4 | 30, 31, 32 (technical strategy, service boundaries, platforms) | The technical direction staff engineers are asked to set |
| 5 | 20, 21 (engineering standards, technical debt) | Standards and debt, which staff engineers usually own |
| 6 | 46 (stakeholders and negotiation) | Influence without authority |

**Practice:** no project is written from a staff engineer's seat, so this path ends with a practice set
on your own system (about 8 hours): write one decision with the
[architecture decision record](templates/architecture-decision-record.md) template, draft one page with
the [engineering strategy](templates/engineering-strategy.md) template, and do the Executive
Decision-Making exercises of Chapters 28 and 29.
**Schedule:** about 12 weeks of reading, about 14 with the practice set.

## Path H: Quality transformation

**For:** leaders responsible for improving quality, reliability, or delivery in an organization that is struggling.
**Prerequisites:** none beyond engineering experience.
**Before you start:** the Northstar overview and the [baseline data](case-studies/northstar/baseline-data.md) (30 minutes).
**Focus:** testing, technical debt, reliability, CI/CD, ownership, metrics, and quality governance.

| Order | Chapters | Why in this order |
|---|---|---|
| 1 | 27 (quality transformation) | The whole transformation first, so that the parts have a place |
| 2 | 19, 18 (defining quality, measuring productivity) | What quality means and how to measure it without being fooled |
| 3 | 21, 22, 23 (technical debt, testing, code review and CI/CD) | Debt, testing, and the delivery pipeline |
| 4 | 24, 25, 26 (reliability, incidents, security) | Reliability, incidents, and security |
| 5 | 20, 31, 32 (standards, service boundaries, platforms) | Standards, ownership boundaries, platforms |
| 6 | 38, 56 (scorecards and capacity, recovering a failing organization) | Funding the work, and recovering an organization in serious trouble |

**Projects:** [Project 3](projects/p3-quality-transformation-plan.md), quality transformation plan (about
25 to 32 hours), and [Project 5](projects/p5-delivery-and-reliability-scorecard.md), delivery and
reliability scorecard (about 22 to 28 hours). Their prerequisite chapters are all in this path.
**Schedule:** about 14 weeks of reading, plus six to eight weeks per project.
