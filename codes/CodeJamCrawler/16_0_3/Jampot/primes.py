##
## Google Code Jam 2016
## Qualification Round, Apr 8
##
## Problem Title: Coin Jam
## Author: James Hall
## Email: james.hall@infinityworks.com
##

from math import gcd
from functools import reduce
import random

def convert(num, base):
    result = 0

    power = 0
    for c in str(num)[::-1]:
        result += int(c) * base ** power
        power += 1
                         
    return result

def g(x, n):
    return (x ** 2 - 1) % n

def pollard_rho(n):
    x = 2
    y = 2
    d = 1
    iters = 0
    while d == 1:
        if iters > 10:
            return -1
        x = g(x, n)
        y = g(g(y, n), n)
        d = gcd(abs(x - y), n)
        iters += 1
    if d == n: 
        return -1
    else:
        return d

used = set()

def getRand(n):
    result = "".join(["1"] + [random.choice(["1", "0"]) for i in range(0, n-2)] + ["1"])

    if result in used:
        return getRand(n)

    return int(result)

def calculate(N, J):

    valid = []
    current = getRand(N)
    
    while len(valid) < J:
        isValid = True
        divisors = []
        for i in range(2, 11):
            curr = convert(current, i)
            divisor = pollard_rho(curr)
            if divisor != -1:
                divisors += [divisor]
            else:
                isValid = False
                break
            
        if isValid:
            used.add(current)
            valid += [[current] + divisors]

        current = getRand(32)
    return valid

if __name__ == "__main__":
    N = 32
    J = 500

    print("Case #1:")

    results = calculate(N, J) 

    sortedResults = sorted(results)
    for result in sortedResults:
        print("{} {}".format(result[0], " ".join(str(x) for x in result[1:])))
        
