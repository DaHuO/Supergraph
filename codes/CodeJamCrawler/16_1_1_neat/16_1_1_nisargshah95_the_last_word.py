T = input()

for i in xrange(T):

	S = raw_input()

	new_s = [0 for j in xrange(2*len(S)-1)]
	first = last = len(new_s)/2

	new_s[first] = S[0]

	#print "new =", new_s, "first =", first, "last =", last

	for j in xrange(1, len(S)):

		char = S[j]
		if char >= new_s[first]:
			first -= 1
			new_s[first] = char
		else:
			last += 1
			new_s[last] = char

		#print "S[j] =", S[j], "new =", new_s, "first =", first, "last =", last


	final_s = ""
	for char in new_s:
		if char != 0:
			final_s += char

	print "Case #"+str(i+1)+": "+final_s