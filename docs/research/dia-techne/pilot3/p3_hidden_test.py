"""Hidden oracle test for R1. Usage: python3 -I p3_hidden_test.py <path to bizdays.py>"""
import sys, random, importlib.util
from datetime import date, timedelta
spec = importlib.util.spec_from_file_location("bd", sys.argv[1]); bd = importlib.util.module_from_spec(spec); spec.loader.exec_module(bd)
def oracle(s, e, hol):
    hs = set(hol); c = 0; d = s
    while d < e:
        d += timedelta(days=1)
        if d.weekday() < 5 and d not in hs: c += 1
    return c
rng = random.Random(42); fails = {"weekend_holiday": 0, "duplicate_holiday": 0, "plain": 0, "same_day": 0}; total = 0
base = date(2026, 1, 1)
for _ in range(3000):
    s = base + timedelta(days=rng.randint(0, 400)); e = s + timedelta(days=rng.randint(0, 60))
    hol = [s + timedelta(days=rng.randint(-5, 65)) for _ in range(rng.randint(0, 6))]
    kind = "plain"
    if rng.random() < 0.3 and hol: hol.append(hol[0]); kind = "duplicate_holiday"
    if any(h.weekday() >= 5 and s < h <= e for h in hol) and kind == "plain": kind = "weekend_holiday"
    if s == e: kind = "same_day"
    total += 1
    try:
        got = bd.business_days_between(s, e, hol)
    except Exception:
        got = None
    if got != oracle(s, e, hol): fails[kind] += 1
print("total", total, "fails", fails, "PASS" if sum(fails.values()) == 0 else "FAIL")
