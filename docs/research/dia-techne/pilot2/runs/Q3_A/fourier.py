import numpy as np
y = np.array([87, 91, 103, 102, 108, 107, 104, 107, 107, 115, 125, 149,
              100, 107, 112, 115, 121, 123, 119, 118, 125, 124, 142, 162], float)
def X(t, K):
    cols=[np.ones_like(t), t]
    for k in range(1,K+1):
        cols += [np.sin(2*np.pi*k*t/12), np.cos(2*np.pi*k*t/12)]
    if K==6: cols=cols[:-1]  # sin(pi t)=0
    return np.column_stack(cols).astype(float)
def fc(h,K):
    t=np.arange(len(h)); b,*_=np.linalg.lstsq(X(t,K),np.log(h),rcond=None)
    return float(np.exp(X(np.array([len(h)]),K)@b)[0])
def aicc(h,K):
    t=np.arange(len(h)); A=X(t,K); b,*_=np.linalg.lstsq(A,np.log(h),rcond=None)
    r=np.log(h)-A@b; n=len(h); k=A.shape[1]+1
    return n*np.log(np.sum(r**2)/n)+2*k+2*k*(k+1)/max(n-k-1,1)
for K in range(1,7):
    e=[(y[t]-fc(y[:t],K))/y[t] for t in range(14,24)]
    print(f"K={K} AICc(full)={aicc(y,K):7.2f} backtest MAPE={np.mean(np.abs(e))*100:5.2f}% bias={np.mean(e)*100:+5.2f}% Jan2026={fc(y,K):6.1f}")
