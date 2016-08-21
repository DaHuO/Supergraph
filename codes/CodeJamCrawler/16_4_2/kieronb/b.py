#!/usr/bin/python

import sys
import logging
import itertools

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def solve(n, k, probs):
    max_p = float('-inf')
    for c in itertools.combinations(range(n), k):
        p = 0.0
        for d in itertools.combinations(range(k), k/2):
            q = 1.0
            r = 1.0
            for i,j in enumerate(c):
                q *= probs[j] if i in d else 1.0 - probs[j]
            p += q
        max_p = max(max_p, p)

    return max_p


first = True
i = 0
for line in sys.stdin:
    if first:
        first = False
        counts = True
    elif counts:
        i += 1
        counts = False
        n, k = map(int, line.split())
    else:
        counts = True
        probs = map(float, line.split())
        ans = solve(n, k, probs)
        print "Case #%d: %f" % (i, ans)
