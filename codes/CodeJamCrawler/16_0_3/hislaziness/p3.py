# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:29:57 2015

@author: vbd
"""

import cPickle

inp = raw_input()
T = int(inp)

for c in range(1,T+1) :
    inp = raw_input().strip().split()
    N = inp[0]
    J = int(inp[1])

    fp = open("C:/VBD/ws/code/GCJ 2016/qual/P3/"+ N + ".jamcoins")
    out = cPickle.load(fp)
    fp.close()
    
    print "Case #{0}:".format(c)
    count = 0
    for key in out:
        val = out[key]
        print key,val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7],val[8]
        count += 1
        if count >= J:
            break
