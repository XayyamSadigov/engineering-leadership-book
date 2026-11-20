# Reference analysis: `ai-engineering-book`

Analyzed on 2026-11-18 from a shallow clone of <https://github.com/XayyamSadigov/ai-engineering-book>
(commit `1bbe8d8`). The reference is MIT (code) and CC BY 4.0 (prose). This project reuses
architectural ideas only; no text, code, or diagrams were copied.

## What the reference is

A 39-chapter textbook on AI engineering, about 420,000 words of chapter prose (7,000–11,000 words
per chapter), with roughly 730 Python files implementing the projects the chapters teach from. It
publishes with MkDocs Material to GitHub Pages and ships a generated single-file edition.

| Element | How the reference does it |
|---|---|
| Source layout | `book/` is the MkDocs `docs_dir`; `chapters/`, `exercises/`, `solutions/`, `projects/`, `capstone/`, `analysis/` |
| Chapter template | Fixed H2 sequence (Why this matters, Mental model, Core concepts, … Exercises, Key takeaways, Further reading) |
| Exercises | Four categories (knowledge, engineering, practical, debugging), ids K1/E1/P1/D1, a "Start here" core set, no answers inline |
| Solutions | One file per chapter, same ids |
| Running example | One fictional company (Northwind) across all chapters and the capstone |
| Authoring control | `analysis/05-authoring-guide.md`: audience, voice, template, ownership map (which chapter owns which topic), quality checklist |
| Review | `analysis/reviews/`: written reviews per chapter wave |
| Single file | `tools/build_book.py` assembles chapters by a hard-coded part list; `--check` validates required sections |
| CI | `tests.yml` runs the code tests and `build_book.py --check`; `pages.yml` runs `mkdocs gh-deploy` |
| Coverage | `coverage-matrix.md` maps topics to chapters |

## What works and should be kept

1. **One running example.** Applying every chapter to the same organization forces consistency and
   lets later chapters build on earlier diagnoses. Northstar Technologies plays this role here.
2. **Exercises separate from solutions, matched by id.** Keeps readers honest and makes automated
   checking easy.
3. **An ownership map.** Each topic has one owning chapter; others cross-reference. This is the main
   defense against repetition in a long book written in several sessions.
4. **A binding authoring guide** that every session reads first. Here it is `CLAUDE.md`.
5. **A "first reading" path inside long chapters.** Readers with limited time get a route.
6. **Single-file edition generated from the same sources.**

## What should change for an engineering-management textbook

| Reference choice | Change here | Reason |
|---|---|---|
| Executable code is the evidence of correctness | Research traceability is the evidence: every substantive claim maps to a verified source or is labeled as opinion or illustration | A management book cannot be unit-tested; its failure mode is unsupported claims, not broken code |
| Single bibliography file in prose | Structured `research/bibliography.yaml` with verification fields, generated into a page | Lets CI refuse citations to unverified sources |
| Exercise categories: knowledge / engineering / practical / debugging | Three difficulty levels: Foundational / Applied Leadership / Executive Decision-Making | Required by the brief; progression by organizational altitude fits the audience |
| Template sections tuned for code (Implementation, Code walkthrough) | The sixteen-section contract in `CLAUDE.md` (Decision Framework, Enterprise Application, CTO Perspective, …) | The reader needs judgment at several altitudes, not an implementation |
| Projects are code packages | Projects are management deliverables built from fictional datasets, with rubrics and worked solutions | The artifact a director produces is a plan, a scorecard, an org design |
| Part list hard-coded in the build script | `curriculum.yaml` is the single source of truth; nav, curriculum page, and checks derive from it | Avoids drift between three copies of the table of contents |
| Every chapter published at once | Chapter `status` (planned, draft, published); only published chapters enter the nav | The book is written incrementally; the site must never show a stub as a chapter |
| `mkdocs gh-deploy` from CI | GitHub Pages artifact deployment (`actions/deploy-pages`) after validation passes | No `gh-pages` branch with force pushes; deployment gated on validation |
| Required-section check only | Plus section order, stub detection, word floor, diagram count, placeholder scan, YAML/JSON block parsing, Mermaid lint and render, link and anchor resolution, exercise–solution matching, citation-to-bibliography resolution | The brief's quality-control list |

## What not to copy

- Chapter length targets of 7,000–11,000 words. This book targets 2,500–5,000 meaningful words and
  prefers a complete shorter chapter.
- The reference's source-mining practice (its authoring guide works from an extracted source book
  that is kept out of git). This book does not work from any single source text.
- Vendor- and code-specific conventions.
