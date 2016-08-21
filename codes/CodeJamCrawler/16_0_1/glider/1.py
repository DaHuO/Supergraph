T = input()

S = set('0123456789')
i = 1
while(T):
	C = N = input()
	if(N == 0):
		print 'Case #'+str(i)+': '+'INSOMNIA'
		i += 1
		T -= 1
		continue
	s = set(str(C))
	while(s < S):
		C = C + N
		t = set(str(C))
		s = s | (t - s)

	print 'Case #'+str(i)+': '+str(C)
	i += 1
	T -= 1
