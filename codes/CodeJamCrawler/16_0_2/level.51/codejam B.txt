for tc in range(input()):
	config = raw_input()
	flips = 0
	if config[-1] == "-":
		flips = flips + 1
	for i in range(len(config) - 1):
		if config[i] != config[i + 1]:
			flips = flips + 1
	print "Case #" + str(tc + 1) + ": " + str(flips)