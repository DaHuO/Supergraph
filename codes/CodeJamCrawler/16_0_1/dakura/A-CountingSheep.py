#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def solve(N):
    if N > 0:
        i = 1
        digits = 0
        while True:
            n = N*i
            while n > 0:
                digits |= 1<<(n%10)
                if digits == 0x3ff:
                    return str(N*i)
                n /= 10
            i += 1

    return 'INSOMNIA'

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        N = int(f.readline())
        answer = solve(N)

        print "Case #%d: %s" % (i+1, answer)


