# Chapter 14 solutions — Distributed Teams, Team Health, and Diagnosing Dysfunction

Worked solutions for the [chapter 14 exercises](../parts/03-high-performing-teams/14-distributed-teams-team-health-and-dysfunction.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Two studies, two headlines

**What each measured.** Gibbs, Mengel, and Siemroth used personnel and analytics data on more than
10,000 professionals at one IT services firm, before and during pandemic work from home. Hours rose,
output did not, so measured productivity fell; coordination time grew while uninterrupted work,
coaching, and supervisor one-on-ones fell. Bloom, Han, and Liang ran a randomized trial of two home days a
week with 1,612 employees of one technology company: quits fell by about a third, with no effect on
performance grades, promotions, or engineers' lines of code.

**Why both headlines overreach.** The first study measures a forced, sudden, fully remote change during
school closures, not a chosen policy. The second measures hybrid, not full remote, and uses coarse
performance measures. Neither says that five office days beat two, because neither tested that
comparison. Each is one firm.

**What neither tells this company:** how its own work depends on unplanned communication, how many newer
engineers it has, or what attrition a mandate would cause in its labor market.

A good answer reads the setting and design before the finding, and ends with what the company would have
to observe for itself. The weak answer picks the study that agrees with the reader's prior, or averages
the two into "it depends" without saying on what.

## F2 — Compensations for a split team of eight

**Channels taxed.** With an hour's time difference, overlap is not the issue; location is. The taxed
channels are decisions (made in whichever office the lead sits), unplanned context (the three-person
office hears late), feedback (the new remote engineer is the most exposed), trust (two offices that rarely
meet), and meetings (room versus screen).

**One compensation each.** Decisions: the lead writes boundary-crossing decisions in the team's decision
log before they take effect (owner: lead; cost: about an hour a week). Unplanned context: one engineer
in each office is the named bridge for the other, rotating quarterly (cost: some focus time). Feedback:
the new remote engineer pairs with a named mentor three half-days a week for the next quarter and gets
reviews within one working day (owner: mentor; cost: perhaps 15 percent of the mentor's time, which is the
transfer Emanuel et al. describe). Trust: the whole team meets in person for quarterly planning (owner:
manager; cost: travel for four people or three, depending on venue). Meetings: one remote means everyone
on their own screen (owner: whoever chairs).

A good answer names an owner and a cost for each, and prioritizes the new remote engineer. The weak
answer lists tools (a chat channel, a video product) without saying which channel each repairs.

## F3 — The traffic-light table

**Prediction.** In the first quarter, teams answer as before and the table shows real variation, some red.
The review discusses the red teams. Their managers feel judged in front of peers, and some ask their teams
to "be fair" next time. In the second quarter, red shrinks across the board while incidents, attrition,
and transfer requests do not move. This is the gaming branch of the chapter's loop, and the pattern
Kniberg and Lindwall warn about and Orosz and Beck describe for survey scores tied to reviews. The table
now shows which managers are most anxious, not which teams need help.

**A design that still finds teams.** Teams keep their results. Each manager brings two lines to the review:
the patterns the team chose to share, and one request for help. The manager of managers looks across
requests for shared problems (several teams naming release pain points to a platform fix), and looks at
system signals the teams did not author: incident load, attrition, transfer requests, skip-level themes.
When those signals and a team's request point the same way, that team gets attention. No color for any
team appears in the deck.

A good answer predicts the mechanism, not only the outcome, and keeps a way to find struggling teams.
The weak answer bans the table and offers nothing in its place, leaving the manager's legitimate need
unmet.

## A1 — Facilitating the Customer Experience health check

**Who and how.** Two sessions, not one: web with the two quality engineers in Minneapolis (remote
engineers on their own screens, so the session runs screen-first), and mobile, which Elena runs
in Bogotá in person if travel allows, otherwise with everyone on video including her. Separate sessions
because the signals (6 of 8 retrospective actions about web, a quiet mobile group) say a joint session
would reproduce the problem being measured.

**Format.** Ten indicators with good and bad examples, silent individual votes first (cards or a
simultaneous reveal on video) so the first speaker does not set the color, then discussion of the reds
and yellows only. Each session ends with at most two actions and a request for help.

**What leaves the room.** Agreed before the session: patterns and requests, not ratings. Because a
structural decision may depend on the results, Elena asks both groups whether they will share their
ratings with the director this once, and accepts no as an answer.

**What she says to Daniel.** That he is not attending, and why: his presence would change what mobile says,
not because he is the problem but because he is the manager. He will get the requests, and she will help
him hear them without defending.

A good answer separates the subgroups, protects candor in the format, and agrees the data rule in advance.
The weak answer lets Daniel attend "to show support", or runs one joint video session.

## A2 — Is distance costing Data and Analytics anything?

**The manager's claim is about the wrong boundary.** The team's internal delivery can be fine while its
links to the rest of the organization are weak; that is exactly the pattern Yang et al. found at scale
(siloed networks, fewer bridges). The baseline already says the team has little contact with others.

**Evidence to look for.** Requests from other teams take 12 points of Data's capacity, more than any
team except Platform Operations: do those requests wait, and are they answered by the same
Minneapolis people? Did search-svc's disputed ownership (its authors moved to Data and Analytics) leave a
gap no one bridged? How long do cross-team items involving Data take compared with the organization's
medians for one dependency (24 days)? Do Bogotá engineers attend other teams' demos or design reviews?
Which Data engineers are named in other teams' incident reviews or dependency links?

**What to change if the cost shows.** Name a bridge for each team that sends Data most of its requests, make demos and design reviews open to both sites, and put one Bogotá engineer in each
cross-team working group. Do not move people or change the team's arrangement on this evidence alone.

A good answer looks at cross-team signals, not the team's own metrics. The weak answer either accepts the
manager's claim or prescribes travel without evidence of a cost.

## A3 — Diagnosing the team that "needs to gel"

**By layer.** *Structure:* check first. Is the team's goal shared, or are there two workstreams
pretending to be one? Repeated identical retrospective actions often mean the cause is outside the team's
control (a dependency, a boundary), so the team keeps naming it and cannot fix it. *Leadership:* decisions
reopened after planning suggest nobody closes decisions; "just needs to gel" suggests the manager sees a
relationship problem and is waiting for it to resolve itself. *Relationships:* two seniors communicating
through review comments is a conflict avoided in the open and fought in the code, which fits Lencioni's
idea that missing trust shows up as artificial harmony and later as weak commitment. *Individuals:* no
evidence yet that one person drives the pattern.

**Remedy.** If structure checks out, coach: the manager closes decisions explicitly with a written record,
the seniors get a facilitated conversation about the disagreement they are having in review, and the
retrospective's repeated actions get an owner outside the team if they need one. Set a recheck in a
quarter.

**What would change the choice.** If the three repeated actions turn out to be about a dependency the team
cannot influence, restructure the boundary or escalate the dependency first. If the manager declines to
close decisions after clear expectations, consider leadership.

A good answer checks structure before relationships and names evidence that would change its mind. The
weak answer goes straight to a team-building event.

## X1 — Four office days and the Bogotá question

**What the evidence supports.** The only randomized trial found two home days cost nothing measurable in
performance and cut quits by about a third. Firm-wide remote work weakens cross-group ties, but Northstar is
already hybrid with anchor days. Proximity helps newer engineers most. No study shows four office days
outperform three.

**Options and costs.** *Four days at headquarters:* risk to retention among the 52 Minneapolis engineers;
at about $76,000 per departure (the chapter's assumption), five extra departures cost about $380,000, under
flat headcount and with 15-week median backfills. It does nothing for Bogotá or the 12 remote engineers,
where the collaboration gaps actually are. *Closing Bogotá:* 16 engineers in Payments and Integrations,
Customer Experience, and Data and Analytics; replacing them in Minneapolis takes quarters, during the renewal
commitments, and loses the mobile team entirely. *Keeping Bogotá and investing in the boundary:* about
$114,000 a year of travel plus the chapter's compensations, with Rajiv Menon's flat-opex constraint
requiring an offset.

**Recommendation.** Keep three anchor days; keep Bogotá; fund the travel as a stated bet with a break-even
of about one and a half avoided departures; target the specific collaboration gaps (Customer Experience's
board, cross-site bridges). Tell Helena Marsh what would change the recommendation: rising cross-site
incidents or slower cross-team lead time despite the investment.

A good answer quantifies with stated assumptions and separates headquarters from Bogotá. The weak answer
argues from personal preference or quotes one study.

## X2 — Customer Experience at the end of quarter 3

**Read the evidence.** One fewer red area is weak improvement, within the noise of a self-assessment.
One mobile Sev2 is no better than the baseline. The split board and cadence were done, so the structural
change happened; what did not happen fully is Daniel's part, one visit of two. Mateo's request is a signal
that mobile wants local leadership, and possibly that the informal lead role has outgrown being informal.

**Decision.** Not leadership change: Daniel met most expectations, and the evidence does not show he cannot
lead across sites, only that he did half of one commitment. Ask him why, and hold him to the second visit.
Coach further for one quarter, but start the work on option C now, because a 17-person team with two
products and two sites is large for one manager and the structural answer may be two teams. A mobile
manager role means a manager position under flat headcount. The constraint counts the whole
engineering organization of 87, so an engineer can become a manager only if that engineering seat is
not backfilled: Customer Experience would lose an engineer's capacity. That trade is a decision for the
CTO, not the director alone.

**Answer to Mateo.** Thank him, take the request seriously, and make no promise: describe the role, the
headcount question, and the selection process that any opening would need (others may apply). Offer him
management-adjacent work now, such as running mobile's planning and one-on-one mentoring of a newer
engineer, with feedback, so either outcome builds on something real.

A good answer weighs each signal honestly, separates the team decision from Mateo's career, and avoids
promising a role that does not exist. The weak answer either rewards Mateo's request with an immediate
promotion or replaces Daniel on thin evidence.
