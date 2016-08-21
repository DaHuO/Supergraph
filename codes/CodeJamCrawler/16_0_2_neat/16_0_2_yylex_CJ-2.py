T = input ()
for j in xrange (T):
	s = list(raw_input())
	i = 0
	current = s[i]
	answer = 0
	while i < len(s) :
		if s[i] == current :
			i += 1
		else :
			answer += 1
			current = s[i]
			i += 1

	if current == '-':
		answer += 1
	print "Case #"+str(j+1)+": "+str(answer)



