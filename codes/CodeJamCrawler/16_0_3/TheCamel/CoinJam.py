N = 32
J = 500

primes = {}
lim =  1000 #int(1111111111111111**0.5)+1

truePrimes = set()

for i in range(2, lim):
	primes[i] = True

for i in range(2,lim):
	if primes[i] == True:
		truePrimes.add(i)
		tmp = 2
		while tmp*i < lim:
			primes[tmp*i] = False
			tmp += 1

digits = [[i**j for j in range(N)] for i in range(11)]

cnt = 0

print("Case #1:")

for n in range(1<<(N-2)):
	nums = [digits[i][0] + digits[i][-1] for i in range(2,11)]

	for i in range(14):
		off = 1<<i
		if n&off:
			for j in range(2,11):
				nums[j-2] += digits[j][i+1]

	coin = True
	dividers = [0 for i in range(2, 11)]

	for i in range(len(nums)):

		isPrime = True
		for prime in truePrimes:
			if nums[i] == prime:
				break
			if nums[i] % prime == 0:
				isPrime = False
				dividers[i] = str(prime)
				break 

		if isPrime == True:
			coin = False
			break

	if coin == True:
		print(nums[-1], " ".join(dividers))
		cnt += 1
		if cnt==J:
			break