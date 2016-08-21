import os
import sys
import fileinput
import itertools

def format_pancakes(stack):
    return ''.join(('+' if p else '-' for p in stack))

def flip_stack(stack, i):
    return list(reversed([not p for p in stack[:i]])) + stack[i:]

def flip_lowest(stack, type):
    # Find index of lowest blank pancake (1-indexed)
    i = len(pancakes) - pancakes[::-1].index(type)
    return flip_stack(pancakes, i)


for line in fileinput.input():
    case = fileinput.lineno() - 1
    if case == 0:
        continue

    pancakes = [p == '+' for p in line.strip()]

    flips = 0
    while not all(pancakes):
        top = pancakes[0]
        i = 1
        try:
            while pancakes[i] == top:
                i += 1
        except IndexError:
            pass

        pancakes = flip_stack(pancakes, i)
        flips += 1

    print "Case #{}: {}".format(case, flips)
