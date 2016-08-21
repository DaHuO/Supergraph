import sys

def get_divisors(jamcoin):
    divisors = []
    for power in range(2, 11):
        n = int(jamcoin, power)
        for d in range(2, int(n**0.5 + 1)):
            if n % d == 0:
                divisors.append(d)
                break
    return divisors

def is_jamcoin(candidate, verbose=False):
    for power in range(2, 11):
        if is_prime(int(candidate, power)):
            if verbose:
                print 'In power %d it is prime: %d' % (power, int(candidate, power))
            return False
    return True

def solve(N, J, verbose=False):
    result = []
    generated = 0

    for inner in xrange(2**N):
        candidate = ('1%0' + str(N - 2) + 'd1') % int(bin(inner)[2:])
        if not is_jamcoin(candidate):
            continue

        print 'FOUND', candidate
        result.append((candidate, get_divisors(candidate)))
        generated += 1
        if generated == J:
            break

    return result

def read_int(fp):
    return int(fp.readline())

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite

def is_prime(n, _precision_for_huge_n=16):
    '''
    Primality test is from
    http://rosettacode.org/wiki/Miller-Rabin_primality_test#Python:_Probably_correct_answers
    '''
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s)
                   for a in _known_primes[:_precision_for_huge_n])

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

if __name__ == '__main__':
    T = read_int(sys.stdin)
    for i in range(T):
        N, J = map(int, sys.stdin.readline().split(' '))
        print 'Case #%d:' % (i + 1)
        for jamcoin, dividers in solve(N, J):
            print '%s %s' % (jamcoin, ' '.join(map(str, dividers)))
