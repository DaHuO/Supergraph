readfile = open("readfile.txt", 'r')
writefile = open('writefile.txt', 'a')
writefile.truncate()

lines = map(int, (readfile.readlines()))

numCases = lines[0]
for case in xrange(1, numCases + 1):
	sleep = True
	seen = set()
	orig = lines[case]
	N = orig
	digits = set()
	for d in str(N):
		digits.add(int(d))
	while len(digits) < 10:
		N += orig
		if N in seen:
			writefile.write("Case #1: INSOMNIA\n")
			sleep = False
			break
		seen.add(N)
		for d in str(N):
			digits.add(int(d))
	if sleep:
		writefile.write("Case #" + str(case) + ": " + str(N) + "\n")

readfile.close()
writefile.close()