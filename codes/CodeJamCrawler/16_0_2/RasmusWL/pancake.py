#!/usr/bin/env python2

f = open('B-large.in')

UP = '+'
DOWN = '-'

testcases = int(f.readline().strip())

def flip(pancakes, stop):
    pancakes[0:stop] = (UP if c == DOWN else DOWN for c in reversed(pancakes[0:stop]))

def removeend(pancakes):
    while pancakes and pancakes[-1] == UP:
        pancakes.pop()

def merge(pancakes):
    i = 0
    while i < len(pancakes)-1:
        if pancakes[i] == pancakes[i+1]:
            pancakes.pop(i)
        else:
            i += 1

for testcase in xrange(testcases):
    pancakes = list(f.readline().strip())

    moves = 0

    merge(pancakes)
    removeend(pancakes)

    moves = len(pancakes)
    print ("Case #%s: %s" % (testcase+1, moves))
