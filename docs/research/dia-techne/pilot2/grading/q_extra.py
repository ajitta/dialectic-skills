import numpy as np
from scipy import stats
from scipy.optimize import brentq
za,zb=1.959964,0.841621
f=lambda q:(q-0.05)-(za+zb)*np.sqrt(.05*.95/2400+q*(1-q)/2380)
q=brentq(f,0.051,0.1);print("MDE unpooled",q,q/.05-1)
f2=lambda q:(q-0.05)-(za*np.sqrt(2*((.05+q)/2)*(1-(.05+q)/2)/2390)+zb*np.sqrt((.05*.95+q*(1-q))/2390))
q=brentq(f2,0.051,0.1);print("MDE pooled",q,q/.05-1)
x1,n1,x2,n2=120,2400,143,2380;p1,p2=x1/n1,x2/n2
for z in [1.96,2.0]:
  se=np.sqrt(p1*(1-p1)/n1+p2*(1-p2)/n2);print(z,(p2-p1-z*se)*100,(p2-p1+z*se)*100)
# Newcombe
def wilson(x,n,z=1.96):
  p=x/n;d=1+z*z/n;c=(p+z*z/(2*n))/d;h=z*np.sqrt(p*(1-p)/n+z*z/(4*n*n))/d;return c-h,c+h
l1,u1=wilson(x1,n1);l2,u2=wilson(x2,n2);d=p2-p1
print("newcombe",(d-np.sqrt((p2-l2)**2+(u1-p1)**2))*100,(d+np.sqrt((u2-p2)**2+(p1-l1)**2))*100)
# Q3 Fourier: log trend + K harmonics, linear
y=np.array([87,91,103,102,108,107,104,107,107,115,125,149,100,107,112,115,121,123,119,118,125,124,142,162],float)
t=np.arange(25)
for K in [1,2,3]:
  cols=[np.ones(25),t]
  for k in range(1,K+1): cols+= [np.sin(2*np.pi*k*t/12),np.cos(2*np.pi*k*t/12)]
  X=np.column_stack(cols);c=np.linalg.lstsq(X[:24],y,rcond=None)[0];cl=np.linalg.lstsq(X[:24],np.log(y),rcond=None)[0]
  print("Fourier K",K,X[24]@c,np.exp(X[24]@cl))
# simple Holt-Winters additive with SSE-optimised params
from scipy.optimize import minimize
def hw(params,y,m=12,mul=False):
  a,b,g=params
  L=y[:m].mean();T=(y[m:2*m].mean()-y[:m].mean())/m
  S=list(y[:m]/L) if mul else list(y[:m]-L)
  sse=0
  for i in range(len(y)):
    s=S[i]
    f=(L+T)*s if mul else L+T+s
    if i>=m: sse+=(y[i]-f)**2
    Lp=L
    L=a*(y[i]/s if mul else y[i]-s)+(1-a)*(L+T)
    T=b*(L-Lp)+(1-b)*T
    S.append(g*(y[i]/L if mul else y[i]-L)+(1-g)*s)
  fc=(L+T)*S[len(y)] if mul else L+T+S[len(y)]
  return sse,fc
for mul in [True,False]:
  r=minimize(lambda p:hw(p,y,mul=mul)[0],[.3,.1,.1],bounds=[(0,1)]*3)
  print("HW mul" if mul else "HW add",r.x,hw(r.x,y,mul=mul)[1])
