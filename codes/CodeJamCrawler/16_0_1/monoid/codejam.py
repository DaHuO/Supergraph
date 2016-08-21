#!/usr/bin/env python2
import sys

def problem_result(v):
    if v == 0:
        return 'INSOMNIA'
    if v < 0:
        v = -v
    flags = [False] * 10
    n = 0
    while not all(flags):
        n += v
        for digit in str(n):
            flags[int(digit)] = True
    return n


def main():
    n = input()

    for i in xrange(1, n+1):
        v = input()
        print "Case #{}: {}".format(i, problem_result(v))


if __name__ == '__main__':
    main()
