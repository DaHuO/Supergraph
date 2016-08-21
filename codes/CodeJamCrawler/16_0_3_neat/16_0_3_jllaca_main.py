import math


def binary_permutations(n):
    if n == 0:
        yield []
    else:
        for permutation in binary_permutations(n - 1):
            yield permutation + [0]
            yield permutation + [1]


def compute_in_base(d, b):
    n = len(d)
    return sum(b ** i * d[n - i -1] for i in range(n))


def first_factor(n):
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return i
    return n


def jam_coins(n, j):
    i = 0
    for permutation in binary_permutations(n - 2):
        if i == j:
            break
        d = [1] + permutation + [1]
        factors = []
        for b in range(2, 11):
            x = compute_in_base(d, b)
            factor = first_factor(x)
            if factor == x:
                break
            else:
                factors.append(factor)
        if len(factors) == 9:
            yield ''.join(map(str, d)), factors
            i += 1


t = input()
for i in range(t):
    n, j = map(int, raw_input().split())
    print 'Case #{}:'.format(i + 1)
    for jam_coin, factors in jam_coins(n, j):
        print jam_coin,
        for factor in factors:
            print factor,
        print
