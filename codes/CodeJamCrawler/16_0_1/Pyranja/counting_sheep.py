#!/usr/bin/env python3
import sys, logging

"""codejam 2016 - counting sheep"""

def solve(n):
    if n == 0:
        return 'INSOMNIA'

    seen = set()
    current = n
    while True:
        for c in str(current):
            seen.add(c)
        if len(seen) >= 10:
            return current
        current += n

# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([formatCase(idx, solve(int(case))) for (idx, case) in enumerate(cases, 1)])

def formatCase(idx, answer):
    return 'Case #{0}: {1}'.format(idx, answer)

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    print(main(sys.stdin.readlines()[1:]))
