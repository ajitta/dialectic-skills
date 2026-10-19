# upstream/

Material the dialectic-skills are rebuilt from (see `docs/spec.md` §11). Never shipped; read-only by convention. Not related to the shipped `skills/<skill>/references/` folders.

- Taken: 2026-10-20
- superclaude commit: `47f791b593cf70ed136eac58932a57b7d83279ca` (branch `stable`, 2026-10-20 00:11:37 +0900)
- SHA-256: over sorted relative paths and file bytes (path, NUL, bytes, NUL), per item; for a file item, the same over that single file.

| Item | Origin | Version | SHA-256 |
|---|---|---|---|
| `installed/confirm-intent` | claude.ai account, installed (synced) copy | unversioned | `b7ea159ff8d4de6c2932d53b23bf67d56f46eae19d955165e6a4514e0cfa2f80` |
| `installed/reductio` | claude.ai account, installed (synced) copy | unversioned | `1b594e742ff886a35ef5e8acb1223551292397bfa44d56a5545b609f1889b5f9` |
| `installed/negative-dialectics` | claude.ai account, installed (synced) copy | unversioned | `2ff6ec502a0bf2faf6687b60ee3845e42936f08e3b07efa6fe1017c1e3b0eab5` |
| `installed/self-refine` | claude.ai account, installed (synced) copy | unversioned | `f523bb388cb16bf50f8239b6833d2bfc383e5c9aba06b7c9ade69edfa2b485ad` |
| `installed/recursive-refine` | claude.ai account, installed (synced) copy | unversioned | `48d02113f8ef0f5ccbdeed454cf9e7232b5131bd929682ae2691da08b6d0f783` |
| `superclaude-stable-47f791b/socratic-brainstorm` | ajitta/superclaude portable-skills/socratic-brainstorm | 3.3.1 @ 47f791b | `fc7459802295d6ba94756c96821a6d2def7ed720aca77df9fdd14ea1c3bc63fd` |
| `superclaude-stable-47f791b/socratic-elenchus` | ajitta/superclaude portable-skills/socratic-elenchus | 1.3.1 @ 47f791b | `c99b204f18b29070cf205dc53909c7f627e20d3b6fd69080bb3493ca75892311` |
| `superclaude-stable-47f791b/package.py` | ajitta/superclaude portable-skills/package.py | @ 47f791b | `6c6da66fdebbb98ee9d16568f5897065be6507c7b60a9388ddd8cafc1a19c8dc` |
| `superclaude-stable-47f791b/README.md` | ajitta/superclaude portable-skills/README.md | @ 47f791b | `7da19e5b0e27625807ed945a52c4ac2ce3bc66249533e5373265d64f3ae4bf56` |
| `superclaude-stable-47f791b/docs-features/portable-skills-single-plugin` | ajitta/superclaude docs/features/portable-skills-single-plugin | @ 47f791b | `5f5af87d7d4499f0cd4fad926f0bd2138073f03d7fbc0455a7a4ac2acfa3aed0` |
| `superclaude-stable-47f791b/docs-features/socratic-brainstorm-skill` | ajitta/superclaude docs/features/socratic-brainstorm-skill | @ 47f791b | `e5a3024ed480c4356502d2fcc906affb0f8c06e70a95a7f745a0d58a83c10017` |

Notes:

- The installed copies were byte-identical to the copies the claude.ai session mounted under `/mnt/skills/plugins/` on 2026-10-20 (checked with `diff -rq`, except confirm-intent, which exists only in the synced folder).
- The superclaude `socratic-*` versions here are newer than the copies installed in the account (3.3.0 / 1.3.0); the spec rebuilds from these.
- `recursive-refine/references/skill-loop.md` documents the skill-folder mode that `dia-iterate` drops (spec §5.7). It is kept here for reference only.
