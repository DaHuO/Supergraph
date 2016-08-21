#!/usr/bin/python
import sys

def stackOk(stack):
    ok = True
    for v in stack: ok &= v > 0
    return ok

def reverseStack(stack, lastIdx):
    nstack = stack[:]
    for i in xrange(lastIdx + 1):
        nstack[i] = -stack[lastIdx - i]
    return nstack


for tc in xrange(1, int(sys.stdin.readline()) + 1):
    result = 0
    pancakes = sys.stdin.readline()
    length = len(pancakes) - 1
    stack = [0] * length
   
    for i in xrange(length):
        stack[i] = 1 if pancakes[i] == '+' else -1
    
    while not stackOk(stack):
        lastMinusIdx = -1
        for i in xrange(length):
            if stack[i] < 0: lastMinusIdx = i
        longestPlusIdx = -1
        while longestPlusIdx + 1 < lastMinusIdx and stack[longestPlusIdx + 1] > 0:
            longestPlusIdx += 1
        
        if lastMinusIdx > -1:
            if longestPlusIdx > -1:
                stack = reverseStack(stack, longestPlusIdx)
                result += 1
            stack = reverseStack(stack, lastMinusIdx)
            result += 1
    
    print "Case #{}: {}".format(tc, result)
