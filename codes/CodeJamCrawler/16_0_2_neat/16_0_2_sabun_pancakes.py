#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sabu
if __name__ == "__main__":
    testcases = int(input())                    #get number of tests     
    for caseNr in range(1, testcases+1):        #for each testcase
        plate = input()                         #get input based on problem
        flips = 0
        ht = len(plate)
        while ('-' in plate):
            icut = ht
            #find the first one from top which shows a different side
            for i in range(1, ht):
                if plate[i]!=plate[i-1]:
                    icut = i
                    break
            #flip the stack at icut from top (cut, reverse, flip, put it down)
            plate = ''.join('-' if c=='+' else '+' for c in plate[:icut][::-1]) + plate[icut:]
            flips += 1
        print("Case #%i: %i" % (caseNr, flips))