# Human review checklist

Automated validation (`tools/validate_book.py`) proves the book is structurally sound: links
resolve, sections exist, exercises have solutions, citations point at verified bibliography
entries. It cannot prove that a claim is true, that a source says what the chapter says it says,
or that the advice is good. A chapter moves from `draft` to `published` only after a person has
worked through this list and recorded the result in `research/quality-report.md`.

Copy this list into the review record for the chapter.

## 1. Claim accuracy

- [ ] Every sentence that states a finding ("research shows", "teams that X have Y") has a citation.
- [ ] For each cited finding, the reviewer opened the source (or its abstract) and confirmed it
      supports the sentence as written, including direction, population, and strength.
- [ ] No finding is generalized beyond its population (for example, a study of one company's
      engineers presented as true of all engineers).
- [ ] Correlational results are not described as causal.
- [ ] Numbers from sources carry their date and population.
- [ ] Nothing is attributed to a source marked `metadata-only` beyond the idea it is widely known
      for, and nothing from such a source is quoted or given a page number.

## 2. Source verification

- [ ] Every citation resolves to an entry with `verified_fields`.
- [ ] The edition cited matches the claim (for example, second-edition content is not attributed
      to the first edition).
- [ ] URLs in the chapter were opened during review and still work.

## 3. Copyright compliance

- [ ] No passage reproduces or closely paraphrases a source's text. Spot-check the three passages
      most dependent on one source against the source where available.
- [ ] No source diagram, table, framework figure, or exercise is reproduced. Diagrams are original.
- [ ] Short quotations, if any, are exact, attributed, necessary, and under about 50 words.
- [ ] Material from CC BY-NC-ND sources (Google SRE books, *Software Engineering at Google*) is
      cited and summarized, never adapted or copied; the book's CC BY license is incompatible with
      redistributing NC-ND material.

## 4. Treatment of opposing views

- [ ] Where practitioners or researchers disagree, the chapter presents the strongest form of each
      position and the conditions under which each holds.
- [ ] The chapter's own recommendation is labeled as such.
- [ ] No framework is presented as universally correct.

## 5. Practical applicability

- [ ] A practicing manager could act on the playbook on Monday without further research.
- [ ] Every metric recommended comes with a description of how it is gamed or distorted.
- [ ] Every organizational change recommended comes with its transition cost.
- [ ] Every framework presented comes with how it fails.

## 6. Internal consistency

- [ ] Northstar facts match `docs/case-studies/northstar/` exactly (names, team sizes, numbers).
- [ ] Terms are used as defined in the owning chapter; no topic is re-taught that another chapter owns.
- [ ] Cross-references point at the correct chapter numbers.
- [ ] Arithmetic in worked examples is correct (recompute it).

## 7. Illustrative versus factual data

- [ ] Every Northstar number and every worked-example number is visibly fictional or illustrative.
- [ ] No real company appears in an invented story. Real companies appear only in sourced,
      verifiable accounts.
- [ ] No real person is quoted or characterized beyond what a cited source supports.

## 8. Writing quality

- [ ] No motivational filler, no generic "leadership matters" paragraphs.
- [ ] No section restates another section.
- [ ] Exercises demand judgment, not recall.
- [ ] Solutions show reasoning and state the criteria a good answer must meet, not only one answer.
