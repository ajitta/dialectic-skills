# Drafting, corrections, and adjudication

## Request and constraints

The owner asked for actual dia-regula violations with exact quotations, original-file line numbers, and the correct Rule or Structure reference; optional Leads were to remain optional. A complete English revision was requested with the original intent preserved and semantic changes minimized. The analysis was in Korean. The original upstream repository was not to be changed.

The original had four sections: thinking before coding, simplicity, surgical changes, and goal-driven execution. The revision retained those sections, metadata, source link, examples, and principal restrictions. It merged separate scope headings and actions into paragraphs, removed separate slogan repetitions, and supplied reasons. The added reasons were editorial interpretations, not quotations attributed to the original author.

## Findings retained after correction

| Original location | Exact excerpt | Basis |
|---|---|---|
| L17 and L18 | `Before implementing:` followed on another line by `- State your assumptions explicitly. If uncertain, ask.` | Rule 1: condition/scope and the action it gates are on separate lines. Similar cases occur at L39-L43 and L45-L47. |
| L27 | `- No features beyond what was asked.` | Rule 3: no local reason for this instruction. |
| L42 | `- Match existing style, even if you'd do it differently.` | Rule 3: no local reason for this instruction. |

Other exact examples of the Rule 3 category were L28-L30 and L40. These are grouped instances, not an assertion that every bullet or prohibition is defective. The general purpose of reducing coding mistakes does not explain every individual restriction.

L60, `For multi-step tasks, state a brief plan:`, was not counted as a separate Rule 1 violation: its condition and requested action are already on the same line, with a template following it. Sentence length, numbered headings, prohibitions, and examples were not violations merely because of their form. Example-related guidance was classified as a Lead. No distinct Rule 4 or Structure breach was established from this file alone.

## Rule 2 finding withdrawn

The initial report classified L41, `- Don't refactor things that aren't broken.`, as a Rule 2 violation because it could forbid requested refactoring of working code. A draft consequently added an exception when the user's request called for it.

A later dia-emend pass withdrew that classification. Rule 2 warns about scope wording that allows the assistant to widen its permission. The quoted prohibition restricts permission; the absence of a requested-refactoring exception does not by itself establish that particular breach. The refactoring example elsewhere also does not logically imply permission for every kind of refactoring.

The exception was therefore removed from the final draft. Adding it remains a possible policy choice and a semantic change, not a required correction supported by the confirmed findings. This withdrawal was based on the rule's actual wording, rather than on repeated requests for another review.

An early revision also changed the prohibition on improving adjacent code into a prohibition on changing adjacent code at all. A separate reviewer caught that scope expansion; the draft restored the original improvement prohibition. Unnecessary explicit default branches were removed as well.

## Separate-context verification

The later requested verification used the same frozen revision and original snapshot. Each reviewer received its own installed method, the target, and the applicable comparison material, without earlier verdicts or peers' reports. The four reports were:

| Label | Method | Main result |
|---|---|---|
| A | dia-regula 2.2.0 | No confirmed breach; one conditional concern about trivial-task discretion; one optional example-related Lead. |
| B | dia-warrant 2.3.0 | The claim that success criteria support independent work lacked measured behavioral support. Questions remained about exceptions and verification that cannot finish. |
| C | dia-negative 2.2.0 | No strict internal gap in the cases tested; ambiguity or a possible undesirable outcome was not promoted to contradiction. |
| D | dia-emend 2.0.0 | No confirmed correction or missing requirement; upstream attribution and behavioral effects had limits. |

Two further agents independently applied dia-adjudicate 2.2.0 to all four reports. They first inventoried the target and then examined the reports. Neither received the other's verdict. They used the same model as the report writers, in separate contexts.

## Judgments and qualifications

Both judges retained the static conclusion that the core requirements and examples were preserved and found no confirmed defect requiring automatic revision. They distinguished the document's stated purpose from a demonstrated effect.

Both judged report B's definite qualifier finding overstated: an imperative alone does not establish an excessive claim, the target includes `For trivial tasks, use judgment.`, and B's general warrant was its own reconstruction. The separate question about verification that cannot finish remained open. The trivial-task exception was not treated as a complete failure-handling rule.

The judges differed in available source access. The first could not retrieve the linked X post. The second obtained its text through another read-only route; the session assistant subsequently read it too. The post contains qualitative observations about success criteria and repeated agent work. This supports thematic attribution and an experiential background, but not controlled evidence that the rewrite improves performance. Report B's broad absence-of-experience reading must be narrowed when the linked source is included. Its narrower point that measured causal support is missing remains valid.

The source is [Karpathy's linked post](https://x.com/karpathy/status/2015883857489522876). The later successful read does not make report D's truthful record of its earlier 403 response an error. Matching themes also does not prove the entire historical drafting lineage.

The judges' results are static review evidence. They are not proof of correctness, behavior equivalence, or improvement. No revision was applied automatically from the adjudication.

## Document tradeoffs discussed

The original's short slogans and bullets are easy to scan and edit item by item. The revision makes condition/action/reason relationships more explicit, but its longer paragraphs are harder to scan and require care when editing one clause. Adding reasons supplies interpretive material that can also introduce semantic drift; it is not merely a shorter rendering of the same commands.

Excluding YAML frontmatter and trimming outer whitespace, body length was 2,224 characters in the original and 2,618 in the revision, an increase of 17.7%. Removing separate slogans did not substantially reduce the behavioral requirements. Both retained open expressions such as trivial-task judgment, impossible scenarios, and verification until completion. Static readability preferences did not establish a model-performance ranking.
