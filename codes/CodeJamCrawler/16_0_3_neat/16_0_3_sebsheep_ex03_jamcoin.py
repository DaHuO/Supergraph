primes = (2,3,5,7,11,13)

def get_factor(n):
	limit = int(n**0.5 + 1)
	for p in primes:
		if n % p == 0:
			return p

	return None # maybe there is a factor... but it's too big for us

from itertools import product, islice
def jamcoins(size):
	for digits in product('01', repeat=size-2):
		coin_str = '1%s1' % (''.join(digits))
		divisors = []
		for base in range(2, 11):
			coin = int(coin_str, base)
			factor = get_factor(coin)
			if factor:
				divisors.append(factor)
			else:
				break
		if len(divisors) == 9:
			yield coin_str, divisors


if __name__ == '__main__':
	n = int(input("N = "))
	j = int(input("J = "))
	postfix = input("postfix = ")
	with open("/tmp/jamcoins%s"%postfix, "w") as out:
		print("Case #1:", file=out)
		for jamcoin, divisors in islice(jamcoins(n), j):
			print(jamcoin, *divisors, file=out)

