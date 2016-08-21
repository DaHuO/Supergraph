#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re


def check_prime(num):
    v = 2
    while v * v <= num:
        if num % v == 0:
            return v
        v += 1
    return -1

if __name__ == '__main__':
    Cases = int(sys.stdin.readline())
    pattern = re.compile(r'^(\d+) (\d+)$')
    for case_id in xrange(1, Cases + 1):
        line = sys.stdin.readline()[:-1]
        match = pattern.match(line)
        N, J = int(match.group(1)), int(match.group(2))

        # print N, J

        print "Case #%d:" % case_id

        for num in xrange(1, (1 << N)):
            digits = [0] * N
            for index in xrange(N):
                if num & (1 << index) != 0:
                    digits[index] = 1
            if digits[0] == 0 or digits[N - 1] == 0:
                continue

            # for index in xrange(N):
            #     print '%d' % digits[index],
            # print

            divisors = []
            for base in xrange(2, 11):
                value = 0
                for index in xrange(N):
                    value = value * base + digits[index]
                divisor = check_prime(value)
                # print "%d %d" % (value, divisor)
                if divisor == -1:
                    break
                divisors.append(divisor)

            if len(divisors) == 9:
                # print digits, divisors
                print "%s %s" % (''.join([str(i) for i in digits]), ' '.join([str(i) for i in divisors]))
                J -= 1
                if J <= 0:
                    break
