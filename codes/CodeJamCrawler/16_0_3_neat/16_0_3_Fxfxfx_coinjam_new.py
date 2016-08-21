import itertools as it
from random import randrange

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] # etc.

number_cases = int(raw_input())
for i in range(1, number_cases+1):
    n = [int(s) for s in raw_input().split(" ")]

length_N = n[0]
J = n[1]

def get_in_all_bases(number_string):
    diff_bases = [int(number_string, base) for base in range(2,11)]
    return diff_bases

def no_prime_in_all_bases(numbers_list):
    primality = [is_prime(n) for n in numbers_list]
    for a in primality:
        if a:
            return not a
    return True
        
def is_prime(n):
	"""Return True if n passes k rounds of the Miller-Rabin 	primality test (and is probably prime). Return False if n is 		proved to be composite.
    """
	k = 1
	if n < 2: return False
	for p in small_primes:
		if n < p * p: return True
		if n % p == 0: return False
	r, s = 0, n - 1
	while s % 2 == 0:
		r += 1
		s //= 2
	for _ in range(k):
		a = randrange(2, n - 1)
		x = pow(a, s, n)
		if x == 1 or x == n - 1:
			continue
		for _ in range(r - 1):
			x = pow(x, 2, n)
			if x == n - 1:
				break
		else:
			return False
	return True

def get_nontrivial_divisors(numbers_list):
    divisors = []
    for number in numbers_list:
        for i in range(2, int(number**0.5)+1):
            if number%i == 0:
                divisors.append(i)
                break
    return divisors

count = 0
possibilities = it.product('01',repeat=length_N-2)
print "Case #1:"
for i in possibilities:
    if count == J:
        break;
    number_string = '1' + ''.join(i) + '1'
    diff_bases = get_in_all_bases(number_string)
    if no_prime_in_all_bases(diff_bases):
        count += 1
        print number_string,
        for a in get_nontrivial_divisors(diff_bases):
            print a,
        print '\n'

#print no_prime_in_all_bases('1001')
#print no_prime_in_all_bases('110111')
#print get_nontrivial_divisors(get_in_all_bases('1001'))
#print get_in_all_bases('100011')
#print get_nontrivial_divisors(get_in_all_bases('100011'))
#print n
