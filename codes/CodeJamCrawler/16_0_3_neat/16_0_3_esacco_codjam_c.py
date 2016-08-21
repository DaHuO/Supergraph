import itertools

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

lists = [[1]] + [[1,0]]*30 + [[1]]

with open('output', 'w') as outputFile:
	outputFile.write('Case #1:\n')
	total_ok = 0
	for element in itertools.product(*lists):
	    is_ok = True
	    divisors = []
	    for base in range(2, 11):
	    	act_n = sum(element[x]*(base**(31-x)) for x in range(32))
	    	if is_prime(act_n):
	    		is_ok = False
	    		break
	    	else:
	    		for p in _known_primes:
	    			if act_n % p == 0:
	    				divisors.append(p)
	    				break
	    if is_ok and len(divisors) == 9: 
	    	total_ok += 1
	    	outputFile.write(' '.join(map(str,[act_n] + divisors)) + '\n')
	    	if total_ok == 500:
	    		break










