
t = int(raw_input() )
for k in range( 1,  t+1 ):
	s = raw_input()
	total_count = 0
	while( s ):
		i = len(s) - 1
		while i>=0 and s[i] == '+':
			i-=1
		s = s[:i+1]
		if len(s)==0:
			break
		i = 0
		increase = False
		while s[i] == '+':
			increase = True
			s = s[:i] + '-' + s[i + 1:]
			i += 1
		if increase:
			total_count += 1
		# flip the whole damn thing
		s = s[::-1]
		wasplusflipped = False
		total_count += 1
		for i in range(0,len(s)):			
			if s[i] == '+':
				s = s[:i] + '-' + s[i + 1:]
			else:
				s = s[:i] + '+' + s[i + 1:]
	print 'Case #{}: {}'.format(k,total_count)








