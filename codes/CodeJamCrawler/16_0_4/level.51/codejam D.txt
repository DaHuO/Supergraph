for tc in range(input()):
	k,c,s = raw_input().split()
	div = int(k) ** (int(c) - 1)
	s_locations = []
	for i in range(int(k)):
		s_locations.append(str(i * div + 1))
	text = ' '.join(s_locations)
	print "Case #" + str(tc + 1) + ": " + text