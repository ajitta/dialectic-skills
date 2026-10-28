"""Test fetch tool: a bare fetch returns a model-written summary of the page; a question returns the page sentences that best answer it."""
import os, re, sys, datetime

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fetchdata")
STOP = set("a an the of to in on at for and or but is are was were be been by with as that this it its from than then so not no do does did has have had what which who whom whose how when where why can could may might will would should about into over under per their there they them she her he his our your you we i".split())


def words(text):
    return [w for w in re.findall(r"[a-z0-9]+(?:\.[0-9]+)?", text.lower()) if w not in STOP]


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"(])", text.strip())
    return [p.strip() for p in parts if p.strip()]


def main():
    args = sys.argv[1:]
    run = "unknown"
    if len(args) >= 2 and args[0] == "--run":
        run, args = args[1], args[2:]
    if not args:
        print("usage: fetch.py --run <run-id> <source-id> [\"question\"]")
        return 2
    source, question = args[0], " ".join(args[1:]).strip()
    raw_path = os.path.join(DATA, "raw", source + ".md")
    if not re.fullmatch(r"[a-z0-9-]+", source) or not os.path.exists(raw_path):
        print("fetch: no page with that id.")
        return 1
    os.makedirs(os.path.join(DATA, "log"), exist_ok=True)
    with open(os.path.join(DATA, "log", run + ".log"), "a", encoding="utf-8") as log:
        log.write(f"{datetime.datetime.now(datetime.timezone.utc).isoformat()}\t{source}\t{'Q' if question else 'FETCH'}\t{question}\n")
    if not question:
        with open(os.path.join(DATA, "summary", source + ".md"), encoding="utf-8") as f:
            print("[fetch tool] The page was summarized by the fetch tool's model; this is a summary, not the raw page.\n")
            print(f.read().strip())
        return 0
    with open(raw_path, encoding="utf-8") as f:
        raw = f.read()
    q = set(words(question))
    need = 1 if len(q) <= 3 else 2
    scored = []
    for i, s in enumerate(sentences(raw)):
        score = len(q & set(words(s)))
        if score >= need:
            scored.append((score, i, s))
    scored.sort(key=lambda t: (-t[0], t[1]))
    print("[fetch tool] Answer to your question, quoting the page:\n")
    if not scored:
        print("The page does not appear to address this.")
    else:
        for _, _, s in sorted(scored[:2], key=lambda t: t[1]):
            print("- " + s)
    return 0


if __name__ == "__main__":
    sys.exit(main())
