# Russian edition: literary editing brief

Goal: each Russian chapter reads as a professional book written in Russian by a Russian author, not as a
translation. Clear, logical, easy to read, precise. Binding together with `research/translation-ru-glossary.md`
(terms, numbers, mechanics) and `CLAUDE.md`.

## How you work

- **Read only the Russian text. Do not open the English chapter.** You are the Russian reader's editor;
  looking at the source pulls the text back toward English structure. (A separate check compares meaning
  afterwards.)
- Edit the `.ru.md` file in place, paragraph by paragraph. Read each paragraph aloud in your head: if a
  Russian editor at a good technical publisher would rewrite it, rewrite it.
- **Meaning stays.** Do not add claims, examples, or facts; do not drop any; do not soften or strengthen a
  claim or an evidence label. Every number, name, week, percentage, and dollar figure stays exactly.
- **Mechanics stay untouched**: heading text may be improved, but every `{ #anchor }` stays; links, link
  targets, citations (`[Forsgren et al., 2018](...)`), exercise labels (`**F1.**`), admonition types,
  Mermaid structure and ids, table structure and every number inside tables. Mermaid labels may be
  improved if they stay short.
- Terms: use the term base and the wave-1 renderings (`research/translation-ru/notes-t*.md`). If a
  rendering reads badly, keep it consistent anyway and propose a better one in your notes.

## What to fix

1. **English skeleton.** Rebuild sentences in natural Russian word order: theme first, new information at
   the end; verbs instead of noun chains («принятие решения о выделении ресурсов» → «решить, сколько
   выделить»); fewer passives.
2. **Chains of «который»**, participial pile-ups, and three-level subordinate clauses: split or rebuild.
3. **Logic of the paragraph.** One thought per paragraph; the point in the first sentence; explicit
   connectives where English relied on juxtaposition («поэтому», «зато», «но», «то есть», «например»);
   no connective where none is needed.
4. **Calques and filler**: «является» (use a dash or a verb), «на самом деле» used as English "actually",
   «в терминах», «это то, что», «делать решение», «адресовать проблему», «играть роль» where not meant,
   «достаточно» as an intensifier, «в то время как» for contrast, «таким образом» as a paragraph opener,
   possessive pronouns English needs and Russian does not («свою команду» where obvious).
5. **Bureaucratic register**: «осуществлять», «данный», «в рамках», «производить», «имеет место»,
   «с целью», «в целях», «на сегодняшний день».
6. **Rhythm**: vary sentence length; avoid three long sentences in a row; a short sentence after a long
   argument lands the point.
7. **Consistency of voice**: «вы» throughout; imperatives in playbooks; the book's direct, concrete tone;
   no added emotion or flourish.
8. **Typography**: «ёлочки», em dash with spaces in prose, en dash in ranges, non-breaking spaces between
   number and unit (glossary rules 3–6), «ё» where the word needs it for clarity.

## Notes you write

`research/translation-ru/editing-<chapter>.md`:
- **Patterns**: the recurring problems you fixed, each with two or three real before → after pairs from
  this chapter. These feed the style guide for the remaining chapters, so be specific.
- **Three showcase paragraphs**: the original and your edit, side by side, for the maintainer to show.
- **Term proposals** and anything that looked wrong in meaning (do not fix meaning; report it).

## Checks before you finish

- `.venv/bin/python tools/validate_book.py` passes (do not run `mkdocs build`).
- Every number in the chapter is unchanged: compare the sorted list of numbers before and after
  (`grep -oE '[0-9][0-9 ,.]*' file | sort`) against the copy in your notes or git (`git diff` shows the
  committed version).
- Do not spawn subagents or forks. Do not commit.
