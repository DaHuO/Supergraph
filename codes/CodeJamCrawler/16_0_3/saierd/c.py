#!/usr/bin/env python3

import itertools
import math


def find_divisor(number, base):
    n = int(number, base=base)

    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return i
    return None


def jamcoins(n, j):
    number_found = 0
    for c in itertools.product(["0", "1"], repeat=(n - 2)):
        number = "1" + "".join(c) + "1"

        divisors = []
        for base in range(2, 11):
            d = find_divisor(number, base)

            if d is None:
                break
            divisors.append(d)
        else:
            print("{} {}".format(number, " ".join(map(str, divisors))))

            number_found += 1
            if number_found == j:
                return


def main():
    t = int(input())
    for i in range(1, t + 1):
        n, j = [int(s) for s in input().split()]
        print("Case #{}:".format(i))
        jamcoins(n, j)


if __name__ == "__main__":
    main()
