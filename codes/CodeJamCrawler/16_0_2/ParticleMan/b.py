#!/usr/bin/env python

def printResult(case, result):
    print "Case #{}: {}".format(case, result)

def flip(s, num):
    return ''.join([other(x) for x in s[:num][::-1]]) + s[num:]

def other(c):
    if c == '+':
        return '-'
    else:
        return '+'

t = int(raw_input())
for i in xrange(1, t + 1):
    state, = [s for s in raw_input().split(" ")]
    if len(state) == 0:
        printResult(i, 0)
    c = other(state[0])
    index = 0
    flips = 0
    while True:
        index = state.find(c, index)
        if index == -1:
            break
        state = flip(state, index)
        flips += 1
        c = other(c)
    if state[0] == '-':
        flips += 1
    printResult(i, flips)
