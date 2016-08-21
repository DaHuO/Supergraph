# read in the file
with open("A-large.in") as f:
	lines = f.readlines()
	for line in enumerate(lines): # skip T
		if line[0] == 0:
			continue
		digits = [False for _ in range(10)]
		N = int( line[1][:-1] )
		if N == 0:
			print("Case #%d: INSOMNIA" % line[0])
			continue
		i = 0
		while sum(digits) < 10:
			i += 1
			n = i * N
			while n != 0:
				digits[n % 10] = True
				n = int(n/10)
		print("Case #%d: %d" % (line[0], i * N))
