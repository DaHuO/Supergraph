from sys import stdin
import math, string, random

bases = range(2, 11)
primes = []
max_prime = 1000

def sieve(limit):
    limit += 1
    prime = [True] * limit
    for i in range(2, limit):
        if prime[i]:
            primes.append(i)
            for j in xrange(i*i, limit, i):
                prime[j] = False

def divided_by(x):
    for prime in primes:
        if x <= prime:
            break
        if not x % prime:
            return prime
    return 0

def increment(x):
    length = len(x) - 2
    x = str(bin(int(x[1:-1], 2) + 1))[2:]
    x = "0" * (length - len(x)) + x
    return "1" + x + "1"

def compute(lenght, num):
    x = "1" + "0" * (length - 2)+ "1"
    jamcoins = {}
    while(num):
        dividors = []
        for base in bases:
            dividor = divided_by(int(x, base))
            if dividor:
                dividors.append(dividor)
            else:
                break
        if len(dividors) == len(bases):
            num -= 1
            jamcoins[x] = dividors
        x = increment(x)
    return jamcoins

def pretty_str(array):
    s = str(array[0])
    for x in range(1, len(array)):
        s = s + " " + str(array[x])
    return s

for i in range(input()):
    sieve(max_prime)
    [length, num] = map(int, raw_input().split()) 
    print "Case #{}:".format(i + 1)
    for key, value in compute(length, num).iteritems():
        print key, pretty_str(value)