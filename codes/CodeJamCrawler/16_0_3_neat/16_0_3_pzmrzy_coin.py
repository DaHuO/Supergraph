#!/usr/bin/python
import math
def conv(n,k):
	c = 1
	result = 0
	sn = str(n)[::-1]
	for i in range(len(sn)):
		result += c * int(sn[i])
		c *= k
	return result

def prime(num):  
	res = 0
	pr = True  
	for i in range(2, int(math.sqrt(1 + num)) + 1):
		if num % i == 0 and i != num :  
			res = i
			pr = False
			break
	return (pr, res)

N=16
J=50
result = []
t = 0
for k in range(32769, 65536):
	if k % 2 == 0:
		continue
	x = bin(k)[2:]
	dic = {}
	f = True
	for j in range(2, 11):
		dic[j] = prime(conv(x, j))
		if dic[j][0] == True:
			f = False
			break
	if f:
		result = [x]
		
		for j in range(2, 11):
			result.append(dic[j][1])
		t += 1
		print "%s %s %s %s %s %s %s %s %s %s " % tuple(result)

		if t == 51:
			break


print "Case #1:"
