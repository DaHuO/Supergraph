import sys
import math

__author__ = 'PC'


def output(out, tc, res):
    out.write("Case #%s:\n" % tc)
    for coin, lst in res:
        out.write("%s %d %d %d %d %d %d %d %d %d\n" % (
            coin, lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7], lst[8]))


def is_prime(num):
    # Returns True if num is a prime number, otherwise False.

    # Note: Generally, isPrime() is slower than primeSieve().

    # all numbers less than 2 are not prime
    if num < 2:
        return False

    # see if num is divisible by any number up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return i
    return None


def test_jamcoin(coin):
    lst = []
    for base in range(2, 11):
        val = int(coin, base)
        prime = is_prime(val)
        if prime:
            lst.append(prime)
        else:
            return None
    return lst


def generate_coin(num, N):
    coin = format(num, 'b').zfill(N - 2)
    coin = "1" + coin + "1"
    num += 1
    return coin, num


def generate_primes(N, J):
    lst = []
    num = 0
    max_num = int("1" * (N - 2), 2)
    while len(lst) != J:
        coin, num = generate_coin(num, N)
        primes = test_jamcoin(coin)
        if primes:
            lst.append((coin, primes))
        if num == max_num:
            return lst if len(lst) == J else None
    return lst

with open('output', 'w+') as out:
    with open('input', 'r') as f:
        T = int(f.readline())
        for tc in range(1, T + 1):
            N, J = f.readline().split()
            N, J = int(N), int(J)

            numbers = generate_primes(N, J)
            if numbers:
                output(out, tc, numbers)
