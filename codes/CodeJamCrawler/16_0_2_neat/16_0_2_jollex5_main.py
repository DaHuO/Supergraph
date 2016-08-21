#!/usr/bin/env python

import sys
from Queue import Queue

input_file = sys.argv[1]

with open(input_file) as f:
    n_tests = int(f.readline().strip())
    stacks = []
    for i in range(n_tests):
        stacks.append(list(f.readline().strip()))

def flip_stack(stack, n_cakes):
    to_flip = stack[:n_cakes]
    same = stack[n_cakes:]
    flipped = [flip(cake) for cake in to_flip]
    flipped.reverse()
    return flipped + same

def flip(cake):
    if cake == '+':
        return '-'
    else:
        return '+'

def stack_done(stack):
    return all([char == '+' for char in stack])

def do_one(stack):
    q = []
    q.append((stack, []))

    seen = []

    while True:
        current, already_done = q.pop(0)
        seen.append(current)
        if stack_done(current):
            return len(already_done)
        for i in range(1, len(stack) + 1):
            if i not in already_done:
                new_stack = flip_stack(current, i)
                new_already_done = [] + already_done + [i]
                if stack_done(new_stack):
                    return len(new_already_done)
                if new_stack not in seen:
                    q.append((new_stack, new_already_done))



results = []
for stack in stacks:
    results.append(do_one(stack))

for i, result in enumerate(results):
    print 'Case #{}: {}'.format(i+1, result)
