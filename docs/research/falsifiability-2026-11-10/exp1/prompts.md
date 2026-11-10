# Agent launch prompts (exp1)

Verbatim first message given to each sub-agent, extracted from the session log after the fact. The serving model is the one recorded in that agent's log. Absolute paths point at the original session's scratch folder; in this repository the same files sit beside this file. Later turns (relayed user replies) are in `relay-log.md` and the transcripts.

## Arm A input 1

Model: `claude-opus-5-5`

````text
You are a helpful general-purpose assistant in a chat with a user. Do not use the Skill tool, do not read any files, and do not search the web. Reply to the user's message as you normally would, in the user's language. Your final message must be ONLY your reply to the user (no notes to anyone else). The user may send further messages later.

User message:
「이 약은 편두통 발작 빈도를 줄인다」는 내 주장인데, 뭘 보면 틀렸다고 할래? 반증 가능한 주장이야?
````

## Arm A input 2

Model: `claude-opus-5-5`

````text
You are a helpful general-purpose assistant in a chat with a user. Do not use the Skill tool, do not read any files, and do not search the web. Reply to the user's message as you normally would, in the user's language. Your final message must be ONLY your reply to the user (no notes to anyone else). The user may send further messages later.

User message:
「시장은 잘못된 가격을 결국 교정한다」는 내 주장인데, 반증 가능해?
````

## Arm A input 3

Model: `claude-opus-5-5`

````text
You are a helpful general-purpose assistant in a chat with a user. Do not use the Skill tool, do not read any files, and do not search the web. Reply to the user's message as you normally would, in the user's language. Your final message must be ONLY your reply to the user (no notes to anyone else). The user may send further messages later.

User message:
「우리 고객 데이터에 숨은 패턴이 있다」는 내 가설인데, 반증 가능해?
````

## Arm B input 1

Model: `claude-opus-5-5`

````text
You are the assistant in a chat with a user. The user's message starts with `dia`, which invokes the dia plugin. Use ONLY the copy of the plugin at /tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/exp/dia-B (do NOT use the Skill tool for any dia skill, since the installed copy differs). Read /tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/exp/dia-B/skills/dia-router/SKILL.md and follow it; it loads the chosen skill by reading ../dia-<x>/SKILL.md relative to itself, and follow that skill (and its references when it says to) exactly as written. Do not read any other file outside that dia-B folder, and do not search the web unless a loaded skill tells you to. Your final message must be ONLY your reply to the user, exactly as the skill says to reply (no notes to anyone else). The user may send further messages later; continue following the same skill then.

User message:
dia 「이 약은 편두통 발작 빈도를 줄인다」는 내 주장인데, 뭘 보면 틀렸다고 할래? 반증 가능한 주장이야?
````

## Arm B input 2

Model: `claude-opus-5-5`

````text
You are the assistant in a chat with a user. The user's message starts with `dia`, which invokes the dia plugin. Use ONLY the copy of the plugin at /tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/exp/dia-B (do NOT use the Skill tool for any dia skill, since the installed copy differs). Read /tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/exp/dia-B/skills/dia-router/SKILL.md and follow it; it loads the chosen skill by reading ../dia-<x>/SKILL.md relative to itself, and follow that skill (and its references when it says to) exactly as written. Do not read any other file outside that dia-B folder, and do not search the web unless a loaded skill tells you to. Your final message must be ONLY your reply to the user, exactly as the skill says to reply (no notes to anyone else). The user may send further messages later; continue following the same skill then.

User message:
dia 「시장은 잘못된 가격을 결국 교정한다」는 내 주장인데, 반증 가능해?
````

## Arm B input 3

Model: `claude-opus-5-5`

````text
You are the assistant in a chat with a user. The user's message starts with `dia`, which invokes the dia plugin. Use ONLY the copy of the plugin at /tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/exp/dia-B (do NOT use the Skill tool for any dia skill, since the installed copy differs). Read /tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/exp/dia-B/skills/dia-router/SKILL.md and follow it; it loads the chosen skill by reading ../dia-<x>/SKILL.md relative to itself, and follow that skill (and its references when it says to) exactly as written. Do not read any other file outside that dia-B folder, and do not search the web unless a loaded skill tells you to. Your final message must be ONLY your reply to the user, exactly as the skill says to reply (no notes to anyone else). The user may send further messages later; continue following the same skill then.

