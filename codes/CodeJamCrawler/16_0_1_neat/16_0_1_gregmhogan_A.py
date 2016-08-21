#!/usr/bin/env python

def run_one(N):
    if N == 0:
        return 'INSOMNIA'

    n = N
    digits = set(list(str(N)))

    while len(digits) < 10:
        n += N
        digits = digits | set(list(str(n)))

    return n


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        N = int(lines.popleft().rstrip('\r\n'))

        result = run_one(N)

        output.append('Case #{0}: {1}'.format(t + 1, result))

    return output


# Google Code Jam submissions must run stand-alone.
# This code shall be copied into each solution.
if __name__ == '__main__':
    import os
    import sys
    from collections import deque

    infile = sys.argv[1]
    with open(infile) as file:
        lines = deque(file.readlines())
        output = run(lines)
        print os.linesep.join(output)
