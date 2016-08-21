#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# Naive solution but the problem is simple enough

import sys

# keep track of the results so that we don't re-compute them
memo = {}

def _suite(n):
    digits = set()
    m = n
    i = 1
    while len(digits) != 10:
        m = n * i
        digits.update(str(m))
        i += 1

    return m

def suite(n):
    if n == 0:
        # That's the only case
        return "INSOMNIA"
    if n not in memo:
        memo[n] = _suite(n)
    return str(memo[n])

def testcase(idx, n):
    print "Case #%d: %s" % (idx, suite(n))

def main(sourcefile):
    with open(sourcefile) as f:
        skip_lines = 1
        test_idx = 0

        for line in f:
            if skip_lines > 0:
                skip_lines -= 1
                continue

            test_idx += 1
            n = int(line)
            testcase(test_idx, n)

if __name__ == "__main__":
    main(sys.argv[1])
