import math
import sys
import random
import os

def is_simple(n):
	for i in range(2, math.floor(math.sqrt(n)) + 1):
		if n%i==0: 
			return i

	return -1

t = input()
task = input()

n, cnt = map(int, task.split())

s = 2**(n-1) + 1
e = 2**n

count = 0

print("Case #1:")

for i in range(s, e):
	if count == cnt:
		break
	b = "{0:b}".format(i)
	if b[-1] == '0': 
		continue
	dividers = []
	for j in range(2, 11):
		c = int(b, j)
		d = is_simple(c)
		if d == -1:
			break
		dividers.append(d)
	if len(dividers) == 9:
		print(b, end=" ")
		for j in dividers:
			print(j, end=" ")
		count+=1
		print()