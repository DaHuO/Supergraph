import sys
import math
import re

def gen_primes():
    svsz = 10000
    sieve = [True] * svsz
    sieve[0] = sieve[1] = False

    for i in range(2, svsz):
        if sieve[i] == False:
            continue

        for j in range(i+i, svsz, i):
            sieve[j] = False

    primes = []
    for i in range(2, svsz):
        if sieve[i] == True:
            primes.append(i)

    return primes


gPrimes = gen_primes()


def is_prime(n):
    for p in gPrimes:
        if p*p > n:
            break

        if n % p == 0:
            return p

    return 0


def convert_from_base2(n, newBase):
    ret = 0
    for shift in range(32, -1, -1):
        ret *= newBase

        dig = n >> shift
        ret += dig & 1

    return ret


def case():
    N, J = (int(x) for x in input().split(' '))

    lo = (1 << (N - 1)) + 1
    hi = (1 << N) - 1

    cnt = 0
    divs = [0] * 11

    for i in range(lo, hi + 1, 2):
        jammin = True
        for b in range(2, 11):
            tmp = convert_from_base2(i, b)

            divs[b] = is_prime(tmp)
            
            if divs[b] == 0:
                jammin = False
                break

        if jammin == True:
            cnt += 1
            
            sys.stdout.write('\n{0:b}'.format(i))

            for b in range(2, 11):
                sys.stdout.write(' {}'.format(divs[b]))

        if cnt == J:
            break


if __name__=="__main__":

	if len(sys.argv) > 1:
		sys.stdin = open(sys.argv[1])

	num_cases = int(input())

	for c in range (1, num_cases+1):
		sys.stdout.write('Case #')
		sys.stdout.write(str(c))
		sys.stdout.write(':')
		case()
		sys.stdout.write('\n')
