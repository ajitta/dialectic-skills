import glob,random,re,os,sys
E=sys.argv[1]; os.makedirs(E+'/blind',exist_ok=True)
fs=sorted(glob.glob(E+'/t/*.md')); random.seed(20261110); random.shuffle(fs)
key=[]
for i,f in enumerate(fs,1):
    s=open(f).read()
    s=re.sub(r'(?m)^→ dia-[^\n]*\n?','',s)
    s=re.sub(r'(?m)^USER: dia ','USER: ',s)
    s=re.sub(r'dia-[a-z]+|dia [0-9]+','[skill]',s)
    n='T%02d.md'%i; open(E+'/blind/'+n,'w').write(s); key.append(n+' '+os.path.basename(f))
open(E+'/key.txt','w').write('\n'.join(key)+'\n')
