#! /usr/bin/python

import sys
import itertools
import functools
import random
import operator
import math

# local list of small primes
import primes


def putative_jamcoins(length):
    if length < 3:
        return
    
    rand = random.SystemRandom()
    while True:
        middle = map(int, bin(random.getrandbits(length - 2)).strip("0b").rjust(length - 2, '0'))
        yield list(itertools.chain([1], middle, [1]))

def extract_factor(value):
    factor = 1
    for p in primes.primes:
        if p > math.sqrt(value):
            break
        
        if divmod(value, p)[1] == 0:
            factor = p
            break
            
    return factor
    
    
if __name__ == "__main__":
    num_tests = int(sys.stdin.readline())
    digits, num_results = map(int, sys.stdin.readline().split())
    
    place_values = [[(base ** x) for x in reversed(range(digits))] for base in range(11)]
    
    print("Case #1:")
        
    results = {}
    for i, jamcoin in enumerate(putative_jamcoins(digits)):
        factors = []
        for base in range(2, 11):
            value = sum(itertools.compress(place_values[base], jamcoin))
            factors.append(extract_factor(value))
        
        if functools.reduce(operator.and_, map(lambda x: x > 1, factors)):
            results["".join(map(str, jamcoin))] = " ".join(map(str, factors))
            
            if len(results) >= num_results:
                break
                
    for jamcoin, factors in results.items():
        print("{} {}".format(jamcoin, factors))