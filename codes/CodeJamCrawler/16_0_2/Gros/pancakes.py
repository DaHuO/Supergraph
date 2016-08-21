#!/usr/bin/python

import re

name='B-large.in'
f=open(name)
f_s=open(name+'_solved','w')
cases=int(f.readline().strip())

def solve(pancake, case):
	sol=len(re.findall('-+', pancake))
	sol+=len(re.findall('\++', pancake))
	if pancake[-1]=='+':
		sol-=1
	f_s.write("Case #{}: {}\n".format(case,sol))
	# print("Case #{}: {}\n".format(case,sol))


for case in range(1,cases+1):
	pancake=f.readline().strip()
	solve(pancake, case)
	
f.close()
f_s.close()

