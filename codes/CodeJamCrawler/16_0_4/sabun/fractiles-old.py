#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sabu
if __name__ == "__main__":
    #get number of tests  
    testcases = int(input())                       
    #for each testcase
    for caseNr in range(1, testcases+1):
        #get inputs
        K, C, S = [int(x) for x in input().split()]
        #logic for small set (S=K)
        tiles = []
        #tile index
        cm = 0
        #degenerated number of tiles after C cycles
        kp = K**(C-1)
        for i in range(S):   
            tiles.append(cm+1) 
            cm += kp              
        print("Case #%i:" % (caseNr), ' '.join(map(str, tiles)))       
