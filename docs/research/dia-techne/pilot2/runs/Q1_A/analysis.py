import math
from scipy import stats
import numpy as np
nA,xA,nB,xB=2400,120,2380,143
pA,pB=xA/nA,xB/nB
d=pB-pA; rel=d/pA
print(f"pA={pA:.5f} pB={pB:.5f} diff={d:.5f} rel={rel:.4f}")
# pooled z test
p=(xA+xB)/(nA+nB); se0=math.sqrt(p*(1-p)*(1/nA+1/nB)); z=d/se0
print(f"pooled z={z:.4f} two-sided p={2*stats.norm.sf(abs(z)):.4f} one-sided p={stats.norm.sf(z):.4f}")
# chi-square with/without Yates
tab=[[xA,nA-xA],[xB,nB-xB]]
for c in (False,True):
    chi2,pv,_,_=stats.chi2_contingency(tab,correction=c); print(f"chi2 yates={c}: chi2={chi2:.4f} p={pv:.4f}")
print("fisher two-sided p=%.4f"%stats.fisher_exact(tab)[1])
# Wald CI diff (unpooled)
se=math.sqrt(pA*(1-pA)/nA+pB*(1-pB)/nB)
lo,hi=d-1.96*se,d+1.96*se
print(f"95% CI abs diff: [{lo:.5f},{hi:.5f}]")
# Newcombe hybrid score CI
def wilson(x,n,z=1.96):
    ph=x/n; den=1+z*z/n; c=(ph+z*z/(2*n))/den; h=z*math.sqrt(ph*(1-ph)/n+z*z/(4*n*n))/den; return c-h,c+h
lA,uA=wilson(xA,nA); lB,uB=wilson(xB,nB)
nlo=d-math.sqrt((pB-lB)**2+(uA-pA)**2); nhi=d+math.sqrt((uB-pB)**2+(pA-lA)**2)
print(f"Newcombe CI abs diff: [{nlo:.5f},{nhi:.5f}]")
# relative lift CI via log RR
lr=math.log(pB/pA); ser=math.sqrt(1/xB-1/nB+1/xA-1/nA)
print(f"RR={pB/pA:.4f} 95% CI RR: [{math.exp(lr-1.96*ser):.4f},{math.exp(lr+1.96*ser):.4f}]")
# SRM
print("SRM chi2 p=%.4f"%stats.chisquare([nA,nB]).pvalue)
# power for observed effect at current n (two-sided 0.05)
za=1.959964
def power(p1,p2,n1,n2):
    pbar=(p1*n1+p2*n2)/(n1+n2); s0=math.sqrt(pbar*(1-pbar)*(1/n1+1/n2)); s1=math.sqrt(p1*(1-p1)/n1+p2*(1-p2)/n2)
    return stats.norm.cdf((abs(p2-p1)-za*s0)/s1)
print("power to detect 5->6 pct at current n: {:.3f}".format(power(0.05,0.06,nA,nB)))
# n per arm for 80% power, 5%->6% (20% rel)
def n_needed(p1,p2,pw=0.8):
    zb=stats.norm.ppf(pw); pbar=(p1+p2)/2
    return ((za*math.sqrt(2*pbar*(1-pbar))+zb*math.sqrt(p1*(1-p1)+p2*(1-p2)))/(p2-p1))**2
for pw in (0.8,0.9): print(f"n per arm for 5%->6% power {pw}: {math.ceil(n_needed(0.05,0.06,pw))}")
# MDE at current n with 80% power
zb=stats.norm.ppf(0.8); mde=(za+zb)*math.sqrt(2*0.05*0.95/2390)
print(f"approx MDE abs at n~2390/arm, 80% power: {mde:.5f} rel {mde/0.05:.3f}")
# Bayesian beta(1,1): P(B>A)
rng=np.random.default_rng(0)
a=rng.beta(1+xA,1+nA-xA,1_000_000); b=rng.beta(1+xB,1+nB-xB,1_000_000)
print(f"P(B>A)={np.mean(b>a):.4f}; P(rel lift>5%)={np.mean(b/a>1.05):.4f}; P(rel lift>10%)={np.mean(b/a>1.10):.4f}")
