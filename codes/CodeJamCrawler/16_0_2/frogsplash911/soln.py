def ans(s):
	s = list(s)
	count = 0
	tps = ''.join(s).rfind('-')
	while tps != -1:
		for i,p in enumerate(s[0:tps+1]):
			if p == '+':
				s[i] = '-'
			else:
				s[i] = '+'
		count+=1
		tps = ''.join(s).rfind('-')
	return count

# print ans('-+')
t=input()
for i in range(0,t):
	ln = raw_input()
	print "Case #"+str(i+1)+": "+str(ans(ln))








