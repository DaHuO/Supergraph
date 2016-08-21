#!/usr/bin/env python

def pancake_flips(stack):
    #simplify
    last_cake = None
    new_stack = []
    for pancake in stack:
        if last_cake != pancake:
            new_stack.append(pancake)
        last_cake = pancake

    #remove last pancake(s) if +
    if new_stack[-1] == '+':
        new_stack.pop()

    return len(new_stack)

# print pancake_flips(list('+--+----++---+'))

t = int(raw_input())
for i in xrange(1, t + 1):
    stack = list(raw_input())
    print "Case #{}: {}".format(i, pancake_flips(stack))
