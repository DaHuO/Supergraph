#!/usr/bin/python
# -*- coding: UTF-8 -*-

def solve(k, c, s):
    step = k ** (c - 1)
    points = [
        step * x + 1 for x in range(s)
    ]
    return points

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        k, c, s = map(int, raw_input().strip().split())
        res = map(str, solve(k, c, s))
        print "Case #%s: %s" % ( i+1, " ".join(res) )