# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 19:28:47 2016

@author: Emad Yehya
"""

inp = open('B-small-attempt0.in', 'r')
o = open('out.txt', 'w')

T = int(inp.readline())

for t in range(1, T+1):
    L = inp.readline().split(' ')
    F = L[0]
    S = L[1]
    
    FL = []
    SL = []    
    
    for i in range(0, 10**(len(F))):
        si = str(i)
        si = "0"*(len(F)-len(si)) + si
        skip = False
        for p in range(0, len(F)):
            if(F[p] != si[p] and F[p] != '?'):
                skip = True
                break
        if(not skip):
            FL.append(i)
        skip = False
        for p in range(0, len(F)):
            if(S[p] != si[p] and S[p] != '?'):
                skip = True
                break
        if(not skip):
            SL.append(i)
            
    bf = 999999
    bs = 0
    mind = bf - bs
    for i in range(0, len(FL)):
        for j in range(0, len(SL)):
            if(abs(FL[i] - SL[j]) < mind):
                bf = FL[i]
                bs = SL[j]
                mind = abs(bf - bs)
            elif(abs(FL[i] - SL[j]) < mind):
                if(FL[i] < bf):
                    bf = FL[i]
                    bs = SL[j]
                    mind = abs(bf - bs)
                elif(FL[i] == bf):
                    if(SL[i] < bs):                        
                        bf = FL[i]
                        bs = SL[j]
                        mind = abs(bf - bs)
    bf = str(bf)
    bs = str(bs)
    bf = "0"*(len(F)-len(bf)) + bf
    bs = "0"*(len(F)-len(bs)) + bs
    
    print "Case #" + str(t) + ": " + bf + " " + bs + "\n"
    
    o.write("Case #" + str(t) + ": " + bf + " " + bs + "\n")
    
        