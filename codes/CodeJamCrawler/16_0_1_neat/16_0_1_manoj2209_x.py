t=int(raw_input())
for x in xrange(t):
    n=int(raw_input())
    i=1
    l=[0]*10
    temp=n
    if n==0:
        print 'Case #%d: INSOMNIA'%(x+1)
    else:
        while(sum(l)!=10):
            s=str(temp)
            for a in s:
                if l[int(a)]==0:
                    l[int(a)]+=1
            i+=1
            temp=n*i
        print 'Case #%d: %d'%(x+1,(n*(i-1)))