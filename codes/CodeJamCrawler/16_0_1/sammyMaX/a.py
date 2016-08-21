import sys

def solve(x):
	if x == 1000000:
		return "9"
	s = set()
	for i in xrange(1, 1000001):
		st = str(i*x)
		for c in st:
			s.add(c)
		if len(s) == 10:
			return st
	return "INSOMNIA"

res = ""
with open("a.in", "r") as f:
	f = f.readlines()
	a = int(f[0])
	for i in xrange(1, a+1):
		a = int(f[i])
		res += "Case #%s: %s\n"%(i, solve(a))
		i += 1
		
with open("a.out", "w+") as f:
	f.write(res)