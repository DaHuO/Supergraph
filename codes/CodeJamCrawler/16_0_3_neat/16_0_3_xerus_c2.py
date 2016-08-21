#!/usr/bin/env python3

import math
import itertools
import bitarray

dec_primes = set()

def eratosthenes(maxnum):
    limit = math.ceil(math.sqrt(maxnum))
    primes = bitarray.bitarray(maxnum)
    primes.setall(True)
    for i in range(2, limit):
        if primes[i]:
            for j in range(i * 2, maxnum, i):
                primes[j] = False
            dec_primes.add(i)
    return primes

def is_prime(num_s, base, primes):
    number = int(num_s, base)
    if number >= len(primes):
        dd = divisor(num_s, base)
        if dd == None:
            dec_primes.add(number)
            return True
        return False
    return primes[number]

def divisor(num_s, base):
    num = int(num_s, base)
    for n in dec_primes:
        if num % n == 0:
            return n
    dsq = int(math.sqrt(num))
    for n in range(max(dec_primes), dsq+1, 2):
        if num % n == 0:
            return n
    return None

def print_jams_coins(N, J):
    valid_jam_coins = 0
    primes = eratosthenes(2**min(N+1, 20))

    for i in itertools.product("10", repeat=(N-2)):
        jamcoin = "1" + "".join(i) + "1"
        valid = True
        divisors = []
        for base in range(2, 11):
            if is_prime(jamcoin, base, primes):
                valid = False
                break
        if valid:
            for base in range(2, 11):
                divisors.append(str(divisor(jamcoin, base)))
            valid_jam_coins += 1
            if valid_jam_coins > J:
                return
            print("{} {}".format(jamcoin, " ".join(divisors)))

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
T = int(input())  # read a line with a single integer
for i in range(1, T + 1):
    N, J = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    print("Case #{}:".format(i))
    print_jams_coins(N, J)
    # check out .format's specification for more formatting options
