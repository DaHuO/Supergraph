from __future__ import print_function
import fileinput
from sets import Set

def get_initial_set():
	return Set([0,1,2,3,4,5,6,7,8,9])

f = fileinput.input()

T = int(f.readline())
for case in range(1,T+1):
	N=int(f.readline().rstrip())
	if N == 0:
		print("Case #"+str(case)+": INSOMNIA")
	else:
		s=get_initial_set()
		count=0
		N_init=N
		while len(s) != 0:
			count += 1
			N = N_init*count
			N_str=str(N)
			for c in N_str:
				i=int(c)
				s.discard(i)
		print("Case #"+str(case)+": "+str(N))
