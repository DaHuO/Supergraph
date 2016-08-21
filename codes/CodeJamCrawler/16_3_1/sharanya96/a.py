import heapq
t=int(input())
sn=1
while sn<=t:
    n=int(input())
    p=[]
    l=input().split()
    for i in range(n):
        p.append(int(l[i]))
    nop=sum(p)
    res=[]
    while nop>0:
        r,s=heapq.nlargest(2,range(len(p)),p.__getitem__)
        comb=[]
        if p[r]==1 and p[s]==1:
            count=0
            for i in range(n):
                count+=p[i]
            if count%2==0:
                p[s]-=1
                comb.append(chr(s+65))
            p[r]-=1
            comb.append(chr(r+65))
        else:
            if p[s]>0:
                p[s]-=1
                p[r]-=1
                comb.append(chr(s+65))
            else:
                p[r]-=2
                comb.append(chr(r+65))
            comb.append(chr(r+65))
        nop=sum(p)
        res.append(''.join(comb))
    print('Case #',sn,': ',' '.join(res),sep='')
    sn+=1
