def flip(s, index):
	new_str = ""
	for i in xrange(0, index+1):
		if s[index-i] == '+':
			new_str += '-'
		else:
			new_str += '+'
	for i in xrange(index+1, len(s)):
		new_str += s[i]
	# print s, "->", new_str
	return new_str

def f(s):
	count = 0
	i = len(s)-1
	while s != len(s)*'+':
		while s[i] == '+': # find the first '-' from last
			i -= 1
		if s[i] != s[0]: # if flip will have no improvement
			j = i
			while s[j] != s[0]: # find the bottom index of stack for a flip
				j -= 1
			s = flip(s, j) # index j included
			count += 1
		s = flip(s, i)
		count += 1
		i -= 1
	return count

T = input()
for i in xrange(T):
	S = raw_input()
	print "Case #"+str(i+1)+": "+str(f(S))