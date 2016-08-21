import time
##import sys
##sys.setrecursionlimit(10002)
def solve(k,c,s):
    return ' '.join([str(i) for i in range(1,k+1)])

def main():
    fi=file('ds.in')
    fo=file('d.out','w')
    time0=time.time()
    t=int(fi.readline())
    for ti in range(t):
        time1=time.time()
        k,c,s=map(int,fi.readline().split())
        ans="Case #%d: %s"%(ti+1,solve(k,c,s))
        print ans,"%.3f"%(time.time()-time1)
        fo.write(ans+'\n')
    print "%.3f"%(time.time()-time0)
    fi.close()
    fo.close()

if __name__ == '__main__':
    main()
