
def solve(n):
	if n == 0:
		return "INSOMNIA"
	a = [0 for i in range(10)]
	i = 1
	while True:
		for j in [int(c) for c in str(n*i)]:
			a[j] = 1
		s = 0
		for aa in a:
			s+=aa
		if s == 10:
			return str(n*i)
		i += 1





f = open("A-large.in")

T = int(f.readline())
for case in range(1,T+1):
	print "Case #{0}: {1}".format(case,solve(int(f.readline())))
