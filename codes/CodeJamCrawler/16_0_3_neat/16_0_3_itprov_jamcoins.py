#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
import re
import math

MAX_DIV = 100 # Max divisor to try
def divisor_of(number):
    """Find a non-trivial divisor of given number"""
    divisor = 0
    for i in range(2, MAX_DIV):
        if number % i == 0 and number / i != 1:
            divisor = i
            break
    return divisor

t = int(input()) # Number of test cases

for i in range(t):
    n, j = [int(s) for s in input().split(" ")] # N & J
    if n - 2 > 0: # Just work on the middle part since the first and last digit will be 1
        jamcoins = [[0 for x in range(10)] for y in range(j)]
        m = n - 2
        l = 0
        for k in range (2**m):
            sf = "{}" * m # Format for middle part of the jamcoin to be tested
            x = [math.floor(k / 2**y % 2) for y in range(m)] # Individual digits of the jamcoin middle part
            num_str = "1" + sf.format(*x) + "1" # Jamcoin to be tested
            for base in range(2, 11):
                num = int(num_str, base)
                divisor = divisor_of(num) # Find a non-trivial divisor
                if divisor > 0:
                    jamcoins[l][0] = num  # first element is the jamcoin itself
                    jamcoins[l][base - 1] = divisor # next elements are the divisors
                else:
                    break
            if 0 in jamcoins[l]:
                continue
            l += 1
            if l + 1 > j:
                break
    else:
        jamcoins = ["Invalid input"]
    print("Case #{}:".format(i + 1))
    for x in jamcoins:
        print(("{} " * 10).format(*x))
