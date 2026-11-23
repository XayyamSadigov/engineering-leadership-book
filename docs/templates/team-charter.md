# Team charter and working agreement

**Used in:** [Chapter 12](../parts/03-high-performing-teams/12-team-charters-working-agreements-and-knowledge-sharing.md)
(team charters, working agreements, and knowledge sharing), [Chapter 13](../parts/03-high-performing-teams/13-decision-making-in-teams.md)
(decision methods), [Chapter 33](../parts/07-organization-design/33-conways-law-team-topologies-and-cognitive-load.md)
(team types and interaction modes).
**Owner:** the team writes and owns both documents, the manager included; the manager takes disputed
boundaries to the director with a proposal.
**Cadence:** written in two sessions when a team forms or its scope changes; working agreements reviewed
at a fixed retrospective each quarter; the charter checked each quarter against the requests the team
actually received.

A [team charter](../glossary.md#team-charter-and-working-agreement) is one page that answers four
questions: why the team exists, what it owns and does not own, how other teams work with it, and which
decisions it makes alone, shares, or escalates ([decision rights](../glossary.md#decision-rights)). A
working agreement is a short list of specific, observable commitments team members make to each other
and enforce on each other, including on the manager. Use them to make boundaries, interfaces, and habits
visible, so that a request that bypasses the interface, or a lapse in an agreement, is visibly an
exception.

!!! tip "Minimum version"
    In the first session, write the mission, the "owns" and "does not own" lists, and how other teams send
    requests. Add decision rights and three working agreements in the second session, and the quarterly
    check once a quarter of requests has arrived.

## How to fill it in

1. **Sample last quarter's work**: what the team did, where requests came from, what it refused. Draft
   from that, not from the team you wish you had.
2. **Write the mission** in one sentence about who gets what from the team.
3. **List what the team owns, what it does not own although people assume it does, and what is
   disputed.** Writing "disputed" turns a silent conflict into an item someone above the team can decide.
4. **Write the interfaces**: where requests go, the response time, what is self-service, what the team
   needs from others, and whom it notifies of changes.
5. **List the recurring decisions** (schema changes to owned data, accepting work from another team,
   breaking an interface), with who decides and who is consulted. A decision not on the list goes to the
   manager, who adds it.
6. **Agree five to seven working agreements** from problems the team has actually had. Each must be
   observable, proposed and agreed by the team, and reviewed at a named retrospective.
7. **Show the charter to the neighbors** named in the interfaces, and send disputes to the director with
   a proposal.

## Template

**Team charter (one page)**

| Section | Contents |
|---|---|
| Mission | One sentence: who gets what from this team |
| Owns | Components, services, and data |
| Does not own | What people assume the team owns but it does not, and who does |
| Disputed | Unsettled boundaries, with the proposal sent to the director |
| Interfaces | Request channel, response time, self-service, notifications, what the team needs from others |
| Decision rights | Recurring decisions: who decides, who is consulted, who is informed |

**Working agreements**

| Agreement | Problem it answers | How a lapse is noticed | Review date |
|---|---|---|---|

```yaml
charter:
  team: ""
  manager: ""
  mission: ""
  owns: []
  does_not_own: []             # {item, owner}
  disputed: []                 # {item, proposal, sent_to, date}
  interfaces:
    requests: ""               # channel and triage days
    first_response: ""
    self_service: []
    notifications: []          # {change, notify, notice}
  decision_rights:
    - {decision: "", decides: "", consulted: [], informed: []}
working_agreements:
  - {agreement: "", problem: "", lapse_signal: "", review: ""}
reviewed: ""
```

## Example: Northstar, Data and Analytics (start of quarter 2)

!!! info "Northstar so far"
    Week 14 of the Engineering Director's first year at Northstar Technologies, a fictional company. Data
    and Analytics, eleven engineers under
    Farah Haddad, has the lowest change failure rate in the organization and little contact with other
    teams. See the [timeline](../case-studies/northstar/timeline.md). New to Northstar? Read
    [the year in brief](../case-studies/northstar/year-in-brief.md) and the
    [cast](../case-studies/northstar/cast.md).

Two facts showed the team needed a charter. Requests from other teams took half its unplanned work. And
its two incidents had boundary causes: INC-408, a month-end report that timed out at new data volume and
was reported by a customer after eight hours, and INC-423, a warehouse maintenance window that overlapped
scheduled customer exports. Reviewing INC-423, the team found nobody had written down who announces
warehouse maintenance or who must be told. Farah drafted the charter with the team over two sessions.

| Section | Draft |
|---|---|
| Mission | Customers and Northstar staff get correct, timely reporting and exports from the order and billing data |
| Owns | reporting-api, export-svc, warehouse pipelines |
| Does not own | Source data correctness in Core (Orders and Billing own it); the export deploy script (Platform Operations, until retired) |
| Disputed | search-svc: nominal owner Orders, written mostly by engineers now in this team; proposal to the director |
| Interfaces | Requests through one queue, triaged Tuesday and Thursday; first response within two working days. Warehouse maintenance windows announced to Payments and Integrations and Customer Experience five working days ahead |
| Decision rights | Warehouse schema: team decides, Li Na Zhou (staff engineer, data and integration) consulted. Accepting work over a week from another team: Farah. Breaking a reporting-api contract: director informed, consumers consulted |

The team agreed six working agreements. Two show its shape, with members in Minneapolis (four), Bogotá
(five), and remote (two):

| Agreement | Problem it answers (this template's reading) |
|---|---|
| Decisions made in a call are written in the team channel the same day | Members in three locations miss decisions taken in a room |
| A warehouse change touching customer exports gets a second reviewer from a different location | INC-423 reached customers without anyone outside the change noticing |

What to notice: the boundary rows did the most work. "Disputed: search-svc" and "Does not own: the
export deploy script" each turned a silent problem into a decision for the director.

## Common mistakes

- **Writing the charter for the team you wish you had.** Start from a sample of real requests.
- **Skipping "does not own" and "disputed".** They are the most useful rows and the most often left out.
- **Agreements that cannot be observed.** "We respect each other's time" cannot be broken or kept;
  "agenda posted a day ahead, or the meeting is cancelled" can.
- **Agreements imposed by the manager.** They are then enforced only downward and become management
  rules in disguise.
- **Never reviewing.** An agreement nobody revisits is a poster on a wall.
- **A charter the neighbors have not seen.** The interface section binds other teams only if they agreed
  to it.

## Review questions

1. Which requests last quarter came through a channel the charter does not name?
2. Which "disputed" item has waited longest for a decision, and who holds it?
3. When did someone last tell the manager that the manager broke an agreement, and what happened?
4. Which working agreement has not been discussed at a retrospective this quarter?
5. Which recurring decision is missing from the decision-rights list?

## Evidence and references

The method is [Chapter 12](../parts/03-high-performing-teams/12-team-charters-working-agreements-and-knowledge-sharing.md).

- [Mathieu and Rapp, 2009](../references/bibliography.md#mathieu2009charters): in 32 student teams in a
  business simulation, the abstract reports that teams high on both charter quality and performance
  strategy sustained the best performance (**research finding**, narrow setting). Charters help alongside
  a good plan, not instead of one.
- [Skelton and Pais, 2019](../references/bibliography.md#skelton2019team): known for the idea of a
  deliberate "team API" and a chosen interaction mode with each neighbor (**expert opinion**).
- [Edmondson, 1999](../references/bibliography.md#edmondson1999psychological): the abstract links team
  psychological safety to team learning in a field study of 51 teams (**research finding**). Peer
  enforcement of agreements works only where raising a lapse is safe.

The one-page structure, the three properties of a working agreement, and the quarterly review are
**this book's recommendation**.
