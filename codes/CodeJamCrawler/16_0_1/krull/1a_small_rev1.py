# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
f = open('A-large.in', 'r')
fout = open('A-large-out.txt', 'w')
t = int(f.readline().split()[0])  # read a line with a single integer

def get_result(N):
	superset = set([x for x in '0123456789'])
	running_set = set([])
	for j in range(1,100):
		r = N * j
		for x in str(r):
			if x not in running_set:
				running_set.add(x)
		if not superset - running_set:
			return str(r)
	return 'INSOMNIA'

for i in xrange(1, t + 1):
  N  = int(f.readline().split()[0]) # read a list of integers, 2 in this case
  res = get_result(N)
  outstr =  "Case #" + str(i) + ": " + res + "\n"
  fout.write(outstr)
  print outstr
  # check out .format's specification for more formatting options


f.close()
fout.close()

