import sys
import math
import time

primelist = [2, 3, 5, 7, 11, 13]

def checkAllNonPrime(currentlist):
	divisor = list()
	l = len(currentlist)
	for num in range(2,11,1):
		total = 0
		base = 1
		for dig in range(l):
			total += currentlist[dig] * (base)
			base = base * num
		# print('total',num,total)
		result = checkNonPrime(total)
		if result == 0:
			return 0
		else:
			divisor.append(result)
	return divisor


def checkNonPrime(total):
	# maxr = math.trunc(math.ceil(math.sqrt(total)))
	# maxr = 12
	for i in primelist:
		if total % i == 0:
			return i
	return 0

start_time=time.time()

T = int(input())

target = open('result.txt', 'w')

for i in range(T):
	strline = raw_input()

	N,J = map(int, strline.split())

	# print(N,J)
	strA = 'Case #%d: \n'%(i+1)
	target.write(strA)

	minrange = 0
	maxrange = 2**(N-2) - 1

	currentlist = [0] * N

	counter = J
	# print('counter initial',counter)

	for x in range(minrange,maxrange + 1):
		currentlist[0] = 1
		midnum = x
		# print('midnum',midnum)
		for k in range(1,N-1):
			currentlist[k] = midnum & 1
			midnum = midnum >> 1
		currentlist[N-1] = 1

		result = checkAllNonPrime(currentlist)
		if result == 0:
			continue
		else:
			currentlist.reverse()
			strB = "".join(str(x) for x in currentlist)
			strC = " ".join(str(x) for x in result)
			strD = strB + ' ' + strC + '\n'
			target.write(strD)

		# currentlist.reverse()
		# print(currentlist)

		print('counter',counter)
		counter -= 1
		if counter == 0:
			break

elapsed_time=time.time()-start_time
print(elapsed_time)