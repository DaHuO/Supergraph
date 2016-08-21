num_test_cases = input()
for ti in xrange(num_test_cases):
	input_letters = raw_input()
	output_letters = input_letters[0]
	for letter in input_letters[1:]:
		if output_letters + letter > letter + output_letters:
			output_letters = output_letters + letter
		else:
			output_letters = letter + output_letters
	print "Case #%d: %s" % (ti+1, output_letters)