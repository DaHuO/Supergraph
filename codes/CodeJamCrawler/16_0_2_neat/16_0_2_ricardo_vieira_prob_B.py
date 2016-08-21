#!/usr/bin/env python

import sys

n_cases = int(sys.stdin.readline())

counter = []

def flip(stack, depth):
    to_flip = stack[:depth+1]
    to_flip.reverse()
    for x, pancake in enumerate(to_flip):
        if pancake == '+':
            to_flip[x] = '-'
        else:
            to_flip[x] = '+'
    return to_flip + stack[depth+1:]

for case_itr in range(1, n_cases+1):
    stack = list(sys.stdin.readline()[:-1])
    counter = 0
    for depth in reversed(range(len(stack))):
        #print("".join(stack))
        if stack[depth] == '-':
            if stack[0] == '+':
                pre_flip = "".join(stack).find('-')
                stack = flip(stack, pre_flip)
                counter += 1
            stack = flip(stack, depth)
            counter += 1
        #print(counter)
    print("Case #" + str(case_itr) + ": " + str(counter))
