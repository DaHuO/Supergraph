import sys
import math
import itertools

def check_prime(num):
    for divisor in xrange(2, 1000):
        if num % divisor == 0:
            return False, divisor
    return True, 0

def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n, j = [int(x) for x in raw_input().split(' ')]
        proofs = []

        for val in itertools.count(2 ** (n - 1) + 1, 2):
            if val >= 2 ** n:
                break
                
            factors = []
            bin_repr = bin(val)[2:]
            for base in xrange(2, 11):
                val_in_base = int(bin_repr, base)
                is_prime, factor = check_prime(val_in_base)
                if not is_prime:
                    factors.append(factor)

            if len(factors) >= 9:
                proofs.append((bin_repr, factors))
                if len(proofs) >= j:
                    break

        print 'Case #{}:'.format(i)
        for binary, factors in proofs:
            print '{} {}'.format(binary, ' '.join(str(x) for x in factors))

if __name__ == '__main__':
    main()