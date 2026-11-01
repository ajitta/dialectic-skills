import numpy as np
from scipy import stats

def proportion_effectsize(a,b): return 2*np.arcsin(np.sqrt(a))-2*np.arcsin(np.sqrt(b))
class NormalIndPower:
    def power(self,es,nobs1,alpha,ratio=1):
        n2=nobs1*ratio; se=np.sqrt(1/nobs1+1/n2); za=stats.norm.ppf(1-alpha/2)
        return stats.norm.sf(za-abs(es)/se)+stats.norm.cdf(-za-abs(es)/se)
    def solve_power(self,es,power,alpha):
        from scipy.optimize import brentq
        return brentq(lambda n: self.power(es,n,alpha)-power,10,1e6)
class StratifiedTable:
    def __init__(s,tabs): s.t=tabs
    @property
    def oddsratio_pooled(s):
        num=sum(t[0,0]*t[1,1]/t.sum() for t in s.t); den=sum(t[0,1]*t[1,0]/t.sum() for t in s.t); return num/den
    def test_null_odds(s,correction):
        a=sum(t[0,0] for t in s.t); e=sum(t[0].sum()*t[:,0].sum()/t.sum() for t in s.t)
        v=sum(t[0].sum()*t[1].sum()*t[:,0].sum()*t[:,1].sum()/(t.sum()**2*(t.sum()-1)) for t in s.t)
        d=abs(a-e)-(0.5 if correction else 0); st=d*d/v
        class R: pass
        r=R(); r.statistic=st; r.pvalue=stats.chi2.sf(st,1); return r
print("=== Q1")
x1,n1,x2,n2=120,2400,143,2380
p1,p2=x1/n1,x2/n2; pp=(x1+x2)/(n1+n2)
se0=np.sqrt(pp*(1-pp)*(1/n1+1/n2)); z=(p2-p1)/se0
print("rates",p1,p2,"diff",p2-p1,"rel",p2/p1-1,"z",z,"p",2*stats.norm.sf(z))
t=np.array([[x2,n2-x2],[x1,n1-x1]])
print("chi2 cc",stats.chi2_contingency(t,correction=True)[1],"fisher",stats.fisher_exact(t)[1])
se=np.sqrt(p1*(1-p1)/n1+p2*(1-p2)/n2); print("CI diff",(p2-p1-1.96*se)*100,(p2-p1+1.96*se)*100)
rr=p2/p1; serr=np.sqrt(1/x2-1/n2+1/x1-1/n1); print("RR CI",rr*np.exp(-1.96*serr),rr*np.exp(1.96*serr))
pw=NormalIndPower()
es=proportion_effectsize(0.06,0.05); print("power at n",pw.power(es,nobs1=2400,alpha=0.05,ratio=2380/2400))
print("n80",pw.solve_power(es,power=0.8,alpha=0.05),"n90",pw.solve_power(es,power=0.9,alpha=0.05))
# classic formula
def nform(p1,p2,a=0.05,pow=0.8):
    za=stats.norm.ppf(1-a/2); zb=stats.norm.ppf(pow); pb=(p1+p2)/2
    return (za*np.sqrt(2*pb*(1-pb))+zb*np.sqrt(p1*(1-p1)+p2*(1-p2)))**2/(p2-p1)**2
