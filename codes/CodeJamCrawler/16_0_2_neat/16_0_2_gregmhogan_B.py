#!/usr/bin/env python

def run_one(S):
    count = 0
    c = S[0]

    for s in S[1:]:
        if s != c:
            c = s
            count += 1

    if c != '+':
        count += 1

    return count


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        S = lines.popleft().rstrip('\r\n')

        result = run_one(S)

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
