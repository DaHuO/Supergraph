#!/usr/bin/env python2
from sys import stdin, stdout, stderr

def solve(case):
    ret = case[0]
    for c in case[1:]:
        if c < ret[0]:
            ret = ret + c
        else:
            ret = c + ret
    return ret

stdin.next()
for idx, case in enumerate(stdin, 1):
    answer = solve(case.rstrip())
    print "Case #%d: %s" % (idx, answer)
    stdout.flush()
