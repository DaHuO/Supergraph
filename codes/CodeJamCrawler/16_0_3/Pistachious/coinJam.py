#!/usr/bin/python

import random
import prime
import primefac
from decimal import Decimal
 
 #Certainly number
_mrpt_num_trials = 100 # number of bases to test
outfile = open("output", "w")
 
def is_probable_prime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite
def is_jam(int_input):
    str_input = bin(int_input)[2::]
    output = str_input
    for i in range(2, 11):
        integer = int(str_input, i)
        if(is_probable_prime(integer)):
            return False 
        temp = integer
        factor = primefac.primefac(integer).next()
        output += " " + str(factor)
    print output
    outfile.write(output + "\n")
    return True

s = set()
mem = set()
if __name__ == "__main__":
    print "Case #1:"
    N = 31
    J = 500
    while(len(s) != J):
        rand = (1 << N) + (random.getrandbits(N - 2 ) << 1) + 1
        while(rand in mem):
            rand = (1 << N) + (random.getrandbits(N - 2 ) << 1) + 1
        mem.add(rand)

        if(is_jam(rand) == True):
            s.add(rand)



