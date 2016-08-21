from sys import stdin
from math import sqrt
from itertools import count, islice, product, imap

def divisor(n):
    for i in islice(count(2), int(sqrt(n)-1)):
        # Primes are spread out pretty far after this point
        # Bad heuristic...but oh well!
        # We can always skip this one and move on to one with smaller divisors
        if i > 2500:
            break
        if not (n % i):
            return i

    return None

def strset(s, index, value):
    return s[:index] + value + s[index + 1:]

def possible_coins(length):
    for coinbody in product('10', repeat=length-2):
        yield '1' + ''.join(coinbody) + '1'

test_cases = int(raw_input())

for i, line in enumerate(stdin, 1):
    N, J = map(int, line.split())

    print "Case #%d:"%i

    for coin in possible_coins(N):
        divisors = []
        for base in xrange(2, 11):
            div = divisor(int(coin, base))
            if div is None:
                break
            divisors.append(div)

        if len(divisors) == (10 - 2 + 1):
            print coin, ' '.join(imap(str, divisors))
            J -= 1
            if J <= 0:
                break


