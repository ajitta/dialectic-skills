from math import sqrt
from scipy.stats import norm
za, zb = norm.ppf(0.975), norm.ppf(0.8)
def n_cc(p1,p2):
    pb=(p1+p2)/2; d=abs(p2-p1)
    n=(za*sqrt(2*pb*(1-pb)) + zb*sqrt(p1*(1-p1)+p2*(1-p2)))**2/d**2
    return n/4*(1+sqrt(1+4/(n*d)))**2
def solve(p1,n,f,up=True):
    lo,hi=(p1,0.9) if up else (1e-6,p1)
    for _ in range(100):
        m=(lo+hi)/2
        need=f(p1,m)
        if up:
            lo,hi=(m,hi) if need>n else (lo,m)
        else:
            lo,hi=(lo,m) if need>n else (m,hi)
    return m
for p in (0.09,0.008):
  for n in (2000,3000):
    print(p,n,'cc up',round(solve(p,n,n_cc)*100,3))
# simple approx using p1 variance only
for p in (0.09,0.008):
  for n in (2000,3000):
    print(p,n,'simple',round((p+(za+zb)*sqrt(2*p*(1-p)/n))*100,3))
