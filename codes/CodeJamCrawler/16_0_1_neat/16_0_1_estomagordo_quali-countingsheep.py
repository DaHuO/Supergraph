fin = open("A-large.in", "r")
fout = open("output.txt", "w")

t = int(fin.readline())

for case in xrange(1,t+1):
	n = int(fin.readline())
	orig = n
	seen = [False for x in range(10)]
	works = False
	
	for x in xrange(1000000):
		for c in str(n):
			seen[int(c)] = True
		if sum(seen) == 10:
			works = True
			break
		n += orig
		
	result = str(n) if works else "INSOMNIA"
	lb = "" if case == t else "\n"
	
	fout.write("Case #" + str(case) + ": " + result + lb)