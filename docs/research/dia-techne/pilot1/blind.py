import random, re, json, pathlib
root = pathlib.Path("/home/claude/exp")
out, blind = root/"out", root/"blind"
def read(p): return (out/p).read_text(encoding="utf-8")

t1a = read("T1_A.md"); t1a = t1a[t1a.index("## 1."):]
t1b = read("T1_B.md")
t3a = (root/"runs/T3_A/notice.revised.md").read_text(encoding="utf-8")
t3b = (root/"runs/T3_B/notice.md").read_text(encoding="utf-8")
t4a = re.search(r"^> (.+)$", read("T4_A.md"), re.M).group(1)
t4b = read("T4_B.md").split("\n")[0]

pairs = {"T1": (t1a, t1b), "T3": (t3a, t3b), "T4": (t4a, t4b)}
rng = random.Random(20261031)
key = {}
for t, (a, b) in pairs.items():
    flip = rng.random() < 0.5
    x, y = (b, a) if flip else (a, b)
    key[t] = {"X": "B" if flip else "A", "Y": "A" if flip else "B"}
    (blind/f"{t}_X.md").write_text(x, encoding="utf-8")
    (blind/f"{t}_Y.md").write_text(y, encoding="utf-8")
(root/"scripts/key.json").write_text(json.dumps(key), encoding="utf-8")
print("written:", sorted(p.name for p in blind.iterdir()))
