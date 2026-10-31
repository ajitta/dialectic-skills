import math, random
# P1 A/B test
c_n, c_x, t_n, t_x = 2400, 120, 2380, 143
pc, pt = c_x/c_n, t_x/t_n
p = (c_x+t_x)/(c_n+t_n)
se0 = math.sqrt(p*(1-p)*(1/c_n+1/t_n))
z = (pt-pc)/se0
pval = math.erfc(abs(z)/math.sqrt(2))
se1 = math.sqrt(pc*(1-pc)/c_n + pt*(1-pt)/t_n)
lo, hi = (pt-pc)-1.96*se1, (pt-pc)+1.96*se1
# power to detect observed diff at alpha .05 two-sided, n as given
zb = abs(pt-pc)/se1 - 1.96
power = 0.5*math.erfc(-zb/math.sqrt(2))
print(f"P1 pc={pc:.4f} pt={pt:.4f} diff={pt-pc:.4f} rel={(pt/pc-1):.3f} z={z:.3f} p={pval:.4f} CI=({lo:.4f},{hi:.4f}) power_obs~{power:.2f}")
# P2 Simpson
d = {"X": {"M": (800, 480), "F": (100, 70)}, "Y": {"M": (200, 40), "F": (700, 175)}}
for k, v in d.items():
    print("P2", k, {g: f"{a}/{n}={a/n:.3f}" for g, (n, a) in v.items()})
for g in "MF":
    n = sum(d[k][g][0] for k in d); a = sum(d[k][g][1] for k in d)
    print("P2 total", g, f"{a}/{n}={a/n:.3f}")
# P3 seasonal series: 24 months Jan 2024..Dec 2025
season = {1:-12, 2:-8, 3:0, 4:2, 5:4, 6:3, 7:1, 8:0, 9:2, 10:6, 11:18, 12:40}
rng = random.Random(7)
vals = []
for i in range(24):
    m = i % 12 + 1
    vals.append(round(100 + 1.0*i + season[m] + rng.uniform(-3, 3)))
print("P3 series", vals)
# naive last-value and linear-trend-on-last-3 vs seasonal naive * growth
last = vals[-1]
jan_prev = vals[12]; jan_prev2 = vals[0]
yoy = sum(vals[12:]) / sum(vals[:12])
print("P3 last value (naive)", last, "| seasonal naive Jan2025", jan_prev, "| seasonal naive x YoY growth", round(jan_prev*yoy, 1), "| true expected Jan2026 (no noise)", 100+24+season[1])
