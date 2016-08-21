N = int(raw_input())

for i in range(N):
	word = list(raw_input())
	last = []

	firstletter = ''
	lastletter = ''
	for letter in word:
		if len(last) == 0:
			last.append(letter)
		elif letter >= last[0]:
			last.insert(0, letter)
		else:
			last.append(letter)

	val = ''.join(last)
	print "Case #%d: %s" % (i+1, val)
