import sys
import math

common_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def has_common_factor(n):
    if (n & 1) == 0:
        return True, 2
    for factor in common_primes:
        if n % factor == 0:
            return True, factor
    return False, 0

def do(N, J):
    num_str = '1' + '0' * (N - 2) + '1'
    space = [0] * 11
    for base in range(2, 11):
        space[base] = int(num_str, base)

    j = 0
    factors = [0] * 11
    while j < J:
        has_factor = True
        for base in range(2, 11):
            has_factor, factors[base] = has_common_factor(space[base])
            if not has_factor:
                has_factor = False
                break
        if has_factor:
            j += 1
            print '{0:b}'.format(space[2]),
            for base in range(2, 11):
                print factors[base],
            print

        space[2] += 2
        num_str = '{0:b}'.format(space[2])
        for base in range(3, 11):
            space[base] = int(num_str, base)

def main():
    print "Case #1:"

    do(32, 500)

if __name__ == '__main__':
    main()
