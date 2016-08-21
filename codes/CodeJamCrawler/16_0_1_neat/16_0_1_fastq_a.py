from sys import stdin, stdout

rl = lambda : stdin.readline().strip()

ncase = int(rl())

def solve(n):
	if n == 0: return "INSOMNIA"
	else:
		named = set()
		i = 1
		while True:
			t = i*n
			for x in str(t):
				named.add(x)	

			if "".join(sorted(list(named))) == "0123456789": 
				return i*n
			i += 1
for caseno in xrange(1,ncase+1):
	print "Case #{0}: {1}".format(caseno, solve(int(rl())))
