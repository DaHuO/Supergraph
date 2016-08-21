

with open('inputfile') as fi:
	lines = fi.readlines()
	numtests = int(lines[0])
	vals = [int(i) for i in lines[1:]]
	for i in range(numtests):
		val = vals[i]
		index = i + 1
		seen = set()
		n = 1
		while len(seen) != 10 and n < 100:
			for addme in str(val*n):
				seen.add(int(addme))
			n += 1
		if len(seen) < 10:
			answer = "INSOMNIA"
		else:
			answer = str(n*val-val)
		print "Case #%s: "%str(index), answer
