from math import sqrt

def as_base(n, k, bn):
	dn = 0
	ns = 1
	for i in range(0,bn):
		if n & (1 << i) > 0:
			dn += ns
		ns *= k
	return dn

def is_prime(n):
	if n % 2 == 0: return 2
	for i in xrange(3, int(sqrt(n)+1),2):
		if i > 1000000: break
		if n % i == 0:
			return i
	return 1

T = int(raw_input())
N,J = [int(x) for x in raw_input().split()]
number = (1 << (N-1)) + 1
j = 1
print("Case #1:")
while j <= J:
	divs = []
	for i in range(2,11):
		dn = as_base(number,i,N)
		div = is_prime(dn)
		if div != 1: divs += [div]
	if len(divs) == 9:
		j += 1
		print("{0:b}".format(number)),
		for i in divs:
			print(i),
		print
	number += 2
