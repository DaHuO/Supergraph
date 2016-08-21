from itertools import product


def gen_coin_halves(n, J):

	coins = list()
	for i, coin in enumerate(product('01', repeat=n-1)):
		coins.append('1' + ''.join(list(coin)))
		if i == J - 1:
			return coins


def get_value(coin, powers):
	return sum([int(coin[i])*p for i, p in enumerate(powers)])


def get_divisor(n):

	for k in range(2, n//2 + 1):
		if n%k == 0:
			return k


infile = 'input.in'


lines = [line.rstrip('\n') for line in open(infile, 'r')]

T = int(lines[0])

bases = list(range(2, 11))

for t in range(1, T + 1):

	print('Case #{case}:'.format(case=t))

	N, J = map(int, lines[t].split(' '))

	l = N//2

	powers = {b: list(reversed([b**n for n in range(N)])) for b in bases}
	
	for coin in gen_coin_halves(l, J):

		divisors = ['']*9
		val = coin + ''.join(list(reversed(coin)))

		for b in powers:

			value = sum([int(val[i])*p for i, p in enumerate(powers[b])])
			divisors[b-2] = str(get_divisor(value))
		
		print(val, ' '.join(divisors))