from math import sqrt
from itertools import count, islice

primes = {}

def isPrime(n, factors):
    global primes
    if n < 2:
        return False
    if n in primes:
        return True
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n % number:
            factors.append(number)
            return False
    primes[n] = True
    return True
    
def getCoinJamCandidate(length, counter):
    binary = str(bin(counter))[2:]
    return "1" + (length - 2 - len(binary)) * "0" + binary + "1"

def primeFree(coinJamCandidate, factors):
    for base in range(2, 11):
        if isPrime(int(coinJamCandidate, base), factors):
            return False
    return True

def solve(n, m):
    counter = 0
    current = getCoinJamCandidate(n, 0)
    found = 0
    last = int("1" + "1" * (n - 2) + "1", 2)
    results = []
    while found < m and int(current, 2) < last:
        factors = []
        if (primeFree(current, factors)):
            results.append(current + " " + " ".join([str(x) for x in factors]))
            found += 1
        counter += 1
        current = getCoinJamCandidate(n, counter)

    return results