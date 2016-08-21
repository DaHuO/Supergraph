for testCase in xrange(input()):
	B, M = map(int, raw_input().split())

	if 2 ** (B - 2) < M:
		solution = 'IMPOSSIBLE'
	else:
		flag = 1
		building = B - 1
		slides = set([B])
		M -= 1

		while M:
			if M & flag:
				slides.add(building)
				M -= flag

			flag = flag << 1
			building -= 1

		solution = 'POSSIBLE'
		for building in xrange(1, B + 1):
			row = '\n'
			for nextBuilding in xrange(1, B + 1):
				if building == 1:
					row += '1' if nextBuilding in slides else '0'
				elif building != B and nextBuilding > building:
					row += '1'
				else:
					row += '0'
			solution += row
	
	print 'Case #{}: {}'.format(testCase + 1, solution)
