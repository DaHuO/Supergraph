import sys

from itertools import product, islice

def is_not_prime(n):
    if n <= 1:
        return 1
    elif n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3

    i = 5
    while i * i <= n:
        if n % i == 0:
            return i
        elif n % (i + 2) == 0:
            return i + 2
        i = i + 6
    return False

def get_divisors(numstr):
    divisors = []
    for i in xrange(2, 11):
        num = int(numstr, base=i)
        divisor = is_not_prime(num)
        if divisor in (False, 1, num):
            return None

        divisors.append(divisor)

    return divisors

def enum_product(N):
    for numtuple in product('01', repeat=N):
        numstr = ''.join(numtuple)
        if numstr[0] != '1' or numstr[-1] != '1':
            continue

        divisors = get_divisors(numstr)
        if divisors is None:
            continue

        yield numstr, divisors

def first_nontrivial_divisor(n):
    for i in xrange(2, n):
        if n % i == 0:
            return i

    return False

def process(N, J):
    print "Case #1:"

    j = 0
    for result in enum_product(N):
        if j >= J: break
        j += 1

        print result[0] + ' ' + ' '.join(str(x) for x in result[1])

if __name__ == "__main__":
    raw_input()
    n, j = raw_input().strip().split()
    n, j = int(n), int(j)
    #n, j = 6, 3
    process(n, j)

