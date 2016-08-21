#!/usr/bin/env python

# from http://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite

def is_prime(n, _precision_for_huge_n=16):
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

def main():
	_ = raw_input()
	N, J = map(long, raw_input().strip().split(' '))
	start_jamcoin = long("1"+"0"*(N-2)+"1", 2)
	max_jamcoin = long(N*"1", 2)
	jamcoin_count = 0

	with open("jamcoin.out", "w") as outfile:
		outfile.write("Case #1:")

		for jamcoin_test in range(start_jamcoin, max_jamcoin+1, 2):
			base_values = [long(bin(jamcoin_test)[2:], base) for base in range(2,10+1)]

			if any(map(is_prime, base_values)):
				continue

			outfile.write("\n%s" % (bin(jamcoin_test)[2:]))
			for base_value in base_values:
				found_divisor = False
				divisor = 2
				while not found_divisor and (divisor < base_value):
					if base_value % divisor == 0:
						found_divisor = True
						outfile.write(" %d" % (divisor))
					divisor += 1

			jamcoin_count += 1
			if jamcoin_count == J:
				break

if __name__ == '__main__':
	main()
