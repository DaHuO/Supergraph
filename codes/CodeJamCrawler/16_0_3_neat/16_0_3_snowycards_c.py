import itertools

def binaryToBaseX(val, base):
	if val == 0:
		return 0

	digit = val % 2
	return digit + base * binaryToBaseX(val / 2, base)



def sieve():

	nums = [True] * 1000000
	for i in range(2, len(nums)):
		j = i * i
		while j < len(nums):
			nums[j] = False
			j += i

	primes = []
	for i in range(2, len(nums)):
		if(nums[i]):
			primes.append(i)

	return primes

def divisable(value, primes):
	for prime in primes:
		if value == prime:
			continue
		if value % prime == 0:
			return prime

	return -1

if __name__ == '__main__':

	primes = sieve()

	print("Case #1:")
	found = 0
	for test in itertools.count(start = (1 << 31) + 1, step = 2):
		if test >= (1 << 32):
			break
		basePrimes = []
		fail = False
		for base in range(2, 11):
			value = binaryToBaseX(test, base)

			div = divisable(value, primes)
			if div == -1:
				fail = True
				break

			basePrimes.append(div)

		if fail:
			continue

		printstr = str(binaryToBaseX(test, 10))
		for prime in basePrimes:
			printstr += " " + str(prime)

		print printstr
		found += 1
		if found == 500:
			break


