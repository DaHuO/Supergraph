#!/bin/env python
#coding: utf8

import sys

def parse_input():
    count = int(sys.stdin.readline())
    for n in range(count):
        x = int(sys.stdin.readline())
        yield n + 1, x


def break_num(n):
    return set(str(n))

def solve_task(n):
    if n == 0:
        return "INSOMNIA"
    seen_nums = break_num(n)
    m = 1
    while len(seen_nums) < 10:
        m += 1
        seen_nums = seen_nums.union(break_num(n * m))
    #print seen_nums
    return n * m

for i, n in parse_input():
    print "Case #%s: %s" % (i, solve_task(n))

