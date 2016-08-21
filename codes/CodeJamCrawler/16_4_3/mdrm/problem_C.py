import sys
from random import randint

from collections import Counter,deque
from itertools import combinations

import itertools

IS_LOCAL = False
try:
    import os
    IS_LOCAL = os.getenv("AGLAE") == "nondual" and os.getenv("SIDONIE") == "improbable"
except:
    pass

def read_ints(inp = sys.stdin):
    return list(map(int,next(inp).strip().split()))


def sol1(r, c, P):

    args = [iter(P)] * 2
    pairs = list(zip(*args))

    for sol in itertools.product(*(["/\\"] *(r*c))):

        def get(i,j):
            return sol[i*c+j]
        def pos(a):
            if a<c:
                return 0,a,'v'
            a-=c
            if a<r:
                return a,c-1,'<'
            a-=r
            if a<c:
                return r-1,c-1-a,'^'
            a-=c
            return r-1-a,0,'>'
        def pos2(a):
            if a<c:
                return -1,a,'v'
            a-=c
            if a<r:
                return a,c,'<'
            a-=r
            if a<c:
                return r,c-1-a,'^'
            a-=c
            return r-1-a,-1,'>'

        for a,b in pairs:
            a-=1
            b-=1
            y,x,d = pos(a)
            while 0<=x<c and 0<=y<r:
                if get(y,x)=='/':
                    if d=='v':
                        x-=1
                        d='<'
                    elif d=='<':
                        y+=1
                        d='v'
                    elif d=='^':
                        x+=1
                        d='>'
                    else:
                        y-=1
                        d='^'
                else:
                    if d=='v':
                        x+=1
                        d='>'
                    elif d=='<':
                        y-=1
                        d='^'
                    elif d=='^':
                        x-=1
                        d='<'
                    else:
                        y+=1
                        d='v'
            yy,xx,_ = pos2(b)
            if x!=xx or y!=yy:
                break
        else:
            res = [''.join(sol[k*c:(k+1)*c]) for k in range(r)]
            return '\n'.join(res)
    return "IMPOSSIBLE"

if IS_LOCAL:
    inp = iter("""4
1 1
1 4 3 2
1 3
1 8 2 7 3 4 5 6
2 2
8 1 4 5 2 3 7 6
1 1
1 3 2 4
""".split('\n'))
    # inp = iter(map(str,[6, "2 3 2", "1 1 1", "2 1 1", "2 1 2", "3 2 3", "100 9 50"]))
    # inp = open("A-small-attempt0.in")
    inp = sys.stdin
else:
    inp = sys.stdin

T ,= read_ints(inp)
# T=1
mm = 0
for t in range(T):
    r,c, =read_ints(inp)
    pairs=read_ints(inp)
    x = sol1(r,c,pairs)
    # if i>=mm:
    #     print(N,i,x)
    #     mm=i
    print("Case #%d:\n%s" % (t+1,x) )
