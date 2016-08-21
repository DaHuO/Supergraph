import sys
import math

def primes(n):
    ''' Return: (primes, sieve) for primes under n
    The sieve has no even numbers in it, and begins at 3
    '''
    # True prime, False not.
    primeSieve = [True] * (n // 2 - 1)
    primeList = [2]
    for i in range(3, n, 2):
        if primeSieve[(i - 3) // 2]:
            primeList.append(i)
            for j in range((i - 3) // 2 + i, len(primeSieve), i):
                primeSieve[j] = False
    return primeList, primeSieve

def test():
    # TODO: Read a test case and return the answer to print
    bin_strs = []
    for x in range(0, 2**14):
        s = bin(x)[2:].zfill(14)
        if (sum(1 for c in s if c == '1') + 2) % 3 == 0:
            bin_strs.append('1' + s + '1')

    prime_list, sieve = primes(10 ** 7)
    new_strs = []
    for s in bin_strs:
        n = int(s, 2)
        if not sieve[(n - 3) // 2]:
            # This number is not prime (approx.)
            new_strs.append(s)

    bin_strs = new_strs
    new_strs = None

    candidates = []
    for s in bin_strs:
        passes = True
        for base in range(3, 10):
            n = int(s, base)
            for p in prime_list:
                if p ** 2 > n:
                    # n is prime
                    passes = False
                    break
                if n % p == 0:
                    break
            if not passes:
                break
        if passes:
            candidates.append(s)
        if len(candidates) >= 50:
            break

    for can in candidates:
        divisors = []
        for base in range(2, 10):
            n = int(can, base)
            for p in prime_list:
                if n % p == 0:
                    divisors.append(p)
                    break
        print(can + ' ' + ' '.join(map(str, divisors)) + ' 3')

def main(n):
    ''' Read and perform n test cases. '''

    for i in range(n):
        print('Case #1:')
        test()

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    main(n)
