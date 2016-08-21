#!/usr/bin/python

import sys
import logging
import itertools

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def solve(n, r, p, s):
    if max(r, p, s) - min(r, p, s) > 1:
        return 'IMPOSSIBLE'

    for d in itertools.permutations('P'*p + 'R'*r + 'S'*s):
        c = d[:]
        ok = True
        for i in range(n):
            res = contest(c)
            if not res:
                ok = False
                break;
            c = res
        if not ok:
            continue
        return ''.join(d)



def winner(pair):
    if pair == {'R', 'P'}:
        return 'P'
    if pair == {'P', 'S'}:
        return 'S'
    if pair == {'S', 'R'}:
        return 'R'
    return 'X'

def contest(lst):
    r = []
    for i in range(len(lst) / 2):
        w = winner({lst[i*2], lst[i*2+1]})
        if w == 'X':
            return False
        r.append(w)
    return r




first = True
i = 0
for line in sys.stdin:
    if first:
        first = False
    else:
        i += 1
        n, r, p, s = map(int, line.split())
        ans = solve(n, r, p, s)
        print "Case #%d: %s" % (i, ans)
