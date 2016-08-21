# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 19:56:36 2016

@author: Emad Yehya
"""

inp = file('C-small-attempt1.in', 'r')
o = file('out.txt', 'w')

T = int(inp.readline())
for t in range(1, T+1):
    print t
    N = int(inp.readline())
    WORDS = []
    for i in range(0, N):
        L = inp.readline()[:-1].split(' ')
        WORDS.append(L)
    
    maxv = 0
    for i in range(1, 2**N):
        bi = str(bin(i))[2:]
                
        bi = "0"*(N-len(bi)) + bi
        c0 = bi.count('0')
        if(c0 <= maxv):
            continue

        YESF = []
        NOF = []
        YESS = []
        NOS = []

        for bii in range(0, len(bi)):
            if(bi[bii] == '1'):
                YESF.append(WORDS[bii][0])
                YESS.append(WORDS[bii][1])
            else:
                NOF.append(WORDS[bii][0])
                NOS.append(WORDS[bii][1])
        fine = True
        for x in NOF:
            if x not in YESF:
                fine = False
                break
        for y in NOS:
            if y not in YESS:
                fine = False
                break
        if(not fine):
            continue
        
        if(c0 > maxv):
            maxv = c0
        
    o.write("Case #" + str(t) + ": " + str(maxv) + "\n")
                