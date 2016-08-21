import random
from math import *

used_string = set()

def find_div(n):
	for i in range(2, ceil(sqrt(n)) + 1):
		if n % i is 0:
			return i
		if (i > 200):
			break			
	return 0

def check(s):
	leg = []
	for i in range(2, 11):
		cur_number = 0
		for c in s:
			cur_number = cur_number*i + (ord(c) - ord('0'))
		div = find_div(cur_number)
		if div is 0:
			return 0
		else:
			leg.append(div)
	f_out.write(s)
	for a in leg:
		f_out.write(" " + str(a))
	f_out.write("\n")		
	return 1

f_in = open('c.txt', 'r')
f_out = open('c.out', 'w')
f_out.write("Case #1:\n")
n = f_in.readline()
line = list(f_in.readline().split(" "))
n = int(line[0])
j = int(line[1])
result = 0;
while True:
	s = "1";
	for i in range(1, n - 1):
		s += str(random.randrange(2))
	s += "1";
	if s in used_string:
		continue
	print(s)
	used_string.add(s)
	result += check(s)
	print(result)
	if result >= j:
		break

