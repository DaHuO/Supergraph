import time
##import sys
##sys.setrecursionlimit(10002)
INFILE='bs.in'
OUTFILE='b.out'
import itertools

def solve(n,k,m):
    p=0
    for i in itertools.combinations(m,k):
        t=cal(i)
        if t>p:
            p=t
    return p

def cal(m):
    l=itertools.combinations(range(len(m)),len(m)/2)
    s=0
    for i in l:
        t=1
        for j in range(len(m)):
            if j in i:
                t*=m[j]
            else:
                t*=(1-m[j])
        s+=t
    return s


def read_input(fi):
    read=lambda type:type(fi.readline()[:-1])
    readArray=lambda type:map(type,fi.readline().split())
    readMatrix=lambda type,x:[map(type,fi.readline().split()) for i in range(x)]
    readLines=lambda type,x:[type(fi.readline()[:-1]) for i in range(x)]
    n,k=readArray(int)
    m=readArray(float)
    return n,k,m

def main():
    fi=file(INFILE)
    fo=file(OUTFILE,'w')
    time0=time.time()
    t=int(fi.readline())
    for ti in range(t):
        time1=time.time()
        t=read_input(fi)
        ans="Case #%d: %s"%(ti+1,solve(*t))
        print ans,"%.3f"%(time.time()-time1)
        fo.write(ans+'\n')
    print "%.3f"%(time.time()-time0)
    fi.close()
    fo.close()


if __name__ == '__main__':
    main()
    # print cal([1,0])