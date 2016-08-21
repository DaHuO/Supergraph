# Primality Testing with the Rabin-Miller Algorithm
# http://inventwithpython.com/hacking (BSD Licensed)

import random

def rabinMiller(num):
    # Returns True if num is a prime number.

    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(5): # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


def isPrime(num):
    # Return True if num is a prime number. This function does a quicker
    # prime number check before calling rabinMiller().

    if (num < 2):
        return False # 0, 1, and negative numbers are not prime

    # About 1/3 of the time we can quickly determine if num is not prime
    # by dividing by the first few dozen prime numbers. This is quicker
    # than rabinMiller(), but unlike rabinMiller() is not guaranteed to
    # prove that a number is prime.
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True

    # See if any of the low prime numbers can divide num
    for prime in lowPrimes:
        if (num % prime == 0):
            return False

    # If all else fails, call rabinMiller() to determine if num is a prime.
    return rabinMiller(num)

nbit = 32
j = 500

def findSmallestDivisor(num):
    i = 1
    while i < 1000:
        i += 1
        if (i > 1):
            if (num % i == 0):
                return i
    return 0

from sys import argv

_, outfile = argv

out = open(outfile, 'w')

def get_bit(byteval, idx):
    return ((byteval & (1 << idx)) != 0)

def convert(value, base, lim):
    res = 0
    for i in range(lim):
        if (get_bit(value, i) == True):
            res += base ** i

    return res

def isGoodEnough(num, lim):
    for i in range(2, 11):
        if (findSmallestDivisor(convert(num, i, lim)) == 0):
            return False
    return True

def isJamCoin(num, lim):
    for i in range(2, 11):
        if (isPrime(convert(num, i, lim))):
            return False

    return isGoodEnough(num, lim)
    
import sys

out.write("Case #1:\n")
for i in xrange(1 << (16 - 2)):
    if j == 0:
        break
        
    num = 1 + i * 2 + (1 << (16 - 1))
    print bin(num)[2:]
    
    if (isJamCoin(num, 16)):
        num = 1 + i * 2 + (1 << (nbit - 1))
        if (isJamCoin(num, nbit)):
            print j
            j -= 1
            out.write(bin(num)[2:])
            #print bin(num)[2:]
            for k in xrange(2, 11):
                out.write(" ")
                out.write("{0}".format(findSmallestDivisor(convert(num, k, nbit)), convert(num, k, nbit)))            
            out.write("\n")

