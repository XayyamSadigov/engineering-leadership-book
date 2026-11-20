# Chapter 30 solutions — Technical Strategy, Technology Selection, and Build versus Buy

Worked solutions for the [chapter 30 exercises](../parts/06-technical-leadership/30-technical-strategy-and-technology-selection.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Diagnosing a vision statement

**What is missing.** The draft has goals ("modern, cloud-native", "faster delivery and fewer
incidents") and favored techniques (microservices, observability), but no diagnosis of what makes
Northstar's situation hard, no policy that rules anything out, and no action with an owner or date. It
is the "goals as strategy" failure: nobody would object to it, which is the sign that it decides
nothing. "Embrace microservices" is a technique chosen before the problem is named, and it may even
conflict with the evidence (Chapter 31 treats that debate).

**A rewritten diagnosis.** "Northstar's technical problem is not the age of Core but that change is
unsafe and knowledge is concentrated. Nineteen of last quarter's 30 Sev1 and Sev2 incidents (63
percent) were triggered by our own changes, nine of them through the Core release train. We build and
deploy in four different ways, and three services are deployed by scripts one person understands.
Eight of 24 components have disputed, shared, or no ownership, and our oldest critical vulnerability
had been open for 19 months because nobody watched dependency versions."

**Criteria.** Each sentence carries a number from the baseline; the diagnosis names causes, not
symptoms; someone could disagree with it. **Weak answer:** a longer list of aspirations, or a diagnosis
that blames "legacy" without evidence.

## F2 — Recomputing and extending the TCO

**Three years, as in the case study.** A: $96,000 + 3 × $92,500 = $373,500. B: $64,000 + 3 × ($150,000
+ $27,750) = $597,250. C: $56,000 + 3 × ($45,000 + $46,250) = $329,750.

**With the new assumptions** (subscriptions up 5 percent a year; A's in-house time 0.6 FTE, $111,000,
from year 3):

| Option | Three years | Five years |
|---|---|---|
| A | $96,000 + 2 × $92,500 + $111,000 = $392,000 | $96,000 + 2 × $92,500 + 3 × $111,000 = $614,000 |
| B | $64,000 + $472,875 subscription + $83,250 = $620,125 | $64,000 + $828,845 + $138,750 ≈ $1,031,600 |
| C | $56,000 + $141,863 + $138,750 ≈ $336,600 | $56,000 + $248,653 + $231,250 ≈ $535,900 |

Subscriptions: B pays $150,000, $157,500, $165,375, $173,644, $182,326; C pays $45,000, $47,250,
$49,613, $52,093, $54,698.

**Ranking.** C is cheapest at both horizons, then A, then B. The ranking is most sensitive to the
in-house operating time, not the subscription increase: if C needed 0.35 FTE instead of 0.25, it would
cost about $628,400 over five years and fall behind A. A strong answer says the operating estimate
deserves the most scrutiny and should be checked against the 0.6 FTE the work takes today. **Weak
answer:** recomputing correctly but not saying which assumption matters.

## F3 — Making the register rankable

Seven items scored 6 cannot be ordered by score, so the review drifts to whoever argues hardest.

**One workable change:** keep the scores, and add two fields used for ordering: the **horizon** (date
or "unknown") and the **cost to reduce exposure by one step** in engineer-days. Order by horizon first
(items whose trigger is closer than the migration time go to the top), then by exposure reduced per
engineer-day. With 20 engineer-days to spend, TR-02's mitigation (about 20 days, score 9) and a second
responder for TR-07 (pairing, a few days a month) beat starting TR-01, whose 120 to 180 days cannot be
finished with 20.

**Alternatives** that are also defensible: a five-point impact scale tied to tier and financial
correctness, or an expected-loss estimate for items with incident history (for example, INC-414's
restoration time and Billing's credit exposure).

**How it is gamed.** Owners inflate the "cost to reduce" to avoid work, or shorten horizons to win
capacity. Countermeasures: horizons must cite a published date or an incident, and a staff engineer
challenges estimates in the monthly review. **Weak answer:** a finer scale with no change in how the
review decides.

## A1 — The graph database proposal

**What to say.** Thank the engineer for the prototype and apply policy 1: a new datastore on a
production path needs a written reason why the existing relational store cannot do the job, an owner,
and a plan to retire something. A faster prototype is evidence about one query on one dataset, not about
operating the database at 3 a.m. (McKinley's point about known failure modes).

**Ring.** Assess, not Trial. Mobile recommendations are not tier 1, so the risk is moderate, but nothing
yet shows that the existing store has failed.

**To move to Trial,** the team should show: the production query and data volume where the relational
store misses a stated latency target after reasonable tuning (indexes, a precomputed table, a cache);
who on Customer Experience would be on call for the new store, with a second person; how it is backed
up, monitored, and upgraded, and by whom (Platform Operations is already the busiest interrupt queue);
a time box and success criteria; and what happens if the trial fails.

**Criteria.** The answer neither bans the idea nor approves it on enthusiasm, and puts the operational
cost in front of the team. **Weak answer:** "we only use the approved stack", which teaches engineers
to stop proposing.

## A2 — Decision record for tax-svc

One defensible answer is **option C, the hybrid**, with B kept as a documented alternative.

**Policy applied.** Policy 2: rate content changes for reasons outside Northstar, so buy it; the
calculation and its link to invoicing stay in-house, where Billing already owns correctness.

**Exit path.** Rate data enters through an import interface tax-svc owns, in a format the team defines.
Switching content vendors means writing a new importer, estimated at a few weeks.

**Fallback on the order path.** C adds no external call at order time: rates are imported and cached in
tax-svc, which also avoids B's latency and availability exposure.

**Ownership.** Marcus Oyelaran owns the vendor relationship; a named engineer plus a second person own
the importer, which removes the one-person rate research (TR-09).

**Timing.** Start after Billing's reserved weeks 1 to 3 for the ledger export; 70 engineer-days over the
rest of the quarter is about one engineer full time, which must come from Billing's prevention share.

**Reversal evidence.** After two quarters: any tax incident traced to content; import failures needing
manual repair more than monthly; or operating time well above 0.25 FTE. Any of these reopens B.

**Criteria and weak answer.** B is also defensible if the team argues that calculation rules (exemptions,
product taxability) are the real risk, not rates. The weak answer chooses on price alone.

## A3 — Keeping TR-02 on the register

**TR-02 stays.** The consolidation decision has not been made, and if it is made it will take quarters
to finish. Meanwhile the controller is a single point of failure for Core and four services, it already
failed once for reasons nobody determined (INC-428), and its expertise is concentrated in Bram
Verhoeven, who spends 45 percent of his time on its interrupts. A future decision does not reduce
today's exposure.

**Fund now (about 20 engineer-days):** controller configuration and job definitions in version control
so the controller can be rebuilt; a tested backup and restore; plugin inventory with versions; and a
second infrastructure engineer paired with Bram on incidents until they can respond alone. These are
useful whatever the consolidation decision is, because they also make migration easier.

**Keeping the register honest.** Record on TR-02 that the long-term response depends on the
consolidation decision, with that decision's owner and date. If the date slips, the register shows it.
The register is where exposure is visible; it is not where the consolidation is decided.

**Criteria.** The answer separates short-term exposure from long-term choice and funds only "no-regret"
work. **Weak answer:** removing TR-02, or using the register to force consolidation without the
decision process Chapters 23 and 27 describe.

## X1 — Framework migration or extended support

**Recommendation (one defensible course).** Buy one year of extended commercial support only if the
horizon requires it, and start the migration in quarter 3 with a scoped first step, not the full job.

**Reasoning.** Extended support at $60,000 a year buys time, not an exit: after two years Northstar has
paid $120,000, roughly the midpoint migration cost of $96,000 to $144,000, and still has to migrate. The
migration is not a rewrite (constraint 3 is about Core's design, not its framework version), but it
touches every module and competes with Ines Carvalho's permissions extraction. So: in quarter 3,
another senior Core engineer leads a dependency inventory and upgrades the modules with owners first
(order-capture, invoicing, ledger), with Ines as reviewer rather than lead. Quarters 4 and 5 finish the
shared modules after the permissions extraction lands.

**Trigger to change course.** A new critical in the old framework that cannot be patched or mitigated
within the 30-day service level, or slippage of the inventory beyond quarter 3, makes extended support
mandatory immediately.

**Criteria.** The answer compares both options over the same horizon, protects Ines from becoming the
bottleneck, and names the trigger. **Weak answer:** "support is cheaper per year", ignoring that it is
paid every year and does not remove the migration.

## X2 — The three-year discount

**Decision (one defensible answer):** decline the three-year commitment this quarter; if B is chosen
at all, sign a one-year contract with renewal price caps, and revisit a multi-year term once the
integration has run for two quarters.

**Arithmetic.** At 30 percent off, the subscription is $105,000 a year, $315,000 committed over three
years, against $150,000 a year undiscounted. The saving is real ($135,000 over three years) but only if
B is the right option. The committed sum exceeds the $250,000 discretionary tooling budget, so it needs
Rajiv Menon's approval on a business case regardless.

**Contract terms** if signing: an availability commitment at least as strict as Northstar's 99.9
percent with credits that pass through; data export in a documented format; exit assistance and a
termination right if service levels are missed; capped renewal increases.

**Technical safeguards:** tax-svc as the interface the vendor sits behind; cached rates as a fallback so
an outage degrades to last-known rates rather than failed orders (Elena Sokolova's concern after INC-413
and INC-425); the import path from option C kept as an exit.

**Approval route:** the director's recommendation with three-year TCO, the CFO for the commitment, and
the vendor recorded in the risk register as a concentration item. **Weak answer:** accepting because
the discount is large, or refusing on principle without a cost comparison.
