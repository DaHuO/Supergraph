#!/usr/bin/env python


def revert(stack):
    return ''.join('+' if l == '-' else '-' for l in stack[::-1])

def plus_count(stack):
    i = 0
    while stack[i] == '+':
        i += 1
    return i

def solve(stack):
    n = 0
    while len(stack) > 0:
        if stack[-1] == '-':
            pc = plus_count(stack)
            if pc > 0:
                stack = revert(stack[:pc]) + stack[pc:]
                n += 1
            stack = revert(stack)
            n += 1
        stack = stack[:-1]
    return n

T = int(raw_input().strip())
for t in range(T):
    stack = raw_input().strip()
    print 'Case #%d: %s' % (t+1, solve(stack))
