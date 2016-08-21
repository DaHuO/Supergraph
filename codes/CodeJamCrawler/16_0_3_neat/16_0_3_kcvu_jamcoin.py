#!/usr/bin/env python

from itertools import product
from math import pow, sqrt

def generate_number(n):
    for v in product([0,1], repeat=n-2):
        yield tuple([1] + list(v) + [1])

def value_with_base(digits, base):
    l = len(digits)
    #print zip(digits,reversed(range(l)))
    return sum([int(pow(base,p)) for d, p in zip(digits,reversed(range(l))) if d == 1])

def find_divisor(v):
    sq_root = int(sqrt(v))
    for i in range(2,sq_root+1):
        if v % i == 0:
            return v / i
    return None

if __name__ == "__main__":
    import sys
    n, j = [int(v) for v in sys.argv[1:3]]
    print "Case #1:"
    cnt = 0
    for digits in generate_number(n):
        divisors = []
        #values = []
        for base in range(2,11):
            value = value_with_base(digits, base)
            divisor = find_divisor(value)
            if divisor is None:
                break
            #values.append(value)
            divisors.append(divisor)
        if len(divisors) == 9:
            print ''.join([str(d) for d in digits]),
            #print ' '.join([str(d) for d in values])
            print ' '.join([str(d) for d in divisors])
            cnt += 1
            if cnt >= j:
                break
    
