#!/usr/bin/env python3
import math

def divisor_table(limit):
    table = [1] * limit
    for i in range(2, limit):
        if table[i] != 1: continue
        for j in range(i * 2, limit, i):
            if table[j] == 1:
                table[j] = i
    return table

table = divisor_table(10 ** 8)
primes = []
for i in range(2, len(table)):
    if table[i] == 1:
        primes.append(i)

def divisor(num):
    if num < len(table):
        return table[num]
    for prime in primes:
        if num % prime == 0:
            return prime
    for i in range(primes[-1], math.floor(math.sqrt(num))):
        if num % i == 0:
            primes.append(i)
            return i
    primes.append(num)
    return 1

def solve(fin, fout):
    n, j = map(int, fin.readline().split())
    fout.write('\n');
    for i in range(1 + 2 ** (n - 1), 2 ** n, 2):
        base2_divisor = divisor(i)
        if base2_divisor == 1: continue
        divisors = [base2_divisor]
        coin = bin(i)[2:]
        for b in range(3, 11):
            num = int(coin, base=b)
            div = divisor(num)
            if div == 1: break
            divisors.append(div)
        if len(divisors) != 9: continue
        for b in range(2, 11):
            num = int(coin, base=b)
            print(num, divisors[b - 2], num / divisors[b - 2])
        fout.write(coin)
        fout.write(' ')
        fout.write(' '.join(map(str, divisors)))
        fout.write('\n');
        j -= 1
        if j == 0: break
