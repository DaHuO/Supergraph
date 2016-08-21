t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	word = raw_input()
	answer = ''
	for letter in word:
		if answer == '' or letter < answer[0]:
			answer += letter
		elif letter >= answer[0]:
			answer = letter + answer
	print "Case #{}: {}".format(i, answer)
	# check out .format's specification for more formatting options