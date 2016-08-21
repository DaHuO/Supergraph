#!/usr/bin/env python
# William Leighton Dawson
# Google Code Jam Qualification Round
# Problem 1: Counting Sheep
# 2016-04-09

import sys

target = [str(i) for i in range(10)]
def count(num):
    current = []
    if num == 0:
        return "INSOMNIA"
    x = 1
    while current != target:
        mul = str(num*x)
        for c in mul:
            if c not in current:
                current.append(c)
        current.sort()
        x += 1
    return mul

# Input as per spec. (with a few conveniences added :P)
if len(sys.argv) == 2:
    filename = sys.argv[-1]
else:
    filename = raw_input("Filename: ")
file = open(filename, 'r')
nums = [int(line) for line in file]
t = nums.pop(0)

# Output as per spec.
for i in range(t):
    num = nums[i]
    out = count(num)
    print "Case #%s: %s" % (i + 1, out)

