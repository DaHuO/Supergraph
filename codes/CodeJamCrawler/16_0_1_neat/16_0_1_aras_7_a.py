for test in range(1, int(raw_input()) + 1):

	n = int(raw_input())

	found = 10 * [False]
	answer = n
		
	repeated = set()
	insomnia = False

	i = 1
	while not all(found):
		answer = i * n
	
		if answer in repeated:
			insomnia = True
			break

		repeated.add(answer)

		for c in str(answer):
			found[ord(c) - 48] = True

		i += 1
	
	if insomnia:
		answer = "INSOMNIA"

	print "Case #{}: {}".format(test, answer)

