# dia-elenchus — low-severity findings

Sources: docs/research/dia-elenchus.md §7–8, review docs/research/review/dia-elenchus.md (the review wins where it disagrees), diff and pass2 reviews. Files touched: `skills/dia-elenchus/SKILL.md` and `skills/dia-elenchus/references/elenchus-patterns.md`. The frontmatter description and record-template.md are unchanged.

## Per finding

- **F9 (name the shift in the user's own words): applied.** SKILL.md Step 5: `Name the shift in one line ("no deliberating → …").` -> `Name the shift in one line, in the user's own words on both sides and with no label of your own ("no deliberating → …").` I left the move categories in patterns "Noticing a birth" alone. They help you notice a move and never tell you to print its kind, so they don't conflict with the new rule. The review downgraded this finding to low, so the edit stays small.

- **F11 (no single defining feature): applied, mapped to an existing label as the review asked.** Added a bullet to patterns "Signs of aporia": `After a definition has fallen, the user shows that the cases of X share no single feature. Don't force another definition; put "whether X has one defining feature at all" under "What we now know we don't know".` The "after a definition has fallen" condition keeps the case inside the aporia criteria ("at least one definition fell … no surviving definition"), so no new result label is created. Before any definition falls, the existing "Depends" row in "Forcing a definition" still covers the case.

- **F12 (scope shift): applied.** SKILL.md intro: `… "Socratic question types". The shape:` -> `… "Socratic question types". Plato applied it to virtues such as piety and courage; here it is applied to the concept behind the user's idea. The shape:`

- **F14 (host "Socratic" study modes): applied by tightening an existing pitfall, not adding a new one.** Pitfalls, "Question-type tour": `… is modern Socratic questioning, not this method.` -> `… not this method, and so are the hints and evidence questions of an app's own study or learning mode.` The wording names no product.

- **M4 (description "during the dialogue"): declined. Owner question.** This changes the description, which needs a routing re-run (P7/L7). The task also says not to change the description. Open question: should "Gives no advice or ideas of its own" become "Gives no advice or ideas of its own during the dialogue", to match "After the dialogue (not Socratic, only on request)"? The description is 970 chars, so it has room.

- **M5 (restatement plus premise question as an implicit second ask): applied.** SKILL.md Step 2: `say "in my words" so they can correct it.` -> `say "in my words" so they can correct it; that is a flag, not a second question.` This keeps Rule 1 (one ask per message) without dropping the correction route ("If they object, take their wording and continue").

- **M6 (Theaetetus 157c-d): applied as a label on the midwife line.** I checked the text on Perseus (Fowler): "merely acting as a midwife to you, and for that reason am uttering incantations and giving you a taste of each of the philosophical theories". SKILL.md intro: `you have no ideas to hand over. You help …` -> `you have no ideas to hand over, which is stricter than the Theaetetus, where the midwife also offers theories to test (157c-d). You help …` This matches the existing "stricter than Socrates" label in Step 5 and review §3 A14.

- **F4 idea-neutral model definition (Laches 192b quickness): applied.** The review verified the locus and said it "fits the rules". Added a row to patterns "Forcing a definition": `| Examples again after you asked once | A one-line definition of something unrelated to X, for the form only (Laches 192b: quickness is the power of getting a great deal done in a little time), then: "Can you say what X is in that form?" |`. Why it fits:
  - It asks one thing.
  - It offers nothing about X, so it does not break "give no answers" or Step 5's ban on offered definitions.
  - The paraphrase is unquoted.

## Consistency reread

I reread all of SKILL.md, elenchus-patterns.md and record-template.md and found no new conflicts:
- **Rule 1:** the M5 flag is not a question, and the quickness row has one ask.
- **Rule 4:** F9 asks for the user's words, but quotation marks are still kept for exact quotes.
- **Labels:** F11 uses the existing aporia label and record section.
- **Stance and Step 5:** the M6 label adds to the "stricter than Socrates" label and does not change it. The F4 row gives only the form of a definition, never content about X.
- **Worked examples:** the l.82-84 example and the Step 5 shift example still match the text.
- **Other checks:** no Hangul, no product names, no new tool use.

## Counts

- SKILL.md: 113 lines (unchanged; every SKILL.md edit is in-line).
- Description: 970 characters (unchanged).
- elenchus-patterns.md: 59 -> 61 lines.
