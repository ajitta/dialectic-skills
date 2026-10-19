---
name: dia-reductio
description: Strict reductio ad absurdum run in one pass. States the thesis, lists every premise with its source, derives a strict contradiction (Q and not-Q) line by line, then lays out which premises could be given up, recommends one, and leaves the decision to the user; ends with a record. Can test the user's claim, the assistant's own earlier answer, a pasted text, or all of them, chosen with --target. Use when the user asks for reductio, proof by contradiction, indirect proof, "assume it's true and show where it breaks", "find the contradiction", or wants to know whether a position is consistent or true, or the same in any language. For the gap between what a concept or plan claims and what it delivers, or the real purpose behind a claim, use dia-negative. For one-question-at-a-time definition dialogue, use dia-elenchus.
license: MIT
metadata:
  author: ajitta
  version: "1.0.0"
  lineage: "reductio (installed copy, unversioned)"
  source: "https://github.com/ajitta/dialectic-skills"
---

# Reductio ad Absurdum

Assume the thesis, derive from it and the listed premises a statement and its negation, and show that the set cannot all be true. Then show the user which members of the set could go, recommend one, and let the user decide.

Theory, history, and the reasons behind the rules are in [references/theory.md](references/theory.md). Read it when the user asks about the method, or when you are unsure whether a step is strict. The output layout is in [references/output-template.md](references/output-template.md); read it before writing the first output.

## Parameters

`--target=user|claude|text|all` sets what is examined.

| value | what is examined |
|---|---|
| `user` | a claim, belief, plan or argument the user states |
| `claude` | your own earlier answer in this conversation (the most recent one unless the user names another); the value is `claude` on every assistant |
| `text` | a pasted or attached text by someone else |
| `all` | every one of the above that is present, each examined separately |

If no flag is given, infer the target: a pasted text means `text`; "your answer", "what you said" (or the same in any language) means `claude`; otherwise `user`. State the target you inferred in the first line of the output so the user can correct it. Natural-language equivalents of the flag count as the flag.

## Hard rules

1. **Strict contradiction only.** The absurdity must be a formal contradiction: some statement Q and its negation not-Q, both derived from the thesis plus the listed premises. A consequence that is only false, implausible, ridiculous or undesirable does not count. It becomes usable only after its negation is written into the premise list, and then the contradiction depends on that premise and says so.
2. **No hidden premises.** List every premise with a source label: **[T]** stated by the target (quote it), **[L]** a logical or definitional truth, **[A]** added by you (an implicit premise the target seems to rely on, or a fact). Give each [A] premise a one-line reason it is needed, and mark facts with their evidence class (verified this session / single source / unverified recall). A contradiction that needs an [A] premise is conditional on it.
3. **Every step names its rule.** Each derivation line cites the lines it uses and the rule (modus ponens, modus tollens, universal instantiation, substitution of a definition, conjunction, and so on). An empirical or causal claim is never a step; if the chain needs one, it goes into the premise list.
4. **One sense per term.** Fix the meaning of each key term in the premise list. If the chain only works when a term shifts meaning, that is equivocation: report it instead of claiming a contradiction.
5. **Charity first.** Test the strongest reasonable reading of the thesis. If two readings are live, test the stronger one and name the other in one line. Refuting a weaker reading is a strawman.
6. **Logic shows inconsistency, not which member is false.** A contradiction shows only that the thesis and the premises cannot all be true together. Write "the thesis is false" only when every other premise it depends on is [L]. Otherwise present the choice.
7. **The user decides.** Recommend one option and stop there. Do not continue as if the recommendation had been accepted.
8. **Language follows the user.** Write the whole output in the language of the user's latest message, including headings, labels, and the fixed result and strength values. Quote the target in its original language. Logic labels ([T], [L], [A]) may stay as they are.
9. **Whole chain in one response.** Lay out the complete argument at once; do not ask premise questions one at a time.

## Procedure

### Step 1: Fix the target and the thesis

State the target and the thesis T in one sentence, with a quote. If the input contains several claims, pick the one the rest depend on and list the others in one line as not tested.

### Step 2: Choose the direction

- **Refute:** assume T and look for a contradiction. If one appears, T or one of the premises must go.
- **Prove (indirect proof):** assume not-T and look for a contradiction. If one appears, T follows, unless a premise goes.
- **Both (default when the user asks whether T is true):** run both and read the pair:
  - only T leads to contradiction → T is untenable on these premises
  - only not-T leads to contradiction → T follows from these premises
  - both lead to contradiction → the premise set itself is inconsistent; the fault is in the premises, not T
  - neither does → these premises do not decide T; name the premise that would

For claims that something exists, an indirect proof shows existence only in classical logic; say so when it matters (see the theory reference).

### Step 3: List the premises

Number them P1, P2, … with labels [T], [L], [A] and the meaning of key terms. Keep the list to what the derivation uses.

### Step 4: Derive

Numbered lines, each with its rule and the lines it uses. Stop at the first contradiction. Keep the chain as short as the logic allows.

### Step 5: State the contradiction

Name the two lines that contradict each other and the full set they depend on, e.g. "Lines 4 and 7: Q and not-Q. Depends on T, P1, P3 [A]."

Then grade its **strength**, and put the grade in the record:

- **internal:** the set is only T plus [T] and [L] premises. The target contradicts itself. This is the strongest result.
- **conditional:** the set includes [A] premises, but they do not settle the matter alone.
- **carried by added premises:** the [A] premises, without T, already entail not-T. Check this every time an [A] premise is in the set. If it holds, say plainly that the reductio only restates what you assumed, so the real question is whether those [A] premises are true. Make the options and the recommendation turn on them.

### Step 6: Lay out the options

One option per member of that set that could be given up, T included. For each: what giving it up means, and what else has to go with it. Add a repair option where one exists: a narrowed thesis T′ that blocks the step that produced the contradiction. State T′ exactly and say whether it still does the job the original T was meant to do.

### Step 7: Recommend

Pick one option and give: the reason; the evidence class of the weakest premise the recommendation rests on; the observation that would change the recommendation. End with a sentence that the decision is the user's.

### Step 8: Record

Close with the record from the output template. Its result is exactly one of: **untenable on these premises**, **follows from these premises**, **premise set inconsistent**, **undecided by these premises**, **stopped**.

### When no contradiction appears

Say so plainly. List the directions and premise sets you tried, write "consistent with these premises, which does not show it is true", and name the premise that would decide it. Never build a contradiction from a loose consequence to have something to show.

## Targets

- **user:** follow the procedure as written.
- **claude:** quote your earlier answer and examine it with the same strictness. Say in one line that this is a self-examination and not independent. If the answer turns out inconsistent, say so directly; do not defend it.
- **text:** quote with location (paragraph or line). Attribute claims to the text, not to the author's motives.
- **all:** run the procedure separately for each target present, in the order user, claude, text, then give one combined record. Skip absent targets with one line.

## Follow-up turns

- **The user picks an option:** apply it (drop the premise, or adopt T′), rerun Steps 3 to 8 on the revised set, and add the decision to the record's history.
- **The user disputes a step:** check it. If the objection holds, withdraw the step and say whether the contradiction survives another way.
- **The user rejects an [A] premise:** remove it and rerun.
- **The user asks about the method:** answer from the theory reference, briefly.

## Pitfalls

- Loose absurdity: "then society would collapse" is a prediction, not a contradiction.
- A slippery slope presented as a deduction: each "would lead to" is a causal premise and must be listed as one.
- A strawman from testing the weak reading.
- Treating "no contradiction found" as "true".
- Quoting words the target did not say, or tidying a quote. If you paraphrase, drop the quotation marks.
