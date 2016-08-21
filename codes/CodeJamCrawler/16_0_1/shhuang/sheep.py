#!/usr/bin/env python

import sys

def helper(N):
    digits_seen = set()
    if N == 0:
        return "INSOMNIA"
    last_N = N
    while True:
        digits = [int(x) for x in list(str(last_N))]
        digits_seen = digits_seen.union(digits)
        if len(digits_seen) == 10:
            break
        last_N += N
        if last_N / N > 1000:
            assert False, str(N) + " may result in INSOMNIA"
    return last_N

def parse_file(num_lines=-1):
    with open(sys.argv[1], 'r') as f:
        lines = [l.rstrip('\n') for l in f.readlines()]
    i = 1
    tests = []
    varying_nlines = False
    if num_lines == -1:
        varying_nlines = True

    while i < len(lines):
        new_test = []
        if varying_nlines:
            num_lines = int(lines[i])
            i += 1

        for j in range(num_lines):
            new_test.append(lines[i])
            i += 1
        tests.append(new_test)
    return int(lines[0]), tests

num_tests, tests = parse_file(num_lines=1)
#num_tests, tests = parse_file()

for case,test in enumerate(tests):
    N = int(test[0])
    sol = helper(N)
    print 'Case #{}: {}'.format(case+1, sol)
