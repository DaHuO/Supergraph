t=input()
for kk in xrange(0,t):
    s="Case #"+str(kk+1)+":"
    n=input()
    h=[0]*10
    if n==0:
        print s,"INSOMNIA"
    else:
        for i in xrange(1,5000000):
            ans=n*i
            while ans>0:
                r=ans%10
                h[r]=1
                ans=ans/10
            ans=n*i
            if sum(h)==10:
                print s,ans
                break
            
