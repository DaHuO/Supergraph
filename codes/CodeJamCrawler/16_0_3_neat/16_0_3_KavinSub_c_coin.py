from math import *
# A global prime set
primes = set()

# generates ith jamcoin
def generate_jamcoin(N, i):
	if N == 2:
		return '11'
	K = N - 2
	num = bin(i)[2:]
	num = ('0' * (K - len(num))) + num
	num = '1' + num + '1'
	return num

# Checks if a coin is a jamcoin. If so, return a list of divisors. Otherwise, return an empty list
def is_jamcoin(coin):
	L = [int(coin, i) for i in range(2, 11)]
	divisors = []
	for num in L:
		div = is_prime(num)
		if div == -1:
			return []
		else:
			divisors.append(div)
	return divisors

# Checks if n is prime. Returns a divisor if not prime, -1 if prime
def is_prime(n):
	if n in primes:
		return -1
	for i in range(2, int(floor(sqrt(n))) + 1):
		if n % i == 0:
			return i
	primes.add(n)
	return -1

def format_list(L):
	L = [str(x) for x in L]
	return ' '.join(L)

T = int(input())
N, J = tuple([int(x) for x in input().split()])

print("Case #1:")

count = 0 
i = 0
while count < J:
	coin = generate_jamcoin(N, i)
	seq = is_jamcoin(coin)
	if len(seq) > 0:
		print(coin + ' ' + format_list(seq))
		count += 1
	i += 1