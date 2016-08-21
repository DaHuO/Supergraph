def flip(s):
	s = s[::-1]
	for i in range(0,len(s)):
		if(s[i]=='+'):
			s = list(s)
			s[i] = '-'
			"".join(s)
		else:
			s = list(s)
			s[i] = '+'
			"".join(s)
	return "".join(s)

def checkDone(s):
	if(s.count('+') == len(s)):
		return 1
	else:
		return -1

test = raw_input()
for t in range(1, int(test)+1):
	string = raw_input()
	count = 0
	m = 0
	while(checkDone(string)==-1):
		# print string
		c = string[0]
		# print c
		cs = ""
		# print cs
		x = 0
		for e in string:
			if(e==c):
				cs = cs + e
				x = x+1
			else:
				break
		cs = flip(cs)
		# print "cs-"+cs
		# print x
		count = count + 1
		string = cs + string[x:]
		# print string
		m = m + 1
	print "Case #"+str(t)+": "+str(count)
