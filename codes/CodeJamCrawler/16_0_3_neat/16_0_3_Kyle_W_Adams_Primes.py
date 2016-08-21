# Compute primes up to and including n
def compute_primes(n):
	primes = (n + 1) * [1]
	primes_result = []

	primes[0] = 0
	primes[1] = 0

	for i in range(2, int(n / 2) + 2):
		if not primes[i]:
			continue
		primes_result.append(i)
		index = 2 * i
		while index < n + 1:
			primes[index] = 0
			index += i

	while i < n + 1:
		if primes[i]:
			primes_result.append(i)
		i += 1
	return primes_result


primes = compute_primes(int("1"*16, 2))

def isPossiblyPrime(n):
	for i in primes:
		x,y = divmod(n, i)
		if not y:
			return i
	return 0

# Compute if a number is prime
def isPrime(n):
	if n > 2**16:
		return isPossiblyPrime(n)
	for i in range(3, int(n**.5 + 1), 2):
		if n % i == 0:
			return i
	return 0