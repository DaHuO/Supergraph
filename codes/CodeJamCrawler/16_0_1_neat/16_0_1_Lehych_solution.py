#!/usr/bin/env python
import sys

FAILED = 'INSOMNIA'

def digits(n):
    return set(str(n))

def main(testcase):
    result = 0
    N = int(testcase)
    if N == 0:
        return FAILED

    last_xN = N
    x = 1
    seen = digits(last_xN)
    while len(seen) != 10:
        if x > 123456789:  # My best guess?
            return FAILED
        x += 1
        last_xN = x * N
        seen.update(digits(last_xN))

    return last_xN

if __name__ == '__main__':
    cases_count = input()
    for i in xrange(1, cases_count+1):
        testcase = raw_input()
        if testcase == '':
            break
        print "Case #%i: %s" % (i,  main(testcase.strip()))

