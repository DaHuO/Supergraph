#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import sympy as sy

N = 32
J = 500

class MyRange:
    def __init__(self, length):
        self.length = length
        del length
        self.short_length = self.length - 2
        range_ = range(0, 2 ** self.short_length)
        self.iter_ = iter(range_)
    def __iter__(self):
        return self
    def __next__(self):
        i = next(self.iter_)
        str0 = '1{0:0' + str(self.short_length) + 'b}1'
        str1 = str0.format(i)
        int_ = int(str1)
        return int_

def getInts(string):
    result = []
    for base in range(2, 11):
        result.append(int(string, base))
    return result

jamcoins = []
factorss = []

for i, n in zip(itertools.count(), MyRange(N)):
    nums = getInts(str(n))
    isFound = True
    factors = []
    for num in nums:
        if (sy.isprime(num)):
            isFound = False
            break
        fi0 = sy.factorint(num, limit=1000)
        fi1 = min(fi0.keys())
        if fi1 == num:
            isFound = False
            break
        factors.append(fi1)
    if isFound:
        jamcoins.append(n)
        factorss.append(factors)
        if len(jamcoins) >= J:
            break;

print("Case #1:")
        
for i, j, f in zip(itertools.count(), jamcoins, factorss):
    str0 = ' '.join(list(map(str, f)))
    print(j, str0)
