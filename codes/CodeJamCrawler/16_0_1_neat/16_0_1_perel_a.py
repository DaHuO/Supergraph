import time
##import sys
##sys.setrecursionlimit(10002)

def solve(n):
    if n==0:
        return 'INSOMNIA'
    df=[0]*10
    i=1
    while 1:
        a=n*i
        while a:
            df[a%10]=1
            a/=10
        if sum(df)==10:
            ans=n*i
            break
        i+=1
    return str(ans)

def main():
    fi=file('al.in')
    fo=file('a.out','w')
    time0=time.time()
    t=int(fi.readline())
    for ti in range(t):
        time1=time.time()
        n=int(fi.readline())
        ans="Case #%d: %s"%(ti+1,solve(n))
        print ans,"%.3f"%(time.time()-time1)
        fo.write(ans+'\n')
    print "%.3f"%(time.time()-time0)
    fi.close()
    fo.close()

if __name__ == '__main__':
    main()
##    for i in range(50000,50999):
##        time0=time.time()
##        print i,solve(i),
##        print time.time()-time0
