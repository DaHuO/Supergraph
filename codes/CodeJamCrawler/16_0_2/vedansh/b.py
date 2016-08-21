def getCount(s,count):
	if len(s)*'+' == s:
		return count
	else:
		count = count + 1
		s = removeAndFlip(s)
		return 	getCount(s,count)


def removeAndFlip(s):
	q = len(s)
	w = -1
	for i in xrange(q-1,0,-1):
		if s[i] == '-':

			break
		elif s[i] == '+':
			w = i
	if w != -1:
		s = s[0:w]	

	if s[0] == '-':
		s = flip(s)
	else:
		w = 0
		for i in xrange(len(s)):
			if s[i] == '-':
				w = i
				break
		s = flip(s[0:w]) + s[w:]
	#print s	

	return s

def flip(s):
	#print s
	q = ''
	for i in s[::-1]:
		#print q
		if i =='+':
			q = q + '-'
		else:
			q = q +	'+'
	#print q		
	return q			


		


t = input()
for i in xrange(t):
	a = raw_input()
	c = getCount(s = a,count = 0)
	print "Case #%d: %d" % (i+1,c)