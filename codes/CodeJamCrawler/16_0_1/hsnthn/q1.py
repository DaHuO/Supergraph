def solve(n):
	nInt = int(n)

	if nInt == 0:
		return "INSOMNIA"

	digits = set()

	i = 1
	while(len(digits) != 10):
		chars = list(str(nInt * i))
		digits.update(chars)
		i += 1

	return str(nInt * (i-1))

inf = open("input.txt", "r")
outf = open("output.txt", "wr")

t = inf.readline()

for i in xrange(1, int(t)+1):
	n = inf.readline()
	r = solve(n)
	print n, r
	outf.write("Case #%d: %s\n" % (i, r))

inf.close()
outf.close()

