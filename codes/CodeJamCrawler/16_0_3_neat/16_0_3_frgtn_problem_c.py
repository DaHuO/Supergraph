import sys
import itertools


def primes_sieve2(limit=2**10):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

prime_tuple = tuple(primes_sieve2(limit=2**16))


def binary_generator(N):
    for middle in itertools.product('01', repeat=N-2):
        yield '1' + ''.join(middle) + '1'


def find_min_divisor(number):
    for prime in prime_tuple:
        if number != prime and number % prime == 0:
            return prime


def nonprime_generator(N):
    for binary in binary_generator(N):
        not_prime = True
        divisors = []
        for base in range(2, 11):
            number = int(binary, base=base)
            divisor = find_min_divisor(number)
            if divisor is None:
                not_prime = False
                continue
            divisors.append(divisor)

        if not_prime:
            yield (binary, divisors)


def solve(T, N, J):
    nonprimes = nonprime_generator(N)
    print('Case #{}:'.format(T))
    for i in range(J):
        nonprime, divisors = next(nonprimes)
        print('{} {}'.format(nonprime, ' '.join(map(str, divisors))))


def main():
    n_cases = int(sys.stdin.readline().strip())
    for case in range(n_cases):
        N, J = map(int, sys.stdin.readline().strip().split(' '))
        solve(case + 1, N, J)


if __name__ == '__main__':
    main()
