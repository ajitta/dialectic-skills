# dialectic-skills — Specification

| | |
|---|---|
| Status | Rules and rulings in force for plugin `dia`. What each skill does is defined by its `skills/<skill>/SKILL.md`, and the package by `tools/package.py` and `tests/`; where this document disagrees with them, they hold and this document is corrected. The current release is in `docs/handoff.md` and the git tags. The decision rows D1 to D126 are in `docs/history/decision-log-to-5.4.1.md`, and the former status line is in `docs/history/spec-sections-to-5.0.0.md`. |
| Date | 2026-10-20 |
| Owner | ajitta |
| Repository | `ajitta/dialectic-skills` (public since 2026-10-20) |
| Scope of this document | The rules the package keeps (§4, §6 to §8, §12.1) and the rulings in force behind the skills and the package (§3). |

## 1. Summary

`dialectic-skills` packages thirteen reasoning-and-review skills and their entry point, `dia-router`, as one plugin, installed under the plugin name `dia`. Seven were first rebuilt from the owner's earlier skills (socratic-brainstorm, socratic-elenchus, reductio, negative-dialectics, self-refine, recursive-refine, confirm-intent); the others came from the candidate research (D35, D40, D41, D55). Every skill has since been rewritten from its purpose (D90 to D119). The target surfaces are:

- Claude Code
- Codex
- Claude desktop
- ChatGPT desktop
- The Claude and ChatGPT mobile apps

The shipped package contains instructions only: Markdown, YAML and JSON. It has no hooks, scripts, binaries or MCP servers, because nothing may depend on an execution harness at run time. Build and validation scripts exist only in the repository, for the developer.

## 2. Goals and non-goals

### Goals

- G1. One plugin, `dia`, containing the skills named in §4.
- G2. The same skill files run unchanged on every target surface, and on a surface that has no tools at all (mobile chat).
- G3. Skill files are written in English. Hangul appears only under `references/ko/` (§6).
- G4. The material the first skills were rebuilt from is kept in `upstream/` as read-only provenance and never shipped.
- G5. Every install route and invocation path is either backed by a source or was probed (`docs/probes.md`).

### Non-goals

