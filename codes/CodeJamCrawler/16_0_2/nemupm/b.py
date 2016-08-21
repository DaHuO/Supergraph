num_test_cases = input()
for ci in xrange(num_test_cases):
	stack = raw_input()
	first_side = stack[0]
	prev_side = stack[0]
	num_side_changed = 0
	optical_flip_count = 0
	for side in stack:
		if prev_side != side:
			num_side_changed += 1
		prev_side = side
	if (num_side_changed + int(first_side == '-')) % 2 == 0:
		optical_flip_count = num_side_changed
	else:
		optical_flip_count = num_side_changed + 1
	print "Case #%d: %d" % (ci+1, optical_flip_count)