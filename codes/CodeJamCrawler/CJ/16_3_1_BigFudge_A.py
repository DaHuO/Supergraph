#!/usr/bin/env python

import numpy as np

def read_stdin_lines():
    import fileinput
    return [line for line in fileinput.input()]

def parse_lines(lines):
    lines = [line[:-1] for line in lines[1:]]
    lines = [map(int, line.split(' ')) for line in lines[1::2]]
    return lines

def valid(state):
    n = max(state)
    val = n <= sum(state) - n
    return val

def subtract(v1, v2):
    return [x - y for (x, y) in zip(v1, v2)]

def convert_to_letters(steps):
    import string
    new_steps = []
    for step in steps:
        new_steps.append([string.uppercase[n] for n in step])
    return new_steps

def total(steps, size):
    t = [0] * size
    for step in steps:
        for n in step:
            t[n] += 1
    return t

def solve(target):
    current = [0] * len(target)
    diff = sorted(list(enumerate(subtract(target, current))), key=lambda e: -e[1])
    steps = []
    while diff[0][1] > 0:
        next_step = [diff[0][0]]
        current[diff[0][0]] += 1
        diff = sorted(list(enumerate(subtract(target, current))), key=lambda e: -e[1])
        if not valid(current):
            next_idx = diff[0][0]
            current[next_idx] += 1
            if not valid(current):
                current[next_idx] -= 1
                next_idx = diff[1][0]
                assert diff[1][1] > 0
                current[next_idx] += 1
                assert valid(current)
            next_step.append(next_idx)
        steps.append(next_step)
        diff = sorted(list(enumerate(subtract(target, current))), key=lambda e: -e[1])
    assert total(steps, len(target)) == target
    return convert_to_letters(steps)[::-1]


def print_outputs(outputs):
    for n, output in enumerate(outputs):
        output = [''.join(o) for o in output]
        output = ' '.join(output)
        print "Case #{}: {}".format(n+1, output)

if __name__ == '__main__':
    lines = read_stdin_lines()
    inputs = parse_lines(lines)
    outputs = map(solve, inputs)
    print_outputs(outputs)
