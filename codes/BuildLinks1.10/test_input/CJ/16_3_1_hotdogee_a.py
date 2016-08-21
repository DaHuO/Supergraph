#!/usr/bin/env python
# -*- coding: utf-8 -*-

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def solve(p):
    t = sum(p) # total
    ep = [] # evacuation plan
    pt = zip(alpha, p) # [('A', 1), ('B', 2), ('C', 3)]
    while (t > 0):
        es = '' # evacuation step
        pt = sorted(pt, key=lambda x: x[1], reverse=True)
        es += pt[0][0]
        pt[0] = (pt[0][0], pt[0][1]-1)
        t -= 1
        if t == 2:
            ep.append(es)
            continue
        if pt[1][1] > pt[0][1]:
            es += pt[1][0]
            pt[1] = (pt[1][0], pt[1][1]-1)
            t -= 1
        else:
            es += pt[0][0]
            pt[0] = (pt[0][0], pt[0][1]-1)
            t -= 1
        ep.append(es)
        #print ep, t, pt
    return ' '.join(ep)
    

if __name__ == "__main__":
    for case in xrange(1, 1+input()):
        n = input()
        p = [int(pi) for pi in raw_input().strip().split()]
        print "Case #{0}: {1}".format(case, solve(p))