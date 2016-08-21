import os
import random

n = int(input())
for i in range(1, n+1):
	s = input().split(" ")[0]
	ori = '#'
	cnt = 1
	for x in list(s):
		if x is ori or ori is '#':
			ori = x
		else:
			ori = x
			cnt = cnt + 1
	cnt = cnt - int(s[-1]=='+')
	print("Case #{}: {}".format(i, cnt))


		
