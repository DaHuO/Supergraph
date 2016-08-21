f = open("D-small-attempt0.in", "r")
fo = open("out.txt","w")

count = int(f.readline())

for case in xrange(0,count):
	print case
	line = f.readline().split()
	k = line[0]
	c = line[1]
	s = line[2]

	fo.write("Case #" + str(case + 1) + ":")
	if s < k:
		fo.write(" IMPOSSIBLE")
	else:
		for x in range(int(k)):
			fo.write(" " + str(x+1))
	fo.write("\n")