def checker(l):
    return max(l)>sum(l)*0.5

def evacuation(l):
    l=l[:]
    plan=[]
    if l.count(1)==sum(l):
        if l.count(1)==3:
            i=l.index(1)
            l[i]=0
            return chr(i+65),l
        else:
            i1=l.index(1)
            i2=l.index(1,i1+1)
            l[i1]=0
            l[i2]=0
            return chr(i1+65)+chr(i2+65),l
    mx=max(l)
    m=l.index(mx)
    if l.count(mx)==1:
        l[m]-=2
        return chr(m+65)*2,l
    else:
        m1=m
        m2=l.index(mx,m1+1)
        l[m1]-=1
        l[m2]-=1
        return chr(m1+65)+chr(m2+65),l
inpt=[]
for i in range(input()):
    n=input()
    inpt.append(map(int,raw_input().split()))

for i in range(len(inpt)):
    sol=[]
    l=inpt[i]
    while sum(l)!=0:
        s,l=evacuation(l)
        sol.append(s)
    print 'Case #'+str(i+1)+': '+' '.join(map(str,sol))
