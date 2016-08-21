#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


primes = []


def is_prime(n):
    for i in xrange(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def pre_primes(n):
    for i in xrange(2, int(n**0.5)+1):
        if is_prime(i):
            primes.append(i)
    return primes


def not_prime(n):
    for x in primes:
        if x >= n:
            return None
        if not n % x:
            return x
    return None


def compute(N, J):
    start = pow(2, 0) + pow(2, N-1)
    end = 0
    for i in range(N):
        end += pow(2, i)

    primes = pre_primes(end)
    result = list()
    for i in xrange(start, end+1, 2):
        bin_temp = bin(i)[2:]
        temp_list = [bin_temp]
        for base in range(2, 11):
            convent = int(bin_temp, base)
            divisor = not_prime(convent)
            if divisor:
                temp_list.append(str(divisor))
        if len(temp_list) > 9:
            result.append(temp_list)
        if len(result) == J:
            return result
    return result


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        num = int(f.readline())
        N, J = [int(item) for item in f.readline().split(' ')]
        result = compute(N, J)
        print('Case #{}:'.format(num))
        for item in result:
            print(' '.join(item))
