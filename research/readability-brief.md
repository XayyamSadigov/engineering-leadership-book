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
