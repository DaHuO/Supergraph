#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout

from operator import itemgetter

def party_letter(n):
    return chr(ord('A') + n)


def check_invariant(P):
    S = sum(p for __, p in P)
    half = S / 2
    #print 'half:', half
    #print 'all:', map(lambda p: p[1] <= half, P)
    return all(map(lambda p: p[1] <= half, P))


def solve(P):
    P = [(party_letter(i), p) for i, p in enumerate(P)]
    #print 'initial:', P
    plan = []
    while len(P) > 0:
        P = sorted(P, key=itemgetter(1))
        largest = P[-1]
        evacuate = largest[0]
        deleted = False
        if largest[-1] > 1:
            P[-1] = (largest[0], largest[-1]-1)
        else:
            deleted = True
            del P[-1]
        if not check_invariant(P):
            next_party_index = -2 if not deleted else -1
            next_party = P[next_party_index]
            evacuate += next_party[0]
            if next_party[1] > 1:
                P[next_party_index] = (next_party[0], next_party[1]-1)
            else:
                del P[next_party_index]
#         if not check_invariant(P):
#             print 'failed!'
#             print P
#             print evacuate
#             print plan
#             import sys
#             sys.exit()
        plan.append(evacuate)
    return plan


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


T = int(ifs.readline())
for t in range(1, T + 1):
    #print t
    __ = int(ifs.readline())
    P = numbers_from_line()
    plan = solve(P)
    ofs.write('Case #%s: %s\n' % (t, ' '.join(plan)))
