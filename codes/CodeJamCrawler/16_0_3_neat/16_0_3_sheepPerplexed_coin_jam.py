import sys
from math import sqrt


def main():
    with open(sys.argv[1], 'r') as f:
        f.next()
        for idx, l in enumerate(f, start=1):
            N, J = [int(i) for i in l.split(' ')]
            print 'Case #{}:'.format(idx)
            for i, divs in coin_jam(N, J):
                print i, ' '.join(divs)


def coin_jam(N, J):
    PRIMES = [2]

    def is_prime(n):
        p_idx = 0
        is_p = True
        divisor = None
        while PRIMES[p_idx] <= sqrt(n):
            if n % PRIMES[p_idx] == 0:
                is_p = False
                divisor = PRIMES[p_idx]
                break
            p_idx += 1
        if is_p:
            PRIMES.append(n)
        return is_p, divisor

    for i in xrange(3, int(sqrt(10**(N-1) + 1))):
        is_prime(i)
    print "done"
    cjs = []
    for i in ['1' + bin(j)[2:].zfill(N-2) + '1' for j in xrange(2 ** (N-2))]:
        is_coin_jam = True
        divisors = []
        for b in xrange(2, 11):
            is_pr, divisor = is_prime(int(i, b))
            if is_pr:
                is_coin_jam = False
            divisors.append(str(divisor))
        if is_coin_jam:
            cjs.append((i, divisors))
        if len(cjs) == J:
            return cjs

if __name__ == '__main__':
    main()
