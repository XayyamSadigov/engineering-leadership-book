# Research gaps

Questions the book needs evidence for and does not yet have. A chapter that touches a gap must admit
it in the text. Each gap records what was searched, what was found, and what to do next.
Updated 2026-11-20 after waves 1 (Part V) and 2 (Parts I and IV).

## Open

| # | Gap | Affects | Searched so far | Next step |
|---|---|---|---|---|
| G1 | Outcome evidence that blameless postmortems improve reliability | Ch 25, 27, 57 | Software: only qualitative incident-response research (`sillito2020failures`, `anandayuvaraj2026learning`) and practice accounts (`google2017postmortem`, `allspaw2012blameless`). Healthcare just-culture reviews (`murray2023just`, `vanmarum2022barriers`) support the mechanism (fear of blame suppresses reporting) and call outcome evidence scant | Aviation and safety-science outcome studies; keep labeling as cross-domain |
| G4 | No study directly compares central, embedded, and team-owned QA | Ch 19, 22, 27 | Indirect evidence added: `mantyla2012who` (who tests in three companies), `mantyla2013rapid` (Firefox under rapid release). Andersson and Runeson 2007 and NASA handbook searched; nothing citable | Keep D4 as the book's recommendation |
| G5 | SPACE and DevEx full texts unread | Ch 18 | Dimension names taken from the first author's own blog post (`forsgren2023navigating`), a GitHub blog (`alwell2021measuring`), and a vendor page (`dx-devex-report`); ACM, Queue, and CACM returned 403 | Read the papers; replace the secondary sources for the dimension names |
| G6 | Origin of cost of delay and WSJF | Ch 15, 21, 45 | WSJF verified as a SAFe method (`safe-wsjf`); attribution of cost of delay to Reinertsen not verified (book is metadata only) | Verify from publisher material or a secondary scholarly source |
| G7 | Exact wording of Campbell's law and Goodhart's popular phrasing | Ch 18, 20, 27 | Campbell 1979 metadata only; Strathern 1997 abstract lacks the phrase | Read before any quotation |
| G8 | Span of control in software organizations | Ch 34, 35 | `rajan2006flattening` (general corporate hierarchies) only | Software-specific search |
| G9 | Cost of technical debt measured on system data across many organizations | Ch 21 | Added `besker2019productivity`, `ernst2015measure` (survey of 1,831), `tornhill2022codered` (39 codebases, observational). No multi-company study on system data | Continue search; present figures only with their samples |
| G10 | Structured interview validity after Sackett et al. 2022 | Ch 7 | Abstract gives no revised structured-interview figure | Read full paper |
| G11 | Prime Video monolith case has no live primary source | Ch 31 | Original URL redirects; InfoQ secondary report | Archived primary copy or label as secondary |
| G12 | Reorganization outcomes | Ch 36 | Not yet searched | Organizational behavior literature |
| G13 | Size of a standing capacity allocation for debt and prevention | Ch 21, 27, 38 | No research found; 10–20 percent presented as this book's recommendation | Search portfolio-allocation literature |
| G14 | On-call load and health among software engineers | Ch 24, 25 | `nicol2004oncall`, `hall2017oncall` cover on-call work generally (largely healthcare); no software-specific peer-reviewed study | Search CHI/CSCW and SE venues |
| G15 | ISO/IEC 25010:2023 characteristic names | Ch 19 | iso.org returned 403; names not printed | Fetch from an accessible ISO preview or a citing paper that reproduces them, then verify |
| G16 | Effect of coding standards or style rules on outcomes | Ch 20 | No verified study; chapter relies on documented practice (`schwartz2020style`, `sadowski2018lessons`) | Search static-analysis and code-convention studies |
| G17 | Outcome evidence that SBOMs, SLSA levels, or remediation SLAs reduce breaches | Ch 26, 53 | None found | Watch for empirical supply-chain security studies |
| G18 | Effect of change size and review turnaround on review quality; outcomes of canary releases | Ch 23 | Not verified; stated as practitioner consensus | Targeted search (MSR, ICSE) |
| G19 | Comparisons of test-portfolio shapes (pyramid, trophy, honeycomb); industrial studies of exploratory testing | Ch 22 | None found | Targeted search |
| G20 | Draft standards that may change before publication: NIST SSDF 1.2 (SP 800-218r1 draft), CISA 2025 SBOM minimum elements draft | Ch 26 | Status confirmed as draft on 2026-11-19 | Re-check before human review |
| G21 | Manager effects on outcomes in software teams specifically | Ch 1, 4 | Manager-effect studies found are economics papers on other workforces (`lazear2015value`, `hoffman2021people`, `artz2017boss`), read at working-paper abstract level | Search software engineering venues |
| G22 | How engineering managers' time split relates to team outcomes | Ch 1 | Nothing found | Search |
| G23 | Full text of research on new managers (Hill) and on delegation (Leana 1986) | Ch 2 | Only publisher summaries; Leana returned 403 | Read via a library |
| G24 | Peer-reviewed estimates of flow efficiency in software delivery; cost of interruptions (Parnin and Rugaber) | Ch 16 | Not found or not readable | Targeted search |
| G25 | Planning fallacy full text (Buehler et al. 1994); Flyvbjerg 2008; McConnell's cone of uncertainty | Ch 17 | Only a course-hosted copy of Buehler exists (not used); others paywalled or unread | Read via a library |
| G26 | Agile method outcome evidence beyond the 2008 systematic review | Ch 15 | `dyba2008empirical` (abstract), `kuhrmann2022agile` (survey) | Look for newer systematic reviews |

## Closed

| # | Gap | Resolution |
|---|---|---|
| G3 | The 2023 McKinsey developer productivity article was unread | Read in full from a Wayback Machine snapshot (2023-08-20) of the original URL on 2026-11-20; entry `mckinsey2023productivity` verified. Its exhibits are images and were not read |
| G2 | Allspaw's "Blameless PostMortems and a Just Culture" unread | Read in full from a Wayback Machine copy (2013-06-09) of the original URL on 2026-11-19; entry `allspaw2012blameless` verified |

## Access problems to retry

- PagerDuty incident response documentation was blocked by the corporate proxy (Chapter 25).
- The VOID report PDFs were not read; only the SREcon22 talk abstract is cited (`nash2022void`).
- Atlassian's incident communication page returned only navigation.
- Several publisher sites (O'Reilly, HarperCollins, Macmillan, MIT Press, HBR Store, Penguin Random House, ACM Queue, iso.org) blocked fetching.
