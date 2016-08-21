#!/usr/bin/env python

import copy
from pprint import pprint

def printResult(case, result):
    numResult = len(result)
    if numResult == 0:
        print "Case #{}: {}".format(case, "IMPOSSIBLE")
    else:
        f = "Case #%d:" + " %d" * numResult
        results = (case, ) + tuple(result)
        print f % results

t = int(raw_input())
for case in xrange(1, t + 1):
    K,C,S = [int(s) for s in raw_input().split(" ")]
    positions = range(1,K+1)
    for i in range(C-1):
        positions = [((x-1)*K)+1 for x in positions]
    printResult(case, tuple(positions))
