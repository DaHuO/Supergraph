CASE = 'Case #{}:'

def next_coin(coin):
	n = len(coin)
	i = int(coin[1:-1],2) - 1
	if i < 0:
		return ''
	i = bin(i)[2:]
	return '1' + ('0' * (n - 2 - len(i))) + i + '1'

def is_prime(n):
	if n == 2 or n == 3:
		return (True, -1)
	if n < 2 or n%2 == 0:
		return (False, 2)
	if n < 9:
		return (True, -1)
	if n%3 == 0:
		return (False, 3)
	r = int(n**0.5)
	f = 5
	while f <= r:
		print f
		if n%f == 0:
			return (False, f)
		if n%(f+2) == 0:
			return (False, f+2)
		f +=6
	return (True  , -1)

def jamcoin(n, j):
	coin = '1' * n
	coins = 0
	while len(coin) == n and coins < j:
		a = []
		for i in range(2,11):
			val = int(coin, i)
			ans, val = is_prime(val)
			if ans:
				break
			else:
				a.append(val)
		else:
			coins += 1
			print coin + ' ' + ' '.join(map(str, a))
		coin = next_coin(coin)

T = int(raw_input())
for x in xrange(T):
	n, j = map(int, raw_input().strip().split())
	print CASE.format(x + 1)
	jamcoin(n, j)



