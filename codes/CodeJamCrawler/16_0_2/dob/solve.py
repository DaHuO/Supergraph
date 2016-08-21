#!/usr/bin/env python
from __future__ import print_function
import sys
import time
from functools import reduce

_dbg = '-d' in sys.argv[1:]

if _dbg:
    def dbg(*args):
        print(*args)
        sys.stdout.flush()
else:
    def dbg(*args):
        pass

def readline():
    return sys.stdin.readline().strip()

def readfloat():
    return float(readline())

def readfloats():
    return [float(x) for x in readline().split()]

def readint():
    return int(readline())

def readints():
    return [int(x) for x in readline().split()]

def flip(stack):
    s = [not x for x in stack]
    s.reverse()
    return s

def flip_tail(stack):
    i = -1
    while stack[i]:
        stack[i] = False
        i -= 1

def solve(stack, cnt=0):
    dbg(stack)
    if not stack:
        return cnt
    if stack[0]:
        return solve(stack[1:], cnt)
    if stack[-1]:
        flip_tail(stack)
        cnt += 1
    stack = flip(stack)
    return solve(stack, cnt + 1)

def solve_case():
    stack = [c == '+' for c in readline()]
    stack.reverse()
    return solve(stack)

def main():
    fmt = 'Case #{0:d}: {1}'
    cases = readint()
    if _dbg:
        for c in range(1, cases + 1):
            t0 = time.time()
            print(fmt.format(c, solve_case()))
            dbg('{:.6f}'.format(time.time() - t0))
    else:
        for c in range(1, cases + 1):
            print(fmt.format(c, solve_case()))

if __name__ == '__main__':
    main()

