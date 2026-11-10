import glob,random,re,os,sys
# usage: python3 -I mkblind.py [EXP_DIR]  (default: this script's folder)
# Overwrites blind/ and key.txt. The 2026-11-10 run also removed one leftover
# routing line from blind/T24.md by hand (relay-log.md), which a rerun will not repeat.
E=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(os.path.abspath(__file__)); os.makedirs(E+'/blind',exist_ok=True)
fs=sorted(glob.glob(E+'/t/*.md')); random.seed(20261110); random.shuffle(fs)
key=[]
for i,f in enumerate(fs,1):
    s=open(f).read()
    s=re.sub(r'(?m)^→ dia-[^\n]*\n?','',s)
    s=re.sub(r'(?m)^USER: dia ','USER: ',s)
    s=re.sub(r'dia-[a-z]+|dia [0-9]+','[skill]',s)
    n='T%02d.md'%i; open(E+'/blind/'+n,'w').write(s); key.append(n+' '+os.path.basename(f))
open(E+'/key.txt','w').write('\n'.join(key)+'\n')
