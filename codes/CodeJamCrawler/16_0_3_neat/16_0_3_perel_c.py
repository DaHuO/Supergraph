import time
##import sys
##sys.setrecursionlimit(10002)
prime=[]
def init(maxn):
    global prime
    ok=[0]*(maxn+1)
    for i in range(2,maxn+1):
        if not ok[i]:
            prime.append(i)
##            for j in xrange(i*i,maxn+1,i):
            j=i*i
            while j<=maxn:
                ok[j]=1
                j+=i
    return

import bisect
def getFactor(n):
    p=bisect.bisect_right(prime,int(n**0.5))
    for i in prime[:p]:
        if n%i==0:
            return i
    return 0

def solve(n,m):
    init(10**4-1)
    ans=[]
    i=2**(n-1)+1
    while i<2**n:
##    for i in xrange(2**(n-1)+1,2**n,2):
        s=bin(i)[2:]
        ln=[int(s,j) for j in range(2,11)]
        res=[getFactor(j) for j in ln]
        if all(res):
            ans.append((s,res))
            if len(ans)==m:
                break
        i+=2
    return '\n'+'\n'.join([i[0]+' '+' '.join([str(j) for j in i[1]]) for i in ans])

def main():
    fi=file('cl.in')
    fo=file('c.out','w')
    time0=time.time()
    t=int(fi.readline())
    for ti in range(t):
        time1=time.time()
        n,j=map(int,fi.readline().split())
        ans="Case #%d:%s"%(ti+1,solve(n,j))
        print ans,"%.3f"%(time.time()-time1)
        fo.write(ans+'\n')
    print "%.3f"%(time.time()-time0)
    fi.close()
    fo.close()

if __name__ == '__main__':
    main()
##    print len(prime)
##    time0=time.time()
##    init(2**16-1)
##    print len(prime),time.time()-time0
