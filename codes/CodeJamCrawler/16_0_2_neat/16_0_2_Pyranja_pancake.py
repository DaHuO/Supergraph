#!/usr/bin/env python3
import sys, logging

"""codejam 2016 - pancake"""

HAPPY_SIDE = '+'
BLANK_SIDE = '-'

def solve(stack):
    flips = 0
    state = stack[0]
    if state == BLANK_SIDE:
        flips += 1
    for pancake in stack:
        if pancake == state:
            continue
        if pancake == BLANK_SIDE:
                flips += 2
        state = pancake
    return flips

# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([formatCase(idx, solve(case)) for (idx, case) in enumerate(cases, 1)])

def formatCase(idx, answer):
    return 'Case #{0}: {1}'.format(idx, answer)

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    print(main(sys.stdin.readlines()[1:]))
