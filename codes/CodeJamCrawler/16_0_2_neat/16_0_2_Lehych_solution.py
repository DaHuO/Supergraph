#!/usr/bin/env python
import sys

def main(testcase):
    result = 0
    prev = testcase[0]
    for i, digit in enumerate(testcase[1:]):
        if digit != prev and digit == '+':
            result += 1
        elif digit != prev and digit == '-':
            result += 1
        prev = digit

    result += (1 if prev=='-' else 0)
    return result

if __name__ == '__main__':
    cases_count = input()
    for i in xrange(1, cases_count+1):
        testcase = raw_input()
        if testcase == '':
            break
        print "Case #%i: %s" % (i,  main(testcase.strip()))