User message:
dia 「우리 고객 데이터에 숨은 패턴이 있다」는 내 가설인데, 반증 가능해?
````

## Arm C input 1

Model: `claude-opus-5-5`

````text
You are the assistant in a chat with a user. The user's message starts with `dia`, which invokes the installed dia plugin: load the skill `dia:dia-router` with the Skill tool and follow it, and the skill it selects, exactly as written. Do not read files under /home/claude or /tmp, and do not search the web unless a loaded skill tells you to. Your final message must be ONLY your reply to the user, exactly as the skill says to reply (no notes to anyone else). The user may send further messages later; continue following the same skill then.

User message:
dia 「이 약은 편두통 발작 빈도를 줄인다」는 내 주장인데, 뭘 보면 틀렸다고 할래? 반증 가능한 주장이야?
````

## Arm C input 2

Model: `claude-opus-5-5`

````text
You are the assistant in a chat with a user. The user's message starts with `dia`, which invokes the installed dia plugin: load the skill `dia:dia-router` with the Skill tool and follow it, and the skill it selects, exactly as written. Do not read files under /home/claude or /tmp, and do not search the web unless a loaded skill tells you to. Your final message must be ONLY your reply to the user, exactly as the skill says to reply (no notes to anyone else). The user may send further messages later; continue following the same skill then.

User message:
dia 「시장은 잘못된 가격을 결국 교정한다」는 내 주장인데, 반증 가능해?
````

## Arm C input 3

Model: `claude-opus-5-5`

````text
You are the assistant in a chat with a user. The user's message starts with `dia`, which invokes the installed dia plugin: load the skill `dia:dia-router` with the Skill tool and follow it, and the skill it selects, exactly as written. Do not read files under /home/claude or /tmp, and do not search the web unless a loaded skill tells you to. Your final message must be ONLY your reply to the user, exactly as the skill says to reply (no notes to anyone else). The user may send further messages later; continue following the same skill then.

User message:
dia 「우리 고객 데이터에 숨은 패턴이 있다」는 내 가설인데, 반증 가능해?
````

## Blind grader of transcripts

Model: `claude-fable-5-2`

````text
You are a blind grader. Read ONLY the nine files /tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/exp/blind/T1.md … T9.md. Do not open any other file in that scratchpad (in particular not key.txt, protocol.md, relay-log.md, or the t/ or dia-B folders), do not search the web, and do not edit anything except your output file.

Each file is one chat between a user and an assistant about whether a claim is falsifiable. The user's replies were produced by fixed scripted rules, so judge only the assistant's messages. Some assistants used a structured method and some did not; ignore style and length and score only the criteria below.

Inputs: files whose claim is about a migraine drug are I1; about markets eventually correcting prices are I2; about a hidden pattern in customer data are I3.

Scoring (per transcript; 1 = met, 0 = not met, NA = not applicable). For every 1, quote the assistant span (one clause) that meets it; for every 0, say in one line what is missing.
- K1 Form classification correct: I1 statistical — falsifiable only given a decision rule (a threshold/effect size); I2 as worded (no time bound) unfalsifiable by form; I3 unfalsifiable/untestable until "pattern" is defined, testable once defined.
- K2 Asks for or states the need for a decision rule (threshold/effect size) — I1 only.
- K3 Names conditions/auxiliary hypotheses to hold fixed (I1; I3 after definition).
- K4 I2 only: (a) a bounded version is treated as a change to the claim, AND (b) the holder's refusal of every criterion is named as making the claim unfalsifiable/immunized. Score 1 only if both.
- K5 Gives no verdict on whether the claim is true (all).
- K6 Does not record a criterion as agreed unless the user agreed to it (all where a criterion appears; NA if no criterion appears).
Applicable items: I1: K1,K2,K3,K5,K6; I2: K1,K4,K5,K6; I3: K1,K3,K5,K6.

Notes for consistency: K1 for I1 needs the assistant to say the claim becomes falsifiable only once a size/threshold (and comparison) is fixed, not merely "needs a comparison". K1 for I3 needs both halves (untestable as stated; testable once defined). K4(b) requires the refusal to be the user's, so it can be 1 only where the user actually refused a bound or criterion. K5 fails if the assistant says the claim is true or false (saying "unfalsifiable" is not a truth verdict).

Output: a Markdown table T#, input, K1–K6 scores, total of applicable items; then the evidence lines per transcript. Write it to /tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/exp/grades.md and return it in full as your final message.
````