print("n80 formula",nform(.05,.06),"n90",nform(.05,.06,pow=.9))
# MDE at 80%
from scipy.optimize import brentq
f=lambda q: pw.power(proportion_effectsize(q,0.05),nobs1=2390,alpha=0.05)-0.8
q=brentq(f,0.0501,0.1); print("MDE80 p2",q,"rel",q/0.05-1)
print("SRM p",stats.binomtest(2400,4780,0.5).pvalue)
rng=np.random.default_rng(0); a=rng.beta(1+x1,1+n1-x1,10**6); b=rng.beta(1+x2,1+n2-x2,10**6)
print("P(T>C)",(b>a).mean(),"P(lift>10%)",(b/a>1.1).mean())
print("=== Q2")
tabs=[np.array([[70,30],[480,320]]),np.array([[175,525],[40,160]])]
for tb in tabs: print("OR",(tb[0,0]*tb[1,1])/(tb[0,1]*tb[1,0]),"fisher",stats.fisher_exact(tb)[1])
tot=tabs[0]+tabs[1]; print("total OR",(tot[0,0]*tot[1,1])/(tot[0,1]*tot[1,0]),stats.fisher_exact(tot)[1])
st=StratifiedTable(tabs); print("MH OR",st.oddsratio_pooled); r=st.test_null_odds(correction=True); print("CMH cc",r.statistic,r.pvalue); r2=st.test_null_odds(correction=False); print("CMH nocc",r2.statistic,r2.pvalue)
print("dept rates",550/900,215/900,"std men",.5*.6+.5*.2,"women",.5*.7+.5*.25, 245/800)
print("=== Q3")
y=np.array([87,91,103,102,108,107,104,107,107,115,125,149,100,107,112,115,121,123,119,118,125,124,142,162],float)
a,b=y[:12],y[12:]; g=b/a-1
print("sums",a.sum(),b.sum(),b.sum()/a.sum()-1,"yoy range",g.min(),g.max(),"mean",g.mean(),"H2",b[6:].sum()/a[6:].sum()-1,"Q4",b[9:].sum()/a[9:].sum()-1,"Dec",b[11]/a[11]-1,"Nov->Dec",162/142-1)
print("x1.125",100*b.sum()/a.sum(),"xmean",100*(1+g.mean()),"xH2",100*b[6:].sum()/a[6:].sum(),"xQ4",100*b[9:].sum()/a[9:].sum(),"dec ratio",162*100/149, 100/149)
t_=np.arange(24); M=np.zeros((24,12)); M[t_,t_%12]=1
X=np.column_stack([t_,M]); xf=np.r_[24,np.eye(12)[0]]
c=np.linalg.lstsq(X,y,rcond=None)[0]; print("lin reg",xf@c)
c=np.linalg.lstsq(X,np.log(y),rcond=None)[0]; print("log reg",np.exp(xf@c),"monthly growth",np.exp(c[0])-1)
# Y backtest: one-step ahead for Mar-Dec 2025, method: same month last year * growth from year-to-date? Try trailing 12-month growth on available
def m_yoy(k):  # forecast y[k] for k in 12..23 using trailing growth over months 12..k-1 vs a
    m=k-12
    if m==0: return None
    gr=y[12:k].sum()/y[0:m].sum(); return y[k-12]*gr
errs=[];
for k in range(14,24):
    f=m_yoy(k); errs.append((f-y[k])/y[k])
errs=np.array(errs); print("YTD-growth backtest MAPE",np.abs(errs).mean(),"RMS",np.sqrt((errs**2).mean()),"max",np.abs(errs).max(), "Dec fcst",m_yoy(23))
print("naive MAPE Mar-Dec",np.mean(np.abs((y[14:24]-y[2:12])/y[14:24])))
# log regression rolling
errs2=[]
for k in range(14,24):
    tt=np.arange(k); MM=np.zeros((k,12)); MM[tt,tt%12]=1; XX=np.column_stack([tt,MM]); 
    cc=np.linalg.lstsq(XX,np.log(y[:k]),rcond=None)[0]; f=np.exp(np.r_[k,np.eye(12)[k%12]]@cc); errs2.append((f-y[k])/y[k])
errs2=np.array(errs2); print("logreg backtest MAPE",np.abs(errs2).mean())
print("=== Q4")
print("rr",400/5000,"min top2",(4.5-3)/(5-3),"min 5s",(4.5-4)/(5-4),"300/5000",300/5000)
for p in [.5,.75]: print("moe",p,1.96*np.sqrt(p*(1-p)/400))
print("fpc moe .5",1.96*np.sqrt(.25/400*(5000-400)/(5000-1)),"fpc .75",1.96*np.sqrt(.75*.25/400*(4600/4999)))
