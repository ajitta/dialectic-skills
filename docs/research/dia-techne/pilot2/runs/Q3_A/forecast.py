import numpy as np
from scipy.optimize import minimize

y = np.array([87, 91, 103, 102, 108, 107, 104, 107, 107, 115, 125, 149,
              100, 107, 112, 115, 121, 123, 119, 118, 125, 124, 142, 162], float)
n = len(y)
m = 12
print("sum 2024", y[:12].sum(), "sum 2025", y[12:].sum(), "YoY", y[12:].sum() / y[:12].sum())
print("monthly YoY ratios", np.round(y[12:] / y[:12], 3))


def sn(h):  # seasonal naive, h = series up to origin
    return h[-12]


def sn_growth(h):  # seasonal naive x YoY ratio over overlapping months
    k = len(h) - 12  # months with a year-ago value
    if k < 1:
        return np.nan
    k = min(k, 12)
    r = h[-k:].sum() / h[-k - 12:-12].sum()
    return h[-12] * r


def sn_growth3(h):  # YoY ratio over last 3 months
    if len(h) < 15:
        return np.nan
    return h[-12] * h[-3:].sum() / h[-15:-12].sum()


def logreg(h):  # log y = a + b t + month effects (needs >= 13 points)
    t = np.arange(len(h))
    if len(h) < 14:
        return np.nan
    X = np.column_stack([t] + [(t % 12 == j).astype(float) for j in range(12)])
    beta, *_ = np.linalg.lstsq(X, np.log(h), rcond=None)
    tn = len(h)
    xn = np.r_[tn, [(tn % 12 == j) for j in range(12)]].astype(float)
    return float(np.exp(xn @ beta))


def hw(h, mult=True, ret_params=False):
    """Holt-Winters (damped=False), multiplicative or additive seasonality, SSE fit."""
    if len(h) < 24:
        return np.nan
    # initial states from first two seasons (classical)
    l0 = h[:12].mean()
    b0 = (h[12:24].mean() - h[:12].mean()) / 12
    s0 = h[:12] / l0 if mult else h[:12] - l0

    def run(p):
        a, b, g = p
        l, bb, s = l0, b0, list(s0)
        sse = 0
        for t in range(len(h)):
            st = s[t]
            f = (l + bb) * st if mult else l + bb + st
            e = h[t] - f
            sse += e * e
            lp = l
            if mult:
                l = a * h[t] / st + (1 - a) * (l + bb)
                bb = b * (l - lp) + (1 - b) * bb
                s.append(g * h[t] / l + (1 - g) * st)
            else:
                l = a * (h[t] - st) + (1 - a) * (l + bb)
                bb = b * (l - lp) + (1 - b) * bb
                s.append(g * (h[t] - l) + (1 - g) * st)
        fc = (l + bb) * s[len(h)] if mult else l + bb + s[len(h)]
        return sse, fc

    best = None
    for a0 in (0.2, 0.5, 0.8):
        for g0 in (0.1, 0.4):
            r = minimize(lambda p: run(p)[0], [a0, 0.05, g0], bounds=[(0.01, 0.99)] * 3)
            if best is None or r.fun < best.fun:
                best = r
    sse, fc = run(best.x)
    if ret_params:
        return fc, best.x, np.sqrt(sse / len(h))
    return fc


methods = {"seasonal_naive": sn, "sn_x_YoY(avail)": sn_growth, "sn_x_YoY(last3)": sn_growth3,
           "log_trend_month": logreg}

# rolling-origin one-step backtest on 2025 months (origins 14..23 -> forecast months 15..24)
print("\nBacktest: one-step forecasts for Mar-Dec 2025 (origin = all data before the month)")
start = 14
res = {}
for name, f in methods.items():
    errs = []
    for t in range(start, n):
        fc = f(y[:t])
        errs.append((y[t] - fc) / y[t])
    errs = np.array(errs)
    res[name] = errs
    print(f"{name:18s} MAPE={np.mean(np.abs(errs))*100:5.2f}%  bias(mean % err)={np.mean(errs)*100:+5.2f}%  "
          f"Dec2025 fc={f(y[:23]):6.1f}")

print("\nForecasts for Jan 2026 (origin = full 24 months)")
for name, f in methods.items():
    print(f"{name:18s} {f(y):6.1f}")
for mult in (True, False):
    fc, p, rmse = hw(y, mult, True)
    print(f"HW {'mult' if mult else 'add '} {fc:6.1f}  params(a,b,g)={np.round(p,3)} in-sample RMSE={rmse:.2f}")

# Jan/Dec ratio check
print("\nJan25/Dec24 ratio", round(100 / 149, 4), "-> x Dec25 =", round(162 * 100 / 149, 1))

# interval from backtest errors of the chosen method
e = res["sn_x_YoY(avail)"]
sd = np.sqrt(np.mean(e ** 2))
print("\nsn_x_YoY RMS % error", round(sd * 100, 2), "max abs % err", round(np.max(np.abs(e)) * 100, 2))
