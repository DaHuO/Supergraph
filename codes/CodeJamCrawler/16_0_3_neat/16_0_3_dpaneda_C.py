#!/usr/bin/python3

import sys
from sympy.ntheory import factorint, isprime

bases = list(range(2, 11))
divisors = [9, 28, 65, 126, 217, 344, 513, 730, 1001]

def valid(coinjam):
    for base in bases:
        n = int(coinjam, base)
#        print(n, base, factorint(n))
        if isprime(n):
            return False
        if n % divisors[bases.index(base)]:
            return False
    return True

def solve():
    N, J = map(int, sys.stdin.readline().split())

    min_coinjam = '1' + ('0' * (N - 2)) + '1'
    bin_coinjam = int(min_coinjam, 2)
    while (bin_coinjam % 9):
        bin_coinjam += 1

    valids = 0
    while valids < J:
        coinjam = bin(bin_coinjam)[2:]
        bin_coinjam += 18
        if valid(coinjam):
            valids += 1
            print(coinjam, " ".join(map(str, divisors)))

#    max_coinjam = '1' * N


#i = 9
#str_n = bin(i)[2:]
#some_primes = False
#for base in bases:
#    n = int(str_n, base)
#    print(n)
#    isprime(n), factorint(n))

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #1:")
    solve()
