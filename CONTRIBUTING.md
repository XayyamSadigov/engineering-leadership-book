# Contributing

Thank you for helping. This book is only as good as its accuracy, so the most useful contributions are
corrections.

## Most wanted

1. **A claim its citation does not support.** Open an issue with the chapter, the sentence, the cited
   source, and what the source actually says (with a link or page reference if you have one).
2. **A better source.** Research that supports, qualifies, or contradicts a claim, especially where the
   book records a gap (`research/research-gaps.md`) or a dispute (`research/disputed-claims.md`).
3. **Practice that contradicts the advice.** If you have led through the situation a chapter describes
   and it went differently, describe what happened and in what context. Experience reports are treated
   as expert opinion, not evidence, but they often show where advice needs a condition attached.
4. **Human review of a chapter in `review` status.** Work through
   `research/human-review-checklist.md` and record the result in a pull request that updates
   `research/quality-report.md`.

## Before opening a pull request

- Read `CLAUDE.md`. It is the authoring guide for everyone, not only for AI tools.
- Run `python tools/build_curriculum.py && python tools/build_single_file.py && python tools/validate_book.py --build`.
- Do not edit generated files by hand (`docs/curriculum.md`, `docs/references/bibliography.md`,
  `docs/exercises/index.md`, `dist/`).
- New sources go into `research/bibliography.yaml` with `verified_fields`, `verified_via`,
  `verified_on`, and an honest `access_level`.
- Keep Northstar facts consistent with `docs/case-studies/northstar/`.

## Rules that are not negotiable

- No invented quotations, statistics, studies, page numbers, or URLs.
- No real company or real person in an invented story.
- No text, figures, or exercises copied or closely paraphrased from copyrighted works.

## Copyright concerns

If you believe a passage is too close to a source, open an issue titled "Copyright concern" with the
passage and the source. It will be reviewed and, if needed, rewritten or removed promptly.

## License of contributions

By contributing, you agree that your contributions to the text are licensed under CC BY 4.0 and your
contributions to code under MIT, as described in `LICENSE-CONTENT.md` and `LICENSE`.

## Conduct

Participation is governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
