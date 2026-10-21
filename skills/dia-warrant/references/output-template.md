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
- Backing: … — stated "…" | none given
- Qualifier: … — stated "…" | none given
- Rebuttal: … — stated "…" | none given

## Scheme
expert opinion | analogy | cause to effect | consequences | sign (two if both fit) | none of these: (the step in one line)

## Critical questions
1. [data] …? — answered in the argument "…" | answered by the user | answered by a source you found (evidence class) | open
2. [warrant/backing] …? — …
3. [rebuttal] …? — …
4. [conclusion] …? — …
Facts added: (each with its evidence class: verified this session (a tool ran) | supplied by the user | single source | unverified recall)

## Qualifier check
The warrant licenses "…"; the claim says "…" → matches | overstated

## Result
Weakest link: [slot], because "[question]" is left open | is answered against the step ("quote")
Why it matters: (one line)
What would strengthen it: (the kind of answer or evidence, not a fact supplied by you)

or

No weak link found among the questions asked; not a proof. Asked: 1–n. Next question I would ask: …

## Record
- Target / claim:
- Mode: audit | ask
- Scheme:
- Warrant: stated | reconstructed (W1; W2 if any)
- Questions: n asked — a answered, m open
- Result: weakest link: [slot], because … | no weak link found among the questions asked; not a proof | stopped
- Would strengthen it:
- Checked by: rereading only | a tool (name it)
- Reconstructed warrant: pending | accepted by the user | rejected by the user | not needed (stated)
- History: (one line per follow-up turn)

Whether the claim is true is not decided by this audit.
(target user, no mode named: If you would rather fill the slots yourself, one question at a time, say so and I will switch to ask mode.)
