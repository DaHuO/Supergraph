#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

def getAllSingleDigit(num):
    digitNumSet = set()
    for ele in str(num):
        digitNumSet.add(ele)
    return digitNumSet

def CS(StartCountNum):
    if StartCountNum == 0:
        return 'INSOMNIA'
    RoundCount = 1
    currentDigitNumSet = set()
    while(True):
        countingNum = RoundCount * StartCountNum
        currentDigitNumSet = currentDigitNumSet.union(getAllSingleDigit(countingNum))
        #print currentDigitNumSet
        if len(currentDigitNumSet) == 10:
            break
        RoundCount += 1
        #print countingNum
    return RoundCount * StartCountNum



f = open("A-large.in", "r")
#f = open("C-small-attempt1.in", "r")
#f = open("C-small-attempt0.in", "r")
#f = open("D.in", "r")

T = int(f.readline())

for x in range(0, T):
    readline = f.readline()
    print "Case #" + str(x+1) + ": " + str(CS(int(readline)))

