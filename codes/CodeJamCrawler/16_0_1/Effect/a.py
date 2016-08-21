fin = open("a.in")
fout = open("a.out", "w")

nt = int(fin.readline())
for tn in xrange(nt):
        fout.write("Case #" + str(tn + 1) + ": ")

        n = int(fin.readline().strip())
	digits = set()
	for i in xrange(100):
		cur = i * n
		while cur > 0:
			digits.add(cur % 10)
			cur /= 10
		if len(digits) == 10:
			fout.write(str(i * n))
			fout.write('\n')
			break
	else:
		fout.write("INSOMNIA\n")
