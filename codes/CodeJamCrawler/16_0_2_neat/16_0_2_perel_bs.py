import time
##import sys
##sys.setrecursionlimit(10002)
from collections import deque
def flip(s):
    return tuple(reversed([not i for i in s]))

def solve(s):
    s=tuple([i=='+'  for i in s])
    return str(solve11(s))

def solve11(s):
    for i in range(len(s)-1,-1,-1):
        if not s[i]:
            break
    else:
        return 0
    s=s[:i+1]
    step=0
    for i in range(len(s)):
        if not s[i]:
            break
    else:
        return 1
    if i:
        step+=1
        s=flip(s[:i])+s[i:]
    return solve11(flip(s))+step+1


def main():
    fi=file('bl.in')
    fo=file('b.out','w')
    time0=time.time()
    t=int(fi.readline())
    for ti in range(t):
        time1=time.time()
        s=fi.readline()[:-1]
        ans="Case #%d: %s"%(ti+1,solve(s))
        print ans,"%.3f"%(time.time()-time1)
        fo.write(ans+'\n')
    print "%.3f"%(time.time()-time0)
    fi.close()
    fo.close()

if __name__ == '__main__':
    main()
