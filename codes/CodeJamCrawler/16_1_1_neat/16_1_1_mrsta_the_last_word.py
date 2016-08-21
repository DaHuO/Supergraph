# the_last_word.py
def test(s):

	x = 'a'

	def maxS(abc):
		m = '0'
		for i in abc:
			if ord(i) > ord(m): m = i
		return m

	for i in xrange(len(s)):
		if i == 0: x = s[i]
		elif ord(s[i]) >= ord(maxS(x)): 
			x = s[i] + x
		else: 
			x = x + s[i]

	return x

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
 	n = raw_input()
 	print "Case #{}: {}".format(i, test(n))