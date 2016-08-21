#!/usr/bin/python2
from sys import stdin
from string import rstrip


def solve(str):
    count = 1
    for i in range(1,len(str)):
        if str[i] != str[i-1]:
            count += 1
    if str[len(str)-1] == '+':
        count -= 1
    return count



lines = int(stdin.readline())
for i in range(1,lines+1):
    l = rstrip(stdin.readline())
    print "Case #%d: %d" % (i,solve(l))