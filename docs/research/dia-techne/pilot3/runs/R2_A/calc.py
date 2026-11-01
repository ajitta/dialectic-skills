from math import sqrt
N=20000; o=0.09; c=0.008
print("열람자", N*o, "클릭자", N*c, "CTOR", round(c/o*100,2))
bench={"전체":(43.46,2.09,6.81),"소프트웨어/웹앱":(39.31,1.15,5.40),"비즈니스/금융":(43.34,2.37,7.96)}
for k,(bo,bc,bt) in bench.items(): print(k,"열람 배수",round(bo/(o*100),2),"클릭 배수",round(bc/(c*100),2),"CTOR 차이",round(c/o*100-bt,2))
# A/B 검출 가능 최소 차이 (alpha .05 양측, power .8 -> z 1.96+0.84)
z=1.96+0.8416
for n in (1000,2000,3000):
    for p,name in ((o,"열람"),(c,"클릭")):
        se=sqrt(2*p*(1-p)/n); print(n,"명/안",name,"MDE(%p)",round(z*se*100,2))
# 열람자 수 시나리오
for target in (0.12,0.15):
    print("열람률",target,"이면 CTOR 8.89% 유지 시 클릭자",round(N*target*c/o))
