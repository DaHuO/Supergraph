#!/usr/bin/python
# coding=utf8
import sys
import math
from time import time
from itertools import permutations, combinations
import collections
import functools
from fractions import gcd, Fraction
import string
import operator
#import random (not working in python3)
import bisect
from numpy import cross, dot, multiply, add, subtract
from numpy.linalg import norm

print_realtime = len(sys.argv) == 2 and sys.argv[1] == "print_realtime"

def dbg(txt):
    sys.stderr.write(str(txt) + "\n")


def print_var(*args):
    for var_name in args:
        assert type(var_name) == str
        calling_frame = sys._getframe().f_back
        var_val = calling_frame.f_locals.get(var_name, calling_frame.f_globals.get(var_name, None))
        dbg(var_name+'='+ str(var_val))


class timed(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        t1 = time()
        ret = self.func(*args)
        dif_time = time() - t1
        print("%s: returned %s in %f seconds" % (self.func.__name__, ret, dif_time))
        return ret


def comp(f1, f2, *args):
    t1 = time()
    r1 = f1(*args) if f1 is not None else None
    t2 = time()
    r2 = f2(*args) if f2 is not None else None
    t3 = time()
    res = "%5s: %s in %f\n%5s: %s in %f" % (f1.__name__ if f1 is not None else None, r1, t2 - t1,
                                            f2.__name__ if f2 is not None else None, r2, t3 - t2)
    if r1 != r2:
        dr = "!! DIFFERENT RESULTS !!"
        res = dr + "\n" + res + "\n" + dr
    print(res)
    return r1 if r1 == r2 else None


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# returns first prime factor
def prime_factor(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            if d != 1 and d != n:
                return d
            n /= d
        d = d + 1
    return None  # it's prime

def alg(N, J):
    start = 0
    str_len = N
    ret = ""
    found = 0

    # precompute exponents
    bases = {}
    for base in range(2, 11):
        bases[base] = [pow(base, i) for i in range(N - 1, -1, -1)]

    # total try = 2^(N-2) becuse extermities are known
    max_tries = pow(2, N - 2)
    for i in range(max_tries):
        nb = "1" + bin(i)[2:].zfill(N - 2) + "1"
        # check if it's prime in all bases
        valid = True
        line_ret = nb + " "
        for base in range(2, 10 + 1):
            base_exp = bases[base]
            conv_nb = 0
            for digit in range(N):
                if nb[digit] == "1":
                    conv_nb += base_exp[digit]
            # check if prime
            if is_prime(conv_nb):
                valid = False
                break;
            factor = prime_factor(conv_nb)
            line_ret += "%d " % factor
        if valid:
            ret += line_ret + "\n"
            found += 1
            if found == J:
                dbg("i = " + str(i))
                return ret
    return None


def main():
    #import cProfile
    #cProfile.runctx('alg()', globals(), locals())
    data = sys.stdin
    nb = int(data.readline())
    #a, b = map(int,data.readline().split())
    for icase in range(nb):
        L = list(map(int, data.readline().split()))  # int
        #L = list(map(float, data.readline().split()))  # float
        #L = data.readline().split()  # string
        #s = data.readline().strip()
        #i = int(data.readline().strip())
        res = alg(L[0], L[1])
        ret = "Case #%d:\n%s" %(icase + 1, res)
        if print_realtime:
            dbg(ret)
        print(ret)


if __name__ == "__main__":
    main()
