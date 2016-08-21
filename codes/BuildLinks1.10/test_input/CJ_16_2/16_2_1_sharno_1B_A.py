#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
inds = [0,6,5,4,3,2,8,7,9,1]
random.shuffle(inds)
def solve(s):
    s = [c for c in s]
    d = {}
    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1
    ans = []
    i = 0
    # print s
    while any(d[c] > 0 for c in d.keys()):
        digit = digits[inds[i]]
        dd = {}
        for c in digit:
            if c not in dd:
                dd[c] = 0
            dd[c] += 1
        if all(c in d.keys() for c in dd.keys()) and all(dd[c] <= d[c] for c in dd.keys()):
            ans.append(inds[i])
            for c in dd.keys():
                d[c] -= dd[c]
            # print "found ", inds[i], " ", d
        else:
            i += 1
    return "".join([str(c) for c in sorted(ans)])

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases + 1):
        s = str(raw_input())
        print("Case #%i: %s" % (caseNr, solve(s)))
