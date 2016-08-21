#!/usr/bin/env python3

import math

def findCoins(size, find_max):
    found_count = 0

    # skipping even values ensures binary string ends with '1'
    for i in range(2 ** (size - 1) + 1 , 2 ** size, 2):
        coin = bin(i)[2:]
        divisors = []
        for base in range(2, 11):
            value = int(coin, base)
            divisor = findDivisor(value)
            if divisor != -1:
                divisors.append(divisor)
            else:
                break

        if len(divisors) == 9:
            found_count += 1
            print(coin, ' '.join([str(i) for i in divisors]))

        if found_count == find_max:
            return found_count
    return found_count


def findDivisor(dividend):
    "return a nontrivial divisor of value, if prime return -1"
    if dividend % 2 == 0:
        return 2

    for divisor in range(3, int(math.sqrt(dividend)), 2):
        if dividend % divisor == 0:
            return divisor
        if divisor > 1000:
            return -1
    return -1
    

cases = int(input())
for i in range(cases):
    print("Case #{}:".format(i+1))

    size, find_max = (int(i) for i in input().split())
    found_count = findCoins(size, find_max)
