n = int(raw_input())

def find(s):
	flag = -1
	for i in range(len(s)):
		if s[i] == '-':
			flag = i
	return flag
		

for T in range(1, n + 1):
	s = raw_input()
	ans = 0
	x = find(s)
	while(x != -1):
		s__ = ''
		for i in range(x + 1):
			if s[i] == '+': s__ += '-'
			else: s__ += '+'
		s__ += s[x+1:]
		s = s__
		#print s
		ans += 1
		x = find(s)
	print "Case #" + str(T) + ": " + str(ans)
