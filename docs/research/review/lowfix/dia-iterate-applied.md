# dia-iterate: low-severity findings (lowfix)

Files edited: `skills/dia-iterate/SKILL.md` and `skills/dia-iterate/references/verification-sources.md`. The description is unchanged. No other files were touched.

## Per finding

- **F6 (misquotation fix): applied, with the review's condition.** :33's no-copy rule is amended in the same edit, and the set-text guardrail (:90) is respected.
  - SKILL.md:33: "never copied into the judgment log, the round log or the final version." -> "never copied into the judgment log or the round log, and into the output only as a misquotation corrected under step 4."
  - SKILL.md:34 (step 4), added after the "groundless" sentence: "A quotation confirmed to misstate a real source may take the source's exact words if they fit in one sentence, with the source; cut a longer one, or one from a widely copied set text, to its location (work, section)."
  - The judgment log still never quotes the source, so verification-sources.md:21 stays consistent. The corrected value is locked under step 5 like any other value fixed from a source.
- **F8 (content-filter wording): applied.** Mechanism claims are now worded as observed risk. C4 concerns citations in the research doc only, so nothing changed in the skill for it.
  - SKILL.md:33: "If output overlaps an existing document sentence by sentence, the content filter blocks the whole response" -> "Long verbatim overlap with an existing document can trigger the host's content filter, which blocks the whole response"
  - SKILL.md:88: "If a response is blocked by content filtering, retry" -> "If a response was blocked by content filtering (the user reports it, or the previous turn is empty or an error), retry"
  - SKILL.md:90: "can block even when reworded" -> "have been reported to block even when reworded"
  - SKILL.md:23: "overlap existing documents sentence by sentence and trip the content filter" -> "overlap existing documents closely and can trip the host's content filter" (removes the same undocumented "sentence by sentence" claim)
  - SKILL.md:56: "the content filter blocks the entire response" -> "the host's content filter can block the entire response" (research §6.3 cites this line as stating the reason as universal fact)
  - verification-sources.md:21: "trips the content filter" -> "can trip the host's content filter"
- **F9 (self-written tests): applied.** verification-sources.md Code row, method cell: "Execution, tests, type checking, linter" -> "… linter. Tests you write yourself share your blind spots: prefer existing or user-supplied tests, and say in the log which kind ran"
- **F10 (shared blind spot): applied.** SKILL.md:14, sentence appended: "Only defects you name can be verified, and an error you would make yourself is unlikely to be named, so a round summary is a lower bound on the defects, not a clean bill." The research wording ("errors you share with the draft") is tightened so that it also reads correctly when the user wrote the draft.
- **F12 (one line per round): applied as an optional fallback.** New Output bullet: "If the table renders poorly (the user says so, or the screen is narrow), one line per round may replace it: `Round 1: named 4, confirmed 2, refuted 1, unverifiable 1; methods: …; changes: …`." The premise that the table wraps badly on phones is still unverified, as the review notes. The bullet only permits a format and requires nothing, so it holds whether or not the premise is true. Owner may decline it if a probe of the table on a phone is wanted first.
- **F13 (fixed point): applied, adapted to the current stop order.** SKILL.md:49: "the revision is materially identical to the previous round. Stop." -> "this round changed nothing in the text, so a confirmed defect went unfixed. Stop and list it under \"Confirmed but not fixed\"."
  - The research proposal said the fixed point "normally coincides with 2". That is outdated after D22: with rules 1–3 checked first, an unchanged round can only mean that a defect was confirmed but no edit was made.
  - So the rule now names that case and routes it to the existing template line. Without this, the defect would go unreported, the same gap pass-2 finding 5 closed for regressions.

## Consistency check (full reread)

- Step 3's exception, step 4's new sentence and Guardrails :89–90 agree. A blocked response still drops source quotations, which is the later and more specific rule. Set texts stay location-only.
- The new rule 4 is checked against the stop order. Rule 2 or 3 fires on any round with nothing confirmed. The worked example ends with round 2 unverifiable and no change, so rule 3 fires first, as the example states.
- "Confirmed but not fixed" now has two feeders (rules 1 and 4) plus rule 5's "say so". All of them use the template line.
- No product names were added, and every tool use is still conditional. Nothing here needs a tool, and there is no Hangul.

## Counts

- SKILL.md: 91 lines (limit 200).
- Description: 582 characters (unchanged; limit 1024).
