#!/usr/bin/python

from collections import defaultdict
import sys

def out(senators):
    if len(senators) == 2:
        s0, s1 = senators[0], senators[1]
        print '%s%s' % (s0[1], s1[1]),
        return [ (s0[0]-1, s0[1]), (s1[0]-1, s1[1]) ]
    else:
        idx = 0
        largest = senators[0]
        for i, s in enumerate(senators):
            if s[0] > largest[0]:
                largest = s
                idx = i
        print '%s' % (largest[1]),
        return senators[:idx] + [ (largest[0]-1, largest[1]) ] + senators[idx+1:]


def solve(seq):
    senators = [ (n, chr(ord('A') + i)) for i, n in enumerate(seq) ]
    senators.sort(reverse=True)
    while any( True for s in senators if s[0] > 0 ):
        senators = out(senators)
        senators = filter(lambda s: s[0] > 0, senators)


lines = sys.stdin.readlines()
T = int(lines[0])

i = 1
case = 1
while i < len(lines):
    ln = lines[i].strip()
    n = int(ln)
    i += 1
    ln = lines[i].strip()
    i += 1
    nums = [int(e) for e in ln.split(' ')]

    if case > 1:
        print ''
    print 'Case #%d:' % (case, ),
    solve(nums)
    case +=1
