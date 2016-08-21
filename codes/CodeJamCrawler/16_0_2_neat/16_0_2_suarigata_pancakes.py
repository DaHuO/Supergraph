import heapq
import math

T = int(raw_input())
for t in range(T):
	pancakes=raw_input()
	last='+'
	if pancakes[0]=='-':
		c=-1
	else:
		c=0
	for p in pancakes:
		if p!=last and p=='-':
			c+=2
		last=p
	
	print("Case #" + str(t+1) + ": " + str(c))
