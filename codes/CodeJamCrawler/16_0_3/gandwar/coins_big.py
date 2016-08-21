from math import sqrt, ceil
from pickle import load

with open(r"D:\Code Jam 2016\Coin\primes - small.p", "rb") as fd:
	PRIMES = load(fd)

MAX_INNER = 16383
NEEDED_NUMBERS = 500
COLLECTED_NUMBERS = {}

print "Case #1: "

def to_coin(integer):
	#print "1%014d1" % (int(bin(integer)[2:]))
	return "1%030d1" % (int(bin(integer)[2:]))

def find_derivative(number):
	limit = int(ceil(sqrt(number)))

	for der in PRIMES:
		if der > limit:
			return None

		if number % der == 0:
			return der

	return None


for x in xrange(MAX_INNER):
	ders = []
	if len(COLLECTED_NUMBERS) == NEEDED_NUMBERS:
		break

	is_legit = True
	coin = to_coin(x)

	for base in [2,3,4,5,6,7,8,9,10]:
		coin_as_int = int(coin, base)
		der = find_derivative(coin_as_int)
		if der is None:
			is_legit = False
			break
		else: 
			ders.append(der)

	if is_legit:
		COLLECTED_NUMBERS[coin] = ders
		# print coin
		# print ders


for item in COLLECTED_NUMBERS.items():
	print "%s %s %s %s %s %s %s %s %s %s" % (item[0], item[1][0], item[1][1], item[1][2], item[1][3], item[1][4], item[1][5], item[1][6], item[1][7], item[1][8])  