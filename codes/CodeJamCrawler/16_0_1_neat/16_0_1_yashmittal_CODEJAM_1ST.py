import sys
f=open("A-large.in",'r')
t=int(f.readline())
sys.stdout=open("ot",'w')
for i in range(1,t+1):
    n=int(f.readline())
    if n==0:
        print("Case #",i,": INSOMNIA",sep='')
        continue
    l=list(str(n))
    l=list(set(l))
    j=2
    while len(l)!=10:
        x=n*j
        j=j+1
        y=list(str(x))
        l=list(set(l) | set(y))
    print("Case #",i,": ",(j-1)*n,sep='')
sys.stdout.close()
f.close
