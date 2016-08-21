import sys
from math import sqrt
from itertools import count, islice

def isPrime(n):
	return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def getFactor(n):
	for i in range(2, n):
		if n%i == 0:
			return i

def next():
	return lines.pop(0)

def main():
	bins = foo(16, 50)
	print("Case #1:")
	for bin in bins:
		factors = [bin]	
		for i in range(2, 11):
			factors.append(
				str(getFactor(int(bin, i)))
				)
		print(' '.join(factors))

def foo(N, J):
	init = int("1" + (N-2)*"0" + "1", 2)
	count = 0
	bins = []
	while count < J:
		x = init
		bin_x = bin(x)[2:]
		if all(not isPrime(int(bin_x, i)) for i in range(2, 11)):
			bins.append(bin_x)
			print("got one")
			count += 1
		init += 2
	return bins



if __name__ == "__main__":
	main()