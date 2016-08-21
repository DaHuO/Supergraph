#!/usr/bin/python3
import math

def int2base(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (int2base(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

input()
N, J = map(int, input().split())
print('Case #1:')
a = (1 << (N - 1)) + 1
s = int2base(a, 2)
while J > 0 and len(s) == N:
	# print('S: ', s)
	arr = []
	for b in range(2, 11):
		val = int(s, b)
		ok = False
		for q in range(2, math.ceil(math.sqrt(val))+1):
			# print('trying to divide {} by {}'.format(val, q))
			if val % q == 0:
				ok = True
				arr.append(str(q))
				break
		if not ok:
			# print('BREAK: {} in base {} (= {}) is prime'.format(s, b, val))
			break
	else:
		print(s, ' '.join(arr))
		J -= 1
	a += 2
	s = int2base(a, 2)
