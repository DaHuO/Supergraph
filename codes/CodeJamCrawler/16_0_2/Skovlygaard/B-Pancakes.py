#!/usr/bin/env python

import sys

f = sys.stdin
testcasecount = int(f.readline())

#print(testcasecount)


def flip(stack, n):
    #print("flip(%r, %d)" % (stack, n))
    while n >= 0:
        if stack[n] == '+':
            stack[n] = '-'
        else:
            stack[n] = '+'
        n -= 1
    return stack

for case in range(testcasecount):
    #print("Case #%d:" % (case +1) )
    stack = list(f.readline()[:-1])
    #print(stack)
    flips = 0
    
    pancake = len(stack)-1
    while pancake >= 0:
        if stack[pancake] =='-':
            stack = flip(stack, pancake)
            flips += 1
        #print("%d New stack %s" % (pancake, stack))
        pancake -= 1
        
    print("Case #%d: %d" % ((case+1), flips))
    
    