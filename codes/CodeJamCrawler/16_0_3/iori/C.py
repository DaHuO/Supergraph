#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from bisect import bisect_left
import math

def prime_range(limits):
    primes = [True] * limits
    primes[0], primes[1] = [False] * 2
    for index, value in enumerate(primes):
        if value is True:
            primes[index*2::index] = [False] * (((limits - 1)//index) - 1)
    return [i for i in range(limits) if primes[i]]


class decompositPrime(object):
    def __init__(self, n):
        self.n = n
        self.factors = {}
        self.calc()
    def __str__(self):
        return str(sorted(self.factors))
    def calc(self):
        A = 2
        N = self.n
        while N >= A * A:
            if N % A == 0:
                if self.factors.get(A) != None:
                    self.factors[A] += 1
                else:
                    self.factors[A] = 1
                N = N // A
            else:
                A += 1
        if self.factors.get(N):
            self.factors[N] += 1
        else:
            self.factors[N] = 1
    def num_of_divisors(self):
        n = 1
        for num in self.factors.itervalues():
            n *= (num + 1)
        return n
    def divisor(self):
        large_divisors = []
        for i in range(1, int(math.sqrt(self.n))+1):
            if self.n % i == 0:
                yield i
                if i is not self.n // i:
                    large_divisors.insert(0, self.n//i)
        for divisor in large_divisors:
            yield divisor
    def factors2set(self):
        ret = set([k for k in self.factors.iterkeys()])
        return ret

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end


import itertools
import random

def prime_gen():
    yield 2
    comp_dict = {}
    for num in itertools.islice(itertools.count(3),0,None,2):
        p = comp_dict.pop(num,None)
        if p is not None:
            test = num + 2*p
            while test in comp_dict:
                test = test + 2*p
            comp_dict[test] = p
        else:
            comp_dict[num*num] = num
            yield num

primes = {}
def is_prime(num):
    if primes.get(num):
        return primes[num]
    result = True
    if num < 4:
        if (num != 2 and num != 3):
            result = False
    else:
        nsqrt = int(num**0.5) + 1
        mygen = prime_gen()
        for p in mygen:
            if p > nsqrt:
                break
            if num%p == 0:
                result = False
                break
        mygen.close()
    primes[num] = result
    return result

def is_prime2(q,k=50):
    """ Miller-Rabin """
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False

    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1

    for i in xrange(k):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)
        while t != q-1 and y != 1 and y != q-1:
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True

def main():
    # limit = 70000000
    # primes = prime_range(limit)

    def bin2int(x, base=2):
        if isinstance(x, int):
            x = bin(x)
        ret = 0
        c = 1
        if x[:2] == '0b':
            x = x[2:]
        for s in x[::-1]:
            if s == '1':
                ret += c
            c *= base
        return ret

    start = 2 ** 15
    last = 2 ** 16

    # for digit in range(2, 11):
    #     print(bin2int('1000000000000001', base=digit))
    print("Case #1:")
    cnt = 0
    for n in range(start, last):
        if not (bin(n)[2] == '1' and bin(n)[-1] == '1'):
            continue
        for digit in range(2, 11):
            tmp = bin2int(n, base=digit)
            if is_prime(tmp):
                break
            # if binary_search(primes, bin2int(n, base=digit)) != -1:
            #     break
        else:
            cnt += 1
            print(bin(n)[2:], end=' ')
            # print()
            for digit in range(2, 11):
                # print(bin2int(n, base=digit), end=' ')
                dc = decompositPrime(bin2int(n, base=digit))
                for i, num in enumerate(dc.divisor()):
                    if i > 0:
                        print(num, end=' ')
                        break
            print()
            if cnt >= 50:
                break

if __name__ == "__main__":
    main()
