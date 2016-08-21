#!/usr/bin/env python3

import sys

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def jamcoins(n):
    smallest = (2 ** (n-1)) + 1
    i = smallest
    while True:
        yield "{:b}".format(i)
        i = i + 2

def to_base(n,b):
    quotient = n
    digits = []
    while quotient > 0:
        digits.append(quotient % b)
        quotient = quotient // b
    return ''.join([str(x) for x in reversed(digits)])

def find_coins(n,amount,primes,file):
    found = 0
    coingen = jamcoins(n)
    while found < amount:
        divisors = []
        coin = next(coingen)
        for base in range(2,11):
            divisor = None
            basecoin = int(coin,base)
            root = basecoin ** 0.5
            for candidate in primes:
                if (candidate > root):
                    break
                elif basecoin % candidate == 0:
                    divisor = candidate
                    break
            if divisor is None:
                break
            else:
                divisors.append(str(divisor))
        if len(divisors) == 9:
            print("{0} {1}".format(coin," ".join(divisors)),file=file)
            found = found + 1

with open(sys.argv[1],'rt') as infile, open("jamcoins.out",'wt') as outfile:
    ncases = infile.readline()
    n,j = [int(x) for x in infile.readline().split(" ")]
    print("Case #1:",file=outfile)
    find_coins(n,j,primes,outfile)
