# dia-reductio: low-severity findings

Worktree: /home/ubuntu/work/dia-review/lowfix, files under skills/dia-reductio/ only. Not run: tools/package.py and tests (per the rules). A scripted scan found no Hangul and no product names in the skill folder.

## Per finding

- **F8 (description over-promises "consistent or true"): applied.** SKILL.md:3, "wants to know whether a position is consistent or true" -> "wants to know whether a position holds together or follows from its premises" (pass-2 finding 5 wording). Every other trigger phrase is unchanged. Step 2's "Both (default when the user asks whether T is true)" still holds, because "follows from its premises" is the relative answer it gives. **Owner/probe note:** this is a description change, so L7 needs a P7 re-run (English and Korean) before release, and ideally the negative probe the research proposes ("is it true that …" must not load the skill).
- **F11 (vagueness): applied, in the review's corrected wording.** SKILL.md Pitfalls, new line after "slippery slope": "A chain of small steps over a vague term ("one more grain does not make a heap"): each step may be valid, and the tolerance premise is the usual weak point. List it as a premise and offer it as an option." The wording says "the usual weak point", not "the fault", as the review asked.
- **F12 (least-assumed contradiction): applied in part.** SKILL.md Step 4, "Stop at the first contradiction." -> "Stop at the first contradiction, unless one that depends on fewer [A] premises is also within reach; then report that one." This settles the conflict the review found with "stop at the first". Declined: "the depends-on set lists only premises used" (the review says Step 3 and Step 5 already cover it) and "number premises in the order the derivation uses them" (a new rule whose evidence [27] is about input order, not output numbering).
- **F13 (classical-logic note): applied, with the review's correction; template line declined.** SKILL.md Step 2, "For claims that something exists, an indirect proof shows existence only in classical logic; say so when it matters" -> "Concluding T from a contradiction with not-T is indirect proof, which intuitionistic logic does not accept in general (it does when T is itself a negation); say so when it matters, above all for claims that something exists". theory.md §2 Indirect proof gets the matching clause: "where reductio proves only negative statements because not-not-A does not imply A in general (SEP, "Intuitionistic Logic"); it does when A is itself a negation". I checked the SEP quote verbatim. I added the SEP source. Declined: the template line "n+1. T — indirect proof (classical)". The result "follows from these premises" already states the conclusion, and a line after the contradiction would sit awkwardly with "stop at the first contradiction".
- **F14 (theory.md sources): applied in part.** theory.md §7, "(IEP, comparing Aristotle, *Rhetoric* II.23)" -> "*Apology* (27b–e) … (Aristotle, *Rhetoric* II.23, uses the same argument)", plus one sentence: it is not a model of strictness, because a premise comes from Meletus' silence ("your silence gives consent", checked verbatim in Jowett; review §2 [18]). I removed the Madhyamaka sentence and its Wikipedia source, since it was only weakly sourced. I added the Jowett *Apology* source. Declined: the "(Rescher presents both as looser…)" note, which the review calls redundant with theory.md:43.
- **F15 (hard cases): applied.** New theory.md "## 9. Hard cases" with three bullets:
  - (a) Euclid IX.20 is a direct proof with one local reductio step (Joyce's text checked: "If possible, let it be so … which is absurd").
  - (b) Zeno, worded as one reconstruction, as the review asked. The premise "an infinite sum of finite quantities must be infinite" is false (SEP checked), so a premise that only sounds mathematical is [A], not [L].
  - (c) Paradoxes: the classical result is "premise set inconsistent", with one line on dialetheism and paraconsistency, and "this skill holds classical logic fixed". The wording avoids the research's overclaim that dialetheism "needs" a paraconsistent logic.
  - Sources added: Joyce, Hardy–Woodgold, SEP Zeno, SEP Dialetheism and Paraconsistent Logic.
  - **Owner question (research OQ7):** is this one-line disclosure of dialetheism the wanted level, or should theory.md say nothing?
- **M5 (unconditional reference read, no fallback): applied.**
  - SKILL.md:16, "read it before writing the first output." -> "read it before writing the first output if you can open it (Step 8 names the record fields in case you cannot)."
  - Step 8, "Close with the record from the output template." -> "…from the output template: target and thesis, result, what the contradiction depends on, strength, how it was checked, options and the recommended one, decision, history." These are the same fields as template:47-54.
- **M6 (confounded probe evidence): declined.** It concerns docs/probes.md and the research text, not the skill.
- **M7 (`all` has no combined record form): applied.** SKILL.md Targets/all, "then give one combined record." -> "then give one combined record with one entry per target on each line." This sits alongside the template's existing "one line per direction when both" without conflict.

## Consistency check

I reread SKILL.md, output-template.md and theory.md in full.
- The new [A] rule in the Zeno bullet matches Rule 1/Rule 2 ("[L] only if it is a theorem of mathematics").
- The Step 4 change matches "keep the chain as short as the logic allows" and the worked example.
- The Step 8 field list matches the template record.
- The F13 text matches theory.md §2.
- No product names, no Hangul, and every tool use is still conditional (none was added).

## Counts

- SKILL.md: 135 lines (limit 200).
- Description: 846 characters (limit 1024; was 824).
- Files changed: skills/dia-reductio/SKILL.md, skills/dia-reductio/references/theory.md. output-template.md is unchanged.
