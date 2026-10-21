# Output template (dia-warrant)

Translate headings, slot names, tags, statuses and the fixed results per SKILL.md Rule 8. Use lines, not wide tables, so it reads on a phone. Print plain Markdown, not a code block. Omit a section's optional lines when they do not apply; an empty slot is a result ("none given"), not a gap to fill.

---

**Target:** user | claude | text | all (inferred from … — correct me if wrong) · **Mode:** audit
(target claude: This is a self-examination, not independent.)

## Claim
C: "…" (location). Qualifier: "…" | none
Not audited: (other claims, or other reasons for C, one line, if any)

## Layout
- Data: … — stated "…" | reconstructed
- Warrant W1: … — stated "…" | reconstructed (least warrant)
- Warrant W2: … — reconstructed (only if a second is plausible; changes the result: yes | no)
- Step warrants (only for a chain): Wa data → C1 "…"; Wb C1 → C — reconstructed
- Backing: … — stated "…" | none given
- Qualifier: … — stated "…" | none given
- Rebuttal: … — stated "…" | none given

## Scheme
expert opinion | analogy | cause to effect | consequences | sign (two if both fit) | none of these: (the step in one line)

## Critical questions
1. [data] …? — answered (in the argument "…" | by the user | by a source you found, evidence class) for | against the step; or open
2. [warrant/backing] …? — …
3. [rebuttal] …? — …
4. [conclusion] …? — …
Facts added: (each with its evidence class: verified this session (a tool ran) | supplied by the user | single source | unverified recall)

## Result
Weakest link: [slot], because "[question]" is left open | is answered against the step ("quote")
Weakest link: qualifier, because the claim says "…" where the warrant licenses "…" (only if every question is answered for the step)
Qualifier check (always): the warrant (stated | my reconstruction) licenses "…"; the claim says "…" → matches | overstated (from the "generally" default? ask whether "certainly" was meant) | no warrant to compare
Why it matters: (one line)
What would strengthen it: (the kind of answer or evidence, not a fact supplied by you)

or

No weak link found among the questions asked; not a proof. Asked: 1–n. Next question I would ask: …

## Record
- Target / claim:
- Mode: audit | ask
- Scheme:
- Warrant: stated | reconstructed (W1; W2 if any; Wa and Wb for a chain) | none given
- Questions: n asked — a answered, m open
- Result: weakest link: [slot], because … | weakest link: qualifier, because the claim says "…" where the warrant licenses "…" | no weak link found among the questions asked; not a proof | stopped
- Qualifier check: matches | overstated ("…" vs "…") | no warrant to compare
- Would strengthen it:
- Checked by: rereading only | a tool (name it)
- Reconstructed warrant: pending | accepted by the user | rejected by the user | not needed (stated)
- History: (one line per follow-up turn)

Whether "…" (C, quoted) is true is not decided by this audit.
(target user, no mode named: If you would rather fill the slots yourself, one question at a time, say so and I will switch to ask mode.)
