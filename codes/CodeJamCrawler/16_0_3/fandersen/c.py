from __future__ import division, print_function
from fileinput import input
from sys import setrecursionlimit
import random
setrecursionlimit(20000)

try:
    xrange  # Python 2?
    range = xrange
except NameError:
    xrange = range
inp = input()


def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	    return False
    return True

def in_base(bstring, base):
    res = 0
    for i,c in enumerate(bstring[::-1]):
        res += int(c) * base**i

    return res

assert in_base("1001", 2) == 9
assert in_base("1001", 6) == 217


def isjamcoin(bstring):
    for i in range (2, 11):
        if is_prime_number(in_base(bstring, i)):
            return False
    return True


assert isjamcoin("1001")
assert (not isjamcoin("101"))
assert isjamcoin("1010101111011011")

def getfac(n):
    for i in range(2, n):
        if n % i == 0:
            return i

    print("what??")

assert getfac(25) == 5
assert getfac(9) == 3


def getfactors(jamcoin):
    res =[]
    for i in range (2, 11):
        res.append(getfac(in_base(jamcoin, i)))
    return res

n = 16
j = 50
print("Case #1:")
total = 0
while True:
    ran = [random.getrandbits(1) for i in range (n-2)]
    current = "1" + "".join(map(str, ran)) + "1"
    if isjamcoin(current):
        print(current + " " + " ".join(map(str, getfactors(current))))
        total += 1
        if total == j:
            exit()
"""
100011 5 13 147 31 43 1121 73 77 629
111111 21 26 105 1302 217 1032 513 13286 10101
111001 3 88 5 1938 7 208 3 20 11"
"""
