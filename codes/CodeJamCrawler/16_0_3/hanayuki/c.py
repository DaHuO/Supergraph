import sys
import math

T = int(raw_input())

fdict = {}

def getfactors(n):
	if n in fdict:
		return fdict[n]

	ret = -1

	if n % 2 == 0:
		fdict[n] = 2
		return 2

	#print n
	i = 3
	while True:
		if i > (int(math.sqrt(n))+1):
			break
		if n % i == 0:
			ret = i
			break
		i += 2

		# stop if too many attempts
		if i > 100000:
			return -1

	fdict[n] = ret
	return ret


for t in range(1, T+1):
	N,J = map(int, raw_input().split())

	print 'Case #%d:' % (t)

	num_str = '1' + '0' * (N-2) + '1'
	num_printed = 0
	while num_str < ('1' * N):
		#print num_str
		isprime = False
		factors =[]
		for base in range(2, 11):
			num = int(num_str, base)
			#print num

			f = getfactors(num)
			if f == -1:
				isprime = True
				break
			else:
				factors.append(f)

		if isprime == False:
			print num_str, ' '.join(map(str, factors))
			num_printed += 1
			if num_printed >= J:
				break

		num_str = bin(int(num_str, 2) + 2)[2:]

