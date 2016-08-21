import math
import sys


def generate_primes(top):
    a = bytearray(b'\x01') * top
    a[0] = a[1] = False

    for i, prime in enumerate(a):
        if prime:
            yield i

            for n in xrange(i*i, top, i):
                a[n] = False

primes = [i for i in generate_primes(10**4)]

def find_nontrivial_divisor(n):
    for i in primes:
        if n % i == 0:
            return i
    else:
        return False

def generate_binaries(bits):
    for i in xrange((2**(bits-1)+1), 2**bits, 2):
        yield bin(i)[2:]

def main():
    T = int(sys.stdin.readline().strip())
    for case in xrange(T):
        N, J = [int(arg) for arg in sys.stdin.readline().strip().split()]
        binary_number_generator = generate_binaries(N)

        print 'Case #{0}:'.format(case+1)

        for _ in xrange(J):
            while True:
                binary = next(binary_number_generator)
                num_bases = [int(binary, base) for base in xrange(2,11)]
                nontrivial_divisors = [find_nontrivial_divisor(num_base) for num_base in num_bases]

                if all(nontrivial_divisors):
                    print binary, ' '.join(str(i) for i in nontrivial_divisors)
                    break


if __name__ == '__main__':
    main()
