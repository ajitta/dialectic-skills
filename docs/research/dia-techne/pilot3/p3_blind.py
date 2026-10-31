import random, json, pathlib
root = pathlib.Path("/home/claude/exp/p3")
def reply(t, a):
    s = (root/f"runs/{t}_{a}/reply.md").read_text(encoding="utf-8")
    extra = root/f"runs/{t}_{a}/email_draft.md"
    if extra.exists():
        s += "\n\n---\n[첨부 파일: email_draft.md]\n\n" + extra.read_text(encoding="utf-8")
    return s
rng = random.Random(1101); key = {}
for t in ("R2", "R3"):
    arms = ["A", "B", "C"]; rng.shuffle(arms)
    key[t] = dict(zip("XYZ", arms))
    for lab, arm in key[t].items():
        (root/f"blind/{t}_{lab}.md").write_text(reply(t, arm), encoding="utf-8")
pathlib.Path("/home/claude/exp/scripts/p3_key.json").write_text(json.dumps(key), encoding="utf-8")
for p in sorted((root/"blind").iterdir()): print(p.name, len(p.read_text(encoding="utf-8")))
