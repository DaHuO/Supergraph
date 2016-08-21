#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint

def solve(k, c, s):
    return " ".join(map(str, xrange(1, k**c+1, k**(c-1))))

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
def test():
    pass

def readInt():
    return int(sys.stdin.readline().strip())

def readInts():
    return [int(x) for x in sys.stdin.readline().strip().split()]

def readStrs():
    return [x for x in sys.stdin.readline().strip().split()]

def main():
    n = readInt()
    for i in xrange(n):
        k, c, s = readInts()
        print 'Case #%d: %s' % (i+1, solve(k, c, s))
    pass

if __name__ == '__main__':
    main()