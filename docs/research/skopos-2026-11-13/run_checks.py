"""Re-run the expected-behaviour checks of plugin 2.13.0 (spec D72, docs/probes.md Part AK).

usage: python run_checks.py <plugin_dir> <out_dir> [name-prefix ...]

<plugin_dir> is a copy of plugins/dia (copy it first, so a rebuild during the batch cannot change
the arm). Each case runs headless on claude-sonnet-5-5 in a new empty working directory with a
new CLAUDE_CONFIG_DIR that holds only a copy of the login, one case after another; a case with
several prompts is one conversation continued with --resume. Every turn's event stream is saved
as <out_dir>/<case>-turn<n>.jsonl. Create <out_dir> outside any `.claude` folder: a working
directory under `.claude` blocks file writes. Korean prompts are written as escapes because
repository files outside the Korean references carry no Hangul.

Safety for the login (Part AK, Credentials): the script stops unless the access token is valid
for at least 90 more minutes, so that no copy has to refresh it; it removes each copy when its
case ends; and it prints whether the home credentials file is byte-identical afterwards.

What to look for (written before the runs of 2026-11-13; * marks the core items):
  every review    * nothing implemented or drafted before approval
                  * the four lines are present, each with a value
                  ends by asking to proceed; facts kept apart from assumptions
  landing         outcome quoted; deliverable criteria apart from outcome criteria; an indirect
                  measure called a proxy; outcome marked unverified
  rename          "not stated"; a labelled hypothesis that asks for confirmation; * no split
  delete          * nothing run; says the step cannot be undone and offers a safeguard
  dialogue        `dia skopos` starts the review; after "Go ahead." the report names the outcome
                  and what has shown it; * an unrelated later task is done at once
  own text        * the task is done without a review
  Korean runs     headings and the four labels in Korean
  4-rename-ko     known to load no skill: the name reads as the folder's name
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time

HOME_CRED = os.path.expanduser("~/.claude/.credentials.json")
RO = "Skill,Read,Glob"
RW = "Skill,Read,Glob,Write,Edit"
CASES = [
    ('1-landing-en', RO, [
        'dia-skopos Build a landing page for our new meal-kit subscription that will increase sales.',
    ]),
    ('2-landing-ko', RO, [
        'dia-skopos \uc0c8\ub85c \ub098\uc628 \ubc00\ud0a4\ud2b8 \uad6c\ub3c5 \uc11c\ube44\uc2a4\uc758 \ub79c\ub529 \ud398\uc774\uc9c0\ub97c \ub9cc\ub4e4\uc5b4\uc918. \ud310\ub9e4\uac00 \ub298\uc5b4\ub098\uac8c.',
    ]),
    ('3-rename-en', RO, [
        'dia-skopos Write a Python script that renames the photos in a folder by the date they were taken.',
    ]),
    ('4-rename-ko', RO, [
        'dia-skopos \ud3f4\ub354 \uc548\uc758 \uc0ac\uc9c4\ub4e4\uc744 \ucc0d\uc740 \ub0a0\uc9dc\ub85c \uc774\ub984\uc744 \ubc14\uafb8\ub294 \ud30c\uc774\uc36c \uc2a4\ud06c\ub9bd\ud2b8\ub97c \uc9dc\uc918.',
    ]),
    ('5-delete-en', RO, [
        'dia-skopos Delete every row older than 2020 from the orders table in our production database.',
    ]),
    ('6-dialogue-en', RO, [
        'dia skopos Write a Python script that prints the ten largest files under a folder.',
        'Go ahead.',
        'Now write a haiku about autumn.',
    ]),
    ('7-owntext-en', RO, [
        '/dia:dia-skopos The Recognizing Approval section in the body of this skill seems too long. Look at where it could be cut.',
    ]),
    ('4b-rename-ko', RO, [
        '/dia:dia-skopos \ud3f4\ub354 \uc548\uc758 \uc0ac\uc9c4\ub4e4\uc744 \ucc0d\uc740 \ub0a0\uc9dc\ub85c \uc774\ub984\uc744 \ubc14\uafb8\ub294 \ud30c\uc774\uc36c \uc2a4\ud06c\ub9bd\ud2b8\ub97c \uc9dc\uc918.',
    ]),
    ('6b-complaint-en', RO, [
        'dia skopos Write a reply to this customer complaint: "My meal kit arrived two days late and the vegetables were wilted. This is the second time this month."',
        'Go ahead.',
    ]),
    ('8-landing-ko', RO, [
        '/dia:dia-skopos \uc0c8\ub85c \ub098\uc628 \ubc00\ud0a4\ud2b8 \uad6c\ub3c5 \uc11c\ube44\uc2a4\uc758 \ub79c\ub529 \ud398\uc774\uc9c0\ub97c \ub9cc\ub4e4\uc5b4\uc918. \ud310\ub9e4\uac00 \ub298\uc5b4\ub098\uac8c.',
    ]),
    ('9-later-en', RO, [
        'dia-skopos Write a reply to this customer complaint: "My meal kit arrived two days late and the vegetables were wilted. This is the second time this month."',
        'Go ahead.',
        'Now write a haiku about autumn.',
    ]),
    ('r1-wedding', RO, [
        "dia-skopos Write a short speech for my brother's wedding.",
        "My brother is Minho, marrying Sara; I'm the best man. He taught me to ride a bike, even though he's younger. Warm, one light joke, about 3 minutes. proceed",
    ]),
    ('r2-menu', RO, [
        'dia',
    ]),
    ('r3-reductio', RO, [
        'dia reductio Assume every prime is odd and show where it breaks.',
    ]),
]


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    arm, out = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
    wanted = sys.argv[3:]
    with open(HOME_CRED, encoding="utf-8") as f:
        cred = json.load(f)["claudeAiOauth"]
    minutes = (cred.get("expiresAt", 0) / 1000 - time.time()) / 60
    if not cred.get("accessToken") or minutes < 90:
        print("STOP: the login token is missing or expires in %d minutes; log in again first" % minutes)
        return 2
    before = sha(HOME_CRED)
    os.makedirs(out, exist_ok=True)
    env = {k: v for k, v in os.environ.items() if not (k.startswith("CLAUDE") or k.startswith("ANTHROPIC"))}
    env["ENABLE_CLAUDEAI_MCP_SERVERS"] = "false"
    exe = shutil.which("claude")
    status = 0
    for name, tools, prompts in CASES:
        if wanted and not any(name.startswith(w) for w in wanted):
            continue
        cfg, work = os.path.join(out, "cfg-" + name), os.path.join(out, "work-" + name)
        for d in (cfg, work):
            shutil.rmtree(d, ignore_errors=True)
            os.makedirs(d)
        shutil.copy(HOME_CRED, cfg)
        env["CLAUDE_CONFIG_DIR"] = cfg
        session = None
        try:
            for i, prompt in enumerate(prompts, 1):
                cmd = [exe, "-p", prompt, "--plugin-dir", arm, "--model", "claude-sonnet-5-5", "--tools", tools,
                       "--max-turns", "12", "--output-format", "stream-json", "--verbose"]
                if tools == RW:
                    cmd += ["--permission-mode", "acceptEdits"]
                if session:
                    cmd += ["--resume", session]
                path = os.path.join(out, "%s-turn%d.jsonl" % (name, i))
                with open(path, "wb") as stream:
                    proc = subprocess.run(cmd, cwd=work, env=env, stdout=stream, stderr=subprocess.PIPE,
                                          stdin=subprocess.DEVNULL, timeout=900)
                result, text = None, ""
                with open(path, encoding="utf-8", errors="replace") as f:
                    for line in f:
                        try:
                            ev = json.loads(line)
                        except ValueError:
                            continue
                        session = ev.get("session_id") or session
                        if ev.get("type") == "result":
                            result, text = ev, str(ev.get("result", ""))
                failed = (not result) or "Failed to authenticate" in text
                print("%s turn %d: exit %s, %s%s" % (name, i, proc.returncode, (result or {}).get("subtype"),
                                                  " AUTH FAILURE" if "Failed to authenticate" in text else ""), flush=True)
                if failed:
                    status = 1
                    break
        finally:
            shutil.rmtree(cfg, ignore_errors=True)
        if status:
            break
    print("home credentials file unchanged: %s" % (sha(HOME_CRED) == before))
    return status


if __name__ == "__main__":
    sys.exit(main())
