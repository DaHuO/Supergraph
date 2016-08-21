from sys import stdin, stdout
rl = lambda : stdin.readline().strip()
ncase = int(rl())

def solve(l):
	k, c, s = map(int,l.split())
	ans = [1]
	for i in xrange(s-1):
		ans.append(ans[-1]+k**(c-1))	
	return " ".join(map(str,ans))

for caseno in xrange(1,ncase+1):
	print "Case #{0}: {1}".format(caseno, solve(rl()))
