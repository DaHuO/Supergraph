def solve(inp):
    res = 0
    for i in range(0, len(inp) - 1):
       if (inp[i] != inp[i+1]):
           res += 1
    if (inp[len(inp) - 1] == '-'):
        res += 1
    return res

#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
