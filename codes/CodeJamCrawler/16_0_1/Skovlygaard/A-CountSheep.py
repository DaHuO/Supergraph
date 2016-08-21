#!/usr/bin/env python

import sys

f = sys.stdin
testcasecount = int(f.readline())

#print(testcasecount)


for case in range(testcasecount):
    hits=[]
    N = int(f.readline())
    #print(N)
    
    if N == 0:
        print("Case #%d: INSOMNIA" % (case+1))
    else:
        i = 1
        while True:
            v = str(i * N)
        
        #print(v)
            for c in v:
                if c not in hits:
                    hits.append(c)
                
            if len(hits) == 10:
                print("Case #%d: %s" % (case+1, v))
                break
        
            if i > 1000000:
                print("Case #%d: INSOMNIA" % (case+1))
                break
        
            i += 1

