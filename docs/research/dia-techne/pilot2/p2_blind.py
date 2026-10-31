import random, json, pathlib
root = pathlib.Path("/home/claude/exp/p2")
def r(q, a): return (root/f"runs/{q}_{a}/reply.md").read_text(encoding="utf-8")
def after(text, marker):
    i = text.index(marker); return text[i+len(marker):].lstrip()
pairs = {
  "Q1": (r("Q1","A"), r("Q1","B")),
  "Q2": (after(r("Q2","A"), "**Result:**"), r("Q2","B")),
  "Q3": (r("Q3","A"), r("Q3","B")),
  "Q4": (after(r("Q4","A"), "**결과:**"), r("Q4","B")),
}
rng = random.Random(311)
key = {}
for q, (a, b) in pairs.items():
    flip = rng.random() < 0.5
    x, y = (b, a) if flip else (a, b)
    key[q] = {"X": "B" if flip else "A", "Y": "A" if flip else "B"}
    (root/f"blind/{q}_X.md").write_text(x, encoding="utf-8")
    (root/f"blind/{q}_Y.md").write_text(y, encoding="utf-8")
pathlib.Path("/home/claude/exp/scripts/p2_key.json").write_text(json.dumps(key), encoding="utf-8")
for p in sorted((root/"blind").iterdir()): print(p.name, len(p.read_text(encoding="utf-8")))
