import math

def dec_from_str(s, b):
	return int(s, b)

def str_from_dec(i, b):
	s = ""

	while (i != 0):
		s += str(i % b)
		i /= b

	return ''.join(reversed(s))

def inc_str(s):
	i = dec_from_str(s, 2)
	i += 2 # since last digit MUST be 1
	return str_from_dec(i, 2)

def get_divisor(n):
	for i in xrange(2, int(math.ceil(math.sqrt(n))) + 1):
		if n % i == 0:
			return i
	return None

def is_jamcoin(coin):
	divs = []

	for i in xrange(2, 11):
		val = dec_from_str(coin, i)
		div = get_divisor(val)

		if not div:
			return False, divs

		divs.append(div)

	return True, divs

def get_jamcoins(n, j):
	# generate starting coin
	coin = "1" + (n-2)*"0" + "1"

	# generate j coins w/ corresponding divisors
	jamcoins = []
	while len(jamcoins) < j:

		is_jc, divs = is_jamcoin(coin)
		if is_jc:
			jamcoins.append((coin, divs))

		coin = inc_str(coin)

	return jamcoins

num_cases = int(raw_input())

for i in xrange(num_cases):
	N, J = map(int, raw_input().split())

	jamcoins = get_jamcoins(N, J)

	print("Case #" + str(i + 1) + ":")
	for coin, divs in jamcoins:
		print(str(coin) + " " + " ".join(map(str, divs)))