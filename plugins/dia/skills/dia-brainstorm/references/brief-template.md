# Brief template

Lead with one plain line before the brief: the verdict and the next step. Fill every section from the user's answers only, and translate the section headers into the user's language. In chat, print the brief as plain Markdown, not inside a code block (code blocks scroll sideways on phones); the block below only shows the structure. Mark an empty section "none" rather than dropping it; if several are empty, list them on one line ("None: parking lot, criteria, options") so the reader still sees they were considered.

```markdown
# Brief: <short name>  ·  <YYYY-MM-DD, if known>

**Verdict:** sharpened | open | refuted  ·  mode: develop|stress  ·  probes: <n>

## Thesis
- Before: <user's first statement, paraphrased>
- After: <the user's restatement from Step 5, or else the working thesis (the user's own statement if none was formed); any tightening marked as yours; any live risky assumption written in as a condition, e.g. "…, piloted for one month first">

## Decisions
- <decision> (confirmed | delegated)

## Assumptions
- <assumption> (validated | unvalidated | risky)

## Open questions
- <what must be answered before or while proceeding>

## Options considered
1. <option> (user's | mine): <one line on how it fared against the criteria>

## Criteria
- <the user's 2-3 criteria, their words>

## Parking lot
- <tangent worth keeping>

## Not tested this session
- <e.g. "no counterexample pressure", "no outside viewpoint">

## Next step
<one concrete action the user takes; one, not a list>
```

Rules:

- `refuted` requires both colliding statements quoted verbatim under Open questions or Thesis, plus the user's attempted reconciliation. Without that, it is `open`.
- `risky` means load-bearing *and* doubtful. Address risky assumptions first in the next step.
- More than one delegated decision: add "Recheck the delegated decisions before building" to the next step.
