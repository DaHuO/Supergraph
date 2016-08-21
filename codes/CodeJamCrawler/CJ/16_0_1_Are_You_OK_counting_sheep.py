#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint


def solve(x):
    if not x:
        return 'INSOMNIA'
    ds = set()
    r = x
    while True:
        for i in str(r):
            ds.add(i)
        if len(ds) == 10:
            return r
        r += x
        pass
    pass

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
        x = readInt()
        print 'Case #%d: %s' % (i+1, solve(x))
    pass

if __name__ == '__main__':
    main()