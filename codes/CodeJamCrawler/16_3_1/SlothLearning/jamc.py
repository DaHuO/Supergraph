from __future__ import print_function
import string
log = open("a.txt", "w")
d=string.ascii_uppercase
def evac(x,y):

    a=0
    for i in x:
        a+=x[i]
    if(a==0):
        return y
    else:
        v=list(x.values())
        k=list(x.keys())
        m=max(v)
        f=[]

        f=[i for i,j in enumerate(v) if j==m]

        if (len(f)%2 is 0 ):
            x[k[f[0]]]-=1
            x[k[f[1]]]-=1
            y.append(k[f[0]]+k[f[1]])
            return evac(x,y)
        else:
            x[k[f[0]]]-=1
            y.append(k[f[0]])
            return evac(x,y)







def jamc():

    a=int(raw_input())
    z=a
    while(a>0):
        di={}
        b=int(raw_input())
        for i in range(b):
            di[d[i]]=0

        numbers = map(int, raw_input().split())

        for i in range(b):
            di[d[i]]=numbers[i]
        p=[]
        l=evac(di,[])

        p.append("Case #"+str(z-a+1)+":")

        for i in l:
            p.append(i)

        o=' '.join(map(str,p))
        print(o)


        a-=1





jamc()
