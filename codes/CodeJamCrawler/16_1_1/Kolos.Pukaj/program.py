t = int(raw_input())

for i in range(t):
	s = raw_input()
	last_word = s[0]
	for x in s[1:]:
		if x >= last_word[0]:
			last_word = x + last_word
		else:
			last_word = last_word + x
	print "Case #{}: {}".format(i+1, last_word)
		
