from __future__ import print_function


def try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    return True


def is_prime(n):
    bases = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)

    if n in (0, 1):
        return False
    if n in bases:
        return True
    if not n % 2:
        return False

    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1

    return not any(try_composite(a, d, n, s) for a in bases)


def to_digits(n):
    digits = []
    while n > 0:
        digits.insert(0, n % 2)
        n //= 2
    return digits


def from_digits(digits, b):
    n = 0
    for d in digits:
        n = b * n + d
    return n


def divisor(n):
    for i in xrange(2, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            return i
    raise 'can not be'


def sln(N, J, out):
    found = 0
    for n in xrange(0, 2 ** (N - 2)):
        is_coin = True
        number = 2 ** (N - 1) + n * 2 + 1
        divisors = []
        for base in xrange(2, 11):
            coin = from_digits(to_digits(number), base)
            if is_prime(coin):
                is_coin = False
                break
            else:
                divisors.append(divisor(coin))
        if is_coin:
            print('{0:016b} {1}'.format(number, ' '.join(str(x) for x in divisors)), file=out)
            found += 1
            if found == J:
                break


with open('sample2.txt', 'r') as inp, open('ans2.txt', 'w') as out:
    T = int(inp.readline())
    case = 0
    for line in inp:
        case += 1
        N, J = (int(x) for x in line.split())
        print('Case #{}:'.format(case), file=out)
        sln(N, J, out)
