

T = int(raw_input())

for i in xrange(T):

	S = raw_input()
	new = ""

	for letter in S:

		if not new:
			new += letter
		else:
			if letter >= new[0]:
				new = letter + new
			else:
				new += letter

	print "Case #%d:"%(i+1),new
