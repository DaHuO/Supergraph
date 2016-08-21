import itertools

# checks if the given integer is prime
# returns an array with the first value being a boolean if it's prime
# and the second value of a non-trivial divisor
def is_prime(n):
    if n < 2:
         return False
    if n % 2 == 0:
         return [n == 2, 2]
    k = 3
    while k*k <= n:
         if n % k == 0:
             return [False, k]
         k += 2
    return [True, 0]

f = open('sample.txt', 'r')
T = int(f.readline())

for t in range(0,T):
	line = map(int, f.readline().split())
	N = line[0] # length of each jamcoin
	J = line[1] # number of jamcoins

	# generate all the possible numbers
	poss = []
	combos = list(itertools.product([0, 1], repeat = N-2))
	for c in combos:
		s = '1' + ''.join(map(str, c)) + '1'
		poss.append(s)

	# remove ones that are primes
	valid = []
	div = []
	completed = 0
	for p in poss:
		# print('completed: ' + str(float(completed)/float(len(poss))*100) + '% ' + '(' + str(completed) + '/' + str(len(poss)) + ')')
		prime = False
		divisors = []
		for base in range(2,11):
			value = int(p, base)
			primeResult = is_prime(value)
			if primeResult[0]:
				prime = True
				break
			else:
				divisors.append(primeResult[1])
		if not prime:
			valid.append(p)
			div.append(divisors)
		completed += 1

	# print(valid)
	# print(div)

	# format the output
	print('Case #' + str(t+1) + ':')
	for i in range(0, J):
		output = valid[i] + ' '
		for d in div[i]:
			output += str(d) + ' '
		output = output[:-1]
		print(output)

f.close()