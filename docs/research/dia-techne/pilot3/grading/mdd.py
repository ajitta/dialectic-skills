from math import sqrt, asin, sin
from scipy.stats import norm
za, zb = norm.ppf(0.975), norm.ppf(0.8)
def mdd_pooled(p1, n):
    # find p2>p1 such that power=0.8, unpooled-variance z test (standard sample size formula, solve)
    lo, hi = p1, 0.9
    for _ in range(100):
        p2=(lo+hi)/2
        pb=(p1+p2)/2
        need = (za*sqrt(2*pb*(1-pb)) + zb*sqrt(p1*(1-p1)+p2*(1-p2)))**2/(p2-p1)**2
        if need>n: lo=p2
        else: hi=p2
    return p2
def mdd_arcsine(p1,n):
    h=(za+zb)*sqrt(2/n); return sin(asin(sqrt(p1))+h/2)**2
for p in (0.09,0.008):
    for n in (2000,3000):
        print(p,n, round(mdd_pooled(p,n)*100,3), round(mdd_arcsine(p,n)*100,3))
print(1800/20000, 160/20000, 0.008/0.09, 0.0889*0.12*20000, 0.0889*0.15*20000, 12/0.68,12/0.79,12/1.6,12/1.8,12/4.78,12/13.26,12/5.35,12/7.15,12/2.4)
