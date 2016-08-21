#! /usr/bin/env pypy

import sys

n = int(sys.stdin.readline().strip())

parties = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def senate_major(p):
    '''
    -> (party_id, majority_count, total_count, party_id_2ndmajor)
    '''
    maxp = maxp_last = None
    maxc = 0
    tot = 0
    for i in range(len(p)):
        if p[i] >= maxc:
            maxp_last = maxp
            maxp = i
            maxc = p[i]
        tot += p[i]
    return (maxp, maxc, tot, maxp_last)
    

def solve(arg):
    n, p = arg
    # indoor = sum(p.values())
    r = []

    while 1:
        pout = ""
        pid, pn, indoor_, pidx = senate_major(p)
        if pn == 0:
            break
        p[pid] -= 1
        pout += parties[pid]
        if indoor_ >= 2:
            pid2, pn2, indoor_2, pidx2 = senate_major(p)
            p_ = p[:]
            p_[pid2] -= 1
            pid3, pn3, indoor_3, pidx3 = senate_major(p_)
            if not (pn3 > (indoor_3 - pn3)):
                pout += parties[pid2]
                p[pid2] -= 1
        r.append(pout)
    
    return " ".join(r)


for i in range(n):
    line = sys.stdin.readline().strip()
    N = int(line)
    line = sys.stdin.readline().strip()
    P = [ int(x) for x in line.split(" ") ]
    r = solve((N, P))
    print("Case #{}: {}".format(i+1, r))

