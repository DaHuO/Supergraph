import sys
import math


def solve(s):
    if (len(s) == 0):
        return 0
    if (len(s) == 1):
        if s == "-":
            return 1
        if s == "+":
            return 0

    s = s + "+"
    res = 0
    for i in xrange(len(s) - 1):
        if s[i] != s[i+1]:
            res += 1

    return res

results = []

with open(sys.argv[1]) as f:
    T = int(f.readline().rstrip())
    for i in xrange(T):
        S = f.readline().rstrip()
        results.append(solve(S))

for i, r in enumerate(results):
    print "Case #{0}: {1}".format(i + 1, r)
