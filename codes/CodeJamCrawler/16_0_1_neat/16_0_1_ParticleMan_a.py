#!/usr/bin/env python

def printResult(case, result):
    print "Case #{}: {}".format(case, result)

def getDigits(num):
    return set(int(x) for x in str(num))
    
t = int(raw_input())
for i in xrange(1, t + 1):
    start, = [int(s) for s in raw_input().split(" ")]
    if start == 0:
        printResult(i, "INSOMNIA")
        continue
    remaining = set(range(10))
    curr = start
    while len(remaining) > 0:
        remaining = remaining - getDigits(curr)
        curr += start
    printResult(i, curr - start)
