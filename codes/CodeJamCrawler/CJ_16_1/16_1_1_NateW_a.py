#!/usr/bin/env python

import sys


def solve(s):
    result = s[0]
    for c in s[1:]:
        if c >= result[0]:
            result = c + result
        else:
            result = result + c
    return result


def main():
    lines = sys.stdin.readlines()
    tests = int(lines[0])
    for i in xrange(tests):
        s = lines[i + 1][:-1]
        print "Case #%d: %s" % (i + 1, solve(s))


if __name__ == "__main__":
    main()
