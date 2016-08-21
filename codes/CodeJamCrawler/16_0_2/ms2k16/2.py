t = int(raw_input())
for i in range(t):
	s = raw_input()
	s_list=list(s)
	z=0
	c=0
	if len(s_list) == 1:
		if s_list[0] == '-':
			s_list[0] = '+'
			c=c+1
		print 'Case #' + str(i+1) + ': ' + str(c)
	else:
		while True:
			if '-' not in s_list:
				print 'Case #' + str(i+1) + ': ' + str(c)
				break
			z=0
			while s_list[z] == s_list[z+1]:
				z=z+1
				if z == len(s_list) - 1 :
					break
			for x in range(z+1):
				if s_list[x] == '+':
					s_list[x] = '-'
				else:
					s_list[x] = '+'
			c=c+1		
