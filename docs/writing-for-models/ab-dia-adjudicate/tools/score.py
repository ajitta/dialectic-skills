"""Score the dia-adjudicate A/B runs against the answer key.

Usage: python3 -I tools/score.py r1|r2|r3   (run from ab-dia-adjudicate/)

r1 = Opus, local sources (plan.json, out/, key.json)
r2 = Haiku, local sources (plan-haiku.json, out-haiku/, key.json)
r3 = Haiku, summarizing fetch tool (plan-r3.json, out-r3/, key-r3.json, fetchdata/log/)

Needs scipy for the tests; without it, only the per-run table is printed.
"""
import json
import os
import re
import statistics
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ROUNDS = {
    "r1": ("plan.json", "out", "key.json"),
    "r2": ("plan-haiku.json", "out-haiku", "key.json"),
    "r3": ("plan-r3.json", "out-r3", "key-r3.json"),
}
OVERTURN = {"wrong", "overstated"}
# Round 3 only: a target error counts as flagged when some inventory claim matching the
# pattern got "fails" or "partly holds" (keys are the ids in key-r3.json target_errors).
TARGET_PATTERNS = {
    "case3": {"M1": r"4 ?°?C", "M2": r"caus|lowers", "M3": r"will reduce|will", "M4": r"reverse",
              "M5": r"day", "M6": r"desert", "M7": r"every"},
    "case4": {"N1": r"two years", "N2": r"every task", "N4": r"never falls|experience", "N5": r"everything",
              "N6": r"embedded", "N7": r"throughout", "N8": r"mandate"},
}


def load(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return json.load(f)


def usage(outdir):
    path = os.path.join(ROOT, outdir, "usage.csv")
    if not os.path.exists(path):
        return {}
    rows = {}
    for line in open(path, encoding="utf-8"):
        if line.strip():
            run, tokens, tools, secs = line.strip().split(",")
            rows[run] = {"tok": float(tokens), "tools": float(tools), "sec": float(secs)}
    return rows


def main(rnd):
    plan_f, outdir, key_f = ROUNDS[rnd]
    plan, key, arm_of = load("key", plan_f), load("key", key_f), {v: k for k, v in load("key", "mapping.json").items()}
    use = usage(outdir)
    rows = []
    for p in plan:
        run, case = p["run"], p["case"]
        out = load(outdir, run + ".json")
        k = key[case]["report_items"]
        v = {d["id"]: d["verdict"] for d in out["report_items"]}
        traps = key[case].get("summary_traps", [])
        r = {
            "run": run, "case": case, "arm": arm_of[p["skill"]],
            "overturned_valid": [i for i, t in k.items() if t in ("valid", "unverifiable") and v.get(i) in OVERTURN],
            "missed_wrong": [i for i, t in k.items() if t == "wrong" and v.get(i) not in OVERTURN],
            "trap_not_valid": [i for i in traps if v.get(i) != "valid"],
            "valid_to_partly": [i for i, t in k.items() if t == "valid" and v.get(i) == "partly valid"],
            "valid_in_step6": [i for i in out.get("step6", []) if k.get(i) == "valid"],
            "unverifiable_kept": all(v.get(i) == "unverifiable" for i, t in k.items() if t == "unverifiable"),
            "note": out.get("note", ""),
        }
        must = " ".join(out.get("must_check", []))
        r["overturns_routed"] = all(re.search(r"\b" + i + r"\b", must) for i in v if v[i] in OVERTURN)
        if case in TARGET_PATTERNS:
            r["target_not_flagged"] = [
                tid for tid, rx in TARGET_PATTERNS[case].items()
                if not any(c["verdict"] in ("fails", "partly holds") and re.search(rx, c["claim"], re.I) for c in out["target_claims"])
            ]
        log = os.path.join(ROOT, "fetchdata", "log", run + ".log")
        if os.path.exists(log):
            kinds = [line.split("\t")[2] for line in open(log, encoding="utf-8") if line.strip()]
            r["q"], r["fetch"] = kinds.count("Q"), kinds.count("FETCH")
        r.update(use.get(run, {}))
        rows.append(r)

    for r in sorted(rows, key=lambda x: (x["case"], x["arm"], x["run"])):
        print(json.dumps(r))

    try:
        from scipy.stats import fisher_exact, mannwhitneyu
    except ImportError:
        return 0
    print()
    for f in ("tok", "sec", "tools", "q", "fetch"):
        a = [x[f] for x in rows if x["arm"] == "A" and f in x]
        b = [x[f] for x in rows if x["arm"] == "B" and f in x]
        if a and b:
            print(f"{f}: A {statistics.mean(a):.1f}  B {statistics.mean(b):.1f}  Mann-Whitney p {mannwhitneyu(a, b).pvalue:.3f}")
    n = {arm: sum(1 for x in rows if x["arm"] == arm) for arm in "AB"}
    for name in ("overturned_valid", "missed_wrong", "trap_not_valid", "valid_to_partly", "valid_in_step6", "target_not_flagged"):
        if not all(name in x for x in rows):
            continue
        a = sum(bool(x[name]) for x in rows if x["arm"] == "A")
        b = sum(bool(x[name]) for x in rows if x["arm"] == "B")
        p = fisher_exact([[a, n["A"] - a], [b, n["B"] - b]])[1]
        print(f"runs with any {name}: A {a}/{n['A']}  B {b}/{n['B']}  Fisher p {p:.3f}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ROUNDS:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
