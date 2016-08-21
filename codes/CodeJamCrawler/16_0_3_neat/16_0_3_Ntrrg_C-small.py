"""Problem C. Coin Jam
		Miguel Angel Rivera Notararigo (ntrrg) <ntrrgx@gmail.com>
"""

from math import sqrt

def check(coinjam):
	numbers = []

	for i in range(2, 11):
		n = int(coinjam, i)

		if n < 4:
			return False

		if n % 2 == 0:
			numbers.append(str(n))
			continue

		if isPrime(n):
			return False

		else:
			numbers.append(str(n))

	return numbers

def isPrime(number):
	return all(number % i for i in mrange(3, int(sqrt(number)) + 1, 2))

def mrange(start, stop, step):
	while start < stop:
		yield start
		start += step

def ntd(number):
	for d in range(2, number // 2):
		if number % d == 0:
			return str(d)

	return False

input = open("C-small-attempt0.in")
output = open("output-small", "w")

T = int(input.readline())
n = 1

while T > 0:
	N, J = [int(x) for x in input.readline().strip().split()]
	p = 2 ** (N - 2)
	first = int("1" + "1".zfill(N - 1), 2)

	output.write("Case #{}:\n".format(n))

	while J > 0 and p > 0:
		coinjam = bin(first)[2:]
		numbers = check(coinjam)

		if numbers:
			output.write("{} {}\n".format(coinjam, " ".join([ntd(int(number)) for number in numbers])))

			J -= 1

		p -= 1
		first += 2

	T -= 1
	n += 1

input.close()
output.close()