import sys,re
# usage: python3 -I tally.py GRADES_FILE [EXP_DIR]  e.g. tally.py grades-opus.md
# Total is printed as earned/(39 - NA); a grader that writes NA for inapplicable
# items (fable) needs the denominator read as 39 minus true NA only.
import os
E=sys.argv[2] if len(sys.argv)>2 else os.path.dirname(os.path.abspath(__file__)); g=os.path.join(E,sys.argv[1])
key=dict(l.split()[0].replace('.md',''),) if False else {}
for l in open(E+'/key.txt'):
    if l.strip(): a,b=l.split(); key[a[:-3]]=b[:-3]
rows={}
for l in open(g):
    m=re.match(r'\|\s*(T\d\d)\s*\|',l)
    if not m: continue
    c=[x.strip() for x in l.strip().strip('|').split('|')]
    vals=c[2:8]
    rows[key[c[0]]]=(c[0],c[1],vals)
arms={}
for cell,(t,inp,v) in sorted(rows.items()):
    k1=v[0].startswith('1'); s=sum(x.startswith('1') for x in v); na=sum(x=='NA' for x in v)
    arms.setdefault(cell[0],[]).append((cell,t,k1,s,na,v))
for a,L in sorted(arms.items()):
    tot=sum(x[3] for x in L); na=sum(x[4] for x in L); k1=sum(x[2] for x in L)
    print(f"{a}: K1 {k1}/9  total {tot}/{39-na} (NA {na})  bar(K1>=8 & >=33): {'MEETS' if k1>=8 and tot>=33 else 'no'}")
    for x in L: print('   ',x[0],x[1],x[3],' '.join(x[5]))
