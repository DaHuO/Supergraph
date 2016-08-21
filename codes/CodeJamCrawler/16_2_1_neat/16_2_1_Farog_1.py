#!/usr/bin/python
import os
import sys

from collections import Counter

dig = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
chars = set(list(''.join(dig)))

N = int(raw_input())

def printDig(puzzle):
    di = Counter(puzzle)
    res = {x:0 for x in range(0,9)}
    res[0]=di['Z']

    res[2]=di['W']

    res[6]=di['X']

    res[8]=di['G']

    res[3]=di['H']-res[8]

    res[4]=di['R'] - res[3] - res[0]
    res[7]=di['S'] - res[6]
    res[5]=di['V'] - res[7]
    res[9]=di['I']-res[8]-res[6]-res[5]
    res[1]=di['O'] - res[0]-res[2]-res[4]

    # print di
    # print res
    for key in res.keys():
        sys.stdout.write(str(key)*res[key])
    sys.stdout.write('\n')




for i in range(1,N+1):
    sys.stdout.write(''.join(['Case #',str(i),': ']))
    printDig(raw_input())


# t = int(raw_input())  # read a line with a single integer
# for i in xrange(1, t + 1):
#   n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
#   print "Case #{}: {} {}".format(i, n + m, n * m)
#   check out .format's specification for more formatting options