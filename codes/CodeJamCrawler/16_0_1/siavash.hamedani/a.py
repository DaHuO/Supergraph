import sys
from sets import Set
import numpy as np

def solve(inp):
	if inp=="0":
		return "INSOMNIA"
	res=Set(map(int,inp))
	c=1
	inp = int(inp)
	while 1:
		q = inp*c
		# print res,q
		res=res.union(Set(map(int,str(q))))
		c+=1
		if len(res)==10:
			return q

for i in range(int(sys.stdin.readline())):
	res = solve(sys.stdin.readline()[:-1])
	print "Case #%d: %s"%(i+1,res)

