for tc in range(input()):
	undyne = raw_input()
	last_word = undyne[0]
	for i in range(len(undyne) - 1):
		if ord(undyne[i + 1]) >= ord(last_word[0]):
			last_word = undyne[i + 1] + last_word
		else:
			last_word = last_word + undyne[i + 1]
	print "Case #" + str(tc+1) + ": " + last_word
