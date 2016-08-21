#!/usr/bin/env python
# -*- coding: utf-8 -*-

inFile = open("input.txt","r")
outFile = open("output.txt","w")

def solve(case, cakes):
    count = 0
    while True:
        if not "-" in cakes: 
            break
        if not "+" in cakes: 
            count += 1
            break

        if cakes.find("-") == 0:
            idx = cakes.find("+")
            cakes = "+"*idx + cakes[idx:]
        else:
            idx = cakes.find("-") 
            cakes = "-"*idx + cakes[idx:]
        count += 1
    
    return "Case #%d: %d\n" % (case, count) 

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
        out = solve(currentCase, items[0])
        outFile.write(out)
        print out
        
        # go next
        currentCase = currentCase + 1
        if currentCase > totalCase:
            break
    
