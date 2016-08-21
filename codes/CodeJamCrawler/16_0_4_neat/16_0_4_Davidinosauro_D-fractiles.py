#!/usr/bin/env python2
from __future__ import division, print_function

import sys
import math
from itertools import izip, tee, izip_longest
from pprint import pprint as pp
from collections import Counter, namedtuple
import operator as op


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)


def dbg(*args, **kwargs):
    kwargs['file'] = sys.stderr
    print(*args, **kwargs)


def result(K, C, S):
    dbg((K, C, S))
    if C == 1:
        if S < K:
            return 'IMPOSSIBLE'
        else:
            return ' '.join(str(1+n) for n in range(K))
    if S < (K//2 + K%2):
        return 'IMPOSSIBLE'

    D = K**(C-1)
    # note: start with 0-based index
    sol = []   ## no:  [1 + n*D for n in range(1, K)]
    for a, b in grouper(range(K), 2, fillvalue=0):
        # if n is gold, then all items in  n*D..n*D+D-1  are gold
        # if n is gold, then all items at  i*K+n  for any  i  in range
        # also, in particular, n*D is a multiple of K
        sol.append(a*D + b)

    assert len(sol) == (K//2 + K%2)
    ret = ' '.join(str(1+x) for x in sol)  # convert to 1-besed index here
    return ret


if __name__ == '__main__':
    #sys.setrecursionlimit(max(2000, sys.getrecursionlimit()))
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        print('===', t+1, '===', file=sys.stderr)

        K, C, S = [int(x) for x in sys.stdin.readline().strip().split()]
        res = result(K, C, S)
        dbg('  ' + res)
        print('Case #{}: {}'.format(t+1, res))
        sys.stdout.flush()

