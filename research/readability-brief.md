# Readability brief (the 4.5 program)

Goal: every scale in `research/readability-assessment.md` (readability, clarity, completeness, Northstar
load) at a book average of at least 4.5, and no chapter below 4, measured by re-running the same rubric
(`research/readability/rubric.md`). This brief is binding for every agent in the program, together with
`CLAUDE.md`. Read both in full, then the assessor report for your scope in `research/readability/`.

## Non-negotiables

- **Facts do not change.** No Northstar or Halvard number, name, week, or outcome changes, and no new
  canon facts, except where your lane explicitly allows it. Restructuring and rewording only.
- **Evidence strength does not increase.** When you remove an access note ("abstract read", "idea level",
  "full text could not be fetched"), the claim must stay at the strength the source supports: a
  `metadata-only` source still gets no finding, number, or quotation. Keep the evidence label words from
  `docs/references/evidence-labels.md` (research finding, practitioner consensus, expert opinion, this
  book's recommendation, illustrative, and so on). Never add a source you have not verified in-session.
- **The chapter contract stays** (CLAUDE.md section 4): same 16 H2 sections in order, exercises with no
  answers, at least 2,500 words, two Mermaid diagrams, no section under 60 words.
- Only edit the files your lane names. Validate with `.venv/bin/python tools/validate_book.py` and fix
  every error you cause (ignore the stale single-file edition and stale generated pages). Do not commit.

## Reader rules (apply in every chapter, solution, template, and project)

1. **No maintainer bookkeeping in reader text.** Remove or rewrite: the word "canon" (say "the case",
   "Northstar's record", or nothing); internal codes ("disputed claim D3", "gap G8"; say "the evidence is
   contested" or "the evidence is thin" and, if useful, link `../../references/...` pages only if they are
   reader pages); access notes (fold the limit into the evidence label: "Larson argues", "a survey
   suggests", "the abstract reports"); "this fact was added for this chapter"; notes on which chapter
   "owns" a fact. Statements that a quarter 4 decision is open stay, phrased for the reader ("the CTO has
   not decided yet").
2. **Define at first use, per chapter.** Each acronym or specialist term is expanded or defined the first
   time it appears in a chapter (a short clause is enough) and linked once to the glossary:
   `[tier 1](../../glossary.md#tier-1)`. The glossary is `docs/glossary.md`.
3. **Roles at first mention, per chapter.** Each person's first mention in a chapter carries the role:
   "Rajiv Menon (CFO)". The cast page is `docs/case-studies/northstar/cast.md`.
4. **Incident IDs never stand alone.** Each INC-number carries a few words of what happened the first time
   it appears in a chapter ("INC-412, the payments outage after a schema change").
5. **"Northstar so far" box.** The first Northstar passage of each chapter (usually the Engineering
   Organization Example or the Case Study) opens with an admonition of two to four lines that tells a
   reader who skipped earlier chapters where the story stands at that week, and links the timeline:

   ```
   !!! info "Northstar so far"
       Week 30 of the director's first year. Sev1 and Sev2 incidents fell from 30 to 17 a quarter after a
       first quarter of ownership and release changes; prevention takes 8 of 80 engineers. See the
       [timeline](../../case-studies/northstar/timeline.md).
   ```

   Facts in the box must come from the case pages, and must be ones available at that week.
6. **Point first, then evidence.** State the claim in the first sentence of a paragraph; follow with the
   evidence. Collapse research tours (three or more studies in a row) into one sentence plus a reference.
7. **Sentences.** Aim for an average under 20 words; split any sentence over 40 words.
8. **Arithmetic.** Move "Check:" sums and multi-step arithmetic out of prose into a small table, a
   footnote-style line under a table, or the solutions file. Keep one headline number per point.
9. **Every exercise solvable from its chapter**, plus the Northstar overview, cast, timeline, and quarter 4
   briefing pages. If an exercise needs a fact the chapter lacks, add the fact to the chapter or to the
   exercise's setup.
10. **Consistent terms.** Use the glossary's term and unit. Capacity is in FTE (full-time equivalent
    engineers) or engineer-weeks; say which, and convert once when a chapter mixes them.

## Length targets (counted by the validator)

Chapters 1–49: keep within about 5,500. Chapters 50–60: the cuts the assessors specify in
`research/readability/a7-ch50-55.md` and `a8-ch56-60.md`, target at most about 6,500 (Chapter 52 and the
capstone may stay near 7,000 if the extra words are definitions or instructions). New content in phase 4
is written as compact sections; it must not push a chapter back over these limits.

## Phase 4: missing content

Write each addition as a compact subsection (`###`) inside the most fitting H2 of the named chapter,
usually Deep Conceptual Explanation, Practical Playbook, or Enterprise Application. Point first, one
worked example or sample where it helps, no research tours. Pay for the words with cuts elsewhere in the
same chapter so the length targets above still hold (chapters 1–49 at most about 5,500 counted words;
50–60 at most about 6,800). New sources are allowed only if verified in-session (CLAUDE.md section 5);
put them in `research/pending-sources/phase4-<scope>.yaml` with the bibliography schema, never edit
`bibliography.yaml`. No new Northstar or Halvard facts unless an item says so; samples and dialogues may
use clearly hypothetical people ("an engineer on your team"). Add an exercise only if the addition is a
skill the reader should practice, and give it a solution.

| Scope | Additions (size in words, roughly) |
|---|---|
| Ch 1–10 | Ch 2: managing former peers (300); managing up as a new manager (400); the new manager's own load and sustainability (300). Ch 4: a method for diagnosing the level someone actually works at (350). Ch 6: a short sample difficult conversation, annotated (400). Ch 7: the hiring funnel beyond the loop (sourcing, closing, interviewer load) and onboarding the first 90 days (500); inclusive hiring practices (300); candidates using AI assistants (200). Ch 8: total compensation and choosing a level at offer (400); bias in calibration, compact (250). Ch 9: the regular performance review cycle (500); performance evidence when code is AI-assisted (150). Ch 10: burnout signals and responses (350) |
| Ch 11–18 | Ch 11: inclusion as part of psychological safety, with what a manager does differently (400). Ch 12: knowledge sharing beyond single points of failure (300). Ch 14: asynchronous work and real time-zone spread (400). Ch 15: a worked outcome roadmap example (350) |
| Ch 19–27 | Ch 24: observability in practice (what to instrument, the three signal types, cost) (400). Ch 26: finding security flaws in your own code (threat modeling, SAST and DAST, bug bounty basics) (450). A short "Part V at a glance" paragraph at the start of Ch 19 that tells the reader how the quality chapters fit together and what the case's first quarter does (200) |
| Ch 28–36 | Ch 28: recovering decisions that were never written down (250). Ch 31: splitting a shared database safely (400). Ch 32: sizing and funding a platform team (300). Ch 35: a worked example at about 100 engineers (350). Ch 36: undoing a reorganization that failed (300) |
| Ch 37–43 | Ch 37: a sample forum charter (250). Ch 38: a good OKR with its paired measure, and a bad one (250). Ch 39: a joint escalation write-up template (200) and ethics of executive reporting (pressure to present misleading numbers) (300). Ch 40: the director's own sustainability and peer network (300). Ch 41: moving or removing a manager who is not working out (400) |
| Ch 44–49 | Ch 47: running the director team (rhythm, conflict, decision rights) (450). Ch 49: a sample page one of a multi-year proposal (300) and running the decision meeting (250) |
| Ch 50–60 | Ch 50: a CTO's first 90 days (400) and the executive's own sustainability (200). Ch 54: AI in the product (inference cost, model-provider dependence, regulation, evaluation) (450). Ch 55: ethics at board level (a misleading headline, disclosure) (300). Ch 58: fairness and ethics in selection, compact (200) |
| Templates | Four new templates: hiring scorecard and interview kit (`hiring-scorecard.md`, used in Ch 7), performance improvement plan (`performance-improvement-plan.md`, Ch 9), team charter and working agreement (`team-charter.md`, Ch 12), new manager's 90-day plan (`new-manager-90-day-plan.md`, Ch 2). Same structure as the existing 20 |
