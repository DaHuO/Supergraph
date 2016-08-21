import sys
from random import randint

from collections import Counter,deque
from itertools import combinations

IS_LOCAL = False
try:
    import os
    IS_LOCAL = os.getenv("AGLAE") == "nondual" and os.getenv("SIDONIE") == "improbable"
except:
    pass

def read_ints(inp = sys.stdin):
    return list(map(int,next(inp).strip().split()))


def sol1(S):
    res = [S[0]]
    for x in S[1:]:
        if x>=res[0]:
            res.insert(0,x)
        else:
            res.append(x)
    return "".join(res)


if IS_LOCAL:
    # inp = iter(map(str,[8, "A", "CAB", "MJA", "OCDE", "BBAAA", "CCCABBBAB", "CCCBAABAB", "ZXCASDQWE" ]))
    # inp = open("A-small-attempt0.in")
    inp = sys.stdin
else:
    inp = sys.stdin

T ,= read_ints(inp)
# T=1
mm = 0
for t in range(T):
    S = next(inp).strip()
    x = sol1(S)
    # if i>=mm:
    #     print(N,i,x)
    #     mm=i
    print("Case #%d: %s" % (t+1,x) )
