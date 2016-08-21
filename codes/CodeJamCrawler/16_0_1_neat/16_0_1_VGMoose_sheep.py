trials = int(raw_input())

for t in range(0, trials):

	N = int(raw_input())
	if N == 0:
		print("Case #" + str(t+1) + ": 	INSOMNIA")
		continue
	
	seen = []
	i = 0
	cur = ""

	while len(seen) != 10:
		i += 1
		# calculate cur (i*N)
		cur = str(i*N)

		for char in cur:
			if char not in seen:
				seen.append(char)

	print("Case #" + str(t+1) + ": " + cur)
