#!/usr/bin/python3 
import sys

prime_list = []

def jamcoin(case, n, j):
    print("Case #" + str(case) + ":")
    n = int("1" + "0"*(n-2) + "1", 2)
    i = 0
    while True:
        if is_jamcoin("{0:b}".format(n)):
            print("{0:b}".format(n), end="")
            for k in range(2, 11):
                print(" " + str(NT_divisor(int("{0:b}".format(n), k))), end="")
            print()
            i = i + 1
            if i == j:
                return
        n = n + 1

def is_jamcoin(n):
    if n[0] != "1":
        return False
    if n[-1] != "1":
        return False
    if any([is_prime(int(n, j)) for j in range(2, 11)]):
        return False
    return True

def is_prime(n):
    for p in prime_list:
        if p >= n:
            return True
        if n%p == 0:
            return False
    return True

def NT_divisor(n):
    for j in range(2, int(n**0.5)+1):
        if n%j == 0:
            return j

def is_prime_slow(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gen_prime_list(max_n):
    for n in range(2, max_n):
        if is_prime_slow(n):
            prime_list.append(n)

if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding="UTF-8") as f:
        f.readline()
        line = 1
        for d in f:
            d = d.strip().split()
            gen_prime_list(int("1" + "1"*(int(d[0])-2) + "1", 2))
            jamcoin(line, int(d[0]), int(d[1]))
            line = line + 1
