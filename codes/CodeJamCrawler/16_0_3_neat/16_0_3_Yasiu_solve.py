#!/usr/bin/env python3

import itertools
import math

def get_divisor(n):
    if n in (1, 0):
        return -1
    for i in range(2, int(math.sqrt(n)+1)):
        if (n % i) == 0:
            return i
    return -1

def generate_nums(n):
    """generate permutation of binary numbers n-2"""
    return ("".join(seq) for seq in itertools.product("01", repeat=n-2))

def main():
    T = int(input())
    for t in range(T):
        s = input()
        n, j = (int(inp) for inp in s.split(" "))
        jamcoins = list()
        candidates = generate_nums(n)

        for candidate in candidates:
            divisors = list()
            for base in range(2, 11):
                #the first and last digits = 1
                str_num = ("1"+candidate+"1")
                num = int(str_num, base)
                divisor = get_divisor(num)
                if divisor == -1:
                    break
                divisors.append(str(divisor))
            if len(divisors) == 9:
                    jamcoins.append((str_num, divisors))
            if len(jamcoins) == j:
                break
        print("Case #{0}:".format(t+1))
        for jamcoin in jamcoins:
            print("{0} {1}".format(
                        jamcoin[0],
                        " ".join(jamcoin[1])
                        ))

if __name__=="__main__":
    main()
