import random;
from math import sqrt
fp =open('a.in');
n = int(fp.readline());
primelist=[]
fp_out = open('a.out','w')
for x in range(2,100000):
    ts=2;
    flag=True;
    while ts*ts<=x:
        if (x %ts ==0):
            flag=False;
            break;
        ts+=1;
    if (flag):
        primelist.append(x);
#print primelist
for ttt in range(n):
    print 'case #%d:'%(ttt)
    data = fp.readline();
    [n,m]=data.split(' ')
    #print n,' ',m
    n=int(n)
    m=int(m)
    ans=[];
    prt=[];
    while m>0:
        lt=[]
        lt.append(1)
        for i in range(n-2):
            lt.append(random.randint(0,1))
        lt.append(1)
        flag=False
        divisor=[];
        for dex in range(2,11):
            if(not flag):
                count=0;
                for i in range(n):
                    count = lt[i] + dex *count;
                ts=int(sqrt(count));
                if (ts>10000):
                    ts=10000
                flag=True
                for i in primelist:
                    if (ts>= i and count%i==0):
                        #print count,' ',i
                        divisor.append(i)
                        flag=False;
                        break;
        lt=map(str,lt)
        divisor=map(str,divisor)
        if (not flag):
            ans.append("".join(lt))
            prt.append(" ".join(divisor))
            m-=1;
    for i in range(len(ans)):
        print ans[i],prt[i]
