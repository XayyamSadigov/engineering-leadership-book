# Source evaluation

How the sources in the bibliography were judged, and what each kind is and is not used for. The
evidence labels a reader sees are defined in `docs/references/evidence-labels.md`; this file records
the reasoning behind them.

## Summary of the bibliography (as of 2026-11-19)

| Evidence class | Entries | Typical access level | Used for |
|---|---|---|---|
| Scholarly | 16 | abstract only | Findings, stated within the population and setting studied |
| Industry research | 4 (DORA guide and 2025 report, *Accelerate*, Google re:Work team effectiveness guide) | full text (guide), summary (report), metadata (book) | Delivery performance definitions and correlations, with survey caveats |
| Standard | 3 (NIST CSF 2.0, NIST SSDF, SLSA) | full text of official pages | Vocabulary and recommended practice, not evidence of effect |
| Official documentation | 1 (AWS Well-Architected) | full text | Vendor framework; recommended practice |
| Practitioner | 49 (the 35 brief books, Google SRE chapters, GitLab handbook, essays) | metadata only for most books; full text for free online chapters | Ideas, mechanisms, vocabulary, documented practice in one organization |

Totals: 73 entries; access level full text 15, abstract only 16, official summary 1, metadata only 41.
The Google SRE chapters are classed as practitioner sources in the YAML and presented to readers as
documented practice.

Three entries have no verified fields and must not be cited until fixed: `allspaw2012blameless`,
`mckinsey2023productivity`, `kolny2023primevideo`.

## Practitioner books

The 35 books in the project brief were verified bibliographically (title, authors, publisher, year,
ISBN) against publisher, author, or catalog pages. They were **not read** for this project, with the
exception of material that is legally free online (the Google SRE books, *Software Engineering at
Google*, and parts of *Staff Engineer* and *The Engineering Executive's Primer*). Consequences:

- Chapters credit a book only for the idea it is widely known for, in the book's own words.
- No quotation, page number, or reported finding is taken from an unread book.
- When a chapter needs more than the headline idea, the free material is read first, or the claim is
  recorded as a gap.

Known metadata issues (recorded in each entry's `access_notes`):

- Unresolved first-publication years: *The Effective Executive* (1966 or 1967), *Turn the Ship
  Around!* (2012 or 2013), *Escaping the Build Trap* (2018 or 2019). The year is excluded from
  `verified_fields` for these.
- Editions with changed authorship or subtitles: *Multipliers*, *The DevOps Handbook*, *Building
  Evolutionary Architectures*, *Inspired*, *Team Topologies*, *Fundamentals of Software Architecture*.
  Chapters cite the edition whose content they rely on.
- Several publisher sites blocked fetching (O'Reilly, HarperCollins, Macmillan, MIT Press, HBR Store,
  Penguin Random House); those entries rest on Open Library records.

## Industry research

DORA is the most important industry source for Parts IV and V. Its strengths: a long-running program,
published definitions, and a method described in *Accelerate*. Its limits, stated wherever it is used:
survey data, self-selected respondents, correlational analysis, vendor sponsorship, and definitions
that change between years (the current guide lists five metrics where *Accelerate* described four).
Chapters cite the guide's current page and date.

## Scholarly sources

Most were read at abstract level only, because full texts are behind publisher paywalls and were not
accessed. Claims are therefore limited to what abstracts state. Specific cautions:

- `edmondson1999psychological`: one manufacturing company, 51 teams, correlational.
- `besker2018technical`: self-reported time, 43 developers.
- `kruchten2012technical`: an editors' introduction, not a study.
- `hilton2016usage`, `vasilescu2015quality`: observational, open-source settings.
- `sillito2020failures`: qualitative, 30 incidents.

## Licensing of sources

The Google SRE books and *Software Engineering at Google* are licensed CC BY-NC-ND 4.0. The book cites
and summarizes them and never copies or adapts their text or figures, because CC BY-NC-ND material
cannot be redistributed under the book's CC BY license. The GitLab handbook states "All Rights
Reserved" in its footer; treat it as copyrighted.
