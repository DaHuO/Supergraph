
def sheepCount(n):
	if n == 0:
		return "INSOMNIA"
	for i in xrange(1,100):
		N = i*n
		[setN.add(int(j)) for j in str(N)]
		if len(setN) == 10:
			return str(N)
	return "INSOMNIA"


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

# t = int(raw_input())  # read a line with a single integer
# for i in xrange(1, t + 1):
#   n = raw_input()
#   setN = set()
#   print "Case #{}: {} ".format(i, sheepCount(int(n)))
#   # check out .format's specification for more formatting options

readFile = "A-large.in"

with open(readFile) as r, open("./output.out", "w") as w:
	i = 0
	t = r.readline()
	print "number of counts ", t
	for n in r:
		setN = set()
		i += 1
		w.write("Case #"+str(i)+": "+sheepCount(int(n))+"\n")



