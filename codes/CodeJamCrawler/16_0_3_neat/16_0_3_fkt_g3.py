#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def is_prime(n):
        for i in range(3, 1000, 2):
                if n % i == 0:
                        return i
        return None

def solve(s):
        n, j = s.split()
        num = 0
        divisors = []
        for i in xrange(2147483649, 4294967295, 2):
                is_jamcoin = True
                bin_i = str(bin(i))[2:]
                for base in xrange(2, 11):
                        x = int(bin_i, base)
                        f = is_prime(x)
                        if f == None:
                                is_jamcoin = False
                                break
                        else:
                                divisors.append(str(f))
                if is_jamcoin:
                        print str(bin(i))[2:] + ' ' + ' '.join(divisors)
                        num += 1
                if num == int(j):
                        break
                divisors = []


if __name__ == "__main__":
        n = input()

        print("Case #1:")
        solve(raw_input())
