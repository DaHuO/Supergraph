import sys, re



def is_prime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True

def dec_to_bin(x):
	return int(bin(x)[2:])

def bin_to_dec(x):
	return int(x, 2)

def limits(n):
	minim = "1"
	for x in xrange(1, n - 1):
		minim += "0"
	minim += "1"

	return minim

def is_jamcoin(coin, n):
	if len(coin) != n or coin[0] != "1" or coin[len(coin) - 1] != "1":
		return False
	for base in xrange(2, 11):
		num = int(coin, base)
		if is_prime(num):
			return False
	return True

def divisor(coin):
	divisors = []
	for base in xrange(2, 11):
		n = int(coin, base)
		for i in xrange(2, n - 1):
			if n % i == 0:
				divisors.append(str(i))
				break
	return divisors

with open(sys.argv[1]) as f:
	content = f.read().splitlines()
cases = int(content[0])

for x in xrange(1,cases + 1):
	n, j = map(int, re.findall('\d+', content[x]))
	minim = bin_to_dec(limits(n))
	coins = 0

	print "Case #" + str(x) + ": "

	while coins < j:
		coin = str(dec_to_bin(minim))
		if is_jamcoin(coin, n):
			coins += 1
			print coin + " " + ' '.join(divisor(coin))
		minim += 1

