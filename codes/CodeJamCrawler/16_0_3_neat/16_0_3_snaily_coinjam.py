primes = [3, 5, 7, 11, 13, 17, 19]

with open('coinjam.large') as file:
	cases = int(file.next())
	for case in xrange(cases):
		print "Case #%d:" % (case+1)
		N, J = map(int, file.next().split())
		coin = '1' + '0' * (N - 2) + '1'
		coins = 0
		while coins < J:
			divisors = []
			for base in xrange(2, 11):
				num = int(coin, base)
				for prime in primes:
					if num % prime == 0:
						divisors.append(prime)
						break
			if len(divisors) == 9:
				print coin, ' '.join(map(str, divisors))
				coins = coins + 1
			coin = "{0:b}".format(int(coin, 2) + 2)