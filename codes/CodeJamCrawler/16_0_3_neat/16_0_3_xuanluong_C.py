def is_prime(n):
	if n <= 1:
		return Flase
	if n <= 3:
		return True
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

def convert_to_base(n, base):
	if n == 0:
		return 0
	lst = []
	while n > 0:
		lst.append(str(n % base))
		n /= base
	lst.reverse()
	num = int("".join(lst))
	return num

def convert_from_base(n, base):
	digits = [int(i) for i in str(n)]
	num = 0
	for digit in digits:
		num *= base
		num += digit
	return num


def check_jamcoin(n, primes):
	lst = [0 for i in xrange(0, 11)]
	for base in xrange(2, 11):
		num = convert_from_base(n, base)
		passed = False
		for prime in primes:
			if prime >= num:
				break
			if num % prime == 0:
				lst[base] = prime
				passed = True
				break
		if not passed:
			lst = None
			break
	return lst

if __name__ == "__main__":
	primes = []
	for num in xrange(2, 101):
		if is_prime(num):
			primes.append(num)
	num = 0
	n_jamcoins = 0

	# Small or large dataset?
	N, J = 32, 500
	print "Case #1:"
	while num < (2 ** (N - 2)):
		tmp = num * 2 + 1 + 2 ** (N - 1)
		value = convert_to_base(tmp, 2)
		result = check_jamcoin(value, primes)
		if not result is None:
			for idx, ele in enumerate(result):
				if idx >= 2:
					n = convert_from_base(value, idx)
			divisors = " ".join([str(i) for i in result[2:]])
			n_jamcoins += 1
			print value, divisors
			if n_jamcoins == J:
				break
		num += 1