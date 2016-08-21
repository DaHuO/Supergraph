#!/usr/bin/python2
from sys import argv

def flip_helper(top, i):
    if len(top) == 0:
        return []
    elif len(top) == 1:
        if top == "+":
            return []

        return [i + 1]
    elif len(top) > 1:
        if top[0] == top[1]:
            return flip_helper(top[1:], i + 1)

        return [i + 1] + flip_helper(top[1:], i + 1)

def flip(stack):
    return flip_helper(stack, 0)

input_file = argv[1]
f = open(input_file, 'r')

nlines = int(f.readline())
for i in xrange(nlines):
    line = f.readline().strip("\n")
    # print line, flip(line)
    print "CASE #%s:" % (i + 1), len(flip(line))

f.close()

