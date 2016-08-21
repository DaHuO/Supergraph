# BasicInputA.py
import math


t = int(input())

for loopNum in range(1, t + 1):
 	k = (input())

 	printstring = "Case #{}: ".format(loopNum)

 	s = []

 	for x in k:
 		if(len(s) == 0) :
 			s.append(x)
 		else:
 			if(s[0] <= x):
 				s.insert(0,x)
 			else:
 				s.append(x)
 	print(printstring + ''.join(s))