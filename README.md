# The Engineering Leadership Handbook

**From Senior Engineer to Engineering Manager, Director, VP Engineering, and CTO**

An open-source, evidence-informed textbook on building, leading, scaling, and transforming software
engineering organizations.

> **Status: early.** The curriculum is fully designed (60 chapters in 15 parts, 20 templates, 8
> projects, a capstone). One flagship chapter and four templates are written and on the site,
> awaiting human review. Everything else is planned. See [`PROJECT_STATUS.md`](PROJECT_STATUS.md) and
> the generated [curriculum](docs/curriculum.md).

## What makes it different

- **Evidence labels.** Each claim says what supports it: research, industry research, a standard,
  documented practice, practitioner consensus, expert opinion, the book's own recommendation, or an
  illustrative example.
- **A verified bibliography.** [`research/bibliography.yaml`](research/bibliography.yaml) records,
  for every source, which citation fields were confirmed on which page and how much of the work was
  actually read. CI refuses citations to unverified entries.
- **One fictional company throughout.** [Northstar Technologies](docs/case-studies/northstar/index.md),
  80 engineers, declining quality, a mandate to recover without new headcount, with data files you
  can analyze yourself.
- **Every chapter teaches judgment:** a decision framework, trade-offs, failure modes, application at
  50 to 150 engineers, the CTO's view, a playbook, and exercises at three levels with separate worked
  solutions.
- **Working templates** with filled-in examples.

## Read it

- Website: <https://xayyamsadigov.github.io/engineering-leadership-handbook/> (published by the
  `docs.yml` workflow once the repository is on GitHub)
- Single file: [`dist/ENGINEERING_LEADERSHIP_HANDBOOK.md`](dist/ENGINEERING_LEADERSHIP_HANDBOOK.md)
- Start with the flagship chapter:
  [Chapter 27 — Quality Transformation at Enterprise Scale](docs/parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md)

## Repository layout

```text
curriculum.yaml        single source of truth for parts, chapters, status, objectives, sources
docs/                  the book (MkDocs docs_dir)
  parts/               chapters, one directory per part
  solutions/           worked solutions, one file per chapter
  templates/           Part XIV template library
  case-studies/        Northstar Technologies and its data
  references/          generated bibliography page, evidence labels
research/              bibliography, research plan, evidence matrix, gaps, disputes, review checklist, quality report
tools/                 validation and build scripts (Python, PyYAML)
dist/                  generated single-file edition
CLAUDE.md              binding authoring, research, and continuation rules
PROJECT_STATUS.md      what is done, what is next
```

## Build and validate

Requires Python 3.9+.

```bash
python -m venv .venv && . .venv/bin/activate
pip install "mkdocs>=1.6,<2" "mkdocs-material>=9.5,<10" "pyyaml>=6"

python tools/build_curriculum.py      # regenerate curriculum, bibliography, and exercise index pages
python tools/build_single_file.py     # regenerate dist/ENGINEERING_LEADERSHIP_HANDBOOK.md
python tools/validate_book.py --build # all checks plus mkdocs build --strict
mkdocs serve                          # preview at http://127.0.0.1:8000/engineering-leadership-handbook/
```

Optional diagram rendering check (needs Node.js):

```bash
npx -p @mermaid-js/mermaid-cli@11 sh -c 'cd tools && python render_diagrams.py'
```

What `validate_book.py` checks: navigation entries exist and match chapter status; internal links and
anchors resolve; every live chapter has the sixteen required sections in order, no stubs, at least
2,500 words and two diagrams; exercises exist at three levels and each has a solution of substance;
citations resolve to verified bibliography entries and each chapter cites at least five sources; the
bibliography is structurally valid; YAML and JSON blocks parse; Mermaid blocks pass a lint; no
placeholder text; generated files are current; the site builds in strict mode.

What it does not check: whether claims are true. That is the human review in
[`research/human-review-checklist.md`](research/human-review-checklist.md).

PDF and EPUB editions are not built yet. The single Markdown file converts with Pandoc
(`pandoc dist/ENGINEERING_LEADERSHIP_HANDBOOK.md -o handbook.epub`), but Mermaid diagrams would need
pre-rendering first; this is on the backlog.

## Publishing

`.github/workflows/validate.yml` runs validation, linting, and diagram rendering on every push and
pull request. `.github/workflows/docs.yml` validates, builds, and deploys to GitHub Pages on pushes to
`main`. In the repository settings, set **Pages → Source** to **GitHub Actions**.

## Contributing

Corrections to claims and sources are the most valuable contribution. See
[`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

Text, templates, and data: [CC BY 4.0](LICENSE-CONTENT.md). Code and configuration: [MIT](LICENSE).
Northstar Technologies and everything about it is fictional.
