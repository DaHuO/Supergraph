#!/usr/bin/python

def N(): return tuple(map(int, raw_input().split()))

T = N()[0]

for c in range(T):
    stack = raw_input()
    s = None
    while s != len(stack):
        s = len(stack)
        stack = stack.replace("--", "-")
        stack = stack.replace("++", "+")

    answer = stack.count("-") * 2 - (1 if stack[0] == '-' else 0)
    # print stack, answer
    print "Case #%d: %d" % (c+1, answer)
