for _i in xrange(int(raw_input())):
	s = raw_input()
	news = s[0]
	
	for i in range(1,len(s)):
		if(news[0]<=s[i]):
			news = s[i]+news
		else:
			news += s[i]
		#print news
	print "Case #"+str(_i+1)+": "+news