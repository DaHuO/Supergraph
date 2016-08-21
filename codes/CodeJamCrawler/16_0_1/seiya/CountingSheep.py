#!/usr/bin/env python
# -*- coding: utf-8 -*-

inFile = open("input.txt","r")
outFile = open("output.txt","w")

def solve(case, N):
    digitsDic = {}
    number = "INSOMNIA"
    if N != 0:
        for i in range(1, 1000):
            if N == 0 or i > 999:
                number = "INSOMNIA"
                break
            number = N * i 
            numberStr = str(number)
            for i in range(len(numberStr)):
                digitsDic[numberStr[i]] = 1
            if len(digitsDic) >= 10:
                break
    return "Case #%d: %s\n" % (case, number) 

if __name__ == "__main__":
    isFirst = True
    totalCase = 0
    currentCase = 1 

    for line in inFile.readlines():
        items = line.split()

        # first Line
        if isFirst == True:
            isFirst = False
            totalCase = int(items[0])
            continue
        
        # execute
        out = solve(currentCase, int(items[0]))
        outFile.write(out)
        print out
        
        # go next
        currentCase = currentCase + 1
        if currentCase > totalCase:
            break
    
