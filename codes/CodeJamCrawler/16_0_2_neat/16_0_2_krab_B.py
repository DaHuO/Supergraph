#!/usr/bin/env python3

import sys

def parse():
    n_cases = int(sys.stdin.readline())
    cases = [(l.strip(),) for l in sys.stdin]

    assert len(cases) == n_cases, cases

    return cases

def solve(stack):
    reverses = 0
    for i, e in reversed(list(enumerate(stack))):
        if (reverses % 2 == 0 and e == "-") or (reverses % 2 == 1 and e == "+"):
            reverses += 1
    return reverses

for i, case in enumerate(parse()):
    print("Case #{}: {}".format(i + 1, solve(*case)))
