#!/usr/bin/env python
# William Leighton Dawson
# Google Code Jam Qualification Round
# Problem 4: Fractiles
# 2016-04-09

import sys

def maketile(instr, c):
    seq = instr
    k = len(instr)
    for i in range(c - 1):
        newseq = ""
        for c in seq:
            if c == 'L':
                newseq += instr
            else:
                newseq += 'G'*k
        seq = newseq
    return seq


# Input as per spec. (with a few conveniences added :P)
if len(sys.argv) == 2:
    filename = sys.argv[-1]
else:
    filename = raw_input("Filename: ")
file = open(filename, 'r')
nums = [line.strip("\n").split(' ') for line in file]
file.close()
t = int("".join(nums.pop(0)))

# Output as per spec.
for i in range(t):
    num = nums[i]
    if num[0] == num[2]:
        out = ' '.join([str(j) for j in range(1, int(num[0]) + 1)])
    else:
        out = "IMPOSSIBLE"
    print "Case #%s: %s" % (i + 1, out)

sys.stderr.write("Done!\n")
