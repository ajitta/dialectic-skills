# Output template (dia-reductio)

Translate headings and labels per Rule 8. Use numbered lines, not wide tables, so it reads on a phone.

---

**Target:** user | claude | text | all (inferred from … — correct me if wrong)

## Thesis
T: one sentence. Quote: "…"
Direction: refute | prove | both
Not tested: (other claims in the input, one line, if any)

## Premises
- P1 [T] … — "quote"
- P2 [L] … (law of logic or mathematics)
- P3 [A] … — needed because …; evidence: verified this session (a tool ran) | supplied by the user | single source | unverified recall
- Key terms: X = … [T "quote" | A], Y = … (a meaning the derivation relies on gets its own P-line)

## Derivation (assume T; when proving, assume not-T)
1. T (not-T when proving) — assumption
2. … — from 1, P1, modus ponens
3. …
n. Q and not-Q — lines a and b

## Derivation (assume not-T)
(only when the direction is "both": the not-T derivation, same format, and its own contradiction and strength below)

## Contradiction
Lines a and b. Depends on: T (or not-T), P1, P3 [A].
Strength: internal | conditional | carried by added premises (if the last: "P3 [A] alone already entails not-T (T, when proving), so this only restates my assumption; the question is whether P3 is true.")
(If a direction found none, say so here.)

## Options
- A. Give up T (when proving: accept T; omit when the result is premise set inconsistent) → what that means; what else goes.
- B. Give up P3 → …
- C. (refuting only) Narrow T to T′ = "…" → blocks step k; does T′ still do T's job? …

## Recommendation
Option X, because …
Rests on: P3 [A, evidence class].
Would change if: …
The decision is yours.

## Record
- Target / thesis:
- Result: untenable on these premises | follows from these premises | premise set inconsistent | no contradiction found | stopped
- Contradiction depends on: (one line per direction when both)
- Strength: internal | conditional (P…) | carried by added premises (P…) (one per direction when both)
- Checked by: rereading only | a tool (name it)
- Options: A, B, C — recommended: X
- Decision: pending | the user chose …
- History: (one line per follow-up turn)
