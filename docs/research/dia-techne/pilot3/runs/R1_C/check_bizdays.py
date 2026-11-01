"""Compare business_days_between against a day-by-day brute-force oracle."""
import random, sys, importlib
from datetime import date, timedelta

mod = importlib.import_module(sys.argv[1] if len(sys.argv) > 1 else "bizdays")
f = mod.business_days_between

def oracle(start, end, holidays=()):
    hs = set(holidays)
    if end < start:
        return -oracle(end, start, holidays)
    n = 0
    d = start + timedelta(days=1)
    while d <= end:
        if d.weekday() < 5 and d not in hs:
            n += 1
        d += timedelta(days=1)
    return n

rng = random.Random(0)
base = date(2024, 1, 1)
fails = {"weekend_holiday": 0, "dup_holiday": 0, "reversed": 0, "other": 0}
examples = {}
total = 0
for _ in range(20000):
    s = base + timedelta(days=rng.randrange(0, 400))
    e = s + timedelta(days=rng.randrange(-30, 60))
    hol = [base + timedelta(days=rng.randrange(0, 460)) for _ in range(rng.randrange(0, 8))]
    if rng.random() < 0.3 and hol:
        hol.append(hol[0])
    total += 1
    got, want = f(s, e, hol), oracle(s, e, hol)
    if got != want:
        if e < s: k = "reversed"
        elif len(set(hol)) != len(hol) and f(s, e, list(set(hol))) == want: k = "dup_holiday"
        elif any(h.weekday() >= 5 and s < h <= e for h in hol): k = "weekend_holiday"
        else: k = "other"
        fails[k] += 1
        examples.setdefault(k, (s, e, sorted(hol), got, want))
# no-holiday exhaustive check over all pairs within 2 years window
nh_fail = 0
for a in range(0, 120):
    for b in range(0, 120):
        s, e = base + timedelta(days=a), base + timedelta(days=b)
        if f(s, e) != oracle(s, e): nh_fail += 1
print("random cases:", total, "mismatches:", fails)
print("exhaustive no-holiday pairs:", 120*120, "mismatches:", nh_fail)
for k, v in examples.items(): print(k, v)
