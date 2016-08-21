#!/usr/bin/python

import re

name='A-large.in'
f=open(name)
f_s=open(name+'_solved','w')
cases=int(f.readline().strip())

def solve(N, case):
	digits=set()
	N_old=N
	#INSOMNIA only for 0
	#range checked for N<=10**6, max is 72
	for one in xrange(1,73):
		N=one*N_old
		digits.update( map(int,str(N)) )
		if len(digits)==10:
			f_s.write("Case #{}: {}\n".format(case,N))
			return
	f_s.write("Case #{}: {}\n".format(case,"INSOMNIA"))

for case in range(1,cases+1):
	N=int(f.readline().strip())
	solve(N, case)
	
f.close()
f_s.close()