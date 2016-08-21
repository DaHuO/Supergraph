#!/usr/bin/python

import sys
from pprint import pprint

def solve(N):
    if not N:
        return 'INSOMNIA'
    found = set([])
    sheep = 0
    while len(found) < 10:
        sheep += N
        s_str = str(sheep)
        for i in xrange(len(s_str)):
            digit = s_str[i:i+1]
            if digit not in found:
                found.add(digit)
    return sheep

if __name__ == '__main__':

    case_N = int(sys.stdin.readline().strip())
    #pprint(case_N)
    for n in xrange(case_N):
        N = int(sys.stdin.readline().strip())
        ans = solve(N)
        print 'Case #' + str(n+1) + ': ' + str(ans)
