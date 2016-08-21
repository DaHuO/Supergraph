T = int(raw_input())

for t in range(T):
	N = raw_input()

	if N == "0":
		print "Case #%d: INSOMNIA" % (t + 1)
		continue

	a = {
		"0": True,
		"1": True,
		"2": True,
		"3": True,
		"4": True,
		"5": True,
		"6": True,
		"7": True,
		"8": True,
		"9": True
	}

	N= int(N)
	n = N
	i = 1
	while a:
		# print n
		n = i * N
		for letter in str(n):
			if a.get(letter):
				# print letter
				a.pop(letter)
		i += 1
		# print n
	print "Case #%d: %d"%(t+1, n) 