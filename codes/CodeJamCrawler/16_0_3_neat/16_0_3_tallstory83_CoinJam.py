#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random

class H:
    def __init__(self, N):
        self.N = int("1"*N, 2)
        x = "0" * N
        self.current = int("1" + x[1:-1] + "1", 2) -1

    def next(self):
        self.current += 1
        while "1" != bin(self.current)[2] or "1" != bin(self.current)[-1]:
            self.current += 1
        if self.N < self.current:
            return ""
        return bin(self.current)[2:]


class P:
    def __init__(self):
        self.primes = [2, 3, 5, 7]
        self.prime_max = 7
    def get(self, idx):
        diff = len(self.primes) - (idx+1)
        i = 0
        while diff < 0:
            i += 2
            if FermatPrimalityTest(self.prime_max + i):
                self.primes.append(self.prime_max + i)
                self.prime_max += i
                diff += 1
        return self.primes[idx]

p = P()
def get_d(n):
    idx = 0
    while p.get(idx)**2+1 < n and idx < 300:
        if 0 == (n % p.get(idx)):
            return p.get(idx)
        idx += 1

    return n


def FermatPrimalityTest(number):
    ''' if number != 1 '''
    if (number > 1):
        ''' repeat the test few times '''
        for time in range(3):
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            randomNumber = random.randint(2, number)-1
            ''' Test if a^(n-1) = 1 mod n '''
            if ( pow(randomNumber, number-1, number) != 1 ):
                return False
        return True
    else:
        ''' case number == 1 '''
        return False

def solve(cipher):
    ret = "\n"
    N, J = cipher.split(" ")
    N = int(N)
    J = int(J)

    cnt = 0
    h = H(N)
    v = h.next()
    while "" != v and cnt < J:
        r = list()
        for i in range(2,11):
            test_num = int(v, i)
            if FermatPrimalityTest(test_num):
                break
            d = get_d(test_num)
            if test_num == d:
                break
            r.append(get_d(test_num))
        if 9 ==len(r):
            cnt += 1
            ret += "%s"%v
            for x in r:
                ret += " %d"%x
            ret += "\n"
        v = h.next()
    return ret

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
