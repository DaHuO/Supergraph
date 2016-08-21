# -*- coding: utf-8 -*-

import math
from collections import deque


def main():
    t = int(input())
    for case in range(1, t + 1):
        n, j = [int(x) for x in input().split()]
        print('Case #{}:'.format(case))

        s = '1{}1'.format('0' * (n - 2))
        primes = gen_prime(10000)
        while j:
            ret = [s]
            for i in range(2, 11):
                num = int(s, i)
                divisor = find_divisor(num, primes)
                if divisor:
                    ret.append(str(divisor))
                else:
                    break
            else:
                print(' '.join(ret))
                j -= 1
            s = bin(int(s, 2) + 2)[2:]


def find_divisor(n, primes):
    for p in primes:
        if p * p > n:
            return 0
        if n % p == 0:
            return p


def gen_prime(n):
    ret = deque([2])
    for i in range(3, n + 1, 2):
        sqrt_ = int(math.sqrt(i))
        for j in range(2, sqrt_ + 1):
            if i % j == 0:
                continue
        else:
            ret.append(i)
    return ret


if __name__ == "__main__":
    main()
