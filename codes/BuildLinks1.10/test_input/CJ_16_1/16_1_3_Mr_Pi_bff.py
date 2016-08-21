#!/usr/bin/env python

import sys
import os
import math
from collections import defaultdict, Counter

def get_answer(f):
    N = int(f.readline().strip())
    F = [x-1 for x in map(int, f.readline().strip().split())]
    
    #circle_set = set()
    #recip_set = set()  # Pairs of reciprocal
    recip_set = dict() # Reciprocal -> other one-way link length
    self_link = 0  # Length to contain a full circle, opposite of recip.
    into_account = set()
    for i in xrange(N):
        if F[F[i]] == i:
            #circle_set.add(i)
            #circle_set.add(F[i])
            recip_set[i] = 0
            recip_set[F[i]] = 0
            into_account.add(i)
            into_account.add(F[i])
            continue
            
    for i in xrange(N):
        if i in into_account: continue
        if recip_set.has_key(i): continue
        
        single_len = 1
        k = F[i]
        qset = Counter()
        qset[i] += 1
        into_account.add(i)
        #qset[k] += 1
        while not recip_set.has_key(k) and qset[k] < 2:
            #print(k, qset)
            into_account.add(k)
            qset[k] += 1
            k = F[k]
            single_len += 1
        if recip_set.has_key(k):
            recip_set[k] = max(recip_set[k], single_len)
        else:
            cyclelen = sum([1 for x in qset.values() if x == 2])
            self_link = max(self_link, cyclelen)
    
    with_recip = len(recip_set) + sum(recip_set.values())
    if with_recip > self_link:
        return with_recip
    else:
        return self_link


if __name__ == "__main__":
    input_filename = sys.argv[1]
    output_filename = input_filename[:-3]+".out"
    if input_filename == "test":
        output_filename = "test.out"

    with open(input_filename) as f:
        with open(output_filename, "w") as g:
            T = int(f.readline().strip())
            for test_idx in xrange(1,T+1):
                ans = get_answer(f)
                g.write("Case #"+str(test_idx)+": "+str(ans)+"\n")

    #
