import os
import random

n = int(input())
for i in range(1, n+1):
	k, c, s = [int(s) for s in input().split(" ")]
	ans = ''
	for j in range(1, k+1):
		ans = ans + " " + str(j)
	print("Case #{}:{}".format(i, ans))


		
