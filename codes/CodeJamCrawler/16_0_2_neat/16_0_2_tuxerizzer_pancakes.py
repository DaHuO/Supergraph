#!/usr/bin/env python
"""
usage: python file.py < X-small/large.in
"""

def solve(stack, res=0):
    if '-' not in stack:
        return res
    if '+' not in stack:
        return res + 1

    sym = '-' if stack[0] == '+' else '+'
    i = stack.index(sym)
    return solve(sym * i + stack[i:], res + 1)

def main():
    t = int(raw_input())
    for casenum in range(t):
        stack = raw_input()
        res = solve(stack)
        print 'Case #%d: %s' % (casenum + 1, res)

if __name__ == '__main__':
    main()
