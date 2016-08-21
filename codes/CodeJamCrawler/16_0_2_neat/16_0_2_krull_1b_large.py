# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
f = open('B-large.in', 'r')
fout = open('B-large.out', 'w')
t = int(f.readline().split()[0])  # read a line with a single integer

def get_result(N):
	flips = 0
	start = N[0]
	for x in N[1:]:
		if x != start:
			start = x
			flips += 1
	if N[-1] == '-':
		flips += 1
	return flips

for i in xrange(1, t + 1):
  N  = f.readline().split()[0] # read a list of integers, 2 in this case
  res = get_result(N)
  outstr =  "Case #" + str(i) + ": " + str(res) + "\n"
  fout.write(outstr)
  print outstr
  # check out .format's specification for more formatting options


f.close()
fout.close()

