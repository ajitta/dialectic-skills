# dia-techne: where the method and the name come from

Read this only when the user asks where the method or the name comes from. The rules are in SKILL.md; this file says what they rest on and where the skill departs from its source. Quotations are from the sources listed at the end.

## 1. The method: Rieseberg's tutorial

Felix Rieseberg's "How to be more ambitious: A tutorial for humans with models" (13 October 2026) sorts ambition into four kinds: "Speed, Altitude, Depth, and Range". It skips speed as well established.

- **Altitude:** "considering the outcome rather than the individual task". The tutorial limits it: it "works best if you really are after some ultimate outcome; it works less well for creative endeavors."
- **Depth:** work on a task "the way a field-leading expert would", touching "the underlying data, tools, and problems". Its depth prompt is the source of questions 1 to 4: "I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that."
- **Range:** draw on other fields, turn nouns into verbs ("A quarterly review isn't 'a deck'. It's 'getting busy people to believe a story about cause and effect, and to decide under uncertainty, in 30 minutes'"), and bring in opposing roles. This is question 5.
- **Outside judge:** "Do not ask the model to judge itself. … insist on outside validation. Ideally that's a tool the model can run to get feedback immediately."
- **No role-play:** "models often switch vocabulary without actually switching methods"; "Don't ask the model to write like a short seller, ask it to do what a short seller does."
- **Challenge what you know:** ask the model "to adversarially check assumptions" against the raw data. This is the tutorial's closest basis for revising a request's stated conclusion.

Not taken: "Pick unreasonable goals" and "Produce new knowledge" (showing a model predicts on data it has not seen) are depth techniques the skill does not ask for by name.

## 2. What the skill adds

These are not in the tutorial, which is written for a person improving their own request:

- The skill runs the rewritten prompt in the same turn, and revises the request's framing, method, stated conclusion and form where the five questions show they would not reach the outcome (the repository owner's decisions).
- In question 4, the option of a separate agent or session that argues the other side. A secondary report of an interview with Rieseberg (Yao Xiao, DEV Community, October 2026) gives "a separate adversarial session when you cannot" use hard outside evidence; the tutorial does not.
- "Deeper not bigger" is read as dropping an answer that adds volume or scope without changing the result, and keeping the request's own choices where practice agrees with them.
- The creative-task branch also skips question 5's restatement; the tutorial limits only altitude.
- Stops, backups, source marks and the report checks (a comparison criterion fixed first, numbers from final values, claims checked against tool output) came from three small pilots in the source repository.

## 3. The name

The name borrows Aristotle's *technē* as a label only. In *Nicomachean Ethics* VI.4 technē is a state of making that involves true reasoning, about things whose origin is in the maker; *Metaphysics* I.1 adds that the person of art knows the why, not only the that. Making, unlike action, has an end beyond itself (NE VI.5), which is why the skill starts from the outcome a request serves and treats a creative task, whose point is the making, differently. The skill does not implement an Aristotelian procedure; its method is Rieseberg's.

## Sources

- Felix Rieseberg, "How to be more ambitious: A tutorial for humans with models", felixrieseberg.com, 2026-10-13. https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/
- Yao Xiao, "Stop Telling Claude to Act Like an Expert", DEV Community, 2026-10-26 (secondary report of an interview). https://dev.to/blobxiaoyao/stop-telling-claude-to-act-like-an-expert-felix-rieseberg-on-costume-prompts-and-skills-debt-2pha
- Aristotle, *Nicomachean Ethics* VI.4–5; *Metaphysics* I.1.
