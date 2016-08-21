import sys
fileinput = sys.stdin

import StringIO
#fileinput = StringIO.StringIO(inputstr)

from  heapq import *
import string
A=string.ascii_uppercase
A=[a for a in A]


T=int(fileinput.readline().strip())
for t in range(T):
    N=fileinput.readline().strip()
    N=int(N)
    P=fileinput.readline().strip().split()
    P=[int(p) for p in P]
    h = []
    S=0
    for n in range(N):
        heappush(h, (-P[n], A[n]))
        S += P[n]
    O=[]
    while True:
        p=heappop(h)
        if p[0]==0:
            break
        S=S-1
        heappush(h, (-(-p[0]-1), p[1]))
        o=p[1]
        if -h[0][0]>S/2:
            p=heappop(h)
            S=S-1
            heappush(h, (-(-p[0]-1), p[1]))
            o=o+p[1]
        O.append(o)
    O=" ".join(O)    
    print "Case #%s: %s" % (t+1, O)

            