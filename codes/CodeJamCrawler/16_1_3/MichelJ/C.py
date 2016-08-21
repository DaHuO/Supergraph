"""
Code Jam 2016 Round 1A 2016
Problem C. BFF
"""

from __future__ import print_function
import sys
import StringIO
from functools import partial
from autolog import logfunction

msg = partial(print, file=sys.stderr)

#===========================================================================

# import networkx as nx
from itertools import permutations
    

def doit(BFF, N):
    for i in xrange(N):
        BFF[i] -= 1
    alli = range(N)
    for l in xrange(N, 2, -1):
        for p in permutations(alli, l):
            ok = True
            for i in xrange(l):
                if BFF[p[i]] != p[(i+1)%l] and BFF[p[i]] != p[(i-1)%l]:
                    ok = False
                    break
            if ok:
                return l
    return "ERROR !"
        


sample = """4
4
2 3 4 1
4
3 3 4 1
4
3 3 4 3
10
7 8 10 10 9 2 9 6 3 3
"""

#===========================================================================

def stripnl(s):
    if s[-1]=="\n":
        return s[:-1]
    return s

def main(data = None):
    if data is None:
        f = sys.stdin
    else:
        f = StringIO.StringIO(data)
    nt = int(f.readline())
    for tc in xrange(1, nt+1):
        N = int(f.readline())
        BFF = map(int, stripnl(f.readline()).split(" "))
        res = doit(BFF, N)
        msg( "Case #%d: %s" % (tc, res) )
        print( "Case #%d: %s" % (tc, res) )

main()
