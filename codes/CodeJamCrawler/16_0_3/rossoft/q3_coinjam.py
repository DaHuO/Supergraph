from __future__ import division
from functools32.functools32 import lru_cache
import sys
import itertools
import os
import re
import string
import math
import sys
import heapq
from collections import namedtuple, defaultdict, deque
from Tools import gcj
from Tools.gcj import printd
from copy import deepcopy
from simpleai.search import SearchProblem, astar
import random
import operator
from Tools import primes
from itertools import product

def is_good(binary_str):
    any_prime = False
    for base in xrange(2, 11):
        num = int(binary_str, base)
        if primes.is_prime(num):
            any_prime = True

    return not any_prime

def find_divisors(binary_str):
    divisors = []
    for base in xrange(2, 11):
        num = int(binary_str, base)
        f = primes.prime_factors(num)
        divisors.append(f[0])

    return divisors

def solver(n, lim):
    count = 0
    result = ''
    for bits in product([0, 1], repeat=(n-2)):
        binary = "1" + "".join(str(bit) for bit in bits) + "1"
        if is_good(binary):
            divisors = find_divisors(binary)
            result += "\n" + binary + " " + ' '.join([str(x) for x in divisors])
            count += 1
            if count == lim:
                break
    return result



def reader(in_file):
    """
    @type in_file: gcj.FileWrapper
    """
    (n, lim) = in_file.getInts()

    return {
        'n': n,
        'lim': lim
    }


if __name__ == "__main__":
    ### GCJ module http://jamftw.blogspot.com.es/2012/05/python-code-jam-wrapper.html
    gcj.GCJ(reader, solver, os.getcwd(), "").run()
