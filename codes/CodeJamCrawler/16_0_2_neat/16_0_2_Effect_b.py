fin = open("b.in")
fout = open("b.out", "w")

nt = int(fin.readline())
for tn in xrange(nt):
	fout.write("Case #" + str(tn + 1) + ": ")

	s = fin.readline().strip() + '+'
	
	diff = 0
	for i in xrange(len(s) -1, 0, -1):
		if s[i] != s[i - 1]:
			diff += 1
	
	first = (s[0] == '-')
	res = diff + (first + diff % 2) % 2

	fout.write(str(res))
	fout.write("\n")
