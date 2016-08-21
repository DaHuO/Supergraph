#!/bin/env python

count = int(raw_input())

def flip(stack):
    #print "orig:", stack
    if len(stack) == 1:
        if stack[0] == '-':
            return 1
        else:
            return 0
    
    moves = 0
    if stack[-1] == '+':
        ##print stack
        return flip(stack[:-1])

    moves = 1
    
    if stack[0] == '+':
        for i in range(0, len(stack)):
            if stack[i] == '+':
                stack[i] = '-'
            else:
                break
        moves = 2

    stack = map((lambda x : '-' if x == '+' else '+'), stack)
    #print "rev:", stack
    
    stack = stack[::-1]
    #print "flip:", stack
    return moves + flip(stack[:-1])

for i in range(0, count):
    stack = raw_input()
    last_char = '+'
    n_moves = 0

    stack = map((lambda x : '-' if x == '-' else '+'), stack)
    
    #print flip(stack)

    print "Case #" + str(i+1) + ":", flip(stack)
#    for c in stack[::-1]:
#        if last_char != c:
#            last_char = c
#            n_moves += 1

