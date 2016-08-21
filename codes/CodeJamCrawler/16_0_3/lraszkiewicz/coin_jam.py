from math import pow
from math import sqrt
import sys

def changeBaseFromDecimal(num, b):
	if num == 0:
		return str(0)
	else:
		return changeBaseFromDecimal(num // b, b).lstrip(str(0)) + str(num % b)

def divisor(n):
	#for i in range(2, int(sqrt(n) + 1)):
	for i in range(2, 100):
		if n % i == 0:
			return i
	return None

def isJamcoin(n):
	ret = [n]
	if n[-1] == '1':
		for i in range(2, 11):
			s = int(n, i)
			tmp = divisor(s)
			if tmp == None:
				return None
			else:
				ret.append(tmp)
	else:
		return None
	return ret

tests = int(input())
for case in range(1, tests + 1):
	n, J = input().split()
	n = int(n)
	J = int(J)
	print("Case #" + str(case) + ":")
	count = 0
	for i in range(int(pow(2, n - 1)) + 1, int(pow(2, n)), 2):
		tmp = isJamcoin(changeBaseFromDecimal(i, 2))
		if tmp != None:
			for t in tmp:
				print(t, end=' ')
			print()
			count += 1
			print(count, file=sys.stderr)
			if count == J:
				break
