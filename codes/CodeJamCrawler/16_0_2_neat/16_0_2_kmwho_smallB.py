#! /usr/bin/python
# kmwho
# Codeforces Round 329 div2

from __future__ import print_function

def check(s):
    return (not "-" in s)

def solvecase():
    stack = input().strip()
    L     = len(stack)
    prev  = stack[0]
    sc    = 0
    for c in stack:
        if c != prev:
            sc += 1
        prev = c
    if prev == '-':
        sc += 1
    return sc

def solve():
    T  = int(input())
    for t in range(T):
       res = solvecase()
       print( "Case #" + str(t+1) + ": " + str(res) )

def main():
	solve()


main()
