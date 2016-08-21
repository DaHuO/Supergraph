import os
import sys
import pickle

with open('primes.pp', 'rb') as f:
    primes = pickle.load(f)

def factor(n):
    for p in primes[1:]:
        if n < p*p:
            return None
        if n % p == 0:
            return p
    return None

def solve(N, J):
    count = 0
    start = int('1' + ('0' * (N - 2)) + '1', 2)
    end = int('1' * N, 2)
    for i in range(start, end + 1, 2):
        coin = bin(i)[2:]
        divisors = []
        for b in range(2, 11):
            f = factor(int(coin, b))
            if f is None:
                break
            divisors.append(f)
        if len(divisors) != 9:
            continue
        yield coin, divisors

        count += 1
        if count >= J:
            break

def check(coin, divisors):
    for b, d in zip(range(2, 11), divisors):
        i = int(coin, b)
        assert(i % d == 0)
        print 'base %d: %d = %d * %d' % (b, i, d, i / d)

def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        N, J = map(int, sys.stdin.readline().strip().split())
        print 'Case #%d:' % (t + 1)
        for coin, divisors in solve(N, J):
            # check(coin, divisors)
            print '%s %s' % (coin, ' '.join(map(str, divisors)))

if __name__ == '__main__':
    main()

