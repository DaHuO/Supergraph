def sheep(n):
	# init
	i = 2
	s = set([str(x) for x in xrange(10)]) - set(str(n))

	# search
	if not n:
		return "INSOMNIA"
	else:
		while s:
			s -= set(str(n*i)) ; i+=1

		return str(n*(i-1))

def out(path):
	with open(path, "r") as f:
		l = map(int, f.readlines())

	with open(path[:-2] + "out", "w") as f:
		for t,n in zip(xrange(1, l[0]+1), l[1:]):
			f.write("case #{}: ".format(t) + sheep(n) + "\n")

