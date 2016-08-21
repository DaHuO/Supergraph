import string
import math
from random import randrange
import pyprimesieve as pp
# Possible digits from the lowest to the highest
DIGITS = '%s%s' % (string.digits, string.ascii_lowercase)
PRIMES = [pp.primes_nth(idx) for idx in range(1, 1001)]


small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]  # etc.


def probably_prime(n, k):
    """Return True if n passes k rounds of the Miller-Rabin primality
    test (and is probably prime). Return False if n is proved to be
    composite.

    """
    if n < 2:
        return False
    for p in small_primes:
        if n < p * p:
            return True
        if n % p == 0:
            return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def baseencode(num, base):
    result = 0
    positive = True
    # If a number is negative let's remove the minus sign
    if num[0] == '-':
        positive = False
        num = num[1:]

    for i, n in enumerate(num[::-1]):
        # Since 0xff == 0xFF
        n = n.lower()
        result += DIGITS.index(n) * base ** i

    if not positive:
        result = -1 * result

    return result


def to_bin(num, bits):
    """
    Convert num to a binary number represent by string and paddle to required
    bits number
    """
    result = [0 for idx in range(bits)]
    tail = list(bin(num))[2:]
    result[len(result) - len(tail):] = tail
    return result


def div(n):
    i = 2
    for prime in PRIMES:
        if n % prime == 0:
            return prime
    return 0


def compute(bits, jams):
    results = []
    zero_ones = [1 for idx in range(bits)]
    for middle in range(2 ** (bits-2)):
        zero_ones[1:-1] = to_bin(middle, bits-2)
        dividors = []
        for base in range(2, 11):
            # get the number in base 10
            num = baseencode([str(ele) for ele in zero_ones], base)
            isPrime = probably_prime(num, 5)
            if not isPrime:
                dividor = div(
                    baseencode([str(ele) for ele in zero_ones], base))
                if dividor == 0:
                    break
                else:
                    dividors.append(dividor)
        if len(dividors) == 9:
            results.append(
                (''.join([str(ele) for ele in zero_ones]), dividors))
        if len(results) >= jams:
            return results

cases = input()
for idx in range(int(cases)):
    bits, jam = input().split()
    results = compute(int(bits), int(jam))
    print("Case #{}:".format(idx+1))
    for num, dividors in results:
        print("{} {}".format(num, ' '.join([str(ele) for ele in dividors])))
# print(compute(32, 500))
