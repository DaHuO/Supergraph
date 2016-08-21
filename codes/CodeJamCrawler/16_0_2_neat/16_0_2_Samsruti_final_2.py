fileout = open('output2large.txt', 'w')
T = int(raw_input())
for cases in range(1,T+1):
	s = raw_input()
	s = list(s)
	count = 0
	i=0
	s_new = s
	for i in xrange(0,len(s)*2):
		current = s[0]
		if(len(s)>1):
			next = s[1]
		else:
			break
		if current == next:
			s.pop(0)
		elif current == '-':
			s[s.index(current)] = '+'
			count+=1
		elif current == '+':
			if next == '-':
				s[s.index(current)]  = '-'
				count +=1
	if len(s)==1:	
			if s[0] is '-':
				s[0] = '+'
				count +=1	
	#print "String S:",s
	print >>fileout ,"Case #"+str(cases)+": ",count
fileout.close()
