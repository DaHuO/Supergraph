#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import random

primes = []
is_prime = []


def prepare_primes_until(till):
    global primes, is_prime
    is_prime = [True] * (till + 1)

    i = 2
    while i < till:
        if is_prime[i]:
            primes.append(i)
            j = i * 2
            while j < till:
                is_prime[j] = False
                j += i
        i += 1


def check_nontrivial_sqrt_1(m, a):
    r = (a * a) % m;
    if 1 < a < m-1 and r == 1:
        return 0
    else:
        return r


def expmod(base, exp, m):
    if exp == 0:
        return 1
    elif (exp & 1) == 0:
        return check_nontrivial_sqrt_1(m, expmod(base, exp/2, m))
    else:
        return (base * expmod(base, exp-1, m)) % m


def miller_rabin_test(n):
    return expmod((1 + random.randint(0, n-1)), n-1, n) == 1


def fast_prime(n, times=3):
    if n == 1: return False
    if n == 2: return True
    elif (n & 1) == 0: return False

    i = times
    while i > 0:
        if not miller_rabin_test(n): return False
        i -= 1

    return True


def nontrivial_divisor(n):
    if (n & 1) == 0: return 2

    i = 1
    c = len(primes)
    while i < c:
        prime = primes[i]
        if prime >= n: return -1
        if n % prime == 0: return prime
        i += 1

    return -1  # give up


def check(N, pat):
    divisors = [-1] * 11

    n = 0
    for b in range(2, 10+1):
        n = 0
        x = 1
        i = 0
        m = 1
        while i < N:
            if pat & m: n += x
            x *= b
            i += 1
            m *= 2
        p = fast_prime(n, 4)
        if p:
            return None

        divisors[b] = nontrivial_divisor(n)
        if divisors[b] == -1: return None

    return (n, divisors)


def solve(N, J):
    cnt = 0

    pat_begin = (2 ** (N-1)) + 1
    pat_end = (2 ** N) - 1
    pat = pat_begin
    while pat <= pat_end:
        res = check(N, pat)
        if res:
            n10, divisors = res
            print n10, ' '.join(map(str, divisors[2:11]))

            cnt += 1
            if cnt == J: return

        pat += 2


def main():
    prepare_primes_until(1000000)

    T = int(input())
    for t in range(1, 1+T):
        print 'Case #%d:' % t
        N, J = map(int, raw_input().split())
        solve(N, J)


if __name__ == '__main__':
    main()
