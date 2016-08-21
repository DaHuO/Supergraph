"""
Code Jam 2016 Round 1A 2016
Problem B. Rank and File
"""

from __future__ import print_function
import sys
import StringIO
from functools import partial
from autolog import logfunction

msg = partial(print, file=sys.stderr)

#===========================================================================

import numpy as np


def try_set(a, pairs, l, missing, N, is_row):
    if len(pairs) == 0:
        yield a, is_row
    else:
        if l == missing:
            p0 = pairs[0][0]
            row_ok = True
            col_ok = True
            for i in xrange(N):
                if a[l,i] != 0 and a[l,i] != p0[i]:
                    row_ok = False
                if a[i,l] != 0 and a[i,l] != p0[i]:
                    col_ok = False
            if row_ok:
                b = np.copy(a)
                b[l] = p0
                for ret in try_set(b, pairs[1:], l+1, missing, N, False):
                    yield ret
            if col_ok:
                b = np.copy(a)
                b[:,l] = p0
                for ret in try_set(b, pairs[1:], l+1, missing, N, True):
                    yield ret
        else:
            p0,p1 = pairs[0]
            row_ok = True
            col_ok = True
            for i in xrange(N):
                if (a[l,i] != 0 and a[l,i] != p0[i]) or (a[i,l] != 0 and a[i,l] != p1[i]):
                    row_ok = False
                if (a[i,l] != 0 and a[i,l] != p0[i]) or (a[l,i] != 0 and a[l,i] != p1[i]):
                    col_ok = False
            if row_ok:
                b = np.copy(a)
                b[l] = p0
                b[:,l] = p1
                for ret in try_set(b, pairs[1:], l+1, missing, N, is_row):
                    yield ret
            if col_ok:
                b = np.copy(a)
                b[l] = p1
                b[:,l] = p0
                for ret in try_set(b, pairs[1:], l+1, missing, N, is_row):
                    yield ret
        
    
    

def doit(N, p):
    lp = len(p)
    a = np.zeros((N,N), dtype = np.int32)
    pairs = []
    for i in xrange(N):
        p.sort(lambda x, y: cmp(x[i], y[i]))
        if len(p) >= 2 and p[0][i] == p[1][i]:
            pairs.append((p[0], p[1]))
            p = p[2:]
        else:
            pairs.append((p[0], None))
            missing = i
            p = p[1:]
#    msg(pairs)
#    msg(missing)

    a[0] = pairs[0][0]
    is_row = None
    if missing > 0:
        a[:,0] = pairs[0][1]
        is_row = False
    for ret in try_set(a, pairs[1:], 1, missing, N, is_row):
        full, is_row = ret
#        msg(full, is_row)
        if is_row:
            sol = list(full[missing])
        else:
            sol = list(full[:,missing])
#        msg(sol)
        return " ".join(map(str,sol))
    return "ERROR !"
        


sample = """1
3
1 2 3
2 3 5
3 5 6
2 3 4
1 2 3
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
        papers = [np.array(map(int, stripnl(f.readline()).split(" ")), dtype = np.int32) for n in xrange(2 * N - 1)]
        assert len(papers[0]) == N
        res = doit(N, papers)
        msg( "Case #%d: %s" % (tc, res) )
        print( "Case #%d: %s" % (tc, res) )

main()
