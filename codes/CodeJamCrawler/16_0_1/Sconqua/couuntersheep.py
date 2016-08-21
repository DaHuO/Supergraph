# Number of test cases
t = int(raw_input())

for i in xrange(1, t + 1):
	chosen = int(raw_input())
	discovered = list()
	factor = 1

	if chosen == 0:
		print "Case #{}: {}".format(i, "INSOMNIA")
	else:
		while len(discovered) != 10:
			for car in str(chosen * factor):
				if car not in discovered:
					discovered.append(car)
			factor += 1
		print "Case #{}: {}".format(i, chosen*(factor-1))