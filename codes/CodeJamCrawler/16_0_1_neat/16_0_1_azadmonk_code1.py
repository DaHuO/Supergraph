# your code goes here
import numpy as np
import sys
T = input()
out = [0,0,0,0,0,0,0,0,0,0]
des = [1,1,1,1,1,1,1,1,1,1]
tmp = 0
tmpn = 0

for i in range(T):
	N = input()
	tmpn = N
	j = 1
	if(N==0):
		sys.stdout.write('Case #'+str(i+1)+': INSOMNIA\n')
	else:
		out = [0,0,0,0,0,0,0,0,0,0]
		while (out!=des):
			tmpn = j*N
			K= map(int,str(tmpn))
			for l in range(len(K)):
				out[K[l]] = 1
			tmp = K
			j+=1
		sys.stdout.write('Case #'+str(i+1)+': '+str(tmpn)+'\n')
