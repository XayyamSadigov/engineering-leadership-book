# Russian translation brief: chapters (wave 1)

Binding for every translator, together with `CLAUDE.md` and `research/translation-ru-glossary.md`
(read both in full first; the term base and style rules in the glossary win any doubt).

## Task

Translate each English chapter `docs/parts/<part>/<NN>-<slug>.md` into `docs/parts/<part>/<NN>-<slug>.ru.md`
beside it. Source: the English file as committed at `b84a765` (the working tree; do not edit English files).

## Quality bar

- **Complete and faithful.** Every paragraph, list item, table row, admonition, exercise, reflection
  question, takeaway, and reference line is translated. Nothing summarized, nothing added, no facts or
  numbers changed. Evidence labels keep their strength (glossary section 4).
- **Natural Russian for engineers**, written as a Russian author would write it (glossary section 2):
  rebuild English noun stacks into verbs, split heavy sentences, no bureaucratic register, «вы».
- **Consistent terms**: use the term base (section 3). If a term is missing, choose a rendering, use it
  consistently, and list it in your notes file for the maintainer.
- **Read your translation back** once, as a Russian reader, and fix anything that reads like a translation.

## Mechanics (glossary section 1, restated)

- Every heading (H1–H4) carries the English anchor: `## Почему это важно { #why-this-matters }`. Compute it
  from the English heading with Python-Markdown's default slugify
  (`from markdown.extensions.toc import slugify; slugify(text, "-")`) or read it from the built English page
  `site/<page path>/index.html`. H1 too: `# Глава 18 — Измерение продуктивности инженеров { #chapter-18-... }`.
  Keep headings in the English order. The H1 uses the Russian chapter title from `mkdocs.yml`'s `ru`
  `nav_translations`, so the nav and the page agree.
- Links keep their English targets and anchors (never link to `*.ru.md`). Citations keep their English link
  text (`[Forsgren et al., 2018](...)`). Exercise labels `**F1.**`, `**A1.**`, `**X1.**` stay as they are.
  The 16 chapter-contract H2 headings and the three exercise levels use the fixed renderings in the
  glossary's section 4 (e.g. `## Почему это важно { #why-this-matters }`, `### Базовый уровень { #foundational }`).
- Mermaid: translate labels, keep ids and structure, keep labels short, quote labels with punctuation.
- Tables: numbers copied exactly as in English (glossary rule 6); prose numbers in Russian format.
- Admonitions: type stays, title translated (`!!! info "Northstar к этому моменту"` or the term base's form).

## Process

- Edit only your `.ru.md` files and your notes file `research/translation-ru/notes-<lane>.md` (new terms,
  doubts, places where the English looked wrong; do not fix English).
- Do not run `mkdocs build` or `validate_book.py --build` (parallel builds collide on `site/`). Validate with
  `.venv/bin/python tools/validate_book.py` and fix every error in your files (broken anchors, links).
- Do not spawn subagents or forks. Do not commit.
- Final report under 200 words: files done, word counts, open terms.
