#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

def get_all_digits(n):
    result = []

    if n < 10:
        result = [n]
    else:
        k = 1
        power = math.pow(10, k)
        while(True):
            digit = int(n % power)
            if k > 1:
                digit = int(digit / math.pow(10, k-1))
            result.append(digit)
            k += 1
            power = math.pow(10, k)
            if n < power/10:
                break


    return result


t = int(raw_input())
for i in xrange(1, t + 1):
    n = [int(s) for s in raw_input().split(" ")][0]

    result = None
    if n == 0:
        result = "INSOMNIA"
    else:
        digits_set = set()
        j = 1
        while(len(digits_set) < 10):
            result = j * n
            digits_set = digits_set.union(set(get_all_digits(result)))
            j += 1

    print "Case #{}: {}".format(i, result)
