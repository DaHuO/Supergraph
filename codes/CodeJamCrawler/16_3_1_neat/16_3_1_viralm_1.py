data='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def f(s,ar):
    if((min(ar)>=0) and (sum(ar)==0)):
        print template,s
        return 1
    val=-1
    for i in xrange(0,n):
        for j in xrange(0,n):
            if(val==1):
                return 1
            z=[]
            for k in ar:
                z.append(k)
            z[i]-=1
            z[j]-=1
            if((z[i]>=0) and (z[j]>=0) and (2*max(z)<=sum(z))):
                if(val==1):
                    return 1
                temp=s+data[i]+data[j]+" "
                val=f(temp,z)
                if(val==1):
                    return 1
    for i in xrange(0,n):
        z=[]
        for k in ar:
            z.append(k)
        z[i]-=1
        if((z[i]>=0) and (2*max(z)<=sum(z))):
            temp=s+data[i]+" "
            if(val==1):
                return 1
            val=f(temp,z)
            if(val==1):
                return 1
t=input()
tc=0
template=""
while(tc<t):
    tc+=1
    template="Case #"+str(tc)+":"
    n=input()
    l=[int(i) for i in raw_input().split()]
    f("",l)
    
