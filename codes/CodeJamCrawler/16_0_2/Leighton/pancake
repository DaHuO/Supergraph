#!/usr/bin/env python
# William Leighton Dawson
# Google Code Jam Qualification Round
# Problem 2: Revenge of the Pancakes
# 2016-04-09

import sys

def switch(ls):
    sl = []
    for i in ls:
        if i == '+':
            sl.append('-')
        else:
            sl.append('+')
    return sl[::-1]


def find(stack):
    if stack[0] == '+':
        i = stack.index('-')
    elif '+' in stack:
        i = stack.index('+')
    else:
        i = -1
    return i


def flip(stack):
    #print "Stack: %s" % ("".join(stack))
    c = 0
    while '-' in stack:
        i = find(stack)
        if i == -1:
            stack = switch(stack)
        else:
            stack[:i] = switch(stack[:i])
        #print "%s: \tFlipping to %s" % (c, "".join(stack))
        c += 1
    #print "Result: %s\n" % ("".join(stack))
    return c


# Input as per spec. (with a few conveniences added :P)
if len(sys.argv) == 2:
    filename = sys.argv[-1]
else:
    filename = raw_input("Filename: ")
file = open(filename, 'r')
stacks = [list(line.strip("\n")) for line in file]
t = int("".join(stacks.pop(0)))


# Output as per spec.
for i in range(t):
    stack = stacks[i]
    out = flip(stack)
    print "Case #%s: %s" % (i + 1, out)