- Changing or deleting the existing skills or the `socratic` plugin in `ajitta/superclaude`. They are reference material only.
- The skill-folder mode of recursive-refine, which depends on subagents and `scripts.package_skill`.
- Publishing to Anthropic's or OpenAI's public directories (a non-goal of 1.0.0; since D32 the package is prepared for them and the submission is the owner's, `docs/directory-submission.md`).
- Automatic migration of existing installs, such as a marketplace `renames` map. The old skills were used by the owner alone (§10).

## 3. Decisions

### 3.1 Rulings in force

Each line is a ruling that still binds work on this repository, with its reason, or an alternative that was tried or weighed and not done, with why. Lines leave out what a skill file or the code already states with its reason; read those files for what the skills do. The numbers point to the full rows, which hold what was decided, why, what was run and the owner's words: D1 to D126 in `docs/history/decision-log-to-5.4.1.md`, D127 on in §3.2. Where a line disagrees with a skill file, `tools/package.py` or `tests/`, those hold and the line is corrected. A ruling is weighed on its merits, not obeyed for having been made: where it is wrong, or its reason no longer holds, a new decision replaces it.

#### Process

- A fault in a skill is changed at its cause in the design or left and reported, never met by a sentence for its case, because bodies rewritten from purpose at a third of the length gave what bodies grown case by case gave. (D114)
- Only a review finding under which a model would act wrongly in an ordinary case is fixed, because fixing nearly every finding of independent reviews kept lengthening the skill text; low harm, a behaviour never run and an earlier decision are not grounds for leaving such a fault. (D72, D123)
- A major plugin version marks a change in how every skill is reached, or skills written afresh from their purpose. The early one-name renames shipped as minor versions only because the owner was the only user and the repository was private; that reason no longer holds. (D30, D56, D90, D114, D118)

#### Evaluation

- In a comparison with a simulated user, the dialogue's ending rule, the skill-loading mechanism and any theory-based answer key are fixed for every arm before the runs, because in the falsifiability study the relay and a narrow key, not the skill, explained several losses. (D70)
- No Sonnet or Haiku cell is run, because a strong model at low effort does better than a weaker model at high effort. (D89)
- A skill text that changes behaviour is released only when runs show it better than the released text, judged by lines written before the runs; only the owner's later word departs from that. (D118)
- A comparison between builds holds every skill text but the changed one fixed and counts against a change only what it could cause, because floor runs that had loaded different dia-techne texts could not show what the dia-skopos sentence did. (D126)
- A test of dia-techne's work after a dia-skopos review holds the review fixed, one review continued under each build, because what the review names shapes what the released work lists (it carried the deciding line when the review gave its number, 4 of 4, and dropped it once when the review placed it loosely) and the review's search varies by chance (it showed that line in 5 of 15 runs in Part CJ and in 6 of 6 in Part CL). (D128)

#### Package

- The provenance folder at the repository root is named `upstream/`, not `references/` or similar, because each skill ships its own `references/` folder and the two must not be confused. (D13)
- `short_description` in `agents/openai.yaml` is UI-only: Codex shows the model the SKILL.md description, not this field, so changing it needs no routing probe; its 25-to-64-character range is OpenAI's skill UI guidance. (D29)
- Each sample prompt in the OpenAI listing starts with a skill's name, because the descriptions start a skill only on invocation by name and a prompt that only sounds like a skill starts none. (D120)
- Not done: keeping sentences that several skills share in one source and inserting them into each body at build, because such a sentence came out different in each skill once reviewed against that skill's own method. Weigh the reason again before relying on it: since D118 several bodies share near-identical sentences. (D105)

#### Names and invocation

- A skill name must not be a word of ordinary AI requests (as refine, instruct, brainstorm and intent were), because a message's first word starts a skill; no single etymology is required of all names. (D56)
- Not done: renaming the plugin `dia`, the repository or the `dia-` prefix; the owner ruled they stay when names were weighed, and a rename breaks every install and invocation that uses the old name. (D45)
- Not done: renaming dia-techne or dia-skopos to a plain word that loads more often on short code-fix requests; a Latin or Greek name keeps such a skill from being reached for casually, and a model doing a short clear task directly is accepted. (D55)
- Not done: a shorter description gate such as "Use only on direct invocation or selection by dia-router", because it let a counterexample request load dia-conjecture; every description keeps the full first-word gate sentence. (D56)
- Not done: a clause in the skill descriptions about use by agents or reviewers, because naming the skill already loaded it in every run and any description clause adds to every session's skill listing. (D67)
- Not done: rewording descriptions so a Korean message with the word for folder right after a skill's name loads the skill, because that phrase is ordinary Korean for the folder of that name, and no description can claim it without taking requests about folders. (D105)
- Not done: a `--` separator in `dia` commands, because iOS Smart Punctuation turns it into an em dash. (D56)
- Not done: three-letter codes or prefix selectors after `dia`, because they were the weakest selector, prefixes collide as names change, and one way to name a skill is wanted. (D57)
- dia-router picks a skill by full name only, never by menu number, although names typed after dia may be autocorrected on a phone, because the numbers and the counting-number exceptions they need are not worth their text. (D72)
- Not done: a keyboard text-replacement route for typing skill names on a phone; the owner ruled it out of scope, and the package meets phone typing through the first word `dia`. (D38)

#### Docs

- The README translations translate the example prompts, so each file shows requests in its own language; only command blocks stay byte-identical with `README.md`. (D31)
- The READMEs, the site, the manifests and the plugin README name no retired way to pick a skill, not even as lookup or in a note that it stopped working, because a removed form shown still teaches it; quoted recorded output is exempt. (D77)

#### All skills

- A skill works from the source that settles the matter (the target's text and prior commitments, the data, what only the user holds), and one handed to a sub-agent or reviewer gets what its caller holds, because otherwise its method runs on something else. (D124)
- The skills that examine a position give the assistant's own judgment; texts that withheld it ("No verdict", "The user rules; you classify") are not brought back, because these skills exist to bring out what was not known and to judge it, not to follow steps. (D118)
- A skill's own result under a caller-fixed output format is kept by text in the skill body, not by a caller checklist in the README, because the session that writes the script or brief never consults the README. (D68)
- Skill files are structured with Markdown headings and bold, not XML tags, because no comparison shows a difference on current models, a prompt's format carries into output that must be Markdown, and most section names belong to one skill. (D76)
- Not done: removing skill text only because the record ties its reason to a Sonnet or Haiku failure, because almost no sentence has an Opus or Fable run without it, so provenance alone cannot show what may go. (D90)
- Not done: cutting skill text on the ground that a host's system prompt already covers it, because the skills run on hosts whose system prompts differ. (D74)
- Not done: rewording the skills' "never" lines because a model treats "never" as absolute, since most state a definition or a ban inside the method, and where a request could clash the model followed the request. (D74)
- Not done: a form standard of required sections and their order across skills, because the bodies grew through measured features rather than form and restructuring has changed a skill's scope before; only sections holding the same kind of thing share a name. (D72)
- Not done: a finer label for where each statement came from, or a shared sentence on sources in every skill, because in runs such a label was printed in place of the act. (D124)
- Not done: moving the limit that keeps what is not known out of text for the user into the judgment sentence in dia-reductio, dia-counterplan, dia-conjecture and dia-adjudicate, as in dia-warrant, because the move showed no effect in dia-warrant. (D124)
- Not done: reconciling "say in the first line" what was taken as the target with "Lead with the judgment" in the remade verifying skills, because both are wanted and either order serves the user. (D123)
- Not done: a separate dia skill for whether a claim is falsifiable, because existing skills already met such requests: dia-conjecture names beforehand what would count against a claim, and dia-quaestio's stress mode asks a falsification question. (D70)
- Not done: a skill that sets standing rules for a whole conversation (such as keeping recall apart from what was checked), because a sentence pasted at the start did the same; the README gives that sentence instead. (D71)
- Not done: moving the wait in dia-conjecture and dia-adjudicate ("nothing is drafted or recommended that an answer could overturn") onto a fact as dia-reductio has it. On tasks where the user holds the deciding facts, every course they gave before the answers that an answer could change came by case, or with its assumption and what the other answer would change, and the case the user was in gave the course she ended with: 4 of 4 runs (probes Part CN), and 4 earlier runs on the same sentence (Part CA). What they made for the user to pass on before the answers carried its condition. (D130)
- Not done: the other researched candidate skills (dia-munazara and dia-defend, dia-hypothesis, dia-commit, a munāẓara pushback rule); the owner picked three by fit for human-AI chat and fidelity, and the rest were left for a batch no later decision took up. (D35)

#### Single skills

dia-adjudicate
- Not done: a 'For the caller' block in dia-adjudicate asking callers to make its second run, because a caller writes its brief without opening the skill; the dia-panel judge workflow, listed to the caller, makes both runs instead. (D78)

dia-elenchus
- dia-elenchus keeps its first-message line for a request that only says "Socratic", because dia-router sends such requests to it even about a plan, and that line is the only place the user learns the dialogue is strict and that dia-quaestio exists. (D97)
- Not done: rewording aporia as "no definition that has not fallen" to remove the literal reading that a stop right after a revision is aporia, because the released wording already gave "stopped before testing" in that case. (D117)

dia-emend
- Not done: sentences guarding dia-emend against a model's habits (no severity filter, no edits for show, being invoked is no sign of error, no sub-agents), because the cases built for them held without them. (D91)
- Not done: treating an audience or tone the user gave as only a criterion with no basis for a change, because runs then left unfixed what that audience itself calls for, such as the greeting, subject line and deadline. (D106)
- Not done: sources beside the sentence inside the revision; dia-emend gives each source with the checked item in its reply, because the revision is the text the user keeps or sends. (D123)
- A file target's passage keeps its wording under step 4's own case for a suspected correction, not as an exception in the Output section, because placed there an unverified correction was still written into the file. (D123)

dia-negative
- Not done: making a finding whose argument splits into cases wholly conditional unless the gap is strict on every branch, because that text lost the strict gap on the vacation-policy task and was reverted. (D47)
- Not done: a further remake of dia-negative; only a real use below the owner's floor (the words the user is left with true when said, then complete) reopens it, because candidates did not differ from the released text and another round would patch. (D119)

dia-quaestio
- Not done: a sentence against dia-quaestio joining two asks in one message, because every joined ask was answered in full and no cause is named. (D124)

dia-ratchet
- The snippet limit stands in step 3, where the verdict is written, and not only in the reference file, because a run that cannot open the reference had no rule against a verdict from a result list. (D123)

dia-reductio
- The wait before making what the user is to act on is conditioned on a fact the model can check, whether the questions it put are answered, not on what an answer could overturn, because under the latter the model judged its own draft safe against every answer and drafted anyway. Shown in dia-reductio only. (D123)
- The ask for the words a position points to and was not given stands where the questions are written, and earlier promises are listed among the target's commitments, because placed in What is examined the ask was printed as a line rather than asked. (D125)
- Not done: rules fixing the logic of dia-reductio's derivation (classical logic, per impossibile) in its body or theory file, because the remade body dropped them and a reference file describes the body rather than adding rules to it. (D123)

dia-regula
- dia-regula's item on an instruction that reads in what a person wants leaves the form to that instruction and requires no labelled lines, because a fixed two-line form made its reviews report dia-skopos and dia-techne, which dropped such lines on purpose, as breaches. (D120)
- Not done: a sentence in dia-regula limiting how far a text it writes grows beyond the rules the user stated, because the additions were mostly the default branches Rule 1 asks for and the user can delete them. (D73)

dia-router
- dia-router chooses for a request by the skills' own descriptions and carries a border sentence only where runs showed the descriptions do not settle it, so there is no second routing layer to keep in step. (D57)
- dia-router keeps its sentence sending a Socratic request about a plan or idea to dia-elenchus, because without it the model picks dia-quaestio; letting the model's own pick decide was considered and not done, as each skill's first message already points to the other. (D101)
- dia-router never picks dia-skopos, dia-ratchet, dia-adjudicate or dia-techne for a request but replies with the form to send; their gates stay explicit, a wrongly started dia-skopos holds the user's task, and dia-techne redefines the request and runs it. (D57)
- Material handed to reviewers is "copied as the user wrote it", not "in the user's own words", because the latter says whose the words are and not their form, and the caller passed its own translation. (D125)
- dia-router's rules are unnumbered bullets, because a numbered rule was quoted back to users ("Rule 4 applies here"). (D57)
- Not done: a dia-router sentence sending falsifiability requests to dia-quaestio's stress mode, because it made routing uniform without a gain graders agreed on, and the routing re-run found no harmful pick for it to fix. (D70)

dia-skopos
- Reading, from the user's own words, the end a request serves is dia-skopos's work and is not handed to dia-quaestio, because dia-quaestio works by asking questions and a review that only restates the request gives no reason to use dia-skopos. (D88)
- Not done: a separate skill or mode for an always-on outcome contract; inferring the result a request serves stays in dia-skopos, because an on-demand skill cannot carry an always-on effect and dia-skopos holds for approval, so a wrong guess is corrected first. (D46)
- A review cannot be relied on to read in the result behind a well-specified request, since no text tried did so reliably, which is why it also asks for the result in the user's own sentence. (D114)
- The review never says what form the work for the result will take, where it will stay, or what of the thing asked for it keeps or drops, because on a closely-following model those promises became limits and the work left no plan file. (D115)
- The review states that work for the result stops before changing anything existing that the user's words do not point to, even where undoable, because under dia-techne's undo test alone the work changed the user's other files once it kept a copy. (D126)
- If a run shows a review that stated the stop and work that passed it, the remedy is a clause in the hand-over of Their word naming the stops the review stated, not another wording of the stop. (D126)
- Not done: rewording the exception in dia-skopos's proposal sentence to keep the work off the user's other files, because two rewordings did not differ from the released text; the cause was the missing stop. (D126)
- Not done: removing "and say what would most limit it" from the review's result item, because in recorded reviews that line carried the user's choice. (D123)
- Not done: a sentence exempting a task about dia-skopos's own text from the review, because an exception for maintaining the skill is not its purpose, and this repository's text is edited by sessions under `AGENTS.md`, not through dia-skopos. (D127)
- Not done: restoring D72 (3)'s sentence that ends dia-skopos's review after the task it was invoked for, because the released text, with no such sentence, did a later unrelated task at once with no review in 2 of 2 runs (probes Part CK). (D127)

dia-techne
- dia-techne names the mechanism for ending a process (only one the run started, by its id, never by name), because a sentence of principle did not stop runs from ending processes by image name. (D114)
- Not done in dia-skopos and dia-techne: labelled lines quoting the user's words, fixed forms of the outcome, ordered cases, case rulings on running, and marks by evidence class, because bodies written from purpose without them gave the same results. (D114) The copy's place and the commit as the copy (D63's ruling) came back in D131, as conditions the model can see, because without them the copy was left in the user's folder.
- dia-techne keeps its copy of a changed file in a new folder next to the repository the given folder lies in (next to the folder where none holds it), and beside the file only where that new folder cannot be made; where the last commit holds the file as it stands, that commit is the copy, and the removal rule spares the copies. Under "keep a copy" and "remove before you report whatever you put anywhere else" alone, the user's folder was the copy's only place, and the copy was left in the site folder in 39 of 39 runs (probes Parts CI, CL, CM) and in a repository's working tree in 2 of 2 (Part CO). (D131)
- Not done: a copy "outside the folder" with no place named, or in a temporary folder, because the copy may be the only way back and a temporary folder does not last, and an open place lets a dated folder in a shared parent be written over; nor a condition on what uses the folder (published, deployed, committed), which asks the model to judge where the named place gives it a fact to check. (D131)
- Not done: stopping, in dia-techne's Acting, "a change beyond the request" to "a file or other thing of the user's that the request does not point to" until the user's word, because the model reads "beyond the request" as what the user's words did not ask for, even a fix the requested edit makes necessary: it held the caller, the test and the generated file that the requested interface change broke, and left her project failing in 3 of 4 runs (probes Part CP). A stop on the user's other things must carry in its own words that what the requested edit makes wrong is part of the request; the plan held that ground and the text did not. (D132)
- Not done: a search in dia-techne's check for each place that states a changed value or one that follows from it, because it could not be shown better than the released text. After a review the released work listed what the review named, and the fault showed once in 6 pairs, where a review placed the line loosely (probes Part CL). Invoked directly, the work changed every page, the derived one included (5 of 5, Part CM), so the fault's condition did not arise there. (D128, D129)
- Not done: moving dia-techne's "say when a claim rests on recall" out of its tool-conditioned list, or conditioning it on a figure's origin, because the move changed nothing and the fault was left with the assistant's unshown statements, whose cause is unnamed. (D125)

dia-warrant
- Not done: further wording against dia-warrant conceding what is not shown in text to send (an "even if" form, a changed sentence on standing), because neither changed the rate; it is left as the model's own, with the judgment unaffected. (D124)

#### dia-panel

- The comparison prompt asks for each judge run's statement of what its rulings leave of the target's conclusion word for word, every line of it, because asked for a run's line word for word it copied only the first sentence and paraphrased the rest. (D112)
- The review panel imposes no shared findings table on its lenses ("not a summary and not a findings table"), because under a findings table the caller imposed the lenses carried out their method in full and in scope far less often than without one. (D64)
- Not done for review panels: an environment step in each lens, because noticing a missing `.git` needs harness knowledge the reviewed text does not hold; nor a shared context pack, because leaving out a lens saves more than a pack. (D64)
- Not done: hiding dia-panel from Codex's plugin listing, because the field that would hide it fails `claude plugin validate --strict`; installing it on Codex adds nothing, since Codex runs no Claude Code workflows. (D69)

### 3.2 Decision rows from D127

A decision adds its row here and changes the lines of §3.1 it affects, in the same commit. A row records what was decided, why, what was run and the owner's words; §3.1 carries only what binds. When this section is next cleaned, its rows move to `docs/history/` as D1 to D126 did.

| # | Decision |
|---|---|
| D127 | Spec §3 split into the rulings in force and the decision rows, and D72 (3) ruled; no skill changed (owner, 2026-11-25: of the spec, "spec.md 가 릴리즈가 계속되면서 쌓였는데 정리가 되지 못한 상태야. 낡고 잘못었다면 과감하게 제거하고 싶어.", and to the plan that moves the rows instead of deleting them, "권고대로"; of D72 (3), to the session's recommendation, "너의 추천대로 하겠다."; branch `spec-rulings-in-force`). The split: §3 held 125 rows, 60,041 of the spec's 63,012 words; later rows corrected earlier ones, and nothing listed what was current. The rows moved unchanged to `docs/history/decision-log-to-5.4.1.md`, with an index of the rows later rows corrected or reversed. §3.1 lists what binds, one line each with its reason, written from a classification of every row against the current files: four sub-agents (opus, effort high), their 250 quotes checked by script, every line read by the session, then one independent review, four of whose five findings were taken (the fifth, on the memory note, did not apply). Left out of §3.1 as not in force: D41's note on the source of dia-regula's draft; D53's held-out case set, unused since D85; D72's "no body gives examples of a host's invocation syntax", since dia-router now gives such examples to start reviewers; D71's language line, moved to §6 L6, which is corrected for D125. Taken from the review: the wait conditioned on a fact (D123) stands under dia-reductio, where it was shown, not under all skills; the rename-as-minor-version clause goes with its reason (D30); a reference to "the §3 rows" is repointed; D64's ruling against a findings table for the lenses gets its line. D72 (3): dia-skopos's sentence "Beyond the task this skill was invoked for and its direct follow-ups, the review is over: any later task is done without this skill, unless the user invokes the skill again, because the skill's text stays in the conversation. A task about this skill's own text is done without the review." held in Part AZ (a later unrelated task done at once, the skill's own text done without a review) and was dropped by the D114 rewrite, which does not list it among its reversals. Its second half is not restored (§3.1, dia-skopos). Its first half is checked before anything is written: one cell of 2 runs on the released 5.4.1, claude-opus-5-5 at effort medium (probes Part CK): `dia-skopos` with a task, "Go ahead.", then an unrelated task. If both runs do the later task with no review and no request for approval, the text stays and §3.1 records that; if either reviews it, the cause is the scope word in "Before any work", which is narrowed ("Before the work you were invoked for") rather than the sentence restored, and that wording gets 2 runs before any release. |
| D128 | dia-techne's check is not changed on the runs of probes Part CL (owner, 2026-11-25: of the plan for the places a change touches, "계획을 리뷰하고 진행해 줘", and of the plan as revised after its review, "수정 계획대로 실행"). The candidate added to the check a search of the material and the folder for each place that states a changed value or one that follows from it, a list of those that still disagree with the result, and where it could not search (69 words, none removed); it was meant for the fault Part CJ traced, a list of places that missed the FAQ's deposit sentence because nothing looks for what follows from a changed value. Four sub-agent reviews, each finding put to a refuter, kept the text and changed the design: both arms load the same dia-skopos, whose first search shows the deciding line by chance, so each review was run once and continued under each build, and the rule became an exact two-sided McNemar test on the pairs (p ≤ 0.05 for the candidate within 10 pairs). After 6 pairs every review had named the line, the released work listed it in 5 and the candidate in 6 (1 pair for, 0 against), so the rule could not be met and the batch stopped. Nothing the candidate could cause went wrong: the named file alone changed in 5 of 6 under each build (in pair 2 both changed all four files, as the review's own "as asked" option said), the other places were listed in every reply, nothing was sent, and the bare proceed changed only the named file. Seen and outside the rule: the candidate said where it could not search in 5 of 6 as-asked replies, the released text in 0 of 6. The fault still shows under the released text (one pair), so the places item stays open; with the review in front on this task the review names the line almost always, so the check's effect shows in few pairs and cannot reach the rule within 10 pairs, and the next test is dia-techne where no review names the places. A test of the work after a review holds the review fixed (§3.1, Evaluation). |
| D129 | The places item is closed and dia-techne's check stays as released (owner, 2026-11-25: to the plan for dia-techne invoked directly, with the rule that a released text listing the line in 3 or more of 5 closes the item, "승인하고 실행"). Probes Part CM: `s-asked` with `dia-techne --aim=request` in front, 5 released and 5 candidate runs, one turn each. In 10 of 10 the work changed all four pages, the FAQ's deposit among them, nine replies naming it as following from the fee; the released runs' closing search named the old deposit in 5 of 5. By the rule the fault does not show on direct use. With Part CL: after a review the work lists what the review names, and the fault showed once in 6 pairs, where a review placed the line loosely; at that rate a batch of 10 pairs would be unlikely to reach the rule, though Part CJ's reviews named the line less often (4 of 15), so the rate is not settled; and §3.1 (D118) releases only what is shown. The target that only the named page changes held in 0 of 10 under both builds: the work went to the other pages with no review in front, each reply marking them as beyond the request, though dia-techne treats `--aim=request` as it treats approval "as asked", under which the work had stayed on the named page (Part CJ 4 of 4, Part CL 5 of 6). The cause is not traced; it may be the one D126 named (dia-techne's undo test alone, with no stop stated at the user's other files), which D126 put in dia-skopos's review only. It is carried in the handoff as seen and left. |
| D130 | The wait in dia-conjecture and dia-adjudicate stays as written (owner, 2026-11-25: "다음 진행" for the next item in the order he approved, and to the plan as revised after its review, "수정 계획대로 실행"). The prompt audit had flagged that both wait on "nothing is drafted or recommended that an answer could overturn", the form D123 found did nothing in dia-reductio. The first plan counted a course or a draft given beside a question whose answer could change it. Its review (two sub-agents, each finding put to a refuter) showed that on `nconjecture`, where the user's facts confirm the files' course, that measures whether a step was kept, not what the user is left with; that the plan misread the earlier `nadjudicate` runs; and that its candidate gated more than dia-reductio's form. The revised plan read the outcome: whether a course or a figure given before the user's answers is one her answers overturn. Probes Part CN, the released 5.4.1 on `nconjecture` and `nadjudicate` (Part CA's tasks), 2 runs each, the dialogue to its end: no such course in 4 of 4, and the final course matched the key in 4 of 4. Every course given before the answers that an answer could change came by case or with its assumption stated, as the skills' sentence on what is not known asks, and what was made for the user to pass on carried its condition; the verdicts given without one were ones no answer could overturn. Not run: a task in which a course given by case would leave the user in a case it got wrong. Seen and left: neither `nadjudicate` run started dia-adjudicate's second run after overturning a report on the quote's own words (0 of 2; Part CA's runs on the task, 3 of 3). |
| D131 | Plugin 5.4.2: dia-techne 4.2.3 keeps its copy of a changed file outside the user's folder, and dia-ratchet 3.0.3's reference names no product. Owner, 2026-11-25: to the plan as revised after four reviews, "승인하고 실행"; in the same answer he judged Part CM's direct use a fault ("결함이다"), for a plan of its own after this release; to the results and the release proposal, "권고대로 진행". Branch `techne-copy-5.4.2`; probes Part CO; batch folder `C:/Users/ajitta/work/dia-probes/copy-2026-11-25/`. Versions: dia-techne 4.2.3, dia-ratchet 3.0.3; the other twelve skills as in D126. (1) dia-techne, Acting, two sentences, 58 words added, none removed. "Before changing or deleting a file of the user's, keep a copy and say where it is." became "... keep a copy of it in a new folder next to the repository the folder you were given lies in, or next to that folder where it lies in none, or beside the file where that new folder cannot be made, and say where it is; where the file as it now stands is in the last commit, that commit is the copy." "remove before you report whatever you put anywhere else" became "..., and, except those copies, remove before you report ...". The fault: every recorded work turn of `s-asked` that changed a file left the copy inside the user's site folder (Parts CI, CL, CM: 39 of 39), and 36 replies asked her to keep it out of the push, a git task she has never done. The cause: the copy must outlast the report, and the removal rule let nothing outside the folder do so. D114 had dropped D63's commit-as-backup with the other case rulings; on its merits that drop removed the copy's place and its link to the history, and this row puts both back as conditions the model can see. The wording went through four forms, each reviewed by sub-agents with a refuter per finding (`review-1.json` to `review-4.json`). An open "outside" was dropped because a temporary copy does not last and a refused write had no result. "Not in a temporary folder" was dropped because an open place in a shared parent can be written over. "Next to the folder" became "next to the repository", because a package's sibling folder is taken up by its repository. "Where nothing outside can be written" became "where that new folder cannot be made". "The version history holds it unchanged" became "the last commit", because `git status` shows nothing for an ignored file. Runs, Part CO: claude-opus-5-5 at effort medium, Claude Code 2.1.332, `dia-techne --aim=request` with the persona's first message, 11 runs, US$4.05. Site folder not under version control: copy kept outside, released 0 of 2 (with Part CM's 5, 0 of 7), candidate 2 of 2, in a new folder beside it and named in the reply (Fisher exact, two-sided, 0.028). Repository with an uncommitted edit: released 0 of 2 (untracked backups in the working tree), candidate 2 of 2 (nothing left in the repository, the edited file copied with the edit, the edit kept, one reply naming the commit for the rest). Writes outside refused: the work done with a copy beside the files, released 1 of 1, candidate 2 of 2. Held only in part: the seeded folders of other work beside the folder were unchanged in 6 of 6, but no run checked that its new folder did not exist. In 4 of 6 the first pick was the seeded name, and only a failed `mkdir` (2) or Claude Code's refusals (2) kept it from writing there. The released text has the same risk inside the folder for a second session on the same day. On a host that refuses the new folder the copy still lands inside the folder; the prepared copies of the review flow are not reached. (2) dia-ratchet's `references/verification-sources.md`: "(for example Context7)" removed from the row on library APIs, against D14 (no product named); a form change, given the release review and no run. Checks: `tools/package.py --check`, 28 tests and `claude plugin validate --strict` pass, and `plugins/dia/skills/dia-techne/SKILL.md` equals the text the candidate runs loaded apart from its version line. Not run: claude-fable-5-2; any surface other than Claude Code; an interactive session; a subfolder of a repository; a repository where the new folder cannot be made (D63's case); an ignored file the work changes; the work after a dia-skopos review; dia-techne for the result. |
| D132 | dia-techne is not changed on the runs of probes Part CP: the stop on changes beyond the request is not released (owner, 2026-11-25: of Part CM, "결함이다", to the plan as revised after three reviews, "다음 세션에서 실행"; and, on 2026-11-26, to the results with the recommendation not to release and to bring one plan for both faults of Acting, "추천대로"). Batch folder `C:/Users/ajitta/work/dia-probes/scope-direct-2026-11-25/` (`PLAN.md` with what happened). The candidate (`C:/Users/ajitta/work/pg/dia`, 5.4.2 with two Acting sentences changed, 74 words added) extended "What the user has not allowed stays undone even when the outcome would be served by it" with "and so does a change beyond the request that you would make in this session to a file or other thing of the user's that the request does not point to: prepare it in a new folder of its own next to the repository or folder, or in your reply where that cannot be made; say where it is and what it would change; and leave it for the user's word", and spared prepared changes from the removal rule. Runs: claude-opus-5-5 at effort medium, Claude Code 2.1.332, one turn, 22 of the 24 planned (cell D not run, the answer being clear), none void, US$7.69. On `s-asked` with `--aim=request` the candidate changed only the named page in 5 of 5 runs against 0 of 5 released (Fisher exact, two-sided, 0.008), put the sign-up form first among the changes it held and named every other place (5 of 5), and held the same in work for the result (2 of 2) and in a clean repository (2 of 2, the commit named as the copy). On a new code task (a flower shop's `fees.py`; the requested free-delivery rule changes `delivery_fee`'s arguments, so its test, its only caller and a page generated from it must change too) the candidate left those three for the user's word in 3 of 4 runs, with `fees.py` changed: in her folder the tests and the README's check failed and her payment messages crashed with a TypeError; the released text applied them in 2 of 2 (and also changed a hand-written auto-reply the request did not need). The diagnosis (three readers, 15 causes, each put to a refuter; 13 upheld in part, 2 refuted): the model reads "beyond the request" as what her words did not ask for, even a fix the requested edit makes necessary; the released replies already filed the broken caller as beyond the request and applied it, and the candidate turned that label into a hold ("does not point to" read as "not the file she named" agrees, and is not shown to decide). The plan's ground, that a file the requested edit makes wrong is part of the request, was in the plan only. Also seen: in 2 of 5 candidate runs of cell A (2 of 9 candidate `s-asked` runs) a `mkdir -p` on an existing `project-backup-<date>` beside the folder overwrote another site's file there, and both replies said the existing files were not touched; that is the released copy sentence's open item (D131), shared by both builds (first name asked for was an existing folder in 12 of 21 runs; a failing plain `mkdir` saved 9). Not run: cell D; claude-fable-5-2; any surface other than Claude Code. |

## 4. Names and identifiers

| Item | Value |
|---|---|
| Repository | `ajitta/dialectic-skills` |
| Marketplace name (`.claude-plugin/marketplace.json`) | `dialectic-skills` |
| Plugin `name` (namespace prefix) | `dia` |
| Plugin `displayName` | `Dialectic Skills` |
| Upload zip | `releases/dialectic-skills.zip` |
| Claude Code install | `/plugin marketplace add ajitta/dialectic-skills`, then `/plugin install dia@dialectic-skills` |

The plugin `name` is the only field that sets the namespace. `displayName` is shown in the UI and is not used for namespacing or lookup. A marketplace entry may carry a different name, but components are still namespaced under the manifest `name` ([Claude Code plugin manifest reference](https://code.claude.com/docs/en/plugins-reference)). The marketplace entry therefore uses `dia`, the same as the manifest, so that install and invocation names agree.

### Skill names

| New skill | Rebuilt from (reference version) | Claude invocation | Codex / ChatGPT invocation |
|---|---|---|---|
| `dia-skopos` (named `dia-confirm` from 1.1.0 to 1.4.0, D30, D42, and `dia-intent` until 2.0.0, D56) | confirm-intent (installed copy, no version field) | `/dia:dia-skopos` | `$dia:dia-skopos` / `@dia-skopos`, or a message starting `dia-skopos` (1.2.0, D33) |
| `dia-elenchus` | socratic-elenchus 1.3.1 (`superclaude@stable`) | `/dia:dia-elenchus` | `$dia:dia-elenchus` / `@dia-elenchus` |
| `dia-quaestio` (named `dia-brainstorm` until 2.0.0, D56) | socratic-brainstorm 3.3.1 (`superclaude@stable`) | `/dia:dia-quaestio` | `$dia:dia-quaestio` / `@dia-quaestio` |
| `dia-reductio` | reductio (installed copy) | `/dia:dia-reductio` | `$dia:dia-reductio` / `@dia-reductio` |
| `dia-negative` | negative-dialectics (installed copy) | `/dia:dia-negative` | `$dia:dia-negative` / `@dia-negative` |
| `dia-emend` (named `dia-refine` until 2.0.0, D56) | self-refine (installed copy) | `/dia:dia-emend` | `$dia:dia-emend` / `@dia-emend` |
| `dia-ratchet` (named `dia-iterate` until 1.4.0, D39) | recursive-refine, output mode only (installed copy) | a message starting `dia-ratchet`, or `/dia:dia-ratchet` | `$dia:dia-ratchet` / `@dia-ratchet`, or a message starting `dia-ratchet` (1.2.0, D33) |
| `dia-warrant` (1.3.0, D35) | new: `docs/research/candidates/argumentation.md` | `/dia:dia-warrant` | `$dia:dia-warrant` / `@dia-warrant` |
| `dia-conjecture` (1.3.0, D35) | new: `docs/research/candidates/modern-dialectic.md` | `/dia:dia-conjecture` | `$dia:dia-conjecture` / `@dia-conjecture` |
| `dia-counterplan` (1.3.0, D35) | new: `docs/research/candidates/argumentation.md` | `/dia:dia-counterplan` | `$dia:dia-counterplan` / `@dia-counterplan` |
| `dia-router` (1.4.0, D38; named `dia-menu` until 2.0.0, D56) | new: menu and router, no method of its own | `dia`, `dia <name>`, `dia <request>`; `/dia:dia-router` | the same first word; `$dia:dia-router` / `@dia-router` |
| `dia-adjudicate` (1.5.0, D40) | new: `docs/research/dia-adjudicate.md` | a message starting `dia-adjudicate`, or `/dia:dia-adjudicate` | `$dia:dia-adjudicate` / `@dia-adjudicate`, or a message starting `dia-adjudicate` |
| `dia-regula` (1.6.0, D41; named `dia-instruct` until 2.0.0, D56) | new: the owner's writing-for-models draft (`docs/writing-for-models/`) | `/dia:dia-regula` | `$dia:dia-regula` / `@dia-regula` |
| `dia-techne` (1.13.0, D55) | new: `docs/research/dia-techne.md` | a message starting `dia-techne`, or `/dia:dia-techne` | `$dia:dia-techne` / `@dia-techne`, or a message starting `dia-techne` |

Since 2.0.0 (D56) every skill in this table also starts on a message whose first word is its name, and through dia-router (`dia <name> …`, or `dia <request>` for every skill except the four that start only by name); none starts from a natural-language request without one of these.

Naming rules:

- Each name is kebab-case and matches its folder name.
- No name is a prefix of another name. A build check enforces this, because every skill is invoked by first word (D56).

On namespacing outside Claude:

- Codex and ChatGPT invoke skills by `$name` or `/skills` in Codex and by `@` in ChatGPT, or implicitly by description.
- Their documentation does not say whether plugin skills get a namespace. Two skills with the same name are not merged; both appear in selectors ([Build skills](https://learn.chatgpt.com/docs/build-skills)).
- P3 (Codex CLI 0.162.1, n=1) showed that Codex does namespace plugin skills: the plugin route lists them as `dia:dia-<x>`, `$dia:dia-<x>` resolves and `$dia-<x>` does not. `$dia-<x>` is the name only when the skill folder is copied to `~/.agents/skills/`. The Codex column above gives the plugin form.
- The `dia-` prefix inside each name is what keeps the names unique there. In Claude the names appear doubled (`dia:dia-emend`). This is accepted (D9).

Until 1.13.0, natural-language requests were the safe default on mobile (the owner's own finding in `superclaude/portable-skills/README.md`, a single source). Since 2.0.0 (D56) the mobile route is the first word `dia`, which needs no hyphen.

## 5. Skills

What each skill does, its steps, its output and its rules are in its `skills/<skill>/SKILL.md` and that skill's `references/`. They are the only description of its behaviour; this section does not restate them. Every skill starts only on its name as the first word of a message, on an explicit invocation by name, or on a choice by dia-router (D56); the gate sentence of each description says so, and `tests/test_package.py` checks it.

By kind: dia-skopos, dia-techne, dia-emend, dia-ratchet and dia-regula do work; dia-elenchus and dia-quaestio question an idea; dia-reductio, dia-negative, dia-warrant, dia-conjecture, dia-counterplan and dia-adjudicate examine a position or a text; dia-router is the entry point. How each kind is judged is in `AGENTS.md` § Judging a skill.

The per-skill sections that stood here until 5.0.0 (purpose, behaviour by version, required changes from the references) are in `docs/history/spec-sections-to-5.0.0.md`; each skill's history is in the decision rows that name it (`docs/history/decision-log-to-5.4.1.md`, and §3.2 from D127).

## 6. Language policy

- L1. `SKILL.md`, `agents/openai.yaml`, manifests and every file under `references/` except `references/ko/` contain no Hangul. A test enforces this boundary. The Hangul ranges are U+1100–11FF, U+3130–318F, U+A960–A97F and U+AC00–D7FF, the same ranges as `superclaude`'s `test_shipped_plugin_has_no_hangul`.
- L2. Hangul is allowed only under `skills/<skill>/references/ko/`. Those files are shipped.
- L3. `references/ko/` holds Korea-specific context, such as Korean statutes, case law, or institutional and administrative practice. It does not hold Korean translations of the English files.
- L4. Each `references/ko/*.md` file starts with an English header block:

  ```
  Scope: <what the file covers>
  Source: <primary source, URL>
  As of: <YYYY-MM-DD>
  Use when: <the condition under which SKILL.md tells the model to read this file>
  ```

  Laws change, so the `As of` date is required. The skill must tell the user that date when it relies on the file.
- L5. `SKILL.md` names each `references/ko/` file and the condition for reading it, for example: "If the claim turns on Korean law or a Korean institution, read `references/ko/<file>.md`". Otherwise the file is not read. This keeps the default context small.
- L6. Replies follow the user's language. Models mostly do this without being told (D71, probes Part AJ), but a reply can follow English material or English labels instead: a skill that prints fixed English headings says to write them in the user's language (D71), and the five skills remade in 5.0.0 say "Write to the user in their language" since dia-warrant answered a Korean user in English (D125). Which rules remain is in the skill files.
- L7. Descriptions carry no Hangul. A Korean request reaches a skill by its name as the first word (D56); do not reintroduce Hangul to route one.

No skill ships `references/ko/` files (D17); the mechanism of L2 to L5 stays available, and `tools/package.py` enforces its boundary.

## 7. Package format and runtime constraints

### 7.1 Runtime constraints (the "no harness" rule)

The shipped package (`plugins/dia/`, `releases/dialectic-skills.zip` and `releases/dialectic-skills-openai.zip`) contains only:

- `.claude-plugin/plugin.json`, or in the OpenAI zip `.codex-plugin/plugin.json` (§7.4);
- `README.md`, generated from `packaging/plugin-README.md` (D32);
- `skills/<skill>/SKILL.md`;
- `skills/<skill>/references/**/*.md`;
- `skills/<skill>/agents/openai.yaml`;
- in the OpenAI zip only, the listing images `assets/icon.svg` and `assets/logo.svg` (D32).

It must not contain any of the following:

- `scripts/`, `bin/` or `hooks/`;
- `.mcp.json` or `.lsp.json`;
- monitors;
- any executable file;
- any non-text file.

Reasons:

- Hooks and scripts do not run on chat surfaces.
- claude.ai and Cowork do not install a plugin that has a top-level `bin/` directory ([plugin manifest reference](https://code.claude.com/docs/en/plugins-reference)).

No skill instruction may require running a command. Tool use is always conditional ("if a search or code tool is available"). Every skill must complete on a surface with no tools.

These rules cover the `dia` plugin. The companion `dia-panel` (D69), listed in the same marketplace, holds a JavaScript workflow, runs only on Claude Code and is in neither zip.

Prerequisite: claude.ai requires "Code execution and file creation" to be enabled for skills to work, even script-free ones ([Claude Help — skills](https://support.claude.com/en/articles/12512180)). The README states this.

### 7.2 Frontmatter

- Allowed keys: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`.
  - This is the owner's `superclaude/portable-skills/package.py` whitelist. That project found that claude.ai upload fails hard on Claude Code-only keys such as `disable-model-invocation`, `argument-hint` and `when_to_use` (single source: the owner's probe notes).
- `name` matches the folder name. `description` is at most 1024 characters.
- Description form (D56, replacing D37): a label of what the skill does, then the gate sentence "Use only when the message starts with <name>, when the skill is invoked by name, or when dia-router selects it; a request that only sounds like this is not an invocation." dia-router's gate is the first word `dia` on its own. `tests/test_package.py` checks both. Dates, rules, lineage and flags stay in the body. The D37 convention is in the history file.
- `metadata`: `author: ajitta`, `version`, `lineage`, `source`.
- `license: MIT` (D18).
- Body length guideline: at most 200 lines, the `superclaude` validator limit. Longer material goes in `references/`.

### 7.3 `agents/openai.yaml` (Codex / ChatGPT)

One per skill:

```yaml
interface:
  display_name: "<Display Name>"
  short_description: "<one line, 25–64 characters>"
  default_prompt: "Use $dia:dia-<x> to <action>: "
policy:
  allow_implicit_invocation: <true|false>
```

| Skill | `allow_implicit_invocation` | Reason |
|---|---|---|
| dia-skopos | true | First word or explicit name; the description gates it (D33, D56) |
| dia-elenchus | true | Listed so its name works as a first word (D33, D56) |
| dia-quaestio | true | Listed so its name works as a first word (D33, D56) |
| dia-reductio | true | Same as the reference (no yaml, default true); first word since D56 |
| dia-negative | true | Same as the reference (no yaml, default true); first word since D56 |
| dia-emend | true | Listed so its name works as a first word (D56) |
| dia-ratchet | true | First word or explicit name; the description and the body gate it (D33; named dia-iterate until 1.4.0, D39) |
| dia-warrant | true | Listed so its name works as a first word (D35, D56) |
| dia-conjecture | true | Listed so its name works as a first word (D35, D56) |
| dia-counterplan | true | Listed so its name works as a first word (D35, D56) |
| dia-router | true | First word `dia`; the description gates it, and full skill names stay with their skills (D38, D56, D57) |
| dia-adjudicate | true | First word or explicit name; the description gates it, and the body did as well until 5.0.0 (D40, D118) |
| dia-regula | true | Listed so its name works as a first word (D41, D56) |
| dia-techne | true | First word or explicit name; the description and the body gate it (D55) |

`allow_implicit_invocation` defaults to `true`. When it is `false`, explicit `$skill` invocation still works ([Build skills](https://learn.chatgpt.com/docs/build-skills)), but the skill is left out of the model-visible list (P3), so a message that starts with its name cannot reach it. All skills are `true` since 1.2.0 (D33), and the three added in 1.3.0 too (D35), dia-menu (D38), dia-adjudicate (D40), dia-instruct (D41) and dia-techne (D55); explicit-only skills are gated by wording, as on Claude.

### 7.4 Manifests

- `.claude-plugin/plugin.json`:
  - `name: dia`, `displayName: Dialectic Skills`, `version`, an English `description`, `author`, `license`, `homepage`, `repository`.
  - No `skills` key, because `skills/` is scanned by default.
- OpenAI manifest: only in `releases/dialectic-skills-openai.zip`, as `.codex-plugin/plugin.json`, generated from `plugin-manifest.json` and `packaging/openai/interface.json` (D32). `plugins/dia/` carries no portable root `plugin.json`; Codex and ChatGPT desktop load it through the marketplace (P3).
- `.claude-plugin/marketplace.json` at the repository root:
  - `name: dialectic-skills`;
  - two plugin entries: `dia` with source `./plugins/dia`, and the companion `dia-panel` with source `./companions/dia-panel` (D69).
  - ChatGPT desktop reads this file as a legacy-compatible marketplace (same OpenAI page).

### 7.5 Source folders stay plain skills

`skills/<skill>/` in the repository source contains no `.claude-plugin/`, `.codex-plugin/`, `skills/` or `bin/`. The manifest lives in `plugin-manifest.json` and is injected only into the generated `plugins/dia/`.

The reason, from the owner's probe notes (single source, Codex 0.160 and Claude Code 2.1.292):

- A manifest inside a skill folder makes Codex register it as `<name>:<name>` and breaks `$skill`.
- Claude Code then loads it as a `skills-dir` plugin instead of a plain skill.

## 8. Repository layout

```
dialectic-skills/
├── skills/                          source: the plain skills
│   └── dia-<x>/
│       ├── SKILL.md
│       ├── references/*.md          optional
│       └── agents/openai.yaml
├── plugin-manifest.json             source for the plugin manifests
├── plugin-release.json              digest record for the current version (not shipped)
├── packaging/                       source: plugin README, OpenAI listing fields and images (D32)
├── .claude-plugin/marketplace.json  marketplace "dialectic-skills" -> ./plugins/dia and ./companions/dia-panel
├── plugins/dia/                     generated, shipped (committed)
├── releases/                        generated, shipped (committed): dialectic-skills.zip, dialectic-skills-openai.zip
├── companions/dia-panel/            Claude Code-only companion workflow, hand-maintained (D69), in neither zip
├── tools/package.py, tests/         developer-only
├── upstream/                        read-only provenance (§11), never shipped
├── docs/                            this decision record, handoff, probe records, research and history; never shipped
├── site/                            project page (GitHub Pages)
├── README.md and three translations
└── LICENSE
```

## 9. Distribution and invocation by surface

Install routes are in `README.md` § Install, and the owner's observations of where an install shows up are in `docs/handoff.md` § Install surfaces. On every surface a skill starts on its name as the first word of a message, on `dia` followed by its name or a request, on `/dia:dia-<x>` in Claude, or on `$dia:dia-<x>` in Codex (§4). The 1.0.0 table of routes by surface is in `docs/history/spec-sections-to-5.0.0.md`.

## 10. Migration (done)

A one-time step of 1.0.0: the owner's earlier installs were replaced by `dia`. Its text is in the history file.

## 11. Bootstrap (done)

A one-time step of 1.0.0: the material the first skills were rebuilt from was imported into `upstream/`. It stays there as read-only provenance (`AGENTS.md`), never shipped, and is not a baseline for current behaviour. The steps are in the history file.

## 12. Verification and acceptance

### 12.1 Build checks

`tools/package.py --check` runs the checks below except the two marked *tests* (in `tests/test_package.py`) and the one marked *CI* (`.github/workflows/check.yml`); run all three before a release.

- Allowed and forbidden frontmatter keys (§7.2). `name` matches the folder. Description length.
- No skill name is a prefix of another (§4).
- Hangul boundary (L1, L2).
- Forbidden paths and files in the shipped output (§7.1), and no `upstream/` path.
- `plugins/dia/` and both zips in `releases/` match the source byte for byte. Reproducible zip: fixed timestamps, modes and `create_system`, LF line endings, and stored entries (D15).
- Version rule: changed skill files under an unchanged plugin `version` fail. This is the `plugin-release.json` digest rule carried over from `superclaude`. Claude Code updates an installed plugin only when its version changes.
- Cross-references: every skill name mentioned exists, and no former name is used. No skill file offers a menu number after `dia`, and the READMEs and the site show no retired way to name a skill (D77).
- *Tests:* every description carries its gate sentence (§7.2), and the README translations keep `README.md`'s structure (D31).
- `companions/dia-panel` has the same version in its `plugin.json` and its marketplace entry.
- *CI:* `claude plugin validate --strict plugins/dia` passes.

### 12.2 Probes and runs

Rules for runs are in `AGENTS.md` § Probes and evals; results are in `docs/probes.md`. The surface probes P1 to P8 and the acceptance of 1.0.0 that stood here are in `docs/history/spec-sections-to-5.0.0.md`.

## 13. Open items

Open items are kept in `docs/handoff.md`, not here.


## 14. Sources

- Claude Code — Plugin manifest reference: https://code.claude.com/docs/en/plugins-reference
- Claude Help — Skills (zip upload, code-execution requirement): https://support.claude.com/en/articles/12512180
- OpenAI — Build plugins: https://developers.openai.com/plugins/build/plugins
- ChatGPT / Codex — Build skills: https://learn.chatgpt.com/docs/build-skills
- OpenAI Help — Plugins in ChatGPT and Codex: https://help-lb.openai.com/en/articles/20001256
- OpenAI Help — Skills in ChatGPT: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- Owner's prior work (single source): `ajitta/superclaude` at `stable` 47f791b — `portable-skills/README.md`, `portable-skills/package.py`, `docs/features/portable-skills-single-plugin/`
