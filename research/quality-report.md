# Quality report

The state of the book's quality assurance: what automated validation shows, what has and has not been
reviewed by a person, and the known limitations a reader or reviewer should be aware of.

## Automated validation

Run `python tools/validate_book.py --build`. Last result recorded: **passed**, 2026-11-20, with
chapters 1–27 live (chapters, navigation, references, exercises, generated pages,
single-file edition, `mkdocs build --strict`). 1 warning: the one unverified bibliography entry
(`kolny2023primevideo`), which no chapter cites. Mermaid: 75 of 75 diagrams render with mermaid-cli 11.
All diagrams of chapters 1–4 and 15–18 measured in a headless browser at 390 px; one squeezed diagram
(chapter 2) fixed. `ruff check tools`: clean. Browser check of all nine Part V chapters at
390 px: no horizontal page overflow; six squeezed left-to-right diagrams redrawn top-to-bottom, and a
phone-width rule added to `CLAUDE.md` section 8.

## How Part V was produced

Chapters 19–26 were written in parallel by eight AI authors under a shared brief, each confined to its
own files (see `CLAUDE.md` section 6a). Each author verified new sources by fetching pages in session
and validated its chapter. The maintainer merged 64 new sources, consolidated Northstar facts into the
canon (`baseline-data.md` extended baseline, new `first-quarter.md`), and resolved conflicts between
authors. A separate AI reviewer, who had not written any chapter, then read all nine chapters against
the canon and the bibliography and reported 23 findings (2 counting errors, conflicting timelines for
two events, inconsistent tier 1 minimums, repetition between chapter 27 and the newer chapters, one
over-reach beyond a source's recorded claim). All 23 were fixed by four parallel fixers and the
maintainer; chapter 27 was cut from about 7,500 to 5,600 counted words.

## Wave 2 (chapters 1–4 and 15–18), 2026-11-20

Same procedure as wave 1, with a revised brief (stay in your topic lane for invented facts, do not
invent first-quarter events, read sources only from legitimate hosts). Authors coordinated directly on
shared facts (renewal dates, Rafael Duarte, a source sample size of 131 versus 214 firms); the
maintainer fixed the renewal dates as canon (accounting integration week 19, bulk ordering week 26)
and merged 44 sources, one duplicate source consolidated. An independent reviewer reported 20
findings (a numeric inconsistency in Priya Raman's time split, introduced by the maintainer's own canon
merge; a claimed one-on-one arithmetic error that was itself wrong, applied, and reverted after a
wave 3 author caught it (30 minutes every two weeks for 14 people is 3.5 hours a week); staff mandates contradicting chapter 27; two unsupported numbers
attributed to a metadata-only source; repetition of manager-effect studies across chapters 1, 2,
and 4). All 20 fixed.

## Wave 3 (chapters 5–14), 2026-11-20

Ten authors in parallel. New brief rules: each chapter assigned one Northstar team; Chapter 14 alone
decides locations, answering other authors on request. Authors resolved most shared facts directly
(names, Customer Experience leads, review cadence, who the script expert is). The maintainer resolved
a name collision (two authors used the same new name), a departures-by-team conflict, Tomasz
Wierzbicki's level, and the flat-headcount rule for promotions to manager. 63 sources merged (242 in
total), one duplicate consolidated. A wave 3 author caught a wrong arithmetic "fix" from the wave 2
review (one-on-one hours in chapter 2); it was reverted. The wave 3 reviewer reported 16 findings
(Bram Verhoeven's timeline placed in quarter 1, two arithmetic errors verified by the maintainer before
fixing, canon facts not merged, repetition of Edmondson, Lencioni, and Scullen et al.); all fixed.
Chapters 7, 9, and 10 end 3 to 15 words over the 5,000-word guide.

## Human review status

| Item | Status | Self-review | Human review |
|---|---|---|---|
| Chapters 5–14 and solutions | review | Author self-review; independent AI review (16 findings, all fixed) | **Not done** |
| Chapters 1–4 and 15–18 and solutions | review | Author self-review; independent AI review (20 findings, all fixed) | **Not done** |
| Chapters 19–26 and solutions | review | Author self-review against the checklist; independent AI cross-chapter review; fixes applied | **Not done** |
| Chapter 27 and solutions | review | As above; trimmed to remove re-teaching of chapters 18–25 | **Not done** |
| Templates t08, t09, t10, t20 | review | Northstar facts rechecked after canon changes | **Not done** |
| Northstar canon pages and data | canon | Aggregates recomputed from CSV; cross-chapter consistency checked by the reviewer | **Not done** |

| Chapter | Counted words | Diagrams | Distinct sources cited |
|---|---|---|---|
| 19 | 4,934 | 2 | 10 |
| 20 | 4,964 | 3 | 12 |
| 21 | 5,094 | 2 | 10 |
| 22 | 4,999 | 3 | 14 |
| 23 | 4,991 | 4 | 17 |
| 24 | 4,998 | 3 | 16 |
| 25 | 4,978 | 3 | 13 |
| 26 | 4,972 | 3 | 14 |
| 27 | 5,609 | 2 | 10 |

## Priorities for the human reviewer

1. Check a sample of findings against their sources, starting with the newest scholarly entries that
   carry specific numbers: `tornhill2022codered`, `ernst2015measure`, `luo2014flaky`,
   `inozemtseva2014coverage`, `just2014mutants`, `mcintosh2014impact`, `rigby2013convergent`,
   `besker2019productivity`, `mantyla2012who`, `decan2018impact`, `meli2019git`.
2. Re-check date-sensitive pages: DORA metrics guide (five metrics, January 2026), SLSA v1.2, NIST SSDF
   1.2 draft, CISA 2025 SBOM draft.
3. Read chapters 24 and 25 as a practicing engineering leader: they make the most specific operational
   recommendations (burn-rate alert parameters, severity definitions, action triage).
4. `allspaw2012blameless` and `mckinsey2023productivity` were read from Wayback Machine copies; `meyer1977institutionalized` from a
   third-party university copy (claims limited to its abstract). Confirm both are acceptable.
5. Decide whether chapter 21 (5,094) and chapter 27 (5,609) may stay above the 5,000-word guide.

## Known limitations

- Most practitioner books are cited at idea level only; they were verified bibliographically and not
  read for this project. See `research/source-evaluation.md`.
- Most scholarly sources were read at abstract level only.
- One bibliography entry is unverified and uncitable (Prime Video 2023).
- SPACE and DevEx dimension names come from the first author's blog, a GitHub blog, and a vendor page, because the papers' publisher pages returned 403 (gap G5).
- Open research gaps are listed in `research/research-gaps.md` (G1, G3–G20).
- Drafting is AI-assisted throughout. The specific risk is confident prose that a source does not
  support; the citation rules, the independent review, and the human review exist for that reason.
- The GitHub repository named in `mkdocs.yml` does not exist yet; the site's repository widget returns
  404 until it does.
